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
print("레진코믹스 계정의 패스워드를 입력하세요")
pw = getpass.getpass("(비밀번호 입력 창에 입력해도 아무것도 보이지 않는 것은 정상입니다) : ") # 패스워드가 cmd 창에 띄워지는 것을 방지하기 위해 getpass를 사용
token = input('레진 계정의 토큰 값을 입력하세요 : ')
print('잠시만 기다려주세요..')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=2')
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
driver.get('https://www.lezhin.com/ko/login')
delay = 3
driver.implicitly_wait(delay)
"""
크롬을 headless 모드로 실행하되, cmd 창에는 log level 2 이상만 표시되게 하며,
창의 해상도는 1920x1080 (==FHD)로 실행되게 하고,
그래픽 가속을 끈채로 웹 사이트에 접속
"""

driver.find_element_by_id('login-email').send_keys(id)
driver.find_element_by_id('login-password').send_keys(pw) # 위에서 입력받은 아이디와 패스워드를 필드에 입력해줌
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(5) # 페이지가 로딩되기 전에 크롤러가 작동하는 것을 방지

while True :
    name = input('만화의 영어 이름을 입력하세요 : ')
    episode = input('다운로드 받을 에피소드의 회차 범위를 지정해주세요\n(입력 예 : 1~3) : ')
    csb = episode # episode에 입력받은 내용을 csb에 저장을 하되, char 형식의 포맷을 str 형식으로 변환
    sgw = csb.split("~") # 위에서 입력받은 내용을 ~을 기준으로 앞과 뒤를 나눠서 리스트에 저장

    try:
        os.mkdir("%s" % (name)) # 폴더를 생성하되 위에서 입력받은 만화의 영어 이름을 폴더의 이름으로 지정해서 생성
    except:
        pass # 만약 이미 존재하는 폴더라면 스킵
    try:
        os.mkdir("%s\\temp" % (name)) # json 임시 파일을 저장해둘 폴더 생성
    except:
        pass

    print("만화 정보를 다운로드 중입니다...", end="")
    for y in range(int(sgw[0]), int(sgw[1]) + 1):
        def download(url, file_name):
            with open(file_name, "wb") as file:
                response = get(url)
                file.write(response.content)
        if __name__ == '__main__':
            url = "http://cdn.lezhin.com/episodes/%s/%s.json?access_token=%s" % (name, y, token) # 임시파일 다운로드
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
            """
            위에서 다운로드한 json 파일에서 cut의 수를 불러와서 cut 변수에 저장하고
            title을 불러와서 title 변수에 저장
            """

        print("만화 다운로드를 준비 중입니다..")

        url = 'https://www.lezhin.com/ko/comic/%s/%s' % (name, a)
        driver.get(url) # 크롬으로 위 링크에 접속
        time.sleep(5) # 페이지가 로딩되기 전에 크롤러가 작동하는 것을 방지

        soup = BeautifulSoup(driver.page_source, "html.parser")
        div_tag = soup.find("div", id="scroll-list")
        l = list()
        for img in div_tag.find_all("img"):
            l.append(img.get("src").split("/"))
        name_code = l[1][5]
        episode_code = l[1][7]
        """
        bs4를 이용해서 html를 파싱하는데, div태그 안에 있는 scroll-list 내용물을 찾는다
        list()라 하는 리스트를 선언하고, l이라 하는 변수에 저장
        그리고 img라고 하는 태그를 찾고, 해당 태그들을 /를 기준으로 나눠서 리스트에 저장한다
        이렇게 저장된 리스트는 2차원 리스트이므로 2차원 리스트에 맞게 name_code와 episode_code를 찾아 각각 저장을 한다
        그냥 만화 페이지에 접속하면 위의 태그들이 뜨지 않으므로 selenium으로 접속해서 우선 이미지들을 불러올 필요가 있다
        """

        print('-----%s화 다운로드를 시작합니다.-----\n%s화의 총 이미지 수는 %s장입니다.' % (a, a, cut))

        try:
            os.mkdir("%s화 - %s" % (a, title))
        except:
            pass

        for i in range(1, cut + 1):
            print('이미지 %s개 중' % (cut) + " %s" % (i) + '번째 이미지 다운로드 중...', end='')
            urllib.request.urlretrieve("https://cdn.lezhin.com/v2/comics/%s/episodes/%s/contents/scrolls/%s?access_token=%s" % (
            name_code, episode_code, i, token), "%s화 - %s\\%s.png" % (a, title, i)) # 입력받고 파싱한 정보들을 바탕으로 이미지 다운로드
            print("완료")
        
        print('%s화 다운로드 완료.' % (a))

        print("pdf 생성 중...", end='') # 이미지들을 pdf로 병합
        dir = "%s화 - %s" % (a, title)
        prefix = ""
        min_range = 1
        max_range = cut
        os.chdir(dir)
        suffix = ".png"
        out_fname = "%s화 - %s.pdf" % (a, title)

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

    print('임시파일 삭제 중...') # 처음에 만들었던 임시파일 폴더를 삭제
    os.chdir(name)
    shutil.rmtree(r"temp")
    print('완료!!')
    os.chdir('..')

    exi = input("크롤러를 종료할까요? (Y/N) : ")
    if exi == 'Y':
        driver.quit() # 좀비 프로세서를 방지하기 위해 크롬 드라이버 세션을 킬
        break
    else:
        continue # While문 처음으로 돌아감
