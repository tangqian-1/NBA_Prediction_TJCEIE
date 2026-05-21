#!/usr/bin/env python3
"""
生成今日比赛模拟数据（季后赛模式）
"""
import sqlite3
from datetime import datetime

DB_PATH = 'data/nba.db'

# 球队信息（使用标准缩写）
TEAMS = {
    'ATL': {'id': '1610612737', 'name': 'Atlanta Hawks'},
    'BOS': {'id': '1610612738', 'name': 'Boston Celtics'},
    'BRK': {'id': '1610612751', 'name': 'Brooklyn Nets'},
    'CHI': {'id': '1610612741', 'name': 'Chicago Bulls'},
    'CHO': {'id': '1610612766', 'name': 'Charlotte Hornets'},
    'CLE': {'id': '1610612739', 'name': 'Cleveland Cavaliers'},
    'DAL': {'id': '1610612742', 'name': 'Dallas Mavericks'},
    'DEN': {'id': '1610612743', 'name': 'Denver Nuggets'},
    'DET': {'id': '1610612765', 'name': 'Detroit Pistons'},
    'GSW': {'id': '1610612744', 'name': 'Golden State Warriors'},
    'HOU': {'id': '1610612745', 'name': 'Houston Rockets'},
    'IND': {'id': '1610612754', 'name': 'Indiana Pacers'},
    'LAC': {'id': '1610612746', 'name': 'LA Clippers'},
    'LAL': {'id': '1610612747', 'name': 'Los Angeles Lakers'},
    'MEM': {'id': '1610612763', 'name': 'Memphis Grizzlies'},
    'MIA': {'id': '1610612748', 'name': 'Miami Heat'},
    'MIL': {'id': '1610612749', 'name': 'Milwaukee Bucks'},
    'MIN': {'id': '1610612750', 'name': 'Minnesota Timberwolves'},
    'NOP': {'id': '1610612740', 'name': 'New Orleans Pelicans'},
    'NYK': {'id': '1610612752', 'name': 'New York Knicks'},
    'OKC': {'id': '1610612760', 'name': 'Oklahoma City Thunder'},
    'ORL': {'id': '1610612753', 'name': 'Orlando Magic'},
    'PHI': {'id': '1610612755', 'name': 'Philadelphia 76ers'},
    'PHO': {'id': '1610612756', 'name': 'Phoenix Suns'},
    'POR': {'id': '1610612757', 'name': 'Portland Trail Blazers'},
    'SAC': {'id': '1610612758', 'name': 'Sacramento Kings'},
    'SAS': {'id': '1610612759', 'name': 'San Antonio Spurs'},
    'TOR': {'id': '1610612761', 'name': 'Toronto Raptors'},
    'UTA': {'id': '1610612762', 'name': 'Utah Jazz'},
    'WAS': {'id': '1610612764', 'name': 'Washington Wizards'}
}

# 今日比赛（西部决赛）
# 2026年5月21日 西部决赛
TODAY_GAMES = [
    ('MIN', 'DEN'),  # 森林狼 vs 掘金（西部决赛）
]

def get_max_id():
    """获取最大ID"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT MAX(id) FROM team_game_stats")
    result = cur.fetchone()
    conn.close()
    return result[0] if result[0] else 0

def delete_today_games():
    """删除今日的比赛数据（包括主队和客队记录）"""
    today = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # 删除所有今日的记录，包括主队和客队
    cur.execute("DELETE FROM team_game_stats WHERE game_date = ?", (today,))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    print(f"DEBUG: 删除了 {deleted} 条记录")
    return deleted

def save_games(recs):
    """保存比赛数据到数据库"""
    if not recs:
        return 0
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cnt = 0
    for r in recs:
        try:
            cur.execute('''INSERT INTO team_game_stats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', r)
            if cur.rowcount > 0:
                cnt += 1
        except Exception as e:
            print(f"保存失败: {e}")
            print(f"数据: {r}")
    conn.commit()
    conn.close()
    return cnt

def create_today_games():
    """创建今日比赛数据"""
    today = datetime.now().strftime('%Y-%m-%d')
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"今日日期: {today}")
    
    all_recs = []
    rec_id = get_max_id() + 1  # 从最大ID之后开始
    
    for home_abbr, away_abbr in TODAY_GAMES:
        if home_abbr in TEAMS and away_abbr in TEAMS:
            base_game_id = f"GAME_{today}_{home_abbr}_{away_abbr}"
            
            # 主队记录
            all_recs.append((
                rec_id,  # id
                base_game_id + '_HOME',  # game_id (主队)
                today,  # game_date
                "2025-26",  # season
                TEAMS[home_abbr]['id'],  # team_id
                home_abbr,  # team_abbr
                TEAMS[home_abbr]['name'],  # team_name
                TEAMS[away_abbr]['id'],  # opponent_id
                away_abbr,  # opponent_abbr
                TEAMS[away_abbr]['name'],  # opponent_name
                1,  # is_home (主队)
                'P',  # result
                0,  # points
                0,  # opponent_points
                0,  # point_diff
                0,  # fg_made
                0,  # fg_attempts
                0.0,  # fg_pct
                0,  # fg3_made
                0,  # fg3_attempts
                0.0,  # fg3_pct
                0,  # ft_made
                0,  # ft_attempts
                0.0,  # ft_pct
                0,  # rebounds
                0,  # assists
                0,  # steals
                0,  # blocks
                0,  # turnovers
                0,  # fouls
                0,  # plus_minus
                now  # created_at
            ))
            rec_id += 1
            
            # 客队记录
            all_recs.append((
                rec_id,  # id
                base_game_id + '_AWAY',  # game_id (客队)
                today,  # game_date
                "2025-26",  # season
                TEAMS[away_abbr]['id'],  # team_id
                away_abbr,  # team_abbr
                TEAMS[away_abbr]['name'],  # team_name
                TEAMS[home_abbr]['id'],  # opponent_id
                home_abbr,  # opponent_abbr
                TEAMS[home_abbr]['name'],  # opponent_name
                0,  # is_home (客队)
                'P',  # result
                0,  # points
                0,  # opponent_points
                0,  # point_diff
                0,  # fg_made
                0,  # fg_attempts
                0.0,  # fg_pct
                0,  # fg3_made
                0,  # fg3_attempts
                0.0,  # fg3_pct
                0,  # ft_made
                0,  # ft_attempts
                0.0,  # ft_pct
                0,  # rebounds
                0,  # assists
                0,  # steals
                0,  # blocks
                0,  # turnovers
                0,  # fouls
                0,  # plus_minus
                now  # created_at
            ))
            rec_id += 1
    
    return all_recs

def verify_games():
    """验证数据库中的比赛"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    today = datetime.now().strftime('%Y-%m-%d')
    cur.execute("SELECT * FROM team_game_stats WHERE game_date = ? AND is_home = 1", (today,))
    
    games = []
    for row in cur.fetchall():
        games.append(dict(row))
    
    conn.close()
    return games

if __name__ == '__main__':
    print("=== 生成今日比赛数据（季后赛模式）===")
    print("2026年5月21日 - NBA西部决赛")
    
    # 删除今日已有的比赛数据
    deleted = delete_today_games()
    print(f"已删除 {deleted} 条旧记录")
    
    # 创建比赛记录
    recs = create_today_games()
    print(f"创建 {len(recs)} 条比赛记录")
    
    # 保存到数据库
    cnt = save_games(recs)
    print(f"已保存 {cnt} 条记录")
    
    # 验证
    games = verify_games()
    print(f"\n数据库中今日比赛 ({len(games)} 场):")
    for g in games:
        print(f"  {g['team_abbr']} vs {g['opponent_abbr']}")
        print(f"  赛事: 西部决赛")
