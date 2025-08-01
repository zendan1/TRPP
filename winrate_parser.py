import argparse
import re
import requests
import json
from bs4 import BeautifulSoup

def get_winrate(champion_slug):
    url = f"https://u.gg/lol/champions/{champion_slug}/build"
    headers={"User-Agent":"Mozilla/5.0"}
    resp=requests.get(url, headers=headers)
    resp.raise_for_status()
    html=resp.text
    match=re.search(r'window.__SSR_DATA__\s*=\s*(\{.*?\})\s*window.__APOLLO_STATE__', html, re.S)
    if not match:
        raise ValueError("Unable to find SSR data")
    data=json.loads(match.group(1))
    rank_key=[k for k in data if k.startswith('rankings_')][0]
    role_stats=data[rank_key]['data']
    best_role=None
    best_pick=0
    best_winrate=0
    for role,stats in role_stats.items():
        pick=stats.get('pick_rate',0)
        if pick>best_pick:
            best_pick=pick
            best_role=role
            best_winrate=stats.get('win_rate')
    return best_role, best_winrate

def main():
    parser=argparse.ArgumentParser(description='Fetch champion winrate from u.gg')
    parser.add_argument('champion', help='Champion slug e.g. ahri')
    args=parser.parse_args()
    role, winrate = get_winrate(args.champion)
    print(f"{args.champion} {role} win rate: {winrate}%")

if __name__=='__main__':
    main()
