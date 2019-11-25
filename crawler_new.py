from requests import get
import json
import urllib.request

name = input("이름을 입력하세요 : ")
name1 = input("숫자 형식의 이름을 입력하세요 : ")
episode = input("에피소드 번호를 입력하세요 : ")
chapter = input("에피소드 숫자를 입력하세요 : ")
token = input("토큰 값을 입력하세요 : ")


def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


if __name__ == '__main__':
        url = "http://cdn.lezhin.com/episodes/%s/%s.json?access_token=%s" % (name, chapter, token)
        download(url, "%s.json" % (chapter))

with open('%s.json'%(chapter), 'rt', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        json_number = json_data["cut"]
        cut = json_number

for i in range(1, cut+1):
    print('%s번째 이미지 중' % (cut) + " %s" % (i) + ' 번째 이미지 다운로드 중...')
    urllib.request.urlretrieve("https://cdn.lezhin.com/v2/comics/%s/episodes/%s/contents/scrolls/%s?access_token=%s" % (name1, episode, i, token), "%s.png" % (i))