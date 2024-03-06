from tkinter import *
import tkinter.font as font

elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

# 숫자 입력
def login():
    global firstT5
    
    if ("firstT5" in globals()):
        firstT5.destroy()
    n = firstIn1.get()
    a = list(n)
    tri = True
    
    if (len(a) != 0):
        for i in range(len(a)):
            if (a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9' or a[i] == '0'):
                continue
            else:
                firstT5 = Label(win, text="잘못 입력", fg="red", bg=color, font=normalF)
                firstT5.place(x=346, y=470)
                firstIn1.delete(0, END)
                tri = False
                break
    else:
        firstT5 = Label(win, text="잘못 입력", fg="red", bg=color, font=normalF)
        firstT5.place(x=346, y=470)
        firstIn1.delete(0, END)
        tri = False
    if (tri):
        if (int(n) > 0 and int(n) < 119):
            Fsecond(int(n))
        else:
            firstT5 = Label(win, text="잘못된 범위", fg="red", bg=color, font=normalF)
            firstT5.place(x=335, y=470)
            firstIn1.delete(0, END)

# 정답 확인
def testing():
    global i, no, secondB1, secondT1, secondIn1, secondT2
    
    if ("secondT2" in globals()):
        secondT2.destroy()

    if (secondIn1.get() == elements[i-1]):
        secondT2 = Label(win, text="O", fg="green", bg=color, font=wowF)
        secondT2.place(x=357, y=60)
        i += 1
    else:
        secondT2 = Label(win, text="X", fg="red", bg=color, font=wowF)
        secondT2.place(x=358, y=60)
        no += 1
    
    secondT1.destroy()
    secondIn1.destroy()
    secondB1.destroy()
    
    if (i < 119):
        second()
    else:
        third()

# 첫번째 화면
def first():
    global firstT1, firstT2, firstT3, firstT4, firstIn1, firstB1, thirdT1, thirdT2, thirdT3, thirdB1
    if ("thirdT1" in globals()):
        thirdT1.destroy()
        thirdT2.destroy()
        thirdT3.destroy()
        thirdB1.destroy()

    firstT1 = Label(win, text="원소주기율표 맞추기!", fg="#000000", bg=color, font=bigF)
    firstT1.place(x=210, y=70)
    firstT2 = Label(win, text="Made by minigold649", fg="green", bg=color, font=smallF)
    firstT2.place(x=300, y=120)
    firstT3 = Label(win, text="몇번째부터 맞추시겠습니까?", fg="#000000", bg=color, font=normalF)
    firstT3.place(x=253, y=230)
    firstT4 = Label(win, text="(1 ~ 118)", fg="gray", bg=color, font=smallF)
    firstT4.place(x=355, y=270)

    firstIn1 = Entry(win)
    firstIn1.place(x=300, y=320, width=200, height=30)

    firstB1 = Button(win, text="확인", bg="silver", fg="#141412", font=smallF, command=login)
    firstB1.place(x=350, y=380, width=100, height=50)

# 두번째 화면 (1회성)
def Fsecond(n):
    global i, no, start
    firstT1.destroy()
    firstT2.destroy()
    firstT3.destroy()
    firstT4.destroy()
    firstIn1.destroy()
    firstB1.destroy()
    if ("firstT5" in globals()):
        firstT5.destroy()
    i = n
    start = n
    no = 0
    second()

# 두번째 화면 (반복)
def second():
    global i, secondB1, secondT1, secondIn1

    if (i < 10):
        secondT1 = Label(win, text=f"{i}번째 원소", fg="#000000", bg=color, font=bigF)
        secondT1.place(x=300, y=250)
    elif (i < 100):
        secondT1 = Label(win, text=f"{i}번째 원소", fg="#000000", bg=color, font=bigF)
        secondT1.place(x=290, y=250)
    else:
        secondT1 = Label(win, text=f"{i}번째 원소", fg="#000000", bg=color, font=bigF)
        secondT1.place(x=280, y=250)
    
    secondIn1 = Entry(win)
    secondIn1.place(x=300, y=360, width=200, height=30)

    secondB1 = Button(win, text="확인", bg="silver", fg="#141412", font=smallF, command=testing)
    secondB1.place(x=350, y=450, width=100, height=50)

# 세번째 화면
def third():
    global secondT2, thirdT1, thirdT2, thirdT3, thirdB1
    secondT2.destroy()

    thirdT1 = Label(win, text=f"시작위치 : {start}번째", fg="#000000", bg=color, font=normalF)
    thirdT1.place(x=299, y=210)
    thirdT2 = Label(win, text=f"틀린횟수 : {no}개", fg="#000000", bg=color, font=normalF)
    thirdT2.place(x=300, y=260)
    thirdT3 = Label(win, text="F I N I S H", fg="#b88700", bg=color, font=bigF)
    thirdT3.place(x=310, y=100)

    thirdB1 = Button(win, text="홈화면", bg="silver", fg="#141412", font=smallF, command=first)
    thirdB1.place(x=350, y=350, width=100, height=50)

# 창 설정
win = Tk()
win.title("원소주기율표 맞추기")
winW, winH = (800, 600)
win.geometry(f"{winW}x{winH}")
win.resizable(False, False)
color = "#d4f5a6"
winbg = Canvas(win)
winbg.config(width=winW, height=winH, bd=0, highlightthickness=0)
winbg.pack()
winbg.create_rectangle((0, 0), (winW, winH), fill=color)

wowF = font.Font(size=80, weight="bold")
bigF = font.Font(size=30, weight="bold")
normalF = font.Font(size=18, weight="bold")
smallF = font.Font(size=15, weight="bold")
first()
win.mainloop()