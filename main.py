import os
import pandas as pd
import requests
from io import StringIO
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
from dotenv import load_dotenv

# --------------------------
# 1️⃣ Load environment variables
# --------------------------
load_dotenv()

KOBO_USERNAME = os.getenv("Kobo_username")
KOBO_PASSWORD = os.getenv("kobo_password")
DATA_URL = "https://kf.kobotoolbox.org/api/v2/assets/ak3QkwKnpveHvN9VpSnHVR/export-settings/esfyvLftAskWE3vJ42Sha8V/data.csv"

SQL_HOST = os.getenv("SQL_Host")
SQL_PORT = os.getenv("SQL_Port")
SQL_USER = os.getenv("SQL_Username")
SQL_PASSWORD = quote_plus(os.getenv("SQL_password"))
SQL_DATABASE = os.getenv("SQL_DATABASE")

SCHEMA_NAME = "quicksupply"
TABLE_NAME = "weekly_inventory"

# --------------------------
# 2️⃣ Fetch data from KoboToolbox
# --------------------------
print("📥 Fetching Kobo data...")

response = requests.get(DATA_URL, auth=(KOBO_USERNAME, KOBO_PASSWORD))
response.raise_for_status()

df = pd.read_csv(StringIO(response.text))
print(f"✅ Fetched {len(df)} rows from Kobo")

# --------------------------
# 3️⃣ Clean and simplify columns
# --------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.replace('[^0-9a-zA-Z_]+', '_', regex=True)
    .str.lower()
)
print(f"🧹 Cleaned {len(df.columns)} columns for PostgreSQL compatibility")

# --------------------------
# 4️⃣ Connect to PostgreSQL
# --------------------------
print("🔗 Connecting to PostgreSQL...")

connection_string = (
    f"postgresql+psycopg2://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DATABASE}"
)
engine = create_engine(connection_string)

# --------------------------
# 5️⃣ Load data into schema.table
# --------------------------
with engine.begin() as conn:  # begin() auto-commits safely
    conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};"))
    df.to_sql(TABLE_NAME, conn, schema=SCHEMA_NAME, if_exists="replace", index=False)

print(f"✅ Data loaded successfully into {SQL_DATABASE}.{SCHEMA_NAME}.{TABLE_NAME}")
