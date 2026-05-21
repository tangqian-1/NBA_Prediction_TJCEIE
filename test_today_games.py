#!/usr/bin/env python3
"""测试今日比赛数据"""

import sys
from datetime import datetime

sys.path.insert(0, '.')

from data_repository import get_today_games

print("=== 测试 get_today_games() ===")
print(f"当前日期: {datetime.now().strftime('%Y-%m-%d')}")

games = get_today_games()
print(f"\n返回的比赛数量: {len(games)}")

for i, game in enumerate(games, 1):
    print(f"\n比赛 {i}:")
    print(f"  game_id: {game.get('game_id')}")
    print(f"  game_date: {game.get('game_date')}")
    print(f"  home_team: {game.get('home_team')}")
    print(f"  home_team_name: {game.get('home_team_name')}")
    print(f"  home_logo_url: {game.get('home_logo_url')}")
    print(f"  away_team: {game.get('away_team')}")
    print(f"  away_team_name: {game.get('away_team_name')}")
    print(f"  away_logo_url: {game.get('away_logo_url')}")
