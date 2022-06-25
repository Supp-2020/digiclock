from tkinter import *
import time

clk = Tk()
clk.title("Digital Clock")
clk.geometry("1350x700+0+0")
#  width,height,x-axis,y-axis respectively and kept x and y axis 0 to make it start from the left top corner                    
clk.resizable(width=False, height=False)  # Cannot resize the GUI app
clk.config(bg = "#0C1E28")

def clock():
    hr = str(time.strftime("%H"))
    mm = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    wd = str(time.strftime("%A"))
    dt = str(time.strftime("%D"))
    print(hr,mm,sc,wd,dt)
    if int(hr) > 12 and int(mm) > 0:     #  For converting AM to PM
        lb_dn.config(text = "PM")
    if int(hr) > 12:
        hr = str(int(int(hr)-12))

    lb_hr.config(text = hr)
    lb_mm.config(text = mm)
    lb_sc.config(text = sc)
    lb_wd.config(text = wd)
    lb_dt.config(text = dt)

    lb_hr.after(200,clock)        #  It makes the clock update every 200 miliseconds


lb_hr = Label(clk,text = "12" , font = ("Times 20 bold",75,'bold'),bg = "#3D405B",fg = "white")
lb_hr.place(x=350 , y=200 , width=150 , height=150)

lb_hr_txt = Label(clk, text = "HOUR",font = ("Times 20 bold",20,'bold'),bg = "#3D405B",fg = "white")
lb_hr_txt.place(x=350 , y=360 , width=150 , height=50)
#hr

lb_mm = Label(clk,text = "12" , font = ("Times 20 bold",75,'bold'),bg = "#D62828",fg = "white")
lb_mm.place(x=520 , y=200 , width=150 , height=150)

lb_mm_txt = Label(clk, text = "MINUTE",font = ("Times 20 bold",20,'bold'),bg = "#D62828",fg = "white")
lb_mm_txt.place(x=520 , y=360 , width=150 , height=50)
#minute

lb_sc = Label(clk,text = "12" , font = ("Times 20 bold",75,'bold'),bg = "#F77F00",fg = "white")
lb_sc.place(x=690 , y=200 , width=150 , height=150)

lb_sc_txt = Label(clk, text = "SECOND",font = ("Times 20 bold",20,'bold'),bg = "#F77F00",fg = "white")
lb_sc_txt.place(x=690 , y=360 , width=150 , height=50)
#seconds

lb_dn = Label(clk,text = "AM" , font = ("Times 20 bold",70,'bold'),bg = "#FCBF49",fg = "white")
lb_dn.place(x=860 , y=200 , width=150 , height=150)

lb_dn_txt = Label(clk, text = "NOON",font = ("Times 20 bold",20,'bold'),bg = "#FCBF49",fg = "white")
lb_dn_txt.place(x=860 , y=360 , width=150 , height=50)
#Day and Night

lb_wd = Label(clk,text = "Monday" , font = ("Times 20 bold",45,'bold'),bg = "#F2CC8F",fg = "white")
lb_wd.place(x=350 , y=430 , width=320 , height=80)
#Week Day

lb_dt = Label(clk,text = "Monday" , font = ("Times 20 bold",45,'bold'),bg = "#81B29A",fg = "white")
lb_dt.place(x=690 , y=430 , width=320 , height=80)
#Date


clock()
clk.mainloop()
