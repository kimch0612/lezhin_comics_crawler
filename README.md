# Lezhin Comics Crawler (KOREAN ver.)  
****This crawler should only be used for educational, research and personal purposes.****  
****Never use it for illegal purposes****  
****Any responsibility for using this crawler is the responsibility of the user who used it.****  

(Development discontinued) crawler_new-ver : Comic crawler that published after March 10, 2017 (* Multiple downloads not possible)  
(Development discontinued) crawler_old-ver : 2Comic crawler that published after before 10, 2017 (* Multiple downloads possible)  
crawler_selenium-ver : All purchased or free comics can be downloaded (* Multiple downloads possible)  
※ To use this crawler, you need to install the [requests, chromedriver_autoinstaller, tqdm, bs4, natsort, Selenium] modules  

Tested environment  
Windows10 64bit 1909 version, Python 3.8.2  

# Site structure  
LezinComics' cdn structure is as follows  
****Comic that published before March 10, 2017****  
http://cdn.lezhin.com/episodes/(comic_name)/(episode)/contents/(image_number)?access_token=(token) // access to comics image  
http://cdn.lezhin.com/episodes/(comic_name)/(episode)?access_token=(token) // can find the number of episode cuts  
http://cdn.lezhin.com/episodes/(comic_name)?access_token=(token) // can find the number of episodes in the comic and the number of cuts in the episodes.  
2nd and 3rd links are composed in json format.  
The above method shows 404 error for comics uploaded after March 10, 2017 or paid comics that have not been purchased.  
****Comic that published after March 10, 2017****  
https://cdn.lezhin.com/v2/comics/(comic_number)/episodes/(episode_number)/contents/scrolls/(image_number)?access_token=(token)  
Unlike the previous, comics names and episodes are made only of numbers  
The numbers seem to be randomly generated, but the names of the comics are the same for all episodes.  
In the case of episode numbers, just because they came out more recently doesn't mean the numbers are bigger.  
The method to find out the number of cuts of the episode is the same as the method above.  

# How to use it
chawler_old(new)-ver : Run by typing python chawler_old-ver.py (or chawler_new-ver.py) in cmd.  
crawler_selenium-ver : Install the required modules and chrome and run python crawler_selenium-ver.py in cmd.  
English name of comics : Can find it in the URL.
(ex. If comics url is https://www.lezhin.com/ko/comic/xxxxx, 'xxxxx' is English name of comics)  
account.json : You can save account names and passwords, tokens and whether to convert PDFs and recalled automatically when use crawler. 
You can download the above file by going to the Release tab,  
You can install a notepad program such as Notepad ++ and modify it according to your information by referring to the default values.    
Below is a description of the settings in account.json  
AccountID : lezhin comics id (like e-mail)  
AccountPW : lezhin comics pw  
AccountToken : lezhin comics token  
Pdfyn : Whether to merge comics into PDFs  
![KakaoTalk_20200421_183846174](https://user-images.githubusercontent.com/10193967/79850899-82a56d00-83ff-11ea-9940-3724fc2d9b13.png)  

# Screenshot  
![KakaoTalk_20200508_222621117](https://user-images.githubusercontent.com/10193967/81410104-2c645800-917b-11ea-8ce3-4d9b68471d65.png) 
문의 : kimch061279@gmail.com
