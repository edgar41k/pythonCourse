# from tkinter import *
# # import tkinter.colorchooser
# from tkinter import messagebox

# root = Tk() # создание окна

# root.title("TKinter sample app") 
# root.geometry("800x600") # задание размера окна
# # root.iconbitmap("python_icon.ico") # задание иконки

# # text_var = StringVar()

# v_var = IntVar()
# h_var = IntVar()

# vertical = Scale(root, from_=0, to=5)
# vertical.pack()
# horizontal = Scale(root, from_=0, to=500, orient=HORIZONTAL)
# horizontal.pack()

# Label(root, textvariable=v_var).pack()
# Label(root, textvariable=h_var).pack()

# Button(root, text='click', command=lambda: print(horizontal.get(), vertical.get())).pack()

# # def make_choice1():
# #     global text_var
# #     text_var.set(f'You selected {radio_choice.get()}')

# # def make_choice2():
# #     global text_var
# #     text_var.set(f'Your choice is {check_choise.get()}')

# # def clicked():
# #     messagebox.showinfo("Im title", "Im message")

# # def clicked():
# #     response = messagebox.askyesno("Im title", "Im message")
# #     Label(root, text=response).pack()
# #     if response == 0:
# #         Label(root, text="You clicked No").pack()
# #     else:
# #         Label(root, text="You clicked Yes").pack()

# # Button(root, text="MessageBox", command=clicked).pack()

# # radio_choice = IntVar()
# # radio_choice.set(2)


# # Radiobutton(root, text='Choice 1', variable=radio_choice, value=1), command=make_choice.pack()
# # Radiobutton(root, text='Choice 2', variable=radio_choice, value=2), command=make_choice.pack()

# # myLabel = Label(root, textvariable=text_var)
# # myLabel.pack()

# # check_choise = StringVar()
# # chk_box = Checkbutton(root, text="Check me out", variable=check_choise, command=make_choice2, 
#                     # onvalue="Selected", offvalue="Not selected")
# # chk_box.deselect()
# # chk_box.pack()

# # image1 = PhotoImage(file="image1.png") # загрузка изображения, не изменяя размер картинки
# # myLabel = Label(root, image=image1) # создание метки с изображением
# # myLabel.pack()

# # quit_button = Button(root, text="Exit", command=root.quit) # создание кнопки 
# # quit_button.pack()

# # frame = LabelFrame(root, text="This is my frame") # создание фрейма
# # frame.pack()

# # btn = Button(frame, text='My frame button') # создание кнопки внутри фрейма
# # btn.pack()

# # user_text = StringVar() # создание переменной для хранения текста

# # user_entry = Entry(root, textvariable=user_text) # создание поля ввода
# # user_entry.place(x=80, y=50) # размещение поля ввода

# # myLabel = Label(root, textvariable=user_text) # создание метки
# # myLabel.pack() # размещение метки

# # myLabel1 = Label(root, text="Hello")
# # myLabel2 = Label(root, text="Hello")
# # myLabel3 = Label(root, text="Hello")
# # myLabel4 = Label(root, text="Hello")

# # myLabel1.grid(row=0, column=0)
# # myLabel2.grid(row=1, column=1)
# # myLabel3.grid(row=2, column=2)

# # def myClick(number):
# #     # Label(root, text=f'Hello {user_entry.get()}').pack()
# #     user_entry.delete(0, END)
# # try:
# #     user_entry.insert(0, int(number) ** 2)
# # except ValueError:
# #     user_entry.insert(0, "Enter your number: ")


# # user_entry= Entry(root, width=300, borderwidth=5, bd=1) # создание поля ввода, с параметрами
# # user_entry.pack()
# # user_entry.insert(0, "Enter your name: ")

# # myButton= Button(root, text="Click me", fg="white", bg="black", pady=20, padx=20, 
# #                 command=lambda: myClick(user_entry.get())) # если у функции нет аргументов, то можно не указывать лямбду

# # myButton.pack()



# # color = tkinter.colorchooser.askcolor() # выбор цвета
# # print(color)


# root.mainloop() # запуск цикла обработки событий

