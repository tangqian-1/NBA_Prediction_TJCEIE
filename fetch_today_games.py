#!/usr/bin/env python3
"""
获取今日NBA比赛数据
"""
import sqlite3
import requests
import time
from datetime import datetime

DB_PATH = 'data/nba.db'
API = 'https://site.api.espn.com/apis/site/v2/sports/basketball/nba'
teams = {}

def init_teams():
    """初始化球队信息"""
    global teams
    print("正在加载球队信息...")
    try:
        r = requests.get(f'{API}/teams', timeout=15)
        print(f"HTTP状态码: {r.status_code}")
        data = r.json()
        
        for sport in data.get('sports', []):
            for lg in sport.get('leagues', []):
                for td in lg.get('teams', []):
                    t = td.get('team', {})
                    teams[t.get('abbreviation')] = {'id': t.get('id'), 'name': t.get('displayName')}
        print(f"已加载 {len(teams)} 支球队信息")
    except Exception as e:
        print(f"加载球队信息失败: {e}")

def fetch_today_games():
    """获取今日比赛"""
    today = datetime.now().strftime('%Y%m%d')
    print(f"正在获取 {today} 的比赛...")
    
    # 尝试多个日期（今天、昨天、明天）
    for offset in [0, -1, 1]:
        try_date = (datetime.now() + timedelta(days=offset)).strftime('%Y%m%d')
        print(f"  尝试日期: {try_date}")
        
        try:
            r = requests.get(f'{API}/scoreboard?dates={try_date}', timeout=5)
            print(f"  HTTP状态码: {r.status_code}")
            
            if r.status_code == 200:
                data = r.json()
                events = data.get('events', [])
                print(f"  返回比赛数: {len(events)}")
                if events:
                    return events, try_date
        except requests.exceptions.Timeout:
            print(f"  请求超时")
        except Exception as e:
            print(f"  获取失败: {e}")
        
        time.sleep(1)
    
    return [], today

def parse_game(event):
    """解析单场比赛"""
    game_id = event.get('id')
    d = event.get('date', '')[:10]
    comp = event.get('competitions', [{}])[0]
    cs = comp.get('competitors', [])
    if len(cs) != 2:
        return []
    
    home = None
    for c in cs:
        if c.get('homeAway') == 'home':
            home = c.get('team', {}).get('abbreviation')
    
    recs = []
    for i, c in enumerate(cs):
        t = c.get('team', {})
        ta = t.get('abbreviation')
        if ta not in teams:
            continue
        oc = cs[1-i]
        oa = oc.get('team', {}).get('abbreviation')
        p, op = c.get('score'), oc.get('score')
        
        # 处理未开始或进行中的比赛
        if p is None or op is None:
            p, op = 0, 0
            result = 'P'  # P表示进行中或未开始
        else:
            result = 'W' if int(p) > int(op) else ('L' if int(p) < int(op) else 'T')
        
        gd = datetime.strptime(d, '%Y-%m-%d')
        season = f"{gd.year}-{str(gd.year+1)[-2:]}" if gd.month >= 10 else f"{gd.year-1}-{str(gd.year)[-2:]}"
        
        recs.append((
            f"{game_id}_{ta}", d, season,
            teams[ta]['id'], ta, teams[ta]['name'],
            teams.get(oa, {}).get('id', ''), oa, teams.get(oa, {}).get('name', ''),
            ta == home if home else i == 0,
            result,
            int(p), int(op), int(p)-int(op),
            None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None,
            int(p)-int(op), 'espn_api'
        ))
    return recs

def save_games(recs):
    """保存比赛数据到数据库"""
    if not recs:
        return 0
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cnt = 0
    for r in recs:
        try:
            cur.execute('''INSERT OR REPLACE INTO team_game_stats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', r)
            if cur.rowcount > 0:
                cnt += 1
        except Exception as e:
            print(f"保存比赛失败: {e}")
    conn.commit()
    conn.close()
    return cnt

def get_today_games_from_db():
    """从数据库获取今日比赛"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    today = datetime.now().strftime('%Y-%m-%d')
    cur.execute("""
        SELECT * FROM team_game_stats 
        WHERE game_date = ? AND is_home = 1
        ORDER BY game_date
    """, (today,))
    
    games = []
    for row in cur.fetchall():
        games.append(dict(row))
    
    conn.close()
    return games

if __name__ == '__main__':
    from datetime import timedelta
    
    print("=== 获取今日NBA比赛 ===")
    
    # 初始化球队信息
    init_teams()
    
    # 获取今日比赛
    events, date_used = fetch_today_games()
    print(f"找到比赛数: {len(events)} (日期: {date_used})")
    
    # 解析并保存
    all_recs = []
    for e in events:
        all_recs.extend(parse_game(e))
    
    if all_recs:
        cnt = save_games(all_recs)
        print(f"已保存 {cnt} 条比赛记录")
    else:
        print("没有可保存的比赛数据")
        
        # 如果没有数据，创建一些模拟数据
        print("\n创建模拟比赛数据...")
        sample_teams = ['LAL', 'GSW', 'BOS', 'MIA', 'DEN', 'PHX']
        sample_recs = []
        today = datetime.now().strftime('%Y-%m-%d')
        
        for i in range(0, len(sample_teams), 2):
            home_abbr = sample_teams[i]
            away_abbr = sample_teams[i+1] if i+1 < len(sample_teams) else 'UTA'
            
            if home_abbr in teams and away_abbr in teams:
                game_id = f"SIM_{today}_{home_abbr}_{away_abbr}"
                sample_recs.append((
                    f"{game_id}_{home_abbr}", today, "2025-26",
                    teams[home_abbr]['id'], home_abbr, teams[home_abbr]['name'],
                    teams[away_abbr]['id'], away_abbr, teams[away_abbr]['name'],
                    True, 'P', 0, 0, 0,
                    None, None, None, None, None, None, None, None, None,
                    None, None, None, None, None, None, 0, 'simulated'
                ))
                sample_recs.append((
                    f"{game_id}_{away_abbr}", today, "2025-26",
                    teams[away_abbr]['id'], away_abbr, teams[away_abbr]['name'],
                    teams[home_abbr]['id'], home_abbr, teams[home_abbr]['name'],
                    False, 'P', 0, 0, 0,
                    None, None, None, None, None, None, None, None, None,
                    None, None, None, None, None, None, 0, 'simulated'
                ))
        
        if sample_recs:
            cnt = save_games(sample_recs)
            print(f"已创建 {cnt} 条模拟比赛记录")
    
    # 验证
    games = get_today_games_from_db()
    print(f"\n数据库中今日比赛: {len(games)}")
    for g in games:
        status = '进行中' if g['result'] == 'P' else ('已结束' if g['result'] in ['W', 'L'] else '未知')
        print(f"  {g['game_date']} {g['team_abbr']} vs {g['opponent_abbr']} - {status}")
