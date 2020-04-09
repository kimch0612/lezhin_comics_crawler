# 레진 코믹스 크롤러
****이 크롤러는 교육, 연구적인 목적으로만 사용하셔야 합니다****

****절대 불법적인 용도로 사용하지 말아주세요****

****이 크롤러를 사용하며 발생한 모든 일의 책임은 이 크롤러를 사용한 사용자에게 있습니다****

crawler_selenium-ver (추천) : 2017년 3월 10일 이후에 연재된 만화 크롤러 (* 복수 다운로드 가능)

crawler_new-ver : 2017년 3월 10일 이후에 연재된 만화 크롤러 (* 복수 다운로드 불가능)

crawler_old-ver : 2017년 3월 10일 이전에 연재됐던 만화 크롤러 (* 복수 다운로드 가능)


※ 이 크롤러를 사용하려면 requests, PIL, [bs4, Selenium(셀레니움 크롤러만 해당)] 모듈을 설치해야 함

구동이 확인된 환경

Windows10 64bit 1909 버전, Python 3.8.0


# 17년 3월 10일 이전에 올라온 만화

레진코믹스의 cdn 구조는 다음과 같다

http://cdn.lezhin.com/episodes/만화이름/회차수/contents/사진번호?access_token=토큰값 // 만화 이미지에 접근

http://cdn.lezhin.com/episodes/만화이름/회차수?access_token=토큰값 // 해당 에피소드 컷 수를 알 수 있음

http://cdn.lezhin.com/episodes/만화이름?access_token=토큰값 // 해당 만화의 에피소드의 개수와 해당 에피소드들의 컷 수를 알 수 있음

2, 3번째 링크는 json 형식으로 구성되어있음  

위의 방식은 2017년 3월 10일 이후에 올라온 만화나 구입하지 않은 유료 만화의 경우 404 오류가 뜸


# 2017년 3월 10일 이후에 올라온 만화

cdn 주소의 구성 방식은 다음과 같다

https://cdn.lezhin.com/v2/comics/(만화_번호)/episodes/(에피소드_번호)/contents/scrolls/(이미지_번호)?access_token=(토큰_값)

기존과 다르게 만화의 이름과 에피소드의 번호가 암호화가 됐음

에피소드 번호는 무작위로 생성되는 듯 하지만 만화의 이름은 모든 에피소드가 동일함

에피소드 번호의 경우에는 최신화라고 해서 무조건 숫자가 큰 것은 아니며 해당 에피소드의 컷 수를 알아내는 방법은 위의 방법과 동일함

# 크롤러 사용 방법

crawler_selenium-ver : 해당 크롤러가 있는 경로에 Chrome Driver를 둬야 함

(ex. C:\에 crawler_selenium-ver.py 파일이 있다면 chromedriver.exe 파일도 C:\에 있어야 함)

이후 cmd에서 python crawler_selenium-ver.py 를 입력해주면 실행 됨

※ 크롬 드라이버의 다운로드 및 사용 방법은 검색 바람


chawler_old(new)-ver : cmd에서 python chawler_old-ver.py (또는 chawler_new-ver.py) 를 입력해주면 실행 됨

실행 되면 크롤러가 안내하는 대로 따르면 됨  
# PDF 병합 관련  
위 크롤러는 만화를 PDF로 병합해주는 기능을 지원하고 있습니다.  
하지만 PIL 라이브러리의 한계로 병합 기능을 사용하게 되면 메모리 점유율이 엄청나게 높아지게 됩니다.  
그렇기 때문에 많은 이미지를 다운로드 및 병합을 할 경우 PDF 병합 기능 사용은 지양해주시기 바랍니다.  
메모리 점유율이 높아지다 보면  memory error가 발생할 가능성이 있습니다.

# 스크린샷  
![스크린샷(45)](https://user-images.githubusercontent.com/10193967/78167958-462ec300-748a-11ea-87a5-bd110bad7e96.png)  
문의 : kimch061279@gmail.com
