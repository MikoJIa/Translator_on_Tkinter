from tkinter import *
from deep_translator import GoogleTranslator


def tran():
    text_eng = text_row1.get('1.0', END)
    res_trans = GoogleTranslator(sourse='auto', target='ru').translate(text_eng)
    text_row2.delete('1.0', END)
    text_row2.insert('1.0', res_trans)


root = Tk()
root.title('Translator with Eng on Ru')
root.geometry('1200x600')
root.resizable(width=False, height=False)
# Создадим обьект класса Translater
translator = GoogleTranslator()

l1_row = Label(root, text='Enter text on English', font=('Comic Sans MS', 25, 'bold'), fg='black')
l1_row.place(relx=0.13, rely=0.01)

l2_row = Label(root, text='Translate with English', font=('Comic Sans MS', 25, 'bold'), fg='black')
l2_row.place(relx=0.58, rely=0.01)

text_row1 = Text(root, width=55, height=20,
                 bg='black',
                 font='Arial 12 bold',
                 fg='white',
                 insertbackground='red',
                 wrap=WORD
                 )
text_row1.place(relx=0.09, rely=0.1)

text_row2 = Text(root, width=55, height=20, bg='black', font='Arial 12 bold', fg='white')
text_row2.place(relx=0.55, rely=0.1)

btn = Button(root, width=55, height=5, text='Translate',
             bg='blue',
             fg='yellow',
             font=('Comic Sans', 10, 'bold'),
             command=tran)
btn.place(relx=0.53, rely=0.85, anchor=CENTER)

root.mainloop()