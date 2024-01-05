import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

# Funktion zum Abrufen des DataFrames
def get_df():
    file_path = "D:/3441/Documents/Familie/Edgar/Weiterbildungen/Kurse/Python Bootcamp/Projekte/SUN-Artikel-Fetcher/db/SUN 24-001/articles.csv"
    dtypes = {0: str, 1: str}
    df = pd.read_csv(file_path, header=None, dtype=dtypes)
    df = df.drop_duplicates()
    return df

# Verbindung zur MySQL-Datenbank herstellen
server = "127.0.0.1"
user = "root"
pw = "12345678"
DB_name = "db"

mydb = mysql.connector.connect(
    host=server,
    user=user,
    passwd=pw,
    database=DB_name
)

# DataFrame abrufen
df = get_df()

# MySQL-Engine erstellen
engine = create_engine(f"mysql+mysqlconnector://{user}:{pw}@{server}/{DB_name}")

# DataFrame in die MySQL-Tabelle einfügen
table_name = "articles"  # Ersetze "deine_tabelle" durch den tatsächlichen Tabellennamen
df.columns = ['article_no', 'article_name']  # Ersetze durch die tatsächlichen Spaltennamen

# DataFrame in die MySQL-Tabelle einfügen
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# Verbindung schließen
mydb.close()
