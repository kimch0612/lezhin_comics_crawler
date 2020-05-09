# 레진 코믹스 크롤러
****이 크롤러는 교육, 연구, 개인적인 목적으로만 사용하셔야 합니다****  
****절대 불법적인 용도로 사용하지 말아주세요****  
****이 크롤러를 사용하며 발생한 모든 일의 책임은 이 크롤러를 사용한 사용자에게 있습니다****  

(개발 중단) crawler_new-ver : 2017년 3월 10일 이후에 연재된 만화 크롤러 (* 복수 다운로드 불가능)  
(개발 중단) crawler_old-ver : 2017년 3월 10일 이전에 연재됐던 만화 크롤러 (* 복수 다운로드 가능)  
crawler_selenium-ver : 구입했거나 무료인 만화는 모두 다운로드 가능 (* 복수 다운로드 가능)  
※ 이 크롤러를 사용하려면 requests, chromedriver_autoinstaller, tqdm, bs4, natsort, Selenium 모듈을 설치해야 함  

구동이 확인된 환경  
Windows10 64bit 1909 버전, Python 3.8.2   

# 사이트 구조  
레진코믹스의 cdn 구조는 다음과 같다  
****2017년 3월 10일 이전에 올라온 만화****  
http://cdn.lezhin.com/episodes/만화이름/회차수/contents/사진번호?access_token=토큰값 // 만화 이미지에 접근  
http://cdn.lezhin.com/episodes/만화이름/회차수?access_token=토큰값 // 해당 에피소드 컷 수를 알 수 있음  
http://cdn.lezhin.com/episodes/만화이름?access_token=토큰값 // 해당 만화의 에피소드의 개수와 해당 에피소드들의 컷 수를 알 수 있음  
2, 3번째 링크는 json 형식으로 구성되어있음  
위의 방식은 2017년 3월 10일 이후에 올라온 만화나 구입하지 않은 유료 만화의 경우 404 오류가 뜸  
****2017년 3월 10일 이후에 올라온 만화****  
https://cdn.lezhin.com/v2/comics/(만화_번호)/episodes/(에피소드_번호)/contents/scrolls/(이미지_번호)?access_token=(토큰_값)  
기존과 다르게 만화의 이름과 에피소드의 번호가 암호화가 됐음  
에피소드 번호는 무작위로 생성되는 듯 하지만 만화의 이름은 모든 에피소드가 동일함  
에피소드 번호의 경우에는 최신화라고 해서 무조건 숫자가 큰 것은 아니며 해당 에피소드의 컷 수를 알아내는 방법은 위의 방법과 동일함  

# 크롤러 사용 방법  
chawler_old(new)-ver : cmd에서 python chawler_old-ver.py (또는 chawler_new-ver.py) 를 입력해주면 실행 됨  
crawler_selenium-ver : 필수 모듈과 크롬을 설치하고 cmd에서 python crawler_selenium-ver.py 를 입력해주면 실행 됨  
만화의 영어 이름 : URL에서 확인 가능함 
(ex. 만화 링크가 https://www.lezhin.com/ko/comic/xxxxx 라면, xxxxx가 영어 이름)  
account.json : json 파일에 계정과 비밀번호, 토큰값, PDF 변환 여부 등 설정값을 저장해서 자동으로 불러올 수 있게 해주는 파일  
위 파일은 Release 탭에 가면 받을 수 있으며,  
Notepad++ 와 같은 메모장 프로그램을 설치해서 기본으로 적혀있는 값을 참고하여 자신의 정보에 맞게 수정을 해주면 됨  
아래의 내용은 setting.json 파일에 있는 설정 값들에 대한 설명임  
AccountID : 레진코믹스 id (이메일 형식)  
AccountPW : 레진코믹스 pw  
AccountToken : 레진코믹스 계정 토큰 값  
Pdfyn : 만화를 PDF로 병합할지 여부  
![KakaoTalk_20200421_183846174](https://user-images.githubusercontent.com/10193967/79850899-82a56d00-83ff-11ea-9940-3724fc2d9b13.png)  

# 스크린샷  
![KakaoTalk_20200508_222621117](https://user-images.githubusercontent.com/10193967/81410104-2c645800-917b-11ea-8ce3-4d9b68471d65.png) 
문의 : kimch061279@gmail.com
