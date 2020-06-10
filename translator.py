from translate import Translator
from tkinter import *
win=Tk()
win.title("A Simple Translator")
win.geometry('330x230')
win.configure(bg='light cyan')

def german():
    word = E1.get()
    translator = Translator(to_lang='German')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial  Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)
    
def French():
    word = E1.get()
    translator=Translator(to_lang='French')
    translation = translator.translate(word)
    l2=Label(win,text=f'translated word : {translation}',font=('Arial Bold',12),fg='DodgerBlue2')
    l2.place(x=5, y=180)


def spanish():
    word = E1.get()
    translator = Translator(to_lang='Spanish')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)
def Swidish():
    word = E1.get()
    translator = Translator(to_lang='Swedish')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)
def turkish():
    word = E1.get()
    translator = Translator(to_lang='Turkish')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5, y=180)
def chinese():
    word = E1.get()
    translator = Translator(to_lang='Chinese')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5, y=180)
def Arabic():
    word = E1.get()
    translator = Translator(to_lang='Arabic')
    translation = translator.translate(word)
    l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5, y=180)
def Greek():
    word = E1.get()
    translator = Translator(to_lang='Greek')
    translation = translator.translate(word)
    word= " "
    l2 = Label(win, text=f'The Translated word IS : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
    l2.place(x=5,y=180)

txt=StringVar()
label1=Label(win,text="Enter your text Here :")
label1.place(x=85,y=1)
label3=Label(win,text="Your Translation: ",font=('Bold',10))
label3.place(x=5,y=160)
Entry1=Entry(win,textvariable=txt,width=23,font=('bold ',15),bg="white")
Entry1.place(x=17,y=20)
Btn1=Button(win,text='French',padx=8,pady=8,bg="powder blue",width=6,command=French)
Btn1.place(x=5,y=55)
Btn2=Button(win,text='German',padx=8,pady=8,bg="powder blue",width=6,command=german)
Btn2.place(x=75,y=55)
Btn3=Button(win,text='Spanish',padx=8,pady=8,bg="powder blue",width=6,command=spanish)
Btn3.place(x=145,y=55)
Btn4=Button(win,text='Swidish',padx=19,pady=8,bg="powder blue",width=6,command=Swidish)
Btn4.place(x=215,y=55)
Btn5=Button(win,text='Turkish',padx=8,pady=8,bg="powder blue",width=6,command=turkish)
Btn5.place(x=5,y=100)
Btn6=Button(win,text='Chinese',padx=8,pady=8,bg="powder blue",width=6,command=chinese)
Btn6.place(x=75,y=100)
Btn7=Button(win,text='Arabic',padx=8,pady=8,bg="powder blue",width=6,command=Arabic)
Btn7.place(x=145,y=100)
Btn8=Button(win,text='Greek',padx=19,pady=8,bg="powder blue",width=6,command=Greek)
Btn8.place(x=215,y=100)
win.mainloop()
