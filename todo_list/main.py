import tkinter
from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("To do List")
root.geometry("400x650+400+100")
root.resizable(False, False)
root.iconbitmap('list.ico')
root.config(bg="red")

task_list= []

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
    
        for task in tasks:
            if task !="\n":
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file= open("tasklist.txt", "w")
        file.close()


def Add():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def delete():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)


#Top Bar
TopImage = ImageTk.PhotoImage(Image.open("Img/list_banner.jpg"))
label1 = Label(root, image= TopImage)
label1.pack()


brainImage = ImageTk.PhotoImage(Image.open("Img/brain_64.png"))
label2 = Label(root, image= brainImage)
label2.place(x=30, y=25)

productivityImage = ImageTk.PhotoImage(Image.open("Img/productivity_64.png"))
label3 = Label(root, image= productivityImage)
label3.place(x= 330, y= 25)

heading= Label(root, text= "All task", font=("Courier", 32), fg= "white", bg= "#32405b")
heading.place(x= 110, y= 25) 


#Main
frame1 = Frame(root, width= 400, height= 35, bg="white")
frame1.place(x= 0, y= 300)

task= StringVar()
task_entry = Entry(frame1, width= 23, font= ("arial", 20), bd= 0, bg="#FDF7C3")
task_entry.place(x= 1 , y= 1)
task_entry.focus()

btn1 = Button(frame1, bd=0, text= "Add", font=("Courier", 16), bg="#A6D0DD", command= Add, fg="#FFD3B0")
btn1.place(x= 290, y= 0)

#ListBox
frame2= Frame(root, bd=3, width= 700, height= 25, bg="black")
frame2.pack()

listbox= Listbox(frame2, font=("Courier",16), width=40, height=16, bg="#333C83", fg="#FDAF75", cursor = "hand2", selectbackground="#4D96FF")
listbox.pack(side= LEFT, fill= "y", padx= 2)

scrollbar1 = Scrollbar(frame2)
scrollbar1.pack(side= RIGHT, fill= BOTH)

listbox.config(yscrollcommand= scrollbar1.set)
scrollbar1.config(command= listbox.yview)


openTaskFile()

#deelete Button

btn2 = Button(frame1, bd=0, text="Del", fg="#FFD3B0", bg="#FF6969", command= delete, font=("Courier", 16))
btn2.place(x=345, y=0)





root.mainloop()
