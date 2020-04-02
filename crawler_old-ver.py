from requests import get
import json
import urllib.request
import os
import shutil
from PIL import Image

print('Welcome to Lezhin Comics Crawler')
print("※ 2017년 3월 10일 이후에 나온 만화는 다운로드가 불가합니다")

"""
토큰은 숫자와 소문자 영어로 구성되어 있으며 xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 형식으로 이루어졌습니다
이름의 경우에는 다운 받으려는 만화로 들어가면 URL에 나와있습니다
레진의 계정 토큰 값은 아무 만화나 들어가고 크롬 기준으로 F12 버튼을 눌러 html 분석기를 켠 뒤에
token 이라고 검색하면 나오는 값을 사용하면 됩니다
"""

token = input('레진 계정의 토큰 값을 입력하세요 : ')

while True :
    name = input('만화의 영문 이름을 입력하세요 : ')
    episode = input('다운로드 받을 에피소드의 회차 범위를 지정해주세요\n(입력 예 : 1~3) : ')
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

    print("만화 정보를 다운로드 중입니다...", end="")
    for y in range(int(sgw[0]), int(sgw[1])+1):
        def download(url, file_name):
            with open(file_name, "wb") as file:
                response = get(url)
                file.write(response.content)
        if __name__ == '__main__':
            url = "http://cdn.lezhin.com/episodes/%s/%s.json?access_token=%s" % (name, y, token)
            download(url, "%s\\temp\\%s.json" % (name, y))
    print("완료")

    for a in range(int(sgw[0]), int(sgw[1])+1):
        os.chdir(name)
        with open('temp\\%s.json'%(a), 'rt', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            json_number = json_data["cut"]
            json_title = json_data["title"]
            title = json_title
            cut = json_number

            print("제목에 사용할 수 없는 단어가 있는지 확인 중입니다..", end="")
            # 만약 title에 폴더 이름으로 사용할 수 없는 단어가 있다면 제거
            if title.find(":") != -1:
                title = title.replace(":", "")
            if title.find("\"") != -1:
                title = title.replace("\"", "")
            if title.find("\\") != -1:
                title = title.replace("\\", "")
            if title.find("/") != -1:
                title = title.replace("/", "")
            if title.find("*") != -1:
                title = title.replace("*", "")
            if title.find("?") != -1:
                title = title.replace("?", "")
            if title.find("<") != -1:
                title = title.replace("<", "")
            if title.find(">") != -1:
                title = title.replace(">", "")
            if title.find("|") != -1:
                title = title.replace("|", "")
            print("완료")

        print('-----%s화 다운로드를 시작합니다.-----\n%s화의 총 이미지 수는 %s장입니다.'%(a, a, cut))

        try:
            os.mkdir("%s화 - %s"%(a, title))
        except:
            pass

        home = str(a) + "화"
        for i in range(1, cut+1):
            print('%s번째 이미지 중'%(cut) + " %s"%(i) + ' 번째 이미지 다운로드 중...', end='')
            urllib.request.urlretrieve("http://cdn.lezhin.com/episodes/%s/%s/contents/%s?access_token=%s"%(name, a, i, token), "%s화 - %s\\%s.png"%(a, title, i))
            print("완료")
        print('%s화 다운로드 완료.'%(a))

        dir = "%s화 - %s"%(a, title)
        print("pdf 생성 중...", end='')
        prefix = ""
        min_range = 1
        max_range = cut
        os.chdir(dir)
        suffix = ".png"
        out_fname = "%s화 - %s.pdf"%(a, title)

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

    print('임시파일 삭제 중...')
    os.chdir(name)
    shutil.rmtree(r"temp")
    print('완료!!')

    exi = input("크롤러를 종료할까요? (Y/N) : ")
    if exi == 'Y':
        break
    else:
        continue