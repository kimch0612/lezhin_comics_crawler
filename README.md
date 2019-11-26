# lezhin_comics_crawler

crawler_new-ver : 2017년 3월 10일 이후에 연재된 만화 크롤러

crawler_old-ver : 2017년 3월 10일 이전에 연재됐던 만화 크롤러

※ 이 크롤러를 사용하려면 아래의 조건이 필요함
1. Python 3.8.0
2. requests 모듈 설치

레진코믹스의 cdn 구조는

http://cdn.lezhin.com/episodes/만화이름/회차수/contents/사진번호?access_token=토큰값 // 만화 이미지에 접근

http://cdn.lezhin.com/episodes/만화이름/회차수?access_token=토큰값 // 해당 에피소드 컷 수를 알 수 있음

http://cdn.lezhin.com/episodes/만화이름?access_token=토큰값 // 해당 만화의 에피소드의 개수와 해당 에피소드들의 컷 수를 알 수 있음

5와 6번째 줄의 경우에는 json 형식으로 저장되어 있음


위의 방식은 2017년 3월 10일 이후에 올라온 만화는 404 오류가 뜨며 접근이 불가능함

단, json 파일은 접근 가능함

구입하지 않은 유료 만화의 경우에도 404 오류가 뜸

**###### **2017년 3월 10일 이후에 올라온 만화를 크롤링 하는 방법****

https://cdn.lezhin.com/v2/comics/(만화 번호)/episodes/(에피소드 번호)/contents/scrolls/(이미지 번호)?access_token=(토큰 값)&purchased=true

기존과 다르게 만화의 이름과 에피소드의 번호가 암호화가 됐음

만화의 이름은 만화마다 다르긴 하지만 같은 만화라면 전부 동일하지만 에피소드의 번호는 모두 무작위 숫자로 추정됨

에피소드 번호의 경우에는 최신화라고 해서 무조건 숫자가 큰 것은 아님

해당 에피소드의 컷 수를 알아내는 방법은 위의 방법과 동일함

~~또한 에피소드의 랜덤 숫자 또한 위의 방식으로 접근이 가능할 것으로 보임~~

바로 위의 정보는 불가능한 것으로 확인됨