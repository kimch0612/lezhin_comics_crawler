from requests import get
import json
import urllib.request
import os
from PIL import Image

print('Welcome to Lezhin Comics Crawler')
print("※ 2017년 3월 10일 이후에 연재된 만화를 다운받을 수 있는 크롤러입니다")

"""
토큰은 숫자와 소문자 영어로 구성되어 있으며 xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 형식으로 이루어졌습니다
이름의 경우에는 다운 받으려는 만화로 들어가면 URL에 나와있습니다
만화의 숫자 코드와 에피소드의 숫자 코드, 레진의 계정 토큰 값은 만화에서 F12를 누르고,
크롬 기준 sources탭에서 cdn.lezhin.com -> v2 -> comics에 들어가면 알 수 있습니다
comics 바로 아래에 있는 폴더가 만화의 숫자 코드이며 그 안에 episodes 폴더가 있는데,
거기로 들어가면 에피소드의 숫자 코드를 알 수 있습니다
이미지 파일의 링크를 복사해서 보면 위의 정보들을 한 눈에 볼 수 있습니다
https://cdn.lezhin.com/v2/comics/만화_숫자코드/episodes/에피_숫자코드/contents/scrolls/이미지_번호?access_token=토큰_값
"""

token = input("레진 계정의 토큰 값을 입력하세요 : ")
name = input("만화의 영어 이름을 입력하세요 : ")
name_code = input("만화의 숫자 코드를 입력하세요\n(숫자는 총 16자리입니다) : ")

while True :
    episode = input("에피소드 회차를 입력하세요\n(ex. 24화라면 24만 입력) : ")
    episode_code = input("에피소드의 숫자 코드를 입력하세요\n(숫자는 총 16자리입니다) : ")

    try:
        os.mkdir("%s"%(name))
    except:
        pass

    print("만화 정보를 다운로드 중입니다...", end="")
    def download(url, file_name):
        with open(file_name, "wb") as file:
            response = get(url)
            file.write(response.content)

    if __name__ == '__main__':
            url = "http://cdn.lezhin.com/episodes/%s/%s.json?access_token=%s" % (name, episode, token)
            download(url, "%s\\%s.json" % (name, episode))

    with open('%s\\%s.json'%(name, episode), 'rt', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            json_number = json_data["cut"]
            json_title = json_data["title"]
            cut = json_number
            title = json_title

    print("완료")
    print('-----%s화 다운로드를 시작합니다.-----\n%s화의 총 이미지 수는 %s장입니다.'%(episode, episode, cut))

    try:
        os.mkdir("%s\\%s화 - %s"%(name, episode, title))
    except:
        pass

    for i in range(1, cut+1):
        print('%s번째 이미지 중' % (cut) + " %s" % (i) + ' 번째 이미지 다운로드 중...', end='')
        urllib.request.urlretrieve("https://cdn.lezhin.com/v2/comics/%s/episodes/%s/contents/scrolls/%s?access_token=%s" % (name_code, episode_code, i, token), "%s\\%s화 - %s\\%s.png" % (name, episode, title, i))
        print("완료")
    print('%s화 다운로드 완료.' % (episode))

    dir = "%s화 - %s" % (episode, title)
    print("pdf 생성 중...", end='')
    prefix = ""
    min_range = 1
    max_range = cut
    os.chdir(name)
    os.chdir(dir)
    suffix = ".png"
    out_fname = "%s화 - %s.pdf" % (episode, title)

    images = []
    for z in range(min_range, max_range + 1):
        fname = prefix + str(z) + suffix
        im = Image.open(fname)
        if im.mode == "RGBA":
            im = im.convert("RGB")
        images.append(im)
    os.chdir('..')
    images[0].save(out_fname, save_all=True, quality=100, append_images=images[1:])
    os.chdir('..')
    print("완료")
    os.remove('%s\\%s.json' % (name, episode))

    exi = input("크롤러를 종료할까요? (Y/N) : ")
    if exi == 'Y':
        break
    else:
        continue

