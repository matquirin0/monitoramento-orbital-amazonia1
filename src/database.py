import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    db = os.getenv("DB_NAME")
    url = f"postgresql://{user}:{password}@{host}/{db}"
    return create_engine(url)

def insert_passes(pass_list):
    engine = get_engine()
    with engine.begin() as conn:
        query = text("""
                     INSERT INTO pass_predictions
                         (id_norad, id_gs, start_utc, end_utc, max_elevation, duration_seconds)
                     VALUES (:id_norad, :id_gs, :start_utc, :end_utc, :max_elevation, :duration_seconds)
                     """)
        for p in pass_list:
            conn.execute(query, p)
    print(f"[DATABASE] {len(pass_list)} passagens gravadas via SQLAlchemy!")