# 포켓몬 게임 개발 시작(240929)
# source code
from bs4 import BeautifulSoup as bs
import requests
import re
import dload
import pandas as pd

for i in range(1,500):
    html = requests.get(f'https://pokemonkorea.co.kr/pokedex/view/{i}')
    if html.status_code == 200: #코드 응답이 정상이면 실행
        soup = bs(html.text, 'html.parser') # 2. bs html.parser의 text parser로 설정
        image = soup.find('div', attrs={"class":"col-lg-6 col-12"}).img["src"]
        dload.save(image,f'C:\python\pkmon_game\image\{i}.png')

for i in range(500,1000):
    html = requests.get(f'https://pokemonkorea.co.kr/pokedex/view/{i}')
    if html.status_code == 200: #코드 응답이 정상이면 실행
        soup = bs(html.text, 'html.parser') # 2. bs html.parser의 text parser로 설정
        image = soup.find('div', attrs={"class":"col-lg-6 col-12"}).img["src"]
        dload.save(image,f'C:\python\pkmon_game\image\{i}.png')

for i in range(1000,1253):
    html = requests.get(f'https://pokemonkorea.co.kr/pokedex/view/{i}')
    if html.status_code == 200: #코드 응답이 정상이면 실행
        soup = bs(html.text, 'html.parser') # 2. bs html.parser의 text parser로 설정
        image = soup.find('div', attrs={"class":"col-lg-6 col-12"}).img["src"]
        dload.save(image,f'C:\python\pkmon_game\image\{i}.png')


texts = []

## 1. 크롤링하는 site url을 requests.get('url')으로 설정
for i in range(1,500):
    html = requests.get(f'https://pokemonkorea.co.kr/pokedex/view/{i}') #1~1252
    # 2. 데이터 받아오기
    if html.status_code == 200: #코드 응답이 정상이면 실행
        soup = bs(html.text, 'html.parser') # 3. bs html.parser의 text parser로 설정
        text = soup.find('h3').getText()    # 4. soup.find로 <h3> tag를 찾아서 getText()로 그중 text만 추출
        texts.append(text)

for i in range(500,1001):
    html = requests.get(f'https://pokemonkorea.co.kr/pokedex/view/{i}') #1~1252
    # 2. 데이터 받아오기
    if html.status_code == 200: #코드 응답이 정상이면 실행
        soup = bs(html.text, 'html.parser') # 3. bs html.parser의 text parser로 설정
        text = soup.find('h3').getText()
        texts.append(text)

for i in range(1001,1253):
    html = requests.get(f'https://pokemonkorea.co.kr/pokedex/view/{i}') #1~1252
    # 2. 데이터 받아오기
    if html.status_code == 200: #코드 응답이 정상이면 실행
        soup = bs(html.text, 'html.parser') # 3. bs html.parser의 text parser로 설정
        text = soup.find('h3').getText()
        texts.append(text)

df = pd.DataFrame(texts,columns=['Name'])
df.to_csv('포켓몬이름.csv',encoding='utf-8',index=False)