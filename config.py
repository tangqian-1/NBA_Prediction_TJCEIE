# -*- coding: utf-8 -*-
"""
NBA比赛预测系统 - 配置文件
包含数据库配置、爬虫配置、机器学习参数等
"""

import os
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).parent

# ==================== 数据库配置 ====================
DATABASE_CONFIG = {
    'type': 'sqlite',
    'path': BASE_DIR / 'data' / 'nba.db',
    'timeout': 30,
    'check_same_thread': False
}

# ==================== 爬虫配置 ====================
CRAWLER_CONFIG = {
    'base_url': 'https://www.basketball-reference.com',
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    },
    'request_delay': 3,  # 请求间隔(秒)，遵守robots.txt
    'max_retries': 3,
    'retry_backoff': [1, 2, 4],  # 重试间隔递增
    'timeout': 30  # 请求超时(秒)
}

# 数据爬取范围
CRAWL_SEASONS = {
    'start_year': 2012,  # 2011-12赛季
    'end_year': 2026     # 2025-26赛季
}

# ==================== NBA球队信息 ====================
TEAM_INFO = {
    'ATL': {'id': '1610612737', 'name': 'Atlanta Hawks', 'city': 'Atlanta', 'name_cn': '亚特兰大老鹰', 'primary_color': '#C8102E', 'secondary_color': '#1D428A'},
    'BOS': {'id': '1610612738', 'name': 'Boston Celtics', 'city': 'Boston', 'name_cn': '波士顿凯尔特人', 'primary_color': '#007A33', 'secondary_color': '#BA9653'},
    'BRK': {'id': '1610612751', 'name': 'Brooklyn Nets', 'city': 'Brooklyn', 'name_cn': '布鲁克林篮网', 'primary_color': '#000000', 'secondary_color': '#FFFFFF'},
    'CHI': {'id': '1610612741', 'name': 'Chicago Bulls', 'city': 'Chicago', 'name_cn': '芝加哥公牛', 'primary_color': '#CE1141', 'secondary_color': '#000000'},
    'CHO': {'id': '1610612766', 'name': 'Charlotte Hornets', 'city': 'Charlotte', 'name_cn': '夏洛特黄蜂', 'primary_color': '#00788C', 'secondary_color': '#1D1160'},
    'CLE': {'id': '1610612739', 'name': 'Cleveland Cavaliers', 'city': 'Cleveland', 'name_cn': '克里夫兰骑士', 'primary_color': '#860038', 'secondary_color': '#FDBB30'},
    'DAL': {'id': '1610612742', 'name': 'Dallas Mavericks', 'city': 'Dallas', 'name_cn': '达拉斯独行侠', 'primary_color': '#00538C', 'secondary_color': '#B8C4CA'},
    'DEN': {'id': '1610612743', 'name': 'Denver Nuggets', 'city': 'Denver', 'name_cn': '丹佛掘金', 'primary_color': '#0E2240', 'secondary_color': '#FEC524'},
    'DET': {'id': '1610612765', 'name': 'Detroit Pistons', 'city': 'Detroit', 'name_cn': '底特律活塞', 'primary_color': '#C8102E', 'secondary_color': '#006BB6'},
    'GSW': {'id': '1610612744', 'name': 'Golden State Warriors', 'city': 'Golden State', 'name_cn': '金州勇士', 'primary_color': '#1D428A', 'secondary_color': '#FFC72C'},
    'HOU': {'id': '1610612745', 'name': 'Houston Rockets', 'city': 'Houston', 'name_cn': '休斯顿火箭', 'primary_color': '#CE1141', 'secondary_color': '#000000'},
    'IND': {'id': '1610612754', 'name': 'Indiana Pacers', 'city': 'Indiana', 'name_cn': '印第安纳步行者', 'primary_color': '#002D62', 'secondary_color': '#FFB612'},
    'LAC': {'id': '1610612746', 'name': 'Los Angeles Clippers', 'city': 'Los Angeles', 'name_cn': '洛杉矶快船', 'primary_color': '#C8102E', 'secondary_color': '#000000'},
    'LAL': {'id': '1610612747', 'name': 'Los Angeles Lakers', 'city': 'Los Angeles', 'name_cn': '洛杉矶湖人', 'primary_color': '#552583', 'secondary_color': '#FDB927'},
    'MEM': {'id': '1610612763', 'name': 'Memphis Grizzlies', 'city': 'Memphis', 'name_cn': '孟菲斯灰熊', 'primary_color': '#5D76A9', 'secondary_color': '#12173F'},
    'MIA': {'id': '1610612748', 'name': 'Miami Heat', 'city': 'Miami', 'name_cn': '迈阿密热火', 'primary_color': '#98002E', 'secondary_color': '#F9A01B'},
    'MIL': {'id': '1610612749', 'name': 'Milwaukee Bucks', 'city': 'Milwaukee', 'name_cn': '密尔沃基雄鹿', 'primary_color': '#00471B', 'secondary_color': '#EEE1C6'},
    'MIN': {'id': '1610612750', 'name': 'Minnesota Timberwolves', 'city': 'Minnesota', 'name_cn': '明尼苏达森林狼', 'primary_color': '#236192', 'secondary_color': '#0C2340'},
    'NOP': {'id': '1610612740', 'name': 'New Orleans Pelicans', 'city': 'New Orleans', 'name_cn': '新奥尔良鹈鹕', 'primary_color': '#0C2340', 'secondary_color': '#E03A3E'},
    'NYK': {'id': '1610612752', 'name': 'New York Knicks', 'city': 'New York', 'name_cn': '纽约尼克斯', 'primary_color': '#006BB6', 'secondary_color': '#F58426'},
    'OKC': {'id': '1610612760', 'name': 'Oklahoma City Thunder', 'city': 'Oklahoma City', 'name_cn': '俄克拉荷马城雷霆', 'primary_color': '#007AC1', 'secondary_color': '#EF3B24'},
    'ORL': {'id': '1610612753', 'name': 'Orlando Magic', 'city': 'Orlando', 'name_cn': '奥兰多魔术', 'primary_color': '#0077C0', 'secondary_color': '#000000'},
    'PHI': {'id': '1610612755', 'name': 'Philadelphia 76ers', 'city': 'Philadelphia', 'name_cn': '费城76人', 'primary_color': '#006BB6', 'secondary_color': '#ED174C'},
    'PHO': {'id': '1610612756', 'name': 'Phoenix Suns', 'city': 'Phoenix', 'name_cn': '菲尼克斯太阳', 'primary_color': '#1D1160', 'secondary_color': '#E56020'},
    'POR': {'id': '1610612757', 'name': 'Portland Trail Blazers', 'city': 'Portland', 'name_cn': '波特兰开拓者', 'primary_color': '#E03A3E', 'secondary_color': '#000000'},
    'SAC': {'id': '1610612758', 'name': 'Sacramento Kings', 'city': 'Sacramento', 'name_cn': '萨克拉门托国王', 'primary_color': '#5A2D81', 'secondary_color': '#6BB9F0'},
    'SAS': {'id': '1610612759', 'name': 'San Antonio Spurs', 'city': 'San Antonio', 'name_cn': '圣安东尼奥马刺', 'primary_color': '#000000', 'secondary_color': '#C4CED4'},
    'TOR': {'id': '1610612761', 'name': 'Toronto Raptors', 'city': 'Toronto', 'name_cn': '多伦多猛龙', 'primary_color': '#CE1141', 'secondary_color': '#000000'},
    'UTA': {'id': '1610612762', 'name': 'Utah Jazz', 'city': 'Utah', 'name_cn': '犹他爵士', 'primary_color': '#002B5C', 'secondary_color': '#F9A01B'},
    'WAS': {'id': '1610612764', 'name': 'Washington Wizards', 'city': 'Washington', 'name_cn': '华盛顿奇才', 'primary_color': '#002B5C', 'secondary_color': '#E31837'}
}

# 球队图标URL模板（使用NBA官方CDN，更稳定可靠）
TEAM_LOGO_URL_TEMPLATE = "https://cdn.nba.com/logos/nba/{team_id}/global/L/logo.svg"
TEAM_LOGO_URL_LARGE = "https://cdn.nba.com/logos/nba/{team_id}/global/L/logo.svg"

# 备用图标URL（使用ESPN的球队图标API）
TEAM_LOGO_ESPN_CDN = "https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/{team_abbr}.png&h=50&w=50"

# ESPN图标缩写特殊映射（ESPN使用球队昵称而非缩写）
ESPN_TEAM_ABBR_MAP = {
    'ATL': 'hawks',     # Atlanta Hawks
    'BOS': 'celtics',   # Boston Celtics
    'BRK': 'nets',      # Brooklyn Nets
    'CHI': 'bulls',     # Chicago Bulls
    'CHO': 'hornets',   # Charlotte Hornets
    'CLE': 'cavs',      # Cleveland Cavaliers
    'DAL': 'mavericks', # Dallas Mavericks
    'DEN': 'nuggets',   # Denver Nuggets
    'DET': 'pistons',   # Detroit Pistons
    'GSW': 'warriors',  # Golden State Warriors
    'HOU': 'rockets',   # Houston Rockets
    'IND': 'pacers',    # Indiana Pacers
    'LAC': 'clippers',  # Los Angeles Clippers
    'LAL': 'lakers',    # Los Angeles Lakers
    'MEM': 'grizzlies', # Memphis Grizzlies
    'MIA': 'heat',      # Miami Heat
    'MIL': 'bucks',     # Milwaukee Bucks
    'MIN': 'timberwolves', # Minnesota Timberwolves
    'NOP': 'orleans',   # New Orleans Pelicans
    'NYK': 'knicks',    # New York Knicks
    'OKC': 'thunder',   # Oklahoma City Thunder
    'ORL': 'magic',     # Orlando Magic
    'PHI': 'sixers',    # Philadelphia 76ers
    'PHO': 'suns',      # Phoenix Suns
    'POR': 'blazers',   # Portland Trail Blazers
    'SAC': 'kings',     # Sacramento Kings
    'SAS': 'spurs',     # San Antonio Spurs
    'TOR': 'raptors',   # Toronto Raptors
    'UTA': 'jazz',      # Utah Jazz - ESPN使用 jazz 而非 uta
    'WAS': 'wizards'    # Washington Wizards
}

# ==================== 机器学习配置 ====================
ML_CONFIG = {
    # K-Means聚类参数
    'clustering': {
        'n_clusters': 4,  # 球队风格分类数
        'max_iter': 300,
        'n_init': 10,
        'random_state': 42
    },
    
    # PCA降维参数
    'pca': {
        'n_components': 0.95,  # 保留95%的方差
        'random_state': 42
    },
    
    # 特征重要性阈值
    'feature_threshold': 0.1,
    
    # 模型评估指标
    'evaluation': {
        'silhouette_threshold': 0.5,  # 轮廓系数阈值
        'variance_threshold': 0.85    # 累计解释方差阈值
    }
}

# ==================== Flask配置 ====================
FLASK_CONFIG = {
    'secret_key': 'nba-prediction-secret-key-change-in-production',
    'debug': True,
    'host': '0.0.0.0',
    'port': 5000
}

# ==================== 日志配置 ====================
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': BASE_DIR / 'logs' / 'nba_prediction.log',
    'max_bytes': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}

# ==================== 数据字段配置 ====================
# 原始特征列表
RAW_FEATURES = [
    'points', 'opponent_points', 'fg_made', 'fg_attempts', 'fg_pct',
    'fg3_made', 'fg3_attempts', 'fg3_pct', 'ft_made', 'ft_attempts', 'ft_pct',
    'rebounds_total', 'assists', 'steals', 'blocks', 'turnovers', 'fouls'
]

# 衍生特征（需要计算的）
DERIVED_FEATURES = [
    'recent_5_avg_points', 'recent_5_avg_points_allowed', 'recent_5_win_pct',
    'home_win_pct', 'away_win_pct',
    'offensive_rating', 'defensive_rating', 'net_rating',
    'pace', 'true_shooting_pct', 'effective_fg_pct',
    'head_to_head_win_pct'
]

# 球队风格标签
TEAM_STYLES = {
    0: '进攻型',
    1: '防守型',
    2: '平衡型',
    3: '快攻型'
}

# ==================== API响应配置 ====================
API_RESPONSE = {
    'success_code': 200,
    'error_codes': {
        400: '参数错误',
        404: '资源不存在',
        500: '服务器错误'
    }
}

# ==================== 路径配置 ====================
PATH_CONFIG = {
    'raw_data': BASE_DIR / 'data' / 'raw',
    'processed_data': BASE_DIR / 'data' / 'processed',
    'logs': BASE_DIR / 'logs',
    'templates': BASE_DIR / 'app' / 'templates',
    'static': BASE_DIR / 'app' / 'static'
}
