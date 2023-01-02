#an time watcher app named pomodoro
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN="#82b74b"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
rep=0
timer=None
#working of timer
#25min work then 5 minn break for 3 times and then a long reak of 20 min at last
# ---------------------------- TIMER RESET ------------------------------- # 
#to reset everything from start

def res_tim():
    strt_but.config(state="normal")
    rest_but.config(state="disabled")
    window.after_cancel(timer)    #to stop time and makeit to start postion
    canva.itemconfig(timer_txt,text="00:00")
    title_lb.config(text="Timer")
    chck_mrk.config(text="")
    global rep
    rep=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def strt_tim():
    global rep
    rep+=1
    strt_but.config(state="disabled")
    rest_but.config(state="normal")
    wrk_sec=WORK_MIN*60
    shrt_brk_sec=SHORT_BREAK_MIN*60
    lng_brk_sec=LONG_BREAK_MIN*60

    if rep%8==0:
        cnt_dw(lng_brk_sec)
        title_lb.config(text=" Long Break",fg=DARK_GREEN)
    elif rep%2==0:
        cnt_dw(shrt_brk_sec)
        title_lb.config(text=" Short Break", fg=YELLOW)
    else :
        cnt_dw(wrk_sec)
        title_lb.config(text="Work Time", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def cnt_dw(count):

    count_min=math.floor(count/60)     #return integer value oly if 4.8 return 4 or if 5.2 reurn 5
    count_sec=count%60                 #dynamic typing is used to make in strat with 2 digit of 00 instead of 5:0 ->5:00
    if count_sec<10:
        count_sec=f"0{count_sec}"      #dynmaic typing concept is used here int to str and then strt to int
    canva.itemconfig(timer_txt,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer= window.after(200,cnt_dw,count-1)       #chnage the speed of time by varying 1st argument of window.after function
    else :
        strt_tim()
        mark=""
        #for every 2 rep 1 work will get complted so one green tick mark
        for i in range(math.floor(rep/2)):
            mark+="✔"
        chck_mrk.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=PINK)


title_lb=Label(text="Timer",fg=GREEN,bg=PINK,font=(FONT_NAME,50))
title_lb.grid(column=1,row=0)

#canva widgets are used to put things on top of eah other its like rea world canva

canva=Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
tom_img=PhotoImage(file="tomato.png")
canva.create_image(100,112,image=tom_img)
timer_txt=canva.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canva.grid(column=1,row=2)


strt_but=Button(text="Start",highlightthickness=0,command=strt_tim)
strt_but.grid(column=0,row=3)


rest_but=Button(text="Reset",highlightthickness=0,command=res_tim)
rest_but.grid(column=2,row=3)

chck_mrk=Label(fg="#82b74b",bg=PINK)
chck_mrk.grid(column=1,row=4)








window.mainloop()