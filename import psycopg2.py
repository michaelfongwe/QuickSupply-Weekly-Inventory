import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    user="postgres",
    password="Doitbig2017@",
    database="Project102"
)
print("Connected!")
conn.close()
