import sqlite3
conn = sqlite3.connect('data/nba.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute('SELECT * FROM team_game_stats')
rows = cur.fetchall()
print('所有记录:')
for row in rows:
    print(f"ID: {row['id']}, game_id: {row['game_id']}, team_abbr: {row['team_abbr']}, is_home: {row['is_home']}, game_date: {row['game_date']}")
conn.close()