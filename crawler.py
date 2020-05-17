import time
import getpass
import os
import json
import urllib.request
import shutil
import natsort
import urllib.error
import sys
import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
from requests import get
from tqdm import tqdm
from img2pdf import convert

print("Welcome To Lezhin Comics Crawler - Selenium version.\n"
      "Crawler Ver : Dev 4.4")

erran = ("크롤러에 오류가 발생하여 다운로드를 재시작하려 했으나, 해결이 불가한 오류가 발생하여 크롤러를 종료합니다.\n"
         "만약 지속적으로 동일한 오류가 발생한다면 아래의 내용들을 복사하여 에러 코드를 개발자에게 보내주세요.\n"
         "오류 제보는 더 나은 크롤러를 만드는데 큰 도움이 됩니다.\n"
         "개발자 이메일 주소 : kimch061279@gmail.com")

if os.path.isfile("account.json"):
    print("json 파일에서 설정값을 불러오는 중입니다...", end="")
    with open('account.json', 'rt', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        id = json_data["AccountID"]
        pw = json_data["AccountPW"]
        token = json_data["AccountToken"]
        pdfyn = json_data["Pdfyn"]
    print("완료")

elif not os.path.isfile("account.json"):
    id = input('레진코믹스 계정의 아이디를 입력하세요 : ')
    print("레진코믹스 계정의 패스워드를 입력하세요")
    pw = getpass.getpass("(비밀번호 입력 창에 입력해도 아무것도 보이지 않는 것은 정상입니다) : ")
    token = input('레진 계정의 토큰 값을 입력하세요 : ')
    pdfyn = input("만화를 PDF 파일로 병합하시겠습니까? (Y/N) : ")

print("Chrome Driver를 다운로드 하는 중입니다..", end='')
chromedriver_autoinstaller.install()
print("완료")

print('****레진코믹스 홈페이지에 로그인 중입니다.****\n잠시만 기다려주세요..')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=2')
options.add_argument('window-size=1080x1920')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://www.lezhin.com/ko/login')
delay = 2
driver.implicitly_wait(delay)

driver.find_element_by_id('login-email').send_keys(id)
driver.find_element_by_id('login-password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(2)

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
    print("만화를 다운로드하기 위해 준비 중입니다..", end="")
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
                shutil.rmtree(r"temp")
                driver.quit()
                sys.exit(1)
            else :
                print("****크롤러에 오류가 발생하여 다운로드를 재시작 하는 중입니다..****")
                print("오류 내용 : TimeoutError")
                err1 += 1
                continue
        except IndexError:
            print("\n크롤러에 오류가 발생했습니다.\n회차를 입력할 때 잘못 입력하지 않았는지 확인해주세요.\n크롤러를 종료합니다.")
            print("오류 내용 : IndexError")
            shutil.rmtree(r"temp")
            driver.quit()
            sys.exit(1)
    print("완료\n"
          "(참고) 제목으로 사용할 수 없는 단어는 자동으로 제거된 상태로 저장됩니다.")
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
        if title.find("？") != -1:
            title = title.replace("？", "")
        if title.find("<") != -1:
            title = title.replace("<", "")
        if title.find(">") != -1:
            title = title.replace(">", "")
        if title.find("|") != -1:
            title = title.replace("|", "")
        if title.find("！") != -1:
            title = title.replace("！", "!")
        titlel.append(title)
        cutl.append(cut)

        err2 = 0
        while True:
            try:
                url = 'https://www.lezhin.com/ko/comic/%s/%s' % (name, a)
                driver.get(url)
                time.sleep(2)

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
                    print("name_code : " + name_code)
                    print("episode_code : " + episode_code)
                    shutil.rmtree(r"temp")
                    driver.quit()
                    sys.exit(1)
                else:
                   try :
                        name_code = 0
                        episode_code = 0
                        name_code = l[0][5]
                        episode_code = l[0][7]
                        break
                        err2 += 1
                   except IndexError:
                        err2 += 1
                        continue

            except AttributeError:
                if err2 == 5:
                    print(erran)
                    print("에러 내용 : AttributeError")
                    print("(아래 항목에선 토큰 값을 꼭 제거하고 보내주세요)\nlist : ", end='')
                    print(l)
                    print("name_code : " + name_code)
                    print("episode_code : " + episode_code)
                    shutil.rmtree(r"temp")
                    driver.quit()
                    sys.exit(1)
                else:
                    err2 += 1
                    continue

        try:
            os.mkdir("%s화 - %s" % (a, title))
        except:
            pass
        try:
            while True:
                for i in tqdm(range(1, cut + 1), desc="%s화" %(a)):
                    urllib.request.urlretrieve("https://cdn.lezhin.com/v2/comics/%s/episodes/%s/contents/scrolls/%s?access_token=%s" % (
                    name_code, episode_code, i, token), "%s화 - %s\\%s.png" % (a, title, i))
                    time.sleep(0.1)
                print("\r")
                break
        except urllib.error.HTTPError:
            print("다운로드에 오류가 발생하여 재시도하는 중입니다.."
                  "오류 내용 : urllib.error.HTTPError")
            continue

    if pdfyn == 'Y' or pdfyn == 'y' or pdfyn == '':
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

    print('임시파일 삭제 중...', end='')
    shutil.rmtree(r"temp")
    print('완료!!')

    while True:
        exi = input("크롤러를 종료할까요? (Y/N) : ")
        if exi == 'Y' or exi == 'y' or exi == '':
            driver.quit()
            sys.exit(1)
        elif exi == 'N' or exi == 'n':
            os.chdir('..')
            break
        else:
            print("문자를 다시 입력해주세요.")
            continue
    continue
