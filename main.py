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
ASSET_ID = "a3vWYSWmr528zJvPrAbL85"
DATA_URL = "https://kf.kobotoolbox.org/api/v2/assets/a3vWYSWmr528zJvPrAbL85/export-settings/esZA8QhsLYoBQtehuYkHn3v/data.csv"

SQL_HOST = os.getenv("SQL_Host")
SQL_PORT = os.getenv("SQL_Port")
SQL_USER = os.getenv("SQL_Username")
SQL_PASSWORD = quote_plus(os.getenv("SQL_password"))
SQL_DATABASE = os.getenv("SQL_DATABASE")

SCHEMA_NAME = "quicksupply"
TABLE_NAME = "weekly_inventory"

# --------------------------
# 2️⃣ Fetch form structure to get Data Column Names mapping
# --------------------------
print("📋 Fetching form structure from Kobo...")

form_url = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_ID}/"
form_response = requests.get(form_url, auth=(KOBO_USERNAME, KOBO_PASSWORD))
form_response.raise_for_status()

form_data = form_response.json()

# Create comprehensive mapping
xml_to_dataname = {}
label_to_dataname = {}

if 'content' in form_data and 'survey' in form_data['content']:
    for question in form_data['content']['survey']:
        xml_name = question.get('name', '')
        data_col_name = question.get('$autoname', '')
        label = question.get('label', '')
        
        if xml_name and data_col_name:
            xml_to_dataname[xml_name] = data_col_name
            
            # Handle labels - they can be strings, lists, or dicts
            if isinstance(label, list) and len(label) > 0:
                # Extract first item from list
                actual_label = label[0] if isinstance(label[0], str) else str(label[0])
                label_to_dataname[actual_label] = data_col_name
            elif isinstance(label, str) and label:
                label_to_dataname[label] = data_col_name
            elif isinstance(label, dict):
                # Handle multi-language labels
                for lang, text in label.items():
                    if text:
                        label_to_dataname[text] = data_col_name

print(f"✅ Found {len(xml_to_dataname)} XML name mappings")
print(f"✅ Found {len(label_to_dataname)} label mappings")

# --------------------------
# 3️⃣ Fetch data from KoboToolbox
# --------------------------
print("\n📥 Fetching Kobo data...")

response = requests.get(DATA_URL, auth=(KOBO_USERNAME, KOBO_PASSWORD))
response.raise_for_status()

# Read CSV with semicolon separator
df = pd.read_csv(StringIO(response.text), sep=';')

# Clean initial column names
df.columns = df.columns.str.strip().str.replace('"', '')

print(f"✅ Fetched {len(df)} rows and {len(df.columns)} columns from Kobo")

print("\n📋 Original columns:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2d}. {col[:80]}{'...' if len(col) > 80 else ''}")

# --------------------------
# 4️⃣ Replace column names with Data Column Names
# --------------------------
print("\n🔄 Replacing column names with Data Column Names...")

renamed_columns = []

for col in df.columns:
    mapped = False
    
    # Strategy 1: Exact match with label
    if col in label_to_dataname:
        new_name = label_to_dataname[col]
        renamed_columns.append(new_name)
        print(f"  ✓ '{col[:50]}' → '{new_name}'")
        mapped = True
    
    # Strategy 2: Exact match with XML name
    elif col in xml_to_dataname:
        new_name = xml_to_dataname[col]
        renamed_columns.append(new_name)
        print(f"  ✓ '{col}' → '{new_name}'")
        mapped = True
    
    # Strategy 3: Check if any XML name is contained in the column
    else:
        for xml_name, data_col_name in xml_to_dataname.items():
            if xml_name in col:
                renamed_columns.append(data_col_name)
                print(f"  ✓ '{col[:50]}' → '{data_col_name}'")
                mapped = True
                break
    
    # Strategy 4: Check if column is contained in any label
    if not mapped:
        for label, data_col_name in label_to_dataname.items():
            if col in label or label in col:
                renamed_columns.append(data_col_name)
                print(f"  ✓ '{col[:50]}' → '{data_col_name}'")
                mapped = True
                break
    
    # If still no match, keep original
    if not mapped:
        renamed_columns.append(col)
        print(f"  ⚠ '{col[:50]}' (kept as is)")

# Apply new column names
df.columns = renamed_columns

# --------------------------
# 5️⃣ Clean columns for PostgreSQL compatibility
# --------------------------
print("\n🧹 Cleaning columns for PostgreSQL...")

df.columns = (
    df.columns
    .str.strip()
    .str.replace('[^0-9a-zA-Z_]+', '_', regex=True)
    .str.lower()
    .str.replace('_+', '_', regex=True)
    .str.strip('_')
)

# Handle duplicate column names
cols = pd.Series(df.columns)
for dup in cols[cols.duplicated()].unique():
    cols[cols[cols == dup].index.values.tolist()] = [dup + '_' + str(i) if i != 0 else dup for i in range(sum(cols == dup))]
df.columns = cols

print(f"✅ Cleaned {len(df.columns)} columns")

# Display final column names
print("\n📋 Final column names:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2d}. {col}")

# --------------------------
# 6️⃣ Connect to PostgreSQL
# --------------------------
print("\n🔗 Connecting to PostgreSQL...")

connection_string = (
    f"postgresql+psycopg2://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DATABASE}"
)
engine = create_engine(connection_string)

# --------------------------
# 7️⃣ Load data into schema.table
# --------------------------
print(f"\n💾 Loading data into {SCHEMA_NAME}.{TABLE_NAME}...")

with engine.begin() as conn:
    conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};"))
    df.to_sql(TABLE_NAME, conn, schema=SCHEMA_NAME, if_exists="replace", index=False)

print(f"\n✅ Data loaded successfully into {SQL_DATABASE}.{SCHEMA_NAME}.{TABLE_NAME}")
print(f"📊 Total rows loaded: {len(df)}")
print(f"📋 Total columns: {len(df.columns)}")