from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent.parent.resolve()
DATABASE_DIR = ROOT_DIR / "database" / "tasks.db"

def get_connection():
    return sqlite3.connect(DATABASE_DIR)
