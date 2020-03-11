from selenium import webdriver
from bs4 import BeautifulSoup
from requests import get
import time
import getpass
import os
import json
import urllib.request
import shutil
from PIL import Image

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

id = input('레진코믹스 계정의 아이디를 입력하세요 : ')
pw = input("레진코믹스 계정의 패스워드를 입력하세요 : ")
token = input('레진 계정의 토큰 값을 입력하세요 : ')

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.lezhin.com/ko/login')
delay = 3
driver.implicitly_wait(delay)

driver.find_element_by_id('login-email').send_keys(id)
driver.find_element_by_id('login-password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(5)

while True :
    name = input('만화의 영어 이름을 입력하세요 : ')
    episode = input('다운로드 받을 에피소드의 회차 범위를 지정해주세요\n(입력 예 : 1~3) : ')
    csb = episode
    sgw = csb.split("~")

    try:
        os.mkdir("%s" % (name))
    except:
        pass
    try:
        os.mkdir("%s\\temp" % (name))
    except:
        pass

    print("만화 정보를 다운로드 중입니다...", end="")
    for y in range(int(sgw[0]), int(sgw[1]) + 1):
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
            cut = json_number

        print("만화 다운로드 준비 중입니다..")

        url = 'https://www.lezhin.com/ko/comic/%s/%s' % (name, a)
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        div_tag = soup.find("div", id="scroll-list")
        l = list()
        for img in div_tag.find_all("img"):
            l.append(img.get("src").split("/"))
        print(l)
        name_code = l[1][5]
        episode_code = l[1][7]

        print('-----%s화 다운로드를 시작합니다.-----\n%s화의 총 이미지 수는 %s장입니다.' % (a, a, cut))

        try:
            os.mkdir("%s화" % (a))
        except:
            pass

        for i in range(1, cut + 1):
            print('%s개 이미지 중' % (cut) + " %s" % (i) + '번째 이미지 다운로드 중...')
            urllib.request.urlretrieve("https://cdn.lezhin.com/v2/comics/%s/episodes/%s/contents/scrolls/%s?access_token=%s" % (
            name_code, episode_code, i, token), "%s화\\%s.png" % (a, i))
        
        print('%s화 다운로드 완료.' % (a))

        print("pdf 변환 중...", end='')
        dir = "%s화" % (a)
        prefix = ""
        min_range = 1
        max_range = cut
        os.chdir(dir)
        suffix = ".png"
        out_fname = "%s화.pdf" % (a)

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
    os.chdir('..')
