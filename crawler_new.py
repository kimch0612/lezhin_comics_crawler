from requests import get
import json
import urllib.request

name = input("이름을 입력하세요 : ")
episode = input("에피소드 번호를 입력하세요 : ")
token = input("토큰 값을 입력하세요 : ")

for i in range(1, 100):
    print('%s번째 이미지 중' % ('ㅁㄴㅇㄹ') + " %s" % (i) + ' 번째 이미지 다운로드 중...')
    urllib.request.urlretrieve("https://cdn.lezhin.com/v2/comics/%s/episodes/%s/contents/scrolls/%s?access_token=%s" % (name, episode, i, token), "%s.png" % (i))