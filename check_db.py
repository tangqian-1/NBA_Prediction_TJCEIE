import sqlite3
import os

db_path = r'd:\vs.py\NBA\NBA_Prediction_TJCEIE\data\nba.db'
print(f"数据库路径: {db_path}")
print(f"文件存在: {os.path.exists(db_path)}")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print('\n数据库表:', tables)

for table in tables:
    cursor.execute(f"PRAGMA table_info({table[0]});")
    print(f'\n{table[0]} 表结构:')
    for col in cursor.fetchall():
        print(f'  {col[1]} ({col[2]})')
    
    cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
    count = cursor.fetchone()[0]
    print(f'  记录数: {count}')

conn.close()
