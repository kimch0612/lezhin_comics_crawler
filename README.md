# lezhin_comics_crawler
**###### **해당 크롤러를 불법적 목적으로 사용하지 말아주세요
이 크롤러를 사용하며 발생한 모든 일의 책임은 사용자에게 있습니다****

crawler_new-ver : 2017년 3월 10일 이후에 연재된 만화 크롤러

crawler_old-ver : 2017년 3월 10일 이전에 연재됐던 만화 크롤러

※ 이 크롤러를 사용하려면 requests 모듈을 설치해야 함

구동이 확인된 환경

Windows10 64bit 1909 버전, Python 3.8.0


레진코믹스의 cdn 구조는

http://cdn.lezhin.com/episodes/만화이름/회차수/contents/사진번호?access_token=토큰값 // 만화 이미지에 접근

http://cdn.lezhin.com/episodes/만화이름/회차수?access_token=토큰값 // 해당 에피소드 컷 수를 알 수 있음

http://cdn.lezhin.com/episodes/만화이름?access_token=토큰값 // 해당 만화의 에피소드의 개수와 해당 에피소드들의 컷 수를 알 수 있음

2, 3번째 링크는 json 형식으로 구성되어있음


위의 방식은 2017년 3월 10일 이후에 올라온 만화나 구입하지 않은 유료 만화의 경우에도 404 오류가 뜸


# 2017년 3월 10일 이후에 올라온 만화를 크롤링 하는 방법

cdn 주소의 구성 방식은 다음과 같다
https://cdn.lezhin.com/v2/comics/(만화 번호)/episodes/(에피소드 번호)/contents/scrolls/(이미지 번호)?access_token=(토큰 값)

기존과 다르게 만화의 이름과 에피소드의 번호가 암호화가 됐음

에피소드 번호는 무작위로 생성되는 듯 하지만 만화의 이름은 모든 에피소드가 동일함

에피소드 번호의 경우에는 최신화라고 해서 무조건 숫자가 큰 것은 아니며 해당 에피소드의 컷 수를 알아내는 방법은 위의 방법과 동일함
