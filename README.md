# lezhin_comics_crawler

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

