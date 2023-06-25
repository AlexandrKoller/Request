import requests
import json

all_hero_url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(all_hero_url)
hero_list = json.loads(response.text)


def get_hero_intelligence(name_hero):
    for hero in hero_list:
        if hero['name'] == name_hero:
            int = hero['powerstats']['intelligence']
            return int
def hero_max_int(hero_list):
    int_list = []
    for hero in hero_list:
        int = get_hero_intelligence(hero)
        int_list.append(int)
    max_int = max(int_list)
    int_index = int_list.index(max_int)
    return hero_list[int_index]


you_hero_list = ['Hulk', 'Captain America', 'Thanos']
print(f'Самым умным оказался: {hero_max_int(you_hero_list)}')

