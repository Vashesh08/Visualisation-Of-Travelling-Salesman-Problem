import tkinter
import tkinter.messagebox
import tkinter.font
import random

def run(val=6, empty_list=[1,2,3,4,5,6]):
    main_window = tkinter.Tk()
    main_window.geometry('735x650')
    
    main_window.title("Travelling Salesman Problem")
    main_window.maxsize(1366, 768)
    main_window.minsize(735, 555)

    font = tkinter.font.Font(font='TkHeadingFont', weight="ITALIC")

    new_list = ['red', 'green', 'orange']
    frame_list = []

    box_list = [[tkinter.IntVar() for i in range(val)] for j in range(val)]
    frame_list = tkinter.Frame(main_window, background=new_list[random.randint(0, 2)], height=150, borderwidth=3, width=75, relief='sunken')
    one_list = []
    k=0
    t = s = 1
    for i in range(val-1):
        tkinter.Label(main_window, text=empty_list[i+1]).grid(row=0, column=s) 
        s += 1

    for i in range(val-1):
        tkinter.Label(main_window, text=empty_list[i]).grid(row=t, column=0) 
        t += 1

    for i in range(val):
        for j in range(i+1, val):
            tkinter.Entry(main_window, background='yellow', font=(font, 18), width=4, relief='sunken', justify='center', fg='black', textvariable=box_list[i][j]).grid(row=1+i, column=j, padx=1, pady=1,
                             ipady=10, ipadx=10)
            k+=1
    frame_list.grid(row=1, rowspan=val-1, column=1, columnspan=val-1, padx=2, pady=2, sticky='se')

    def solve():
        main_window.destroy()
        import minipr
        list3 = []
        for i in range(val):
            temp = []
            for j in range(val):
                temp.append(box_list[i][j].get()+box_list[j][i].get())
            list3.append(temp)    
        minipr.run(list2=empty_list,dist=list3, cities=empty_list)


    def new_game():
        for i in range(val):
            for j in range(val):    
                box_list[i][j].set(0) 
        

    Solve_Button = tkinter.Button(main_window, text="Solve", fg='white', relief='raised', font=(font, 20), background='blue', activebackground='light green'
    , command=solve
    )
    Solve_Button.grid(row=val + 1, column=0, sticky='nsew', pady=5, padx=2)
    
    New_Game_Button = tkinter.Button(main_window, text="Reset", fg='black', relief='raised', font=(font, 12), background='orange', activebackground='light green'
    , command=new_game
    )
    New_Game_Button.grid(row=val +1, column=1, sticky='nsew', pady=5, padx=2)

    main_window.mainloop()

if __name__ == '__main__':
    run()