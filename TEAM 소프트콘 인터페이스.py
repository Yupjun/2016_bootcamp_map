#coding=utf-8


#데이터 리스트정리
import time
vacation=['Jan','Feb','Jul','Aug']
weekend = ['Sat','Sun']
hu_cs=[[8,22,8,16,0,0],[8,22,8,16,0,0]] #편의점 convinient store
hu_c=[[8,22,8,16,0,0],[8,22,8,16,0,0]]  #cafe
hu_r=[[4.5,24,4.5,24,4.5,24],[4.5,24,4.5,24,4.5,24]] #열람실 reading
lib_r=[[9,17.5,10,17,0,0],[9,17.5,10,17,0,0]] #2,3,4층 열람실
lib_cs=[[9,21,9,21,9,21],[9,21,9,21,9,21]] #편의점
lib_c=[[9,19,9,18,9,18],[9,19,9,18,9,18]] #카페
lib_r1f=[[5,24,5,24,5,24],[5,24,5,24,5,24]] #1층 1,3 열람실
lib_r1f2rd=[[6,5,6,5,6,5],[6,5,6,5,6,5]] #1층 2열람실
lib_cp=[[9,17.5,10,17,0,0],[9,17.5,10,17,0,0]] #복사실 copy
pro_cafeteria=[[0,0,0,0,0,0],[0,0,0,0,0,0]] #옥류천 식당
law_cafeteria=[[11,18.5,0,0,0,0],[11,18.5,0,0,0,0]] #학생식당
law_cp=[[0,0,0,0,0,0],[0,0,0,0,0,0]] #복사실
law_cs=[[9,20,9,19,9,18],[9,20,9,19,9,18]] #편의점
art_cs=[[10,17,0,0,0,0],[10,17,0,0,0,0]] #매점
art_pc=[[9,21,0,0,0,0],[9,21,0,0,0,0]] #pc실
art_cp=[[0,0,0,0,0,0],[0,0,0,0,0,0]] #복사실
art_d5f=[[5,24,5,24,5,24],[5,24,5,24,5,24]] #5층 정문 door at first floor
art_d8f=[[5,22,0,0,0,0],[5,22,0,0,0,0]] #8층 별관문
art_d1f=[[5,22,5,22,0,0],[5,22,5,22,0,0]] #1층 정문
ec_pc=[[9,17,0,0,0,0],[9,21.5,9,17,0,0]] #Creative Smart Zone (pc실)
ec_pc4f1st=[[9,17,0,0,0,0],[9,21.5,9,17,0,0]] #4층 제 1pc실
ec_pc4f2st=[[9,17,0,0,0,0],[9,21.5,9,17,0,0]] #4층 제 2pc실
ec_pc5=[]
ec_ezone=[[9,17.5,0,0,0,0],[9,17.5,0,0,0,0]] #3층 글로벌 ezone
ec_gl=[[9,18,0,0,0,0],[9,18,0,0,0,0]] #여학생 휴게실 gir's lounge
ec_Satm=[] #신한은행 ATM
ec_p=[] # 프린터 printer
st_gl=[[9,17.5,0,0,0,0],[9,17.5,0,0,0,0]] #여학생 휴게실
st_cs=[[9,18,0,0,0,0],[9,18,0,0,0,0]] #편의점
st_Watm=[] #우리은행 atm
st_pc=[] #2층 컴퓨터
st_p=[] #2층 프린터
st_charging=[] #2층 핸드폰 충전기 charging cell phone
glb_c=[[8,18.5,10,17,0,0],[8,20,10,17,0,0]] #카페
glb_r=[] #열람실
glb_d1f=[[5,23,0,0,0,0],[5,23,5,23,5,23]] #1층 출입문
glb_d2f=[[5,23,5,23,5,23],[5,23,5,23,5,23]] #2층 출입문
glb_d1B=[] #지하 1층 주차장 출입문
glb_d2B=[] #지하 2층 주차장 출입문
glb_l2B=[] #지하 2층 학생 라운지
glb_l3B=[] #지하 3층 학생 라운지
glb_p=[] # 지하2층 프린터 3대
bus_pc=[[9,17,0,0,0,0],[9,22,0,0,0,0]] #pc실
bus_cafeteria=[[9,18.5,9,14,0,0],[7.5,19.5,9,18,0,0]] #금잔디 식당
bus_mt=[[11,14,0,0,0,0],[11,17,0,0,0,0]] #맘스터치 mom's touch
bus_my=[[8.5,18.5,10,14,0,0],[7.5,19.5,7.5,15.5,0,0]] #마이도시
bus_bs=[[9,19,9,15,0,0],[9,19,9,18,0,0]] #서점 book store
bus_s=[[9,19,9,15,0,0],[9,19,9,18,0,0]] #문방사우 stationery
bus_multi=[[10,19.5,11,19.5,0,0],[9,19.5,10,19.5,0,0]] # 멀티미디어샵 multimedia shop
bus_photo=[[10,18,10,16,0,0],[9,19.5,10,17.5,0,0]] #사진관
bus_flower=[[10,17.5,0,0,0,0],[10,19.5,0,0,0,0]] #꽃집
bus_telecom=[[10,19.5,0,0,0,0],[10,19.5,0,0,0,0]] #통신사
bus_cs=[[9,22,9,22,9,22],[8,22,8,22,8,22]] #편의점
bus_s=[[10,18,0,0,0,0],[9,19,0,0,0,0]] #기념품샵 souvenir
bus_g=[[10,18,0,0,0,0],[9,19,0,0,0,0]] #안경점 glasses
bus_v=[[10,18,0,0,0,0],[9,19,0,0,0,0]] #여행사 vacation
bus_cp=[[9.5,16,0,0,0,0],[9,19,0,0,0,0]] #복사실
bus_h=[[7.5,20,0,0,0,0],[7,22,0,0,0,0]] #헬스장 health
bus_c=[[8.5,18.5,9,17.5,0,0],[8,20,8,20,0,0]] #사랑방 cafe
euk_w=[[9,16,0,0,0,0],[9,16,0,0,0,0]] #우리은행
euk_r=[]
euk_po=[[9,18,0,0,0,0],[9,18,0,0,0,0]] #우체국 post office
euk_Watm=[] #우리은행 atm
euk_p=[] #프린터
euk_sofa=[] #소파랜드
euk_h=[]


#각 시설물, 기자재 정보 창 실행 함수(약 60개)
#info1: 인문관 편의점
'''
def info1():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')
    photo_info1 = PhotoImage(file="성대사진/인문관편의점.gif")
    label_info1 = Label(info_hu_cs, image=photo_info1, anchor=N)
    #label_info1 = Label(info_hu_cs, text="인문관 편의점", side=BOTTOM)
    label_info1.pack()
    info_hu_cs.mainloop()

'''


### 각 버튼 클릭후 이벤트에는 command = etc1() 넣어주시고  사진란에는
### 해당장소 사진 이름 넣어주시면 됩니다
#인문관 편의점
def info1():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = hu_cs  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/인문관편의점.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<인문관 편의점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="인문관 2층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="전화번호:02-740-1935 위치:인문관 2층 엘리베이터 앞")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info2():
    info_hu_c = Toplevel()
    info_hu_c.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = hu_c  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_c, text="<<인문관 까페>>", font=30)
    info_hu_cs2 = Label(info_hu_c, text=words)
    info_hu_cs3 = Label(info_hu_c, text="인문관외부 정원")
    info_hu_cs4 = Label(info_hu_c, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_c, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_c, text="맛있는 쿠키와 커피가 많이 있어요")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_c.mainloop()


def info3():
    info_hu_cs= Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = hu_r  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/인문관열람실.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<인문관 열람실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="인문관 2층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="공부하는 열람실이에요")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info4():
    info_hu_cs= Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = lib_r  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<중앙학술정보관 열람실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="2층, 3층, 4층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="열심히 공부하는 곳이에요")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info5():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = lib_cs  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<중앙학술 정보관 편의점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="1층 왼쪽")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="소분해서 파는게 많아서 좋음.")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info6():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = lib_c  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<중앙학술 정보관 까페>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="1층 왼쪽")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="가끔 알바하는 분이 불친절함.")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info7():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = lib_r1f  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<1층 1,3 열람실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="1층 안쪽")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="노트북, 철야가능")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info8():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = lib_r1f2rd  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<1층 2열람실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="1층 왼쪽")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="평범한 열람실 공간이 겁나 크다.")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info9():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = lib_cp  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<중앙학술정보관 복사실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="4층 000~200 도서 있는 곳")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="전공책도 친절하게 복사해주시는데 죄송함..")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info10():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = pro_cafeteria  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<교수회관 옥류천식당>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1294,가격에 비해 양도 적고 교수님들 입맛")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info11():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = law_cafeteria  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<법학관 학생식당>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1929,맛은 있는데 조금 멀고 먹기 좀 쑥쓰러움")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info12():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')
    # photo = PhotoImage(file="성대사진/경영관꽃집.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<법학관 복사실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="지하 2층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


def info13():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = law_cs  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<법학관 편의점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="지상 1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1934")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info14():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = art_cs  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<수선관 매점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1936")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info15():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = art_pc  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<수선관 PC실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="8층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="수선관 8층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


def info16():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')
    # photo = PhotoImage(file="성대사진/경영관꽃집.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<수선관 복사실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="수선관 정문이 닫혀있으면 못감")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


def info17():
    info_hu_c = Toplevel()
    info_hu_c.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = art_d5f  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/인문관편의점.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<수선관 5층정문>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="5층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="12시가 되면은 문을 닫는다~")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


# 8층 별관문
def info18():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = art_d8f  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/8층 별관문.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<8층 별관문>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="수선관 별관 8층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# 1층 정문
def info19():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x400')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = art_d1f  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/1층 정문.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<1층 정문>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="수선관 1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# Creative Smart Zone(PC실)
def info20():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x450')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = ec_pc  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경제관크리에이티브.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경제관 4층>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경제관 4층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# 4층 제 1 PC 실
def info21():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = ec_pc4f1st  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경제관제1PC실.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경제관 4층>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경제관 4층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# 4층 제 2 PC 실
def info22():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = ec_pc4f2st  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경제관제2PC실.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경제관 4층>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경제관 4층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#경제관 5,6 PC실
def info23():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/경제관제6PC실.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경제관 제5,6 PC실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시 자체 수업 진행")
    info_hu_cs3 = Label(info_hu_cs, text="경제관 5층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()

# 3층 글로벌 e zone
def info24():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = ec_ezone  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경제관EZONE.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경제관 3층>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경제관 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# 여학생 휴게실
def info25():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = ec_gl  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/여학생 휴게실.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    #info_hu_cs1 = Label(info_hu_cs, text="<<여학생 휴게실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경제관 지하1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# 신한은행ATM
def info26():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/경제관신한ATM.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<신한은행ATM>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="경제관 1층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


# 프린터
def info27():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/경제관4층프린터.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<프린터>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="경제관 4층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


# 여학생휴게실
def info28():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = st_gl  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/여학생휴게실.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<여학생휴게실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="학생회관 4층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# 편의점
def info29():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = st_cs  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/편의점_학관.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<편의점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="학생회관 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1933")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()


# 우리은행 atm
def info30():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/600우리ATM.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<우리은행 atm>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="학생회관 2층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


# 2층 컴퓨터
def info31():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/학생회관컴퓨터.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<2층 컴퓨터>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="학생회관 2층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


# 2층 프린터
def info32():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/학생회관프린터.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<2층 컴퓨터>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="학생회관 2층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


# 2층 핸드폰 충전기
def info33():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/학생회관충전기.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<2층 핸드폰 충전기>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="학생회관 2층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


# 카페(팬도로시)
def info34():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]

    location = glb_c  # 수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    # photo = PhotoImage(file="성대사진/카페(팬도로시).gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<카페(팬도로시)>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="국제관 지하1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시" % shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시" % shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


# 국제관 열람실
def info35():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    #photo = PhotoImage(file="성대사진/인문관편의점.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 열람실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="국제관 지하2층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()

# 국제관 1층 출입문
def info36():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = glb_d1f #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/인문관편의점.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 1층 출입문>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs4 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs.pack()
    info_hu_cs.mainloop()

# 국제관 2층 출입문
def info37():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = glb_d2f #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/인문관편의점.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 2층 출입문>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs4 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs.pack()
    info_hu_cs.mainloop()

# 국제관 지하1층 주차장 출입문
def info38():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    #photo = PhotoImage(file="성대사진/인문관편의점.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 지하1층 주차장 출입문>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs.mainloop()

# 국제관 지하2층 주차장 출입문
def info39():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    #photo = PhotoImage(file="성대사진/인문관편의점.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 지하2층 주차장 출입문>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs.mainloop()

# 국제관 지하2층 학생라운지
def info40():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    photo = PhotoImage(file="성대사진/국제관B2라운지.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 지하2층 학생라운지>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="국제관 지하2층")
    info_hu_cs3 = Label(info_hu_cs, text="상시개방")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()

# 국제관 지하3층 학생라운지
def info41():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    photo = PhotoImage(file="성대사진/국제관B3라운지.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 지하3층 학생라운지>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="국제관 지하3층")
    info_hu_cs3 = Label(info_hu_cs, text="상시개방")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()

# 국제관 지하2층 프린터 3대
def info42():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    photo = PhotoImage(file="성대사진/국제관B3프린터.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<국제관 지하3층 프린터 3대>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="국제관 지하3층")
    info_hu_cs3 = Label(info_hu_cs, text="상시개방")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()

# 경영관 PC실
def info43():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_pc #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관PC실.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 PC실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 2층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

# 경영관 금잔디식당
def info44():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_cafeteria #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관금잔디식당.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 금잔디식당>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하2층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1927, 02-740-1928")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()

# 경영관 맘스터치
def info45():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_mt #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관맘스터치.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 맘스터치>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하2층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

# 경영관 마이도씨
def info46():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_my #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/인문관편의점.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 마이도씨>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하2층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

# 경영관 서점
def info47():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_bs #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관서점.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 서점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1908")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()

# 경영관 문방사우
def info48():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_s #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관문방사우.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 문방사우>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1911")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()

# 경영관 멀티미디어샵
def info49():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_multi #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/인문관편의점.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 멀티미디어샵>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

# 경영관 사진관
def info50():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_photo #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관사진관.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 사진관>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs6 = Label(info_hu_cs, text="☎ 02-740-1909")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs6.pack()
    info_hu_cs.mainloop()

#경영관 꽃집
def info51():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_flower #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관꽃집.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 꽃집>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#경영관 통신사
def info52():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_telecom #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관통신사.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 통신사>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#경영관 편의점
def info53():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_cs #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관편의점.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 편의점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#경영관 기념품샵
def info54():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_s #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관기념품점.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 기념품샵>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#경영관 여행사
def info55():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_flower #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관여행사.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 여행사>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#경영관 안경점
def info56():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_g #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관안경점.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 안경점>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#경영관 복사실
def info57():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_cp #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관복사실.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 복사실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


#경영관 헬스장
def info58():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_h #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관헬스장.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 헬스장>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


#경영관 사랑방
def info59():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = bus_c #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    photo = PhotoImage(file="성대사진/경영관사랑방.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<경영관 사랑방 카페>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="경영관 지하 3층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#600주년 우리은행
def info60():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = euk_w #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/경영관꽃집.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<600주년 기념관 우리은행>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="600주년 기념관 1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()


#600주년 우체국
def info61():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = euk_po #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/경영관꽃집.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<600주년 기념관 우체국>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text=words)
    info_hu_cs3 = Label(info_hu_cs, text="600주년 기념관 1층")
    info_hu_cs4 = Label(info_hu_cs, text="금일오픈시간 : %d 시"%shop_open)
    info_hu_cs5 = Label(info_hu_cs, text="금일마감시간 : %d 시"%shop_close)
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs4.pack()
    info_hu_cs5.pack()
    info_hu_cs.mainloop()

#600주년 은행골식당
def info62():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')

    import time
    evaluate = time.ctime()

    month = "evaluate[4:7]"
    day = evaluate[0:3]
    hour = int(evaluate[11:13])

    if day == weekend[0]:
        day_1 = [2, 3]
    elif day == weekend[1]:
        day_1 = [4, 5]
    else:
        day_1 = [0, 1]

    if month == vacation[0] or month == vacation[1] or month == vacation[2] or month == vacation[3]:
        month_1 = [0]
    else:
        month_1 = [1]


    location = euk_r #수정
    shop_open = location[month_1[0]][day_1[0]]
    shop_close = location[month_1[0]][day_1[1]]

    if shop_open == shop_close:
        words = "휴무일"

    elif hour > shop_open or hour < shop_close:
        words = "이용 가능"

    else:
        words = "이용 불가"

    #photo = PhotoImage(file="성대사진/경영관꽃집.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<600주년 기념관 은행골식당>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="개선공사중")
    info_hu_cs3 = Label(info_hu_cs, text="600주년 기념관 지하 1층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


#600주년 우리은행ATM
def info63():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/600우리ATM.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<600주년 기념관 우리은행 ATM>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="600주년 기념관 1층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()

#600주년 프린터
def info64():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    photo = PhotoImage(file="성대사진/600프린터.gif")
    LT_PH = Label(info_hu_cs, image=photo)
    LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<600주년 기념관 프린터>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="600주년 기념관 1층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


#600주년 소파랜드
def info65():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    #photo = PhotoImage(file="성대사진/경영관꽃집.gif")
    #LT_PH = Label(info_hu_cs, image=photo)
    #LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<600주년 기념관 소파랜드>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="상시개방")
    info_hu_cs3 = Label(info_hu_cs, text="600주년 기념관 1층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()


#600주년 휴게실
def info66():
    info_hu_cs = Toplevel()
    info_hu_cs.geometry('400x430')
    # photo = PhotoImage(file="성대사진/600휴게실.gif")
    # LT_PH = Label(info_hu_cs, image=photo)
    # LT_PH.pack()
    info_hu_cs1 = Label(info_hu_cs, text="<<600주년 기념관 휴게실>>", font=30)
    info_hu_cs2 = Label(info_hu_cs, text="학생이용금지")
    info_hu_cs3 = Label(info_hu_cs, text="600주년 기념관 1층")
    info_hu_cs1.pack()
    info_hu_cs2.pack()
    info_hu_cs3.pack()
    info_hu_cs.mainloop()

#기타 기자재 연결 함수
# 노트북 대여
def etc1():
    LT = Toplevel()
    LT.geometry('400x430')
    photo = PhotoImage(file="성대사진/경제관크리에이티브.gif")
    LT_PH = Label(LT, image=photo)
    LT_PH.pack()
    LT1 = Label(LT, text="<<노트북 대여>>", font=30)
    LT2 = Label(LT, text="다산경제관 4층 Creative Smart Zone(PC실)")
    LT3 = Label(LT, text="'GLS-정보광장-IT서비스-노트북대여신청'으로 예약접수 후 ")
    LT4 = Label(LT, text="신분증(학생증, 주민등록증 동시제출) 제시, 본인 확인")
    LT5 = Label(LT, text="대여에 대한 각서를 작성하고 물품을 수령")

    LT1.pack()
    LT2.pack()
    LT3.pack()
    LT4.pack()
    LT5.pack()
    LT.mainloop()


# 휴대폰 충전기
def etc2():
    MC = Toplevel()
    MC.geometry('400x450')
    photo = PhotoImage(file="성대사진/학생회관충전기.gif")
    MC_PH = Label(MC, image=photo)
    MC_PH.pack()
    MC1 = Label(MC, text="<<휴대폰 충전기>>")
    MC2 = Label(MC, text="퇴계인문관 4층")
    MC3 = Label(MC, text="중앙학술정보관 4층 데스크")
    MC4 = Label(MC, text="수선관 별관 5층")
    MC5 = Label(MC, text="학생회관 3층")
    MC6 = Label(MC, text="경영관 지하2층")
    MC7 = Label(MC, text="법학관 지하2층")

    MC1.pack()
    MC2.pack()
    MC3.pack()
    MC4.pack()
    MC5.pack()
    MC6.pack()
    MC7.pack()

    MC.mainloop()


# 흑백 프린터
def etc3():
    PR = Toplevel()
    PR.geometry('400x550')
    photo = PhotoImage(file="성대사진/경제관4층프린터.gif")
    PR_PH = Label(PR, image=photo)
    PR_PH.pack()
    PR1 = Label(PR, text="<<흑백 프린터>>", font=30)
    PR2 = Label(PR, text="경영관 2층")
    PR3 = Label(PR, text="경영관 지하1층")
    PR4 = Label(PR, text="퇴계인문관 5층")
    PR5 = Label(PR, text="퇴계인문관 6층")
    PR6 = Label(PR, text="퇴계인문관 7층")
    PR7 = Label(PR, text="학생회관 2층")
    PR8 = Label(PR, text="다산경제관 층")
    PR9 = Label(PR, text="600주년기념관 1층")
    PR10 = Label(PR, text="국제관 지하2층")

    PR1.pack()
    PR2.pack()
    PR3.pack()
    PR4.pack()
    PR5.pack()
    PR6.pack()
    PR7.pack()
    PR8.pack()
    PR9.pack()
    PR10.pack()

    PR.mainloop()


# 칼라 프린터
def etc4():
    CPR = Toplevel()
    CPR.geometry('400x430')
    photo = PhotoImage(file="성대사진/경제관칼라프린터.gif")
    CPR_PH = Label(CPR, image=photo)
    CPR_PH.pack()
    CPR1 = Label(CPR, text="<<칼라 프린터>>", font=30)
    CPR2 = Label(CPR, text="중앙학술정보관 3층")

    CPR1.pack()
    CPR2.pack()

    CPR.mainloop()


# 스캐너
def etc5():
    SC = Toplevel()
    SC.geometry('400x430')
    photo = PhotoImage(file="성대사진/경제관스캐너.gif")
    SC_PH = Label(SC, image=photo)
    SC_PH.pack()
    SC1 = Label(SC, text="<<스캐너>>", font=30)
    SC2 = Label(SC, text="다산경제관 4층 Creative Smart Zone(PC실)")
    SC3 = Label(SC, text="중앙학술정보관 3층")

    SC1.pack()
    SC2.pack()
    SC3.pack()

    SC.mainloop()


# 소파랜드
def etc6():
    SF = Toplevel()
    SF.geometry('400x430')

    photo = PhotoImage(file="성대사진/국제관소파.gif")
    SF_PH = Label(SF, image=photo)
    SF_PH.pack()
    SF1 = Label(SF, text="<<소파랜드>>", font=30)
    SF2 = Label(SF, text="xx관 x층")
    SF3 = Label(SF, text="xx관 x층")

    SF1.pack()
    SF2.pack()
    SF3.pack()

    SF.mainloop()


# 학생 라운지
def etc7():
    LO = Toplevel()
    LO.geometry('400x430')
    photo = PhotoImage(file="성대사진/국제관B1라운지.gif")
    LO_PH = Label(LO, image=photo)
    LO_PH.pack()
    LO1 = Label(LO, text="<<학생 라운지>>", font=30)
    LO2 = Label(LO, text="국제관 지하1층")
    LO3 = Label(LO, text="XX관 X층")

    LO1.pack()
    LO2.pack()
    LO3.pack()

    LO.mainloop()


# 국민은행 ATM
def etc8():
    KB = Toplevel()
    KB.geometry('400x430')
    photo = PhotoImage(file="성대사진/경영관ATM.gif")
    KB_PH = Label(KB, image=photo)
    KB_PH.pack()
    KB1 = Label(KB, text="<<국민은행 ATM>>", font=30)
    KB2 = Label(KB, text="경영관 지하1층")
    KB3 = Label(KB, text="교수회관 1층")

    KB1.pack()
    KB2.pack()
    KB3.pack()

    KB.mainloop()


# 신한은행 ATM
def etc9():
    SB = Toplevel()
    SB.geometry('400x430')
    photo = PhotoImage(file="성대사진/경제관신한ATM.gif")
    SB_PH = Label(SB, image=photo)
    SB_PH.pack()
    SB1 = Label(SB, text="<<신한은행 ATM>>", font=30)
    SB2 = Label(SB, text="다산경제관 1층 외부")

    SB1.pack()
    SB2.pack()

    SB.mainloop()


# 우리은행 ATM
def etc10():
    WB = Toplevel()
    WB.geometry('400x500')
    photo = PhotoImage(file="성대사진/600우리ATM.gif")
    WB_PH = Label(WB, image=photo)
    WB_PH.pack()

    WB1 = Label(WB, text="<<우리은행 ATM>>", font=30)
    WB2 = Label(WB, text="수선관 7층")
    WB3 = Label(WB, text="600주년기념관 1층")
    WB4 = Label(WB, text="국제관 1층")
    WB5 = Label(WB, text="경영관 지하1층")
    WB6 = Label(WB, text="다산경제관 1층")
    WB7 = Label(WB, text="중앙학술정보관 3층 앞")
    WB8 = Label(WB, text="법학관 1층")
    WB9 = Label(WB, text="수선관 별관5층")
    WB10 = Label(WB, text="학생회관 3층")
    WB11 = Label(WB, text="교수회관 1층")

    WB1.pack()
    WB2.pack()
    WB3.pack()
    WB4.pack()
    WB5.pack()
    WB6.pack()
    WB7.pack()
    WB8.pack()
    WB9.pack()
    WB10.pack()
    WB11.pack()

    WB.mainloop()

# 분실물센터
def etc11():
    LC = Toplevel()
    LC.geometry('400x430')
    #photo = PhotoImage(file=".gif")
    #LC_PH = Label(LC, image=photo)
    #LC_PH.pack()
    LC1 = Label(LC, text="<<분실물센터>>", font=30)
    LC2 = Label(LC, text="600주년기념관 1층 학생지원팀")
    LC3 = Label(LC, text="주중 09:00-17:30 ☎ 02-760-1077")

    LC1.pack()
    LC2.pack()
    LC3.pack()

    LC.mainloop()


# 식당
def etc12():
    CA = Toplevel()
    CA.geometry('400x450')
    photo = PhotoImage(file="성대사진/경영관금잔디식당.gif")
    CA_PH = Label(CA, image=photo)
    CA_PH.pack()

    CA1 = Label(CA, text="<<식당>>", font=30)
    CA2 = Label(CA, text="금잔디식당 : 경영관 지하2층 → ☎ 02-740-1927")
    CA3 = Label(CA, text="법고을식당 : 법학관 지하2층 → ☎ 02-740-1929")
    CA4 = Label(CA, text="옥류천식당 : 교수회관 1층 → ☎ 02-740-1924")
    CA5 = Label(CA, text="은행골식당 : 600주년기졈관 지하1층 → ☎ 02-740-1926")
    CA6 = Label(CA, text="패컬티식당 : 600주년기념관 6층 → ☎ 02-740-1925")

    CA1.pack()
    CA2.pack()
    CA3.pack()
    CA4.pack()
    CA5.pack()
    CA6.pack()

    CA.mainloop()

# 매점
def etc13():
    CS = Toplevel()
    CS.geometry('400x430')
    #photo = PhotoImage(file=".gif")
    #CS_PH = Label(CS, image=photo)
    #CS_PH.pack()

    CS1 = Label(CS, text="<<매점>>", font=30)
    CS2 = Label(CS, text="경영관 지하3층 → ☎ 02-740-1931")
    CS3 = Label(CS, text="중앙학술정보관 1층 → ☎ 02-740-1932")
    CS4 = Label(CS, text="법학관 지하2층 → ☎ 02-740-1934")
    CS5 = Label(CS, text="수선관 별관5층 → ☎ 02-740-1936")
    CS6 = Label(CS, text="퇴계인문관 2층 → ☎ 02-740-1935")
    CS7 = Label(CS, text="학생회관 3층 → ☎ 02-740-1933")

    CS1.pack()
    CS2.pack()
    CS3.pack()
    CS4.pack()
    CS5.pack()
    CS6.pack()
    CS7.pack()

    CS.mainloop()

# 여학생 휴게실
def etc14():
    GL = Toplevel()
    GL.geometry('400x430')
    #photo = PhotoImage(file=".gif")
    #GL_PH = Label(GL, image=photo)
    #GL_PH.pack()

    GL1 = Label(GL, text="<<여학생 휴게실>>", font=30)
    GL2 = Label(GL, text="다산경제관 1층 → ☎ 02-760-1095")
    GL3 = Label(GL, text="법학관 지하2층 → ☎ 02-760-1095")
    GL4 = Label(GL, text="학생회관 4층 → ☎ 02-760-1095")

    GL1.pack()
    GL2.pack()
    GL3.pack()
    GL4.pack()

    GL.mainloop()



#학사일정, 식단 url 연결 함수
def sch() :
    import webbrowser
    url='http://www.skku.edu/new_home/edu/bachelor/ca_de_schedule_2017.jsp'
    webbrowser.open(url)
#옥류천식당 URL
def food1():
    import webbrowser
    url="http://www.skku.ac.kr/new_home/campus/support/pop_menu1.jsp?restId=101"
    webbrowser.open(url)
#패컬티식당 URL
def food2():
    import webbrowser
    url="http://www.skku.ac.kr/new_home/campus/support/pop_menu1.jsp?restId=102"
    webbrowser.open(url)
#은행골식당 URL
def food3():
    import webbrowser
    url="http://www.skku.ac.kr/new_home/campus/support/pop_menu1.jsp?restId=103"
    webbrowser.open(url)
#금잔디식당 URL
def food4():
    import webbrowser
    url="http://www.skku.ac.kr/new_home/campus/support/pop_menu1.jsp?restId=104"
    webbrowser.open(url)
#은행나무아래식당 URL
def food5():
    import webbrowser
    url="http://www.skku.ac.kr/new_home/campus/support/pop_menu1.jsp?restId=105"
    webbrowser.open(url)
#법고을식당 URL
def food6():
    import webbrowser
    url="http://www.skku.ac.kr/new_home/campus/support/pop_menu1.jsp?restId=106"
    webbrowser.open(url)


#기본 인터페이스 정리
from tkinter import*

map=Tk()
map.title("성균관 대학교 방방곡곡")
map.geometry("720x430")

'''
현재시간
import datetime
s = datetime.datetime.now()
labeltime=Label(text="s", font=("맑은 고딕",20), fg="yellow green")
labeltime.pack()
print(s)
'''

#중앙 현재시간표시
import time
time_string = time.ctime()
time_string = time_string[:16] + ' ' + time_string[20:]
labeltime=Label(text=time_string, font=("맑은 고딕",20), fg="yellow green")
labeltime.pack()


#지도표시
photo=PhotoImage(file="맵/진짜임.gif")
label1=Label(map, image=photo)
label1.pack(anchor=N)


#메뉴 버튼"인문관"
HUM= Menubutton (map, text="인문관", relief=RAISED)
HUM.menu = Menu (HUM, tearoff = 0)
HUM["menu"] = HUM.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
HUM.menu.add_checkbutton ( label = "편의점", variable=PL1VAR, command=info1)
HUM.menu.add_checkbutton ( label = "카페", variable=PL1VAR, command=info2)
HUM.menu.add_checkbutton ( label = "열람실", variable=PL1VAR, command=info3)
HUM.pack(side="left", anchor = N)

#메뉴 버튼 "중앙도서관"
LIB= Menubutton (map, text="중앙도서관", relief=RAISED)
LIB.menu = Menu (LIB, tearoff = 0)
LIB["menu"] = LIB.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
PL4VAR = IntVar ()
PL5VAR = IntVar ()
PL6VAR = IntVar ()
LIB.menu.add_checkbutton ( label = "2,3,4층 열람실", variable=PL1VAR, command=info4)
LIB.menu.add_checkbutton ( label = "편의점", variable=PL2VAR, command=info5)
LIB.menu.add_checkbutton ( label = "카페", variable=PL3VAR, command=info6)
LIB.menu.add_checkbutton ( label = "1층 1,3 열람실", variable=PL4VAR, command=info7)
LIB.menu.add_checkbutton ( label = "1층 2 열람실", variable=PL5VAR, command=info8)
LIB.menu.add_checkbutton ( label = "복사실", variable=PL6VAR, command=info9)
LIB.pack(side="left", anchor = N)


#메뉴 버튼 "교수회관"
PRO= Menubutton (map, text="교수회관", relief=RAISED)
PRO.menu = Menu (PRO, tearoff = 0)
PRO["menu"] = PRO.menu

PL1VAR = IntVar ()
PRO.menu.add_checkbutton ( label = "옥류천식당", variable=PL1VAR, command=info10)
PRO.pack(side="left", anchor = N)

#메뉴 버튼 "법학관"
LAW= Menubutton (map, text="법학관", relief=RAISED)
LAW.menu = Menu (LAW, tearoff = 0)
LAW["menu"] = LAW.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
LAW.menu.add_checkbutton ( label = "법고을식당", variable=PL1VAR, command=info11)
LAW.menu.add_checkbutton ( label = "복사실", variable=PL2VAR, command=info12)
LAW.menu.add_checkbutton ( label = "편의점", variable=PL3VAR, command=info13)
LAW.pack(side="left", anchor = N)

#메뉴 버튼 "수선관"
ART= Menubutton (map, text="수선관", relief=RAISED)
ART.menu = Menu (ART, tearoff = 0)
ART["menu"] = ART.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
PL4VAR = IntVar ()
PL5VAR = IntVar ()
PL6VAR = IntVar ()
ART.menu.add_checkbutton ( label = "매점", variable=PL1VAR, command=info14)
ART.menu.add_checkbutton ( label = "PC실", variable=PL2VAR, command=info15)
ART.menu.add_checkbutton ( label = "복사실", variable=PL3VAR, command=info16)
ART.menu.add_checkbutton ( label = "5층 정문", variable=PL4VAR, command=info17)
ART.menu.add_checkbutton ( label = "8층 별관문", variable=PL5VAR, command=info18)
ART.menu.add_checkbutton ( label = "1층 정문", variable=PL6VAR, command=info19)
ART.pack(side="left", anchor = N)

#메뉴 버튼 "경제관"
ECO= Menubutton (map, text="경제관", relief=RAISED)
ECO.menu = Menu (ECO, tearoff = 0)
ECO["menu"] = ECO.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
PL4VAR = IntVar ()
PL5VAR = IntVar ()
PL6VAR = IntVar ()
PL7VAR = IntVar ()
PL8VAR = IntVar ()
ECO.menu.add_checkbutton ( label = "Creative Smart Zone(PC실)", variable=PL1VAR, command=info20)
ECO.menu.add_checkbutton ( label = "4층 제1PC실", variable=PL2VAR, command=info21)
ECO.menu.add_checkbutton ( label = "4층 제2PC실", variable=PL3VAR, command=info22)
ECO.menu.add_checkbutton ( label = "5층 제5,6PC실", variable=PL4VAR, command=info23)
ECO.menu.add_checkbutton ( label = "3층 글로벌 E-Zone", variable=PL5VAR, command=info24)
ECO.menu.add_checkbutton ( label = "여학생휴게실", variable=PL6VAR, command=info25)
ECO.menu.add_checkbutton ( label = "신한은행 ATM", variable=PL7VAR, command=info26)
ECO.menu.add_checkbutton ( label = "4층 프린터", variable=PL8VAR, command=info27)
ECO.pack(side="left", anchor = N)


#메뉴 버튼 "학생회관"
STU= Menubutton (map, text="학생회관", relief=RAISED)
STU.menu = Menu (STU, tearoff = 0)
STU["menu"] = STU.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
PL4VAR = IntVar ()
PL5VAR = IntVar ()
PL6VAR = IntVar ()
STU.menu.add_checkbutton ( label = "여학생 휴게실", variable=PL1VAR, command=info28)
STU.menu.add_checkbutton ( label = "편의점", variable=PL2VAR, command=info29)
STU.menu.add_checkbutton ( label = "우리은행 ATM", variable=PL3VAR, command=info30)
STU.menu.add_checkbutton ( label = "2층 컴퓨터", variable=PL4VAR, command=info31)
STU.menu.add_checkbutton ( label = "2층 프린터", variable=PL5VAR, command=info32)
STU.menu.add_checkbutton ( label = "2층 충전기", variable=PL6VAR, command=info33)
STU.pack(side="left", anchor = N)

#메뉴 버튼 "국제관"
GLB= Menubutton (map, text="국제관", relief=RAISED)
GLB.menu = Menu (GLB, tearoff = 0)
GLB["menu"] = GLB.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
PL4VAR = IntVar ()
PL5VAR = IntVar ()
PL6VAR = IntVar ()
PL7VAR = IntVar ()
PL8VAR = IntVar ()
PL9VAR = IntVar ()
GLB.menu.add_checkbutton ( label = "팬도로시(카페)", variable=PL1VAR, command=info34)
GLB.menu.add_checkbutton ( label = "열람실", variable=PL2VAR, command=info35)
GLB.menu.add_checkbutton ( label = "1층 출입문", variable=PL3VAR, command=info36)
GLB.menu.add_checkbutton ( label = "2층 출입문", variable=PL4VAR, command=info37)
GLB.menu.add_checkbutton ( label = "B1층 주차장 출입문", variable=PL5VAR, command=info38)
GLB.menu.add_checkbutton ( label = "B2층 주차장 출입문", variable=PL6VAR, command=info39)
GLB.menu.add_checkbutton ( label = "B2층 라운지", variable=PL7VAR, command=info40)
GLB.menu.add_checkbutton ( label = "B3층 라운지", variable=PL8VAR, command=info41)
GLB.menu.add_checkbutton ( label = "B2층 프린터", variable=PL9VAR, command=info42)
GLB.pack(side="left", anchor = N)

#메뉴 버튼 "경영관"
BUS= Menubutton (map, text="경영관", relief=RAISED)
BUS.menu = Menu (BUS, tearoff = 0)
BUS["menu"] = BUS.menu

PL1VAR = IntVar ()
PL2VAR = IntVar ()
PL3VAR = IntVar ()
PL4VAR = IntVar ()
PL5VAR = IntVar ()
PL6VAR = IntVar ()
PL7VAR = IntVar ()
PL8VAR = IntVar ()
PL9VAR = IntVar ()
PL10VAR = IntVar ()
PL11VAR = IntVar ()
PL12VAR = IntVar ()
PL13VAR = IntVar ()
PL14VAR = IntVar ()
PL15VAR = IntVar ()
PL16VAR = IntVar ()
PL17VAR = IntVar ()
BUS.menu.add_checkbutton ( label = "PC실", variable=PL1VAR, command=info43)
BUS.menu.add_checkbutton ( label = "금잔디식당", variable=PL2VAR, command=info44)
BUS.menu.add_checkbutton ( label = "맘스터치", variable=PL3VAR, command=info45)
BUS.menu.add_checkbutton ( label = "마이도씨", variable=PL4VAR, command=info46)
BUS.menu.add_checkbutton ( label = "서점", variable=PL5VAR, command=info47)
BUS.menu.add_checkbutton ( label = "문방사우", variable=PL6VAR, command=info48)
BUS.menu.add_checkbutton ( label = "멀티미디어 샵", variable=PL7VAR, command=info49)
BUS.menu.add_checkbutton ( label = "사진관", variable=PL8VAR, command=info50)
BUS.menu.add_checkbutton ( label = "꽃집", variable=PL9VAR, command=info51)
BUS.menu.add_checkbutton ( label = "통신사", variable=PL10VAR, command=info52)
BUS.menu.add_checkbutton ( label = "편의점", variable=PL11VAR, command=info53)
BUS.menu.add_checkbutton ( label = "기념품샵", variable=PL12VAR, command=info54)
BUS.menu.add_checkbutton ( label = "여행사", variable=PL13VAR, command=info55)
BUS.menu.add_checkbutton ( label = "안경점", variable=PL14VAR, command=info56)
BUS.menu.add_checkbutton ( label = "복사실", variable=PL15VAR, command=info57)
BUS.menu.add_checkbutton ( label = "헬스장", variable=PL16VAR, command=info58)
BUS.menu.add_checkbutton ( label = "사랑방(카페)", variable=PL17VAR, command=info59)
BUS.pack(side="left", anchor = N)

#메뉴 버튼 "600주년 기념관"
EUK= Menubutton (map, text="600주년기념관", relief=RAISED)
EUK.menu = Menu (EUK, tearoff = 0)
EUK["menu"] = EUK.menu

for k in range(1,7):
    PLkVAR = IntVar ()

EUK.menu.add_checkbutton ( label = "우리은행", variable=PL1VAR, command=info60)
EUK.menu.add_checkbutton ( label = "우체국", variable=PL2VAR, command=info61)
EUK.menu.add_checkbutton ( label = "은행골식당", variable=PL3VAR, command=info62)
EUK.menu.add_checkbutton ( label = "우리은행 ATM", variable=PL4VAR, command=info63)
EUK.menu.add_checkbutton ( label = "1층 프린터", variable=PL5VAR, command=info64)
EUK.menu.add_checkbutton ( label = "1층 소파랜드", variable=PL6VAR, command=info65)
EUK.menu.add_checkbutton ( label = "휴게실", variable=PL7VAR, command=info66)

EUK.pack(side="left", anchor = N)

#메뉴 버튼 "기타"
ETC= Menubutton (map, text="기타", relief=RAISED)
ETC.menu = Menu (ETC, tearoff = 0)
ETC["menu"] = ETC.menu

for i in range(1,14):
    PLiVAR = IntVar ()
ETC.menu.add_checkbutton ( label = "노트북 대여", variable=PL1VAR, command=etc1)
ETC.menu.add_checkbutton ( label = "핸드폰 충전기", variable=PL2VAR, command=etc2)
ETC.menu.add_checkbutton ( label = "프린터", variable=PL3VAR, command=etc3)
ETC.menu.add_checkbutton ( label = "칼라 프린터", variable=PL4VAR, command=etc4)
ETC.menu.add_checkbutton ( label = "스캐너", variable=PL5VAR, command=etc5)
ETC.menu.add_checkbutton ( label = "소파랜드", variable=PL6VAR, command=etc6)
ETC.menu.add_checkbutton ( label = "학생 라운지", variable=PL7VAR, command=etc7)
ETC.menu.add_checkbutton ( label = "국민은행 ATM", variable=PL8VAR, command=etc8)
ETC.menu.add_checkbutton ( label = "신한은행 ATM", variable=PL9VAR, command=etc9)
ETC.menu.add_checkbutton ( label = "우리은행 ATM", variable=PL10VAR, command=etc10)
ETC.menu.add_checkbutton ( label = "분실물센터", variable=PL10VAR, command=etc11)
ETC.menu.add_checkbutton ( label = "식당", variable=PL10VAR, command=etc12)
ETC.menu.add_checkbutton ( label = "매점", variable=PL10VAR, command=etc13)
ETC.menu.add_checkbutton ( label = "여학생휴게실", variable=PL10VAR, command=etc14)
ETC.pack(side="left", anchor = N)


#메뉴 버튼 "식단"
FOOD= Menubutton (map, text="식당메뉴", relief=RAISED)
FOOD.menu = Menu (FOOD, tearoff = 0)
FOOD["menu"] = FOOD.menu

for j in range(1,6):
    PLjVAR = IntVar ()
FOOD.menu.add_checkbutton ( label = "옥류천식당", variable=PL1VAR, command=food1)
FOOD.menu.add_checkbutton ( label = "패컬티식당", variable=PL2VAR, command=food2)
FOOD.menu.add_checkbutton ( label = "은행골식당", variable=PL3VAR, command=food3)
FOOD.menu.add_checkbutton ( label = "금잔디식당", variable=PL4VAR, command=food4)
FOOD.menu.add_checkbutton ( label = "은행나무아래식당", variable=PL5VAR, command=food5)
FOOD.menu.add_checkbutton ( label = "법고을식당", variable=PL6VAR, command=food6)
FOOD.pack(side="left", anchor = N)

#학사일정 버튼
frame = Frame(map)
frame.pack(anchor=NE)

buttomframe = Frame(map)
buttomframe.pack(side="right")

SCH = Button(frame, text="학사일정", fg="blue", command=sch)
SCH.pack(side="right")

map.mainloop()
