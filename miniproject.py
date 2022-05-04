from tkinter import *
from tkinter import ttk

def next_pg():
    if s.get()!=0:
        new_list = []
        for m in range(s.get()):
            new_list.append(empty_list[m][1].get())
        root.destroy()
        import dac
        dac.run(prev, new_list)
    else:
        label3 = Label(root,text="Please select the number of cities", font=("Calibri 10 bold"), bg="beige" )
        label3.place(x=175, y = c+50)

def sel(event):
    global prev
    if prev < s.get():
        for m in range(prev, s.get()):
            empty_list[m][0].place(x=150, y=empty_list[m][2])
            empty_list[m][1].place(x=250,y=empty_list[m][2])
    prev = s.get()
    for m in range(prev, 6):
        empty_list[m][0].place_forget()
        empty_list[m][1].place_forget()

prev = 0
root=Tk()
root.title("ENTRY PAGE")
root.geometry("760x790+0+0")
root.configure(bg="beige")
#HEADING
Label(text="TRAVELLING SALESMEN PROBLEM", font=("Lucida 20 bold underline"), bg="beige", pady=20).pack()

#Entering Number of Cities
l1=Label(text="Enter number of cities: ", bg="beige", font=("Times 12 bold"))
l1.place(x=50, y=100)

options = ["3","4","5","6"]
s=IntVar()
Comb1= ttk.Combobox(root, value=options, textvariable=s,state='readonly',font=("Times 10 bold"))
Comb1.bind("<<ComboboxSelected>>", sel)
Comb1.place(x=250, y=105)


#TODO: WATCHOUT FOR COLORS IN COMBOBOX
#Comb1.configure(selectbackground="gray")

empty_list = []

c=200
for m in range(6):
    label1 = Label(root,text=f"Enter City {m+1}", font=("Calibri 10 bold"), bg="beige" )
    label1.place(x=150, y=c)
    entry1 = Entry(root,width=40,)
    entry1.place(x=250,y=c)
    empty_list.append([label1,entry1,c])
    c += 30

c+=50
button = Button(root, text="Next", width=50, bg='#90EE99', command=next_pg)
button.place(x=175, y=c)
root.attributes('-alpha',0.9)

if __name__=='__main__':
    root.mainloop()


