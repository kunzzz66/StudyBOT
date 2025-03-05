import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # 取得當前目錄的父目錄路徑
DB_PATH = os.path.join(BASE_DIR, "data", "states.db")

def getDbConnection():
    print(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    
    # conn.row_factory = sqlite3.Row
    return conn