from selenium import webdriver
from bs4 import BeautifulSoup
from requests import get
import time
import getpass
import os
import json
import urllib.request
import shutil
import natsort
import urllib.error
from img2pdf import convert
import sys

erran = ("크롤러에 오류가 발생하여 다운로드를 재시작하려 했으나, 해결이 불가한 오류가 발생하여 크롤러를 종료합니다.\n"
         "만약 지속적으로 동일한 오류가 발생한다면 아래의 내용들을 복사하여 에러 코드를 개발자에게 보내주세요.\n"
         "오류 제보는 더 나은 크롤러를 만드는데 큰 도움이 됩니다."
         "개발자 이메일 주소 : kimch061279@gmail.com")

jsonyn = input("설정 정보를 json 파일에서 불러오시겠습니까? (Y/N) : ")

if jsonyn == 'Y':
    print("파일을 불러오는 중입니다...", end='')
    with open('setting.json', 'rt', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        id = json_data["AccountID"]
        pw = json_data["AccountPW"]
        token = json_data["AccountToken"]
        pdfyn = json_data["Pdfyn"]
    print("완료")

else:
    id = input('레진코믹스 계정의 아이디를 입력하세요 : ')
    print("레진코믹스 계정의 패스워드를 입력하세요")
    pw = getpass.getpass("(비밀번호 입력 창에 입력해도 아무것도 보이지 않는 것은 정상입니다) : ")
    token = input('레진 계정의 토큰 값을 입력하세요 : ')
    pdfyn = input("만화를 PDF 파일로 병합하시겠습니까? (Y/N) : ")

print('레진코믹스 홈페이지에 로그인 중입니다. 잠시만 기다려주세요..')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=2')
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1280x720')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
driver.get('https://www.lezhin.com/ko/login')
delay = 3
driver.implicitly_wait(delay)

driver.find_element_by_id('login-email').send_keys(id)
driver.find_element_by_id('login-password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(3)

while True :
    name = input('만화의 영어 이름을 입력하세요 : ')
    episode = input('다운로드 받을 에피소드의 회차 범위를 지정해주세요\n(입력 예 : 1~3) : ')
    csb = episode
    sgw = csb.split("~")
    h = "0"
    titlel = []
    cutl = []

    try:
        os.mkdir("%s" % (name))
    except:
        pass
    try:
        os.mkdir("%s\\temp" % (name))
    except:
        pass

    os.chdir(name)
    print("만화 정보를 다운로드 및 분석 중입니다...", end="")
    err1 = 0
    while True:
        try:
            for y in range(int(sgw[0]), int(sgw[1]) + 1):
                def download(url, file_name):
                    with open(file_name, "wb") as file:
                        response = get(url)
                        file.write(response.content)
                if __name__ == '__main__':
                    url = "http://cdn.lezhin.com/episodes/%s/%s.json?access_token=%s" % (name, y, token)
                    download(url, "temp\\%s.json" % (y))
            break
        except TimeoutError:
            if err1 == 5:
                print(erran)
                print("에러 내용 : TimeoutError")
                print("(아래 항목에선 토큰 값을 꼭 제거하고 보내주세요)\nURL : ", end='')
                print(url)
                driver.quit()
                sys.exit(1)
            else :
                print("****크롤러에 오류가 발생하여 다운로드를 재시작 하는 중입니다..****")
                print("오류 내용 : TimeoutError")
                err1 += 1
                continue

    for a in range(int(sgw[0]), int(sgw[1])+1):
        with open('temp\\%s.json'%(a), 'rt', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            json_number = json_data["cut"]
            json_title = json_data["title"]
            cut = json_number
            title = json_title

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
        titlel.append(title)
        cutl.append(cut)
        print("완료")

        print("만화 다운로드를 준비 중입니다..")
        err2 = 0
        while True:
            try:
                url = 'https://www.lezhin.com/ko/comic/%s/%s' % (name, a)
                driver.get(url)
                time.sleep(3)

                soup = BeautifulSoup(driver.page_source, "html.parser")
                div_tag = soup.find("div", id="scroll-list")
                l = list()
                for img in div_tag.find_all("img"):
                    l.append(img.get("src").split("/"))
                name_code = l[1][5]
                episode_code = l[1][7]
                break
            except IndexError:
                if err2 == 5:
                    print(erran)
                    print("에러 내용 : IndexError")
                    print("(아래 항목에선 토큰 값을 꼭 제거하고 보내주세요)\nlist : ", end='')
                    print(l)
                    print("name_code : ", end='')
                    print(name_code)
                    print("episode_code : ", end='')
                    print(episode_code)
                    driver.quit()
                    sys.exit(1)
                else:
                   try :
                        print("****오류가 발생하여 다운로드를 다른 방식으로 시도하는 중입니다..****")
                        print("오류 내용 : IndexError")
                        name_code = 0
                        episode_code = 0
                        name_code = l[0][5]
                        episode_code = l[0][7]
                        break
                   except IndexError:
                        continue

            except AttributeError:
                if err2 == 5:
                    print(erran)
                    print("에러 내용 : AttributeError")
                    print("(아래 항목에선 토큰 값을 꼭 제거하고 보내주세요)\nlist : ", end='')
                    print(l)
                    print("name_code : ", end='')
                    print(name_code)
                    print("episode_code : ", end='')
                    print(episode_code)
                    driver.quit()
                    sys.exit(1)
                else:
                    print("****크롤러에 오류가 발생하여 다운로드를 재시작 하는 중입니다..****")
                    print("오류 내용 : AttributeError")
                    err2 += 1
                    continue

        print('-----%s화 다운로드를 시작합니다.-----\n%s화의 총 이미지 수는 %s장입니다.' % (a, a, cut))
        try:
            os.mkdir("%s화 - %s" % (a, title))
        except:
            pass

        for i in range(1, cut + 1):
            print('이미지 %s개 중' % (cut) + " %s" % (i) + '번째 이미지 다운로드 중...', end='')
            urllib.request.urlretrieve("https://cdn.lezhin.com/v2/comics/%s/episodes/%s/contents/scrolls/%s?access_token=%s" % (
            name_code, episode_code, i, token), "%s화 - %s\\%s.png" % (a, title, i))
            print("완료")
            time.sleep(0.1)
        print('%s화 다운로드 완료.' % (a))

    if pdfyn == 'Y':
        h = 0
        g = 0
        print("만화를 PDF로 병합 중입니다..", end='')

        for a in range(int(sgw[0]), int(sgw[1]) + 1):
            title = titlel[h]
            cut = cutl[g]

            outpath1 = "%s화 - %s" % (a, title)
            outpath2 = os.path.dirname(os.path.realpath(__file__))
            outpath3 = os.path.dirname(os.path.realpath('__file__'))

            with open("%s화 - %s.pdf" % (a, title), "wb") as f:
                dir = ('%s화 - %s' % (a, title))
                os.chdir(dir)
                img_list_png = natsort.natsorted([file for file in os.listdir() if file.endswith(".png")])
                pdf = convert(img_list_png)
                f.write(pdf)
                os.chdir('..')
                h += 1
                g += 1
        print("완료")

    print('임시파일 삭제 중...')
    shutil.rmtree(r"temp")
    print('완료!!')

    exi = input("크롤러를 종료할까요? (Y/N) : ")
    if exi == 'Y':
        driver.quit()
        sys.exit(1)
    else:
        os.chdir('..')
        continue