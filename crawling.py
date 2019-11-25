from requests import get
import json
import urllib.request
import os
import shutil
from img2pdf import convert

print('Welcome to Lezhin Comics Crawler')
print("※ 2017년 3월 10일 이후에 나온 만화는 다운로드가 불가합니다")


def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


name = input('만화의 영문 이름을 입력하세요 : ')
episode = input('다운로드 받을 에피소드의 회차 범위를 지정해주세요\n(입력 예 : 1~3) : ')
token = input('레진 계정의 토큰값을 입력하세요 : ')
csb = episode
sgw = csb.split("~")

try:
    os.mkdir("%s"%(name))
except:
    pass
try:
    os.mkdir("%s\\temp"%(name))
except:
    pass

for a in range(int(sgw[0]), int(sgw[1])+1):
    if __name__ == '__main__':
        url = "http://cdn.lezhin.com/episodes/%s/%s.json?access_token=%s" % (name, a, token)
        download(url, "%s\\temp\\%s.json" % (name, a))

    with open('%s\\temp\\%s.json'%(name, a), 'rt', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        json_number = json_data["cut"]
        cut = json_number

    print('%s화 다운로드를 시작합니다.\n%s화의 총 컷 수는 %s장입니다.'%(a, a, cut))

    try:
        os.mkdir("%s\\%s화"%(name, a))
    except:
        pass

    for i in range(1, cut+1):
        print('%s번째 컷 중'%(cut) + " %s"%(i) + ' 번째 컷 다운로드 중...')
        urllib.request.urlretrieve("http://cdn.lezhin.com/episodes/%s/%s/contents/%s?access_token=%s"%(name, a, i, token), "%s\\%s화\\%s.png"%(name, a, i))
    print('%s화 다운로드 완료.'%(a))

print('임시폴더 삭제 중...')
shutil.rmtree(r"%s\\temp"%(name))
print('완료!!')