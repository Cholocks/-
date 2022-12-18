from tkinter import * #사람들이 보기 좋게 창을 만들 수 있게 하는 역할
import requests #크롤링 기능(html 문서 가져옴)
from bs4 import BeautifulSoup #html문서를 예쁘게 만들어주고, find함수를 쓸수 있게 함
win = Tk() #프로그램 창 생성

win.title('로또 당첨 확인기 ver: 1.0') #프로그램 창의 제목
win.geometry('300x100') #프로그램 실행시 창 크기
win.option_add('*Font', '나눔 20') #글꼴

ent = Entry(win) #입력창 생성
ent.pack() 

url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=883' #로또 당첨 번호 사이트

def click(): #이게 핵심이죠 ㅋㅋㅋ 이거 만든다고 힘들었습니다 ㅋㅋㅋ 역할: 버튼 눌렀을때 지시 사항
    global url #전역 변수 url를 가져다 쓰겠다.
    lotto_number = ent.get() #로또 ***회
    real_url = url.split('=') #변수 이름을 real_url로 하고 url을 '='을 기준으로 나누 겠다. ('='을 기준으로 나누면 '='은 없어지고 list 형식이 됨.)
    real_url[2] = lotto_number #나누었을때 3번째에 있는 리스트를 입력한 걸로 바꾼다.(ent.get())
    rreal_url = '='.join(real_url) #완전한 URL 이제 입력창에 번호 입력하면 주소가 정상적으로 생성됨
    
    html = requests.get(rreal_url) #1차적으로 크롤링 함.
    real_html = BeautifulSoup(html.text) #크롤링 한걸 텍스트 형식으로 나타내고 BeautifulSoup을 이용하여 html문서를 예쁘게 다듬어준다.
    txt = real_html.find('div',attrs = {'class','win_result'}).get_text() #txt라는 변수 이름을 설정하고 real_html 즉, html 문서에서 'div' ,'class', 'win_result'를 찾는다.
    real_txt = txt.split('\n') #로또 당첨 번호, 원하는 것을 찾아서 '\n'을 기준으로 나누어 준다. 그리고 나누어 준 것을 real_txt에 담아준다.
    print('로또 당첨 번호:',real_txt[7]+',',real_txt[8]+',',real_txt[9]+',',real_txt[10]+',',real_txt[11]+',',real_txt[12])
    print('보너스 번호:', real_txt[-4])
    

btn = Button(win) #버튼 생성
btn.config(text='로또 당첨 버튼 확인') #버튼 제목
btn.config(command=click) #버튼을 눌렀을때 지시사항 실행, 여기서는 click이라는 사용자 지정 함수를 실행 하라는 것이 지시사항이다.
btn.pack()
    
win.mainloop() #프로그램 실행