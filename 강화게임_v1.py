import random as r
import os
import tkinter.font as font
from pathlib import Path
from tkinter import *


def home(): # 홈화면
    global newbt, newtb, newtx, newtx2, newtx3, ftx, ftx2, ftx3
    
    # 기존 삭제
    if ("bt" in globals()):
        tx3.destroy()
        bt.destroy()
        bt2.destroy()
        bt3.destroy()
    if ("tx" in globals()):
        tx.destroy()
        tx2.destroy()
    if ("ftx" in globals()):
        ftx.destroy()
        ftx2.destroy()
        ftx3.destroy()
    if ("hltx1" in globals()):
        hltx1.destroy()
        hltx2.destroy()
        hltx3.destroy()

    # 기타 생성
    newbt = Button(win, text="확인", bg="silver", fg="#141412", font=mf, command=login)
    newbt.pack()
    newbt.place(x=350, y=350, width=100, height=50)

    newtb = Entry(win)
    newtb.place(x=300, y=285, width=200, height=30)

    newtx = Label(win, text="닉네임을 입력해주세요.", fg="#141412", font=mf)
    newtx.pack()
    newtx.place(x=290, y=210)
    newtx2 = Label(win, text="강 화 게 임", fg="#141412", font=tf)
    newtx2.pack()
    newtx2.place(x=270, y=60)
    newtx3 = Label(win, text="Made by minigold649", fg="gray", font=minf)
    newtx3.pack()
    newtx3.place(x=320, y=120)



def login(): # 로그인
    global htx, tri
    tri = True
    if ("htx" in globals()):
        htx.destroy()
    name = newtb.get()
    na = list(name)
    if (len(na) != 0):
        for i in range(len(na)):
            if (na[i] == '/' or na[i] == '\\' or na[i] == '*' or na[i] == ':' or na[i] == '?' or na[i] == '"' or na[i] == '<' or na[i] == '>' or na[i] == '|'):
                htx = Label(win, text="사용 불가능한 닉네임입니다.", fg="red", font=mf)
                htx.pack()
                htx.place(x=270, y=450)
                newtb.delete(0, END)
                tri = False
                break
        if (tri):
            main(name)
    else:
        htx = Label(win, text="닉네임을 입력해주세요.", fg="red", font=mf)
        htx.pack()
        htx.place(x=290, y=450)
    


def main(nam):
    global rname, lvl, per, tx, tx2, tx3, bt, bt2, bt3, new
    rname = nam
    new = True
    with open("C:\강화게임파일\\NameList.txt", 'r') as f: # 기존 유저인지 확인
        nl = f.read()
        nl = nl.split("\n")
        for i in range(0, len(nl)):
            if (rname == nl[i]):
                new = False

    if (new): # 새로운 유저
        lvl = 0
        per = 100

    else:
        # 값 불러오기
        with open(f"C:\강화게임파일\{rname}.txt", 'r') as f:
            p = f.read()
            p = p.split("\n")
            lvl = int(p[1])
            per = float(p[0])
    
    # 기존삭제
    newbt.destroy()
    newtb.destroy()
    newtx.destroy()
    newtx2.destroy()
    newtx3.destroy()

    # 기타 생성
    tx = Label(win, text=f"{lvl}강", fg="#141412", font=tmf)
    tx.pack()
    tx.place(x=150, y=280)
    tx2 = Label(win, text=f"성공확률 : {per}%", fg="#141412", font=tmf)
    tx2.pack()
    tx2.place(x=390, y=280)
    tx3 = Label(win, text=f"이름 : {rname}", fg="#141412", font=mf)
    tx3.pack()
    tx3.place(x=50, y=50)

    ldbd()

    bt = Button(win, text="강화", bg="silver", fg="#141412", font=mf, command=hbt1)
    bt.pack()
    bt.place(x=150, y=400, width=100, height=50)
    bt2 = Button(win, text="홈화면", bg="silver", fg="#141412", font=mf, command=home)
    bt2.pack()
    bt2.place(x=350, y=400, width=100, height=50)
    bt3 = Button(win, text="종료", bg="silver", fg="#141412", font=mf, command=hbt3)
    bt3.pack()
    bt3.place(x=550, y=400, width=100, height=50)



def hbt1(): # 강화
    global lvl, per, tx, tx2, ftx, ftx2, ftx3, new
    
    tx.destroy()
    tx2.destroy()
    if ("ftx" in globals()):
        ftx.destroy()
        ftx2.destroy()
        ftx3.destroy()
    
    perc = per*100
    ran = r.randint(1, 10000)
        
    ms = 99 # 확률 내려가는 정도
    udran = r.randint(1,100)
    if (perc >= ran): # 성공
        lvl += 1
        duml = 1
        if (udran > 10):
            lvl += 1
            duml += 1
            if (udran > 20):
                lvl += 1
                duml += 1
                if (udran > 30):
                    lvl += 1
                    duml += 1
                    if (udran > 40):
                        lvl += 1
                        duml += 1
                        if (udran > 50):
                            lvl += 1
                            duml += 1
                            if (udran > 60):
                                lvl += 1
                                duml += 1
                                if (udran > 70):
                                    lvl += 1
                                    duml += 1
                                    if (udran > 80):
                                        lvl += 1
                                        duml += 1
                                        if (udran > 90):
                                            lvl += 1
                                            duml += 1
        for i in range(duml):
            per = int(per * ms)/100
        
        ftx3 = Label(win, text=f"강화 성공! (+{duml})", fg="green", font=tmf)
        ftx3.pack()
        ftx3.place(x=300, y=160)
        
    else: # 실패
        de = r.randint(1, 100)
        if (de > 5): # 대실패 확률
            lvl -= 1
            dumlm = -1
            if (udran > 5):
                lvl -= 1
                dumlm -= 1
                if (udran > 15):
                    lvl -= 1
                    dumlm -= 1
                    if (udran > 25):
                        lvl -= 1
                        dumlm -= 1
                        if (udran > 35):
                            lvl -= 1
                            dumlm -= 1
                            if (udran > 45):
                                lvl -= 1
                                dumlm -= 1
                                if (udran > 55):
                                    lvl -= 1
                                    dumlm -= 1
                                    if (udran > 65):
                                        lvl -= 1
                                        dumlm -= 1
                                        if (udran > 75):
                                            lvl -= 1
                                            dumlm -= 1
                                            if (udran > 85):
                                                lvl -= 1
                                                dumlm -= 1
            if (lvl < 0):
                lvl = 0
            per = 100
            for i in range(0, lvl):
                per = int(per*ms)/100
            
            ftx3 = Label(win, text=f"강화 실패.. ({dumlm})", fg="red", font=tmf)
            ftx3.pack()
            ftx3.place(x=300, y=160)
        else:
            lvl = 0
            per = 100
            ftx3 = Label(win, text=f"강화 대실패 (파괴됨)", fg="red", font=tmf)
            ftx3.pack()
            ftx3.place(x=300, y=160)

    # 저장
    with open(f"C:\강화게임파일\{rname}.txt", 'w') as f:
        f.write(f"{per}\n{lvl}")
        if (new):
            with open("C:\강화게임파일\\NameList.txt", 'a') as fn:
                fn.write(f"{rname}\n")
        new = False

    ftx = Label(win, text=f"{lvl}강", fg="#141412", font=tmf)
    ftx.pack()
    ftx.place(x=150, y=280)
    ftx2 = Label(win, text=f"성공확률 : {per}%", fg="#141412", font=tmf)
    ftx2.pack()
    ftx2.place(x=390, y=280)

    ldbd()



def hbt3(): # 종료
    win.destroy()



def ldbd(): # 순위
    global hltx1, hltx2, hltx3

    if ("hltx1" in globals()):
        hltx1.destroy()
        hltx2.destroy()
        hltx3.destroy()
    # 닉네임 + 강화레벨 가져오기
    lb = []
    temp = []
    with open(f"C:\강화게임파일\\NameList.txt", 'r') as f:
        name = f.read()
        name = name.split("\n")
        for i in range(len(name)-1):
            temp.append([])
    if (len(name) > 1):
        for i in range(len(name)-1):
            with open(f"C:\강화게임파일\{name[i]}.txt", 'r') as f:
                upg = f.read()
                upg = upg.split("\n")
                info = [upg[1], name[i]]
                temp[i] = info
        
        # 강화 큰 순서대로 배열
        lens = len(temp)
        for j in range(lens):
            max = 0
            temp2 = []
            for i in range(len(temp)):
                if (int(temp[i][0]) > max):
                    max = int(temp[i][0])
            for i in range(len(temp)):
                if (max == int(temp[i][0])):
                    temp2 = temp[i]
                    temp.remove(temp[i])
                    break
            lb.append(temp2)
        
    if (0 == len(lb)):
        hltx1 = Label(win, text=f"1등 / ? : ?강", fg="gold", bg="#012e07", font=minf)
        hltx1.pack()
        hltx1.place(x=50, y=100)
        hltx2 = Label(win, text=f"2등 / ? : ?강", fg="silver", bg="#012e07", font=minf)
        hltx2.pack()
        hltx2.place(x=50, y=150)
        hltx3 = Label(win, text=f"3등 / ? : ?강", fg="#b37c60", bg="#012e07", font=minf)
        hltx3.pack()
        hltx3.place(x=50, y=200)
    elif(1 == len(lb)):
        hltx1 = Label(win, text=f"1등 / {lb[0][1]} : {lb[0][0]}강", fg="gold", bg="#012e07", font=minf)
        hltx1.pack()
        hltx1.place(x=50, y=100)
        hltx2 = Label(win, text=f"2등 / ? : ?강", fg="silver", bg="#012e07", font=minf)
        hltx2.pack()
        hltx2.place(x=50, y=150)
        hltx3 = Label(win, text=f"3등 / ? : ?강", fg="#b37c60", bg="#012e07", font=minf)
        hltx3.pack()
        hltx3.place(x=50, y=200)
    elif(2 == len(lb)):
        hltx1 = Label(win, text=f"1등 / {lb[0][1]} : {lb[0][0]}강", fg="gold", bg="#012e07", font=minf)
        hltx1.pack()
        hltx1.place(x=50, y=100)
        hltx2 = Label(win, text=f"2등 / {lb[1][1]} : {lb[1][0]}강", fg="silver", bg="#012e07", font=minf)
        hltx2.pack()
        hltx2.place(x=50, y=150)
        hltx3 = Label(win, text=f"3등 / ? : ?강", fg="#b37c60", bg="#012e07", font=minf)
        hltx3.pack()
        hltx3.place(x=50, y=200)
    else:
        hltx1 = Label(win, text=f"1등 / {lb[0][1]} : {lb[0][0]}강", fg="gold", bg="#012e07", font=minf)
        hltx1.pack()
        hltx1.place(x=50, y=100)
        hltx2 = Label(win, text=f"2등 / {lb[1][1]} : {lb[1][0]}강", fg="silver", bg="#012e07", font=minf)
        hltx2.pack()
        hltx2.place(x=50, y=150)
        hltx3 = Label(win, text=f"3등 / {lb[2][1]} : {lb[2][0]}강", fg="#b37c60", bg="#012e07", font=minf)
        hltx3.pack()
        hltx3.place(x=50, y=200)




tri2 = True
for i in Path("C:\\").iterdir(): # 파일 검사
    i2 = str(i)
    fil = i2.replace("C:\\", "")
    if (fil == "강화게임파일"):
        tri2 = False
        break

if (tri2):
    os.mkdir("C:\강화게임파일") # 파일 생성

f = open("C:\강화게임파일\\NameList.txt", 'a') # 닉넴 리스트 파일 생성
f.close()

win = Tk()
minf = font.Font(size=12, weight="bold")
mf = font.Font(size=15, weight="bold")
tmf = font.Font(size=25, weight="bold")
tf = font.Font(size=40, weight="bold")

# 창 설정
win.title("강화 게임")
win.geometry("800x600")
win.resizable(False, False)

home()

win.mainloop()