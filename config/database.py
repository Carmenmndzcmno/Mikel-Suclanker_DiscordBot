import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")
user = os.getenv("DB_USER", "postgres")
password = os.getenv("DB_PASSWORD", "password")
database = os.getenv("DB_NAME", "mikel_sumclanker")
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"