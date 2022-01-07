import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

color = {
    'black': '#323232',
    'white': '#F0F0F0',
    'red': '#FF5050',
    'yellow': '#FFDC50',
    'green': '#78FF96',
    'blue': '#00DCF0',
    'purple': '#7850FF'
}

root = Tk()


w_root = 500
h_root = 450

pos_right = round(root.winfo_screenwidth() / 2 - w_root / 2)
pos_down = round(root.winfo_screenheight() / 2 - h_root / 2)

root.geometry('{}x{}+{}+{}'.format(w_root, h_root, pos_right, pos_down))
root.title("Timer")
root['background'] = color['black']
root.resizable(False, False)

hour = StringVar(value='00')
minute = StringVar(value='00')
second = StringVar(value='00')

hour_timer = StringVar(value='00')
minute_timer = StringVar(value='00')
second_timer = StringVar(value='00')

tk.Label(root, text='Enter the values', font=('Tenorite Bold', 30), bg=color['black'], fg=color['white'])\
    .place(x=50, y=20, width=400)

tk.Label(root, text='Enter hours here:', font=('Tenorite', 15), bg=color['black'], fg=color['white'])\
    .place(x=80, y=100)

tk.Label(root, text='Enter minutes here:', font=('Tenorite', 15), bg=color['black'], fg=color['white'])\
    .place(x=80, y=140)

tk.Label(root, text='Enter seconds here:', font=('Tenorite', 15), bg=color['black'], fg=color['white'])\
    .place(x=80,  y=180)

lbl_timer = tk.Label(root, text='00:00:00', font=('Consolas', 40), bg=color['black'], fg=color['white'])
lbl_timer.place(x=80, y=340, width=340)


hourEntry = Entry(root, width=3, font=("Tenorite", 18), fg=color['black'], bd=0,justify='center', textvariable=hour, bg=color['white'])
hourEntry.place(x=320, y=100, width=100)

minuteEntry = Entry(root, width=3, font=("Tenorite", 18),fg=color['black'], bd=0,justify='center', textvariable=minute, bg=color['white'])
minuteEntry.place(x=320, y=140, width=100)

secondEntry = Entry(root, width=3, font=("Tenorite", 18), fg=color['black'], bd=0,justify='center', textvariable=second, bg=color['white'])
secondEntry.place(x=320, y=180, width=100)


def clr():
    global done
    hour.set('00')
    minute.set('00')
    second.set('00')
    hour_timer.set('00')
    minute_timer.set('00')
    second_timer.set('00')
    lbl_timer.configure(text ='00:00:00')
    done = True


clr()

def submit():
    global done
    done = False
    temp = 0
    mins =  0
    secs =  0
    hours =  0

    try:
        temp = int(hourEntry.get()) * 3600 + int(minuteEntry.get()) * 60 + int(secondEntry.get())

    except:
        messagebox.showerror('Timer', 'Integer values required')

    mins, secs = divmod(temp, 60)
    if mins >= 60: hours, mins = divmod(mins, 60)

    hour.set("{0:0=2d}".format(hours))
    minute.set("{0:0=2d}".format(mins))
    second.set("{0:0=2d}".format(secs))

    while temp > 0 and not done:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins >= 60:
            hours, mins = divmod(mins, 60)

        hour_timer.set("{0:0=2d}".format(hours))
        minute_timer.set("{0:0=2d}".format(mins))
        second_timer.set("{0:0=2d}".format(secs))

        lbl_timer.configure(text='{}:{}:{}'.format(hour_timer.get(), minute_timer.get(), second_timer.get()))
        root.update()
        time.sleep(1)
        # root.after(1000)        --- also works correctly
        # pygame.time.wait(1000)  --- also works correctly

        if temp == 1:
            messagebox.showinfo("Timer", "Time's up")
        temp -= 1

    clr()


def closing():
    global done
    action = messagebox.askyesno(title='Exit prompt', message='Are you sure you want to exit?',icon='warning', default='no')
    if action == True:
        clr()
        root.quit()
        print('Have a nice day!')
        quit()



btn_set = Button(root, text='Set Timer', bd='0', command=submit, font=('Tenorite Bold', 15), background=color['green'],activebackground=color['blue'])
btn_set.place(x=320, y=250, width=120)


btn_clr = Button(root, text='Clear', bd='0', command=clr, font=('Tenorite Bold', 15), background=color['yellow'],activebackground=color['purple'])
btn_clr.place(x=190, y=250, width=120)


btn_exit = Button(root, text='Exit', bd='0', command=closing, font=('Tenorite Bold', 15), background=color['red'],activebackground=color['yellow'])
btn_exit.place(x=60, y=250, width=120)


root.protocol("WM_DELETE_WINDOW", closing)

root.mainloop()
