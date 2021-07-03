# 컴활 일정 조사 앱
# 2021.07.02 전대룡

import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

# 창 생성
win = tk.Tk()
win.title('상공회의소 시험장 확인 - PITCA')
win.geometry('800x600')

# selenium 설정
driver = webdriver.Chrome('/Users/jeondaelyong/Documents/python/web_crawling/chromedriver')

# 상설검정페이지 요청 및 구문 분석
url = 'https://license.korcham.net/ex/dailyExamPlaceConf.do'
resp = requests.get(url)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, 'html.parser')

# 웹 드라이버 페이지 요청
driver.get('https://license.korcham.net/')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/ul/li[2]/a')

# 종목선택 데이터 추출
sel_item = soup.find('select', id='selectJmcd')
cmb_item_opts = sel_item.find_all('option')
cmb_item_code = [one['value'] for one in cmb_item_opts]
cmb_item_txt = [one.text for one in cmb_item_opts]


# 종목 선택 시 값 전달
def select_item(event):
    sel = cmb_item.get()
    idx = cmb_item_txt.index(sel)
    print(sel, cmb_item_code[idx])

    # time.sleep(0.1)
    sel_cb = Select(driver.find_element_by_id('selectJmcd'))
    sel_cb.select_by_visible_text(sel)



# 위젯 추가
str_item = tk.StringVar()
cmb_item = ttk.Combobox(win, width=20, textvariable=str)
cmb_item['value'] = cmb_item_txt
cmb_item.bind('<<ComboboxSelected>>', select_item)


# 위젯 표시
cmb_item.pack()


# 창 표
win.mainloop()
