import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import scrolledtext as scl
from tkinter import font
from tkinter import Menu
from tkinter import *
import os
# import time

# 메인 윈도우: win --------------------------------------------------------------------------------------------------------------------------------------------------------
win = tk.Tk()
win.config(padx = 10, pady = 10)
win.title("파이썬 GUI로 나만의 일기장 만들기")
win.resizable(False, False) # GUI 메인 창 사이즈 고정
photo = PhotoImage(file = "로고.png")
win.wm_iconphoto(False, photo)
win.title('로고')

#### 메뉴바: START -------------------------------------------------------------------------------------------------
menu_bar = Menu(win)
win.config(menu = menu_bar)

setting_menu = Menu(menu_bar, tearoff = 0)
def produce_about():
    msg.showinfo('제작', '제작자: 박수현 \n제작 일자: 2024년 5~6월')
def produce():
    return(produce_about())
setting_menu.add_command(label = '제작', command = produce)
def produce_intent():
    msg.showinfo('제작 의도', '오늘 했던 일과와 생각들, 그리고 해야 할 일과 마무리 한 일을 한 눈에 정리하고 싶었습니다. \n이러한 생각을 바탕으로 \'나만의 일기장 만들기\'를 제작하게 되었습니다.')
def produce():
    return(produce_intent())
setting_menu.add_command(label = '제작 의도', command = produce_intent)

file_save_menu = Menu(menu_bar, tearoff = 0)
def file_save_root():
    msg.showinfo('파일 저장 위치', '파일이 저장되는 위치는 %s입니다'% os.getcwd())
def save_root():
    return(file_save_root())
file_save_menu.add_command(label = '저장 위치', command = save_root)

menu_bar.add_cascade(label = '기본 설정', menu = setting_menu)
menu_bar.add_cascade(label = '파일 저장', menu = file_save_menu)
#### 메뉴바: END -------------------------------------------------------------------------------------------------

#### '오늘의 날짜' 선택: START -------------------------------------------------------------------------------------------------
date_font = tk.font.Font(family = '맑은 고딕', size = 18, weight = 'bold')
date = ttk.Label(win, text="오늘의 날짜", font = date_font) # '오늘의 날짜' 추가
date.grid(column = 0, row = 0) # '오늘의' 배치

font_date = tk.font.Font(family = '맑은 고딕', size = 13) 

year_number = tk.StringVar() # 연도를 선택하면 저장할 문자열 변수
year = ttk.Combobox(win, width = 5, textvariable = year_number, state = 'readonly', font = font_date) # 연도 선택
year['value'] = (2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040)
year.grid(column = 1, row = 0)
year.current(0) # 처음 표시되는 숫자를 '2024'로 설정
year_kor = ttk.Label(win, text="년  ", font = font_date) # '년' 추가
year_kor.grid(column = 2, row = 0) # '년' 배치

month_number = tk.StringVar() # 월을 선택하면 저장할 문자열 변수
month = ttk.Combobox(win, width = 5, textvariable = month_number, state = 'readonly', font = font_date) # 월 선택
month['value'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
month.grid(column = 3, row = 0)
month.current(0) # 처음 표시되는 숫자를 '1'로 설정
month_kor = ttk.Label(win, text="월  ", font = font_date) # '월' 추가
month_kor.grid(column = 4, row = 0) # '월' 배치

day_number = tk.StringVar() # 일을 선택하면 저장할 문자열 변수
day = ttk.Combobox(win, width = 5, textvariable = day_number, state = 'readonly', font = font_date) # 일 선택
day['value'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
day.grid(column = 5, row = 0)
day.current(0) # 처음 표시되는 숫자를 '1'로 설정
day_kor = ttk.Label(win, text="일  ", font = font_date) # '일' 추가
day_kor.grid(column = 6, row = 0) # '일' 배치

week_number = tk.StringVar() # 요일을 선택하면 저장할 문자열 변수
week = ttk.Combobox(win, width = 5, textvariable = week_number, state = 'readonly', font = font_date) # 요일 선택
week['value'] = ('월', '화', '수', '목', '금', '토', '일')
week.grid(column = 7, row = 0)
week.current(0) # 처음 표시되는 글자를 '월'로 설정
week_kor = ttk.Label(win, text="요일  ", font = font_date) # '요일' 추가
week_kor.grid(column = 8, row = 0) # '요일' 배치

gap_3 = ttk.Label(win, text = '                                                     ')
gap_3.grid(column = 9, row = 0) # 배치를 위해

year.focus() # 연도를 선택하는 곳에 커서 위치
#### '오늘의 날짜' 선택: END -------------------------------------------------------------------------------------------------

tabControl = ttk.Notebook(win) #'TO-DO'와 '일기장'이 들어갈 Tab Control 생성 - win의 하위
tabControl.grid(column = 0, row = 1, sticky = 'WE', columnspan = 12, padx = 5, pady = 5) # 탭 가시화
######## TODO 작성란: START -----------------------------------------------------------------------------------------
todo = ttk.Frame(tabControl) # 'TO-DO'가 들어갈 tab 만들기
tabControl.add(todo, text = 'TO-DO') # 'TO-DO' 탭 추가

todo_label_font = tk.font.Font(family = "맑은 고딕", size = 14, weight = 'bold')
todo_label = ttk.Label(todo, text ='오늘 할 일', font = todo_label_font) # '오늘 할 일' 텍스트 추가
todo_label.grid(column = 0, row = 0, sticky = tk.W, padx = 5, pady = 5) # '오늘 할 일' 배치

add_label_font = tk.font.Font(family = "맑은 고딕", size = 12)
add_label = ttk.Label(todo, text = '추가하기: ', font = add_label_font) # '추가하기: ' 텍스트 추가
add_label.grid(column = 0, row = 1, sticky = tk.W, padx = 5, pady = 5) # '추가하기: ' 배치

add_text = tk.StringVar() # 할 일을 입력하면 저장할 문자열 변수
add = ttk.Entry(todo, textvariable = add_text, width = 90) # 할 일 입력하기
add.grid(column = 1, row = 1, columnspan = 7)

# '추가' 버튼의 자리를 undo 탭으로 옮김 - undo에 추가해야 해서, undo가 생성되고 난 이후로 옮기기

gap_1 = ttk.Label(todo, text = ' ')
gap_1.grid(column = 0, row = 2) # 공백 한 줄 띄우기 위해

############ UNDO 작성란: START -----------------------------------------------------------------------------------------
ttk.Label(todo, text = '미완료한 일').grid(column = 0, row = 3, sticky = tk.W, padx = 5, pady = 5) # '미완료한 일' 추가하기
undo = tk.Listbox(todo, width = 40, height = 10) # '미완료한 일'을 추가할 Listbox 생성
undo.grid(column = 0, row = 4, sticky = 'WENS', columnspan = 3, rowspan = 2, padx = 5, pady = 5, ipadx = 5, ipady = 5) # '미완료한 일' Listbox 배치

undo_sclbar = Scrollbar(todo, orient = 'vertical') # undo에 붙을 스크롤바 생성
undo_sclbar.config(command = undo.yview)
undo_sclbar.grid(column = 3, row = 4, sticky = 'NS', rowspan = 2) # undo에 붙을 스크롤바 배치
undo.config(yscrollcommand = undo_sclbar.set) # undo의 Listbox + undo의 스크롤바 붙이기

def no_content_undo():
    msg.showwarning('No content', '추가할 내용이 없습니다! \n내용을 추가해주세요.')

def click_add_undo():
    if add_text.get() == '':
        #경고창 띄우기
        return(no_content_undo())
    else:
        # undo Listbox에 할 일 추가하는 함수
        undo.insert(END, add_text.get())
        add.delete(0, 'end')  # 안에 있는 내용 지우기 -> 새로 입력할 수 있도록

add_button = ttk.Button(todo, width = 5, text = '추가', command = click_add_undo)
add_button.grid(column = 8, row = 1, sticky = tk.W, padx = 3, pady = 3)

def delete_undo(): # '미완료한 일'을 '삭제'하는 버튼 생성
    undo_delete_index = undo.curselection()
    undo.delete(undo_delete_index)

undo_delete_button = ttk.Button(todo, text = '삭제', command = delete_undo)
undo_delete_button.grid(column = 2, row = 6, sticky = tk.E)

############ UNDO 작성란: END -----------------------------------------------------------------------------------------

gap_2 = ttk.Label(todo, text = '      ')
gap_2.grid(column = 4, row = 4) # 공백을 위해

############ DONE 작성란: START -----------------------------------------------------------------------------------------
ttk.Label(todo, text = '완료한 일').grid(column = 5, row = 3, sticky = tk.W, padx = 5, pady = 5) # '완료한 일' 추가하기
done = tk.Listbox(todo, width = 40, height = 10) # '완료한 일'을 추가할 Listbox 생성
done.grid(column = 5, row = 4, sticky = 'WENS', columnspan = 3, rowspan = 2, padx = 5, pady = 5, ipadx = 5, ipady = 5) # '완료한 일' Listbox 배치

done_sclbar = Scrollbar(todo, orient = 'vertical') # done에 붙을 스크롤바 생성
done_sclbar.config(command = done.yview)
done_sclbar.grid(column = 8, row = 4, sticky = 'WNS', rowspan = 2) # done에 붙을 스크롤바 배치
done.config(yscrollcommand = done_sclbar.set) # done의 Listbox + done의 스크롤바 붙이기

# date_check_var = IntVar() # '날짜 표시하기' 체크버튼의 체크 상태 저장
# date_check = tk.Checkbutton(todo, text = '날짜 표시하기', variable = date_check_var)
# date_check.grid(column = 7, row = 3, sticky = tk.E)

def from_undo_to_done(): # undo에서 완료한 일 done으로 옮기기
    done_ing_index = undo.curselection()
    done_ing_list = undo.get(done_ing_index)
    undo.delete(done_ing_index)
    done.insert(END, done_ing_list)        

done_button = ttk.Button(todo, text = '할 일 완료 -→', width = 15, command = from_undo_to_done)
done_button.grid(column = 4, row = 4, padx = 5)

def from_done_to_undo(): # done에서 미완료한 일 undo로 옮기기
    undo_ing_index = done.curselection()
    undo_ing_list = done.get(undo_ing_index)
    done.delete(undo_ing_index)
    undo.insert(END, undo_ing_list)

done_button = ttk.Button(todo, text = '←- 할 일 미완료', width = 15, command = from_done_to_undo)
done_button.grid(column = 4, row = 5, padx = 5)

def delete_done(): # '완료한 일'을 '삭제'하는 버튼 생성
    done_delete_index = done.curselection()
    done.delete(done_delete_index)

done_delete_button = ttk.Button(todo, text = '삭제', command = delete_done)
done_delete_button.grid(column = 7, row = 6, sticky = tk.E)

############ DONE 작성란: END -----------------------------------------------------------------------------------------
def todo_store():
    # todo에 기록한 내용 저장하는 곳
    save_todo_filename = '오늘의 할 일들_' + year_number.get() + month_number.get() + day_number.get() + '.txt'  # '오늘의 할 일들_(연월일)'을 파일명으로 설정

    # todo에 작성한 모든 내용 합치기 - 저장할 내용을 아예 따로 만들어서 한 번에 저장할 수 있도록
    todo_date = '오늘의 날짜: ' + year_number.get() + '년 ' + month_number.get() + '월 ' + day_number.get() + '일 ' + week_number.get() + '요일'

    todo_undo_total = ''  # todo_undo_total 초기화
    if undo != '':  # undo에 입력된 내용이 있으면
        undo_total = list(undo.get(0, END))
        for i in range(undo.size()):
            todo_undo_total += undo_total[i] + '\n'

    todo_done_total = ''  # todo_done_total 초기화
    if done != '':   # done에 입력된 내용이 있으면
        done_total = list(done.get(0, END))
        for i in range(done.size()):
            todo_done_total += done_total[i] + '\n'

    todo_text = todo_date + '\n\n' + '[미완료한 일]\n' + todo_undo_total + '\n' + '[완료한 일]\n' + todo_done_total

    with open(save_todo_filename, 'w', encoding = 'utf8') as file:
        file.write(todo_text)

todo_store_button = ttk.Button(todo, width = 8, text = '저장하기', command = todo_store)
todo_store_button.grid(column = 9, row = 7, padx = 5, pady = 5)

######## TODO 작성란: END--------------------------------------------------------------------------------------------

# ######## 일기장 작성란: SRATR  -----------------------------------------------------------------------------------------
diary = ttk.Frame(tabControl) # '일기장'이 들어갈 tab 만들기
tabControl.add(diary, text = '일기장') # '일기장' 탭 추가

mood_font = tk.font.Font(family = '맑은 고딕', size = 13, weight = 'bold')
mood_kor = ttk.Label(diary, text="오늘의 기분 ", font = mood_font) # '오늘의 기분' 추가
mood_kor.grid(column = 0, row = 0, padx = 5, pady = 5) # '오늘의 기분' 배치
mood_txt = tk.StringVar() # '오늘의 기분'을 선택하면 저장할 문자열 변수
mood = ttk.Combobox(diary, width = 10, textvariable = mood_txt) # '오늘의 기분' 선택
mood['value'] = ('행복', '우울', '화사', '기쁨', '상쾌', '낭만', '막막', '분노')
mood.grid(column = 1, row = 0, sticky = 'W')
mood.current(0) # 처음 표시되는 '오늘의 기분'을 '행복'으로 설정

gap_4 = ttk.Label(diary, text = ' ')
gap_4.grid(column = 0, row = 1) # 한 행의 공백을 위해
gap_5 = ttk.Label(diary, text = ' ')
gap_5.grid(column = 2, row = 0) # 한 행의 공백을 위해

today_diary_kor = ttk.Label(diary, text="오늘의 일기 ", font = mood_font) # '오늘의 일기' 추가
today_diary_kor.grid(column = 0, row = 2, sticky = 'N', padx = 5, pady = 5) # '오늘의 일기' 배치
today_diary = scl.ScrolledText(diary, width = 90, height = 20, wrap = tk.WORD)
today_diary.grid(column = 1, row = 2, columnspan = 2) # '오늘의 일기' 입력란 배치

def diary_store():
    # diary에 기록한 내용 저장하는 곳
    save_diary_filename = '오늘의 일기_' + year_number.get() + month_number.get() + day_number.get() + '.txt'  # '오늘의 일기_(연월일)'을 파일명으로 설정

    # diary에 작성한 모든 내용 합치기 - 저장할 내용을 아예 따로 만들어서 한 번에 저장할 수 있도록
    diary_date = '오늘의 날짜: ' + year_number.get() + '년 ' + month_number.get() + '월 ' + day_number.get() + '일 ' + week_number.get() + '요일'

    if today_diary == '':
        diary_total = '(없음) \n'
    else:
        diary_total = today_diary.get(1.0, END)

    todo_text = diary_date + '\n\n' + '오늘의 기분은 ' + mood_txt.get() + '\n\n' + '오늘의 일기\n' + diary_total

    with open(save_diary_filename, 'w', encoding = 'utf8') as file:
        file.write(todo_text)

diary_store_button = ttk.Button(diary, width = 8, text = '저장하기', command = diary_store)
diary_store_button.grid(column = 3, row = 3, padx = 5, pady = 5)

# ######## 일기장 작성란: END  -----------------------------------------------------------------------------------------

# GUI 실행하기 -------------------------------------------------------------------------------------------------
win.mainloop()