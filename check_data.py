import sqlite3

conn = sqlite3.connect('data/nba.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("SELECT * FROM team_game_stats")
rows = cur.fetchall()

print(f"总记录数: {len(rows)}")
for row in rows:
    print(f"\nID: {row['id']}")
    print(f"game_id: {row['game_id']}")
    print(f"game_date: {row['game_date']}")
    print(f"team_abbr: {row['team_abbr']}")
    print(f"opponent_abbr: {row['opponent_abbr']}")
    print(f"is_home: {row['is_home']}")
    print(f"result: {row['result']}")

conn.close()
