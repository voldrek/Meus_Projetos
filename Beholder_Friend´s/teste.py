from tkinter import *
from tkinter import messagebox

co0 = '#f0f3f5' #preto
co1 = '#feffff' #branco
co2 = '#3fb5a3' #verde
co3 = '#38576b' #valor
co4 = '#403d3d' #letra

login = Tk()

def tela_prinpal():
    login.geometry('500x300')
    login.resizable(width=False, height=False)
    login.configure(background=co1)

    #Dividindo tela
    frame_cima = Frame(login, width=310 , height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = Frame(login, width=500 , height=250, bg=co1, relief='flat')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #configurando frame_cima
    l_nome = Label(frame_cima, text='', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)
    l_linha = Label(frame_cima, text='', width=470, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    #configurando frame baixo
    lista_personagens = Listbox(frame_baixo, width=30, height=14)
    lista_personagens.place(x=310,y=15)
    with open('personagens.txt', 'r') as arquivo:
        for personagem in arquivo:
            lista_personagens.insert(END, personagem.strip())

    login.mainloop()

tela_prinpal()
