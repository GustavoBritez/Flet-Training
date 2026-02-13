from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib


connectionString = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;" 
    "Database=FletLoginDB;"
    "Trusted_Connection=yes;"
)
params = urllib.parse.quote_plus(connectionString)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
Session = sessionmaker(bind=engine)

def obtener_sesion():
    return Session()