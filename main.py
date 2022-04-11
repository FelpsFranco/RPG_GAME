from tkinter import *
import selecao
from heroes import Warior, Anao, Assassin
from monster import Esqueleto, Zombie, Afogado

esqueleto = Esqueleto()
afogado = Afogado()
zumbi = Zombie()
guerreiro = Warior()
assassino = Assassin()
anao = Anao()

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def change(button, hover, leave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=hover))

    button.bind("<Leave>", func=lambda e: button.config(
        background=leave))

def troca_anao(bg, name, vida, arm, dano):
    global anao
    bg['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Anão.png'
    name['text'] = anao.name
    vida['text'] = anao.vida
    arm['text'] = anao.arm
    dano['text'] = anao.dano

def troca_warior(bg, name, vida, arm, dano):
    global guerreiro
    bg['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Guerreiro.png'
    name['text'] = guerreiro.name
    vida['text'] = guerreiro.vida
    arm['text'] = guerreiro.arm
    dano['text'] = guerreiro.dano

def troca_assassin(bg, name, vida, arm, dano):
    global assassino
    bg['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Assassino.png'
    name['text'] = assassino.name
    vida['text'] = assassino.vida
    arm['text'] = assassino.arm
    dano['text'] = assassino.dano

def troca_esqueleto(bg, name, vida, arm, dano):
    global esqueleto
    bg['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Esqueleto.png'
    name['text'] = esqueleto.name
    vida['text'] = esqueleto.vida
    arm['text'] = esqueleto.arm
    dano['text'] = esqueleto.dano

def troca_afogado(bg, name, vida, arm, dano):
    global afogado
    bg['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Afogado.png'
    name['text'] = afogado.name
    vida['text'] = afogado.vida
    arm['text'] = afogado.arm
    dano['text'] = afogado.dano

def troca_zumbi(bg, name, vida, arm, dano):
    global zumbi
    bg['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Zombie.png'
    name['text'] = zumbi.name
    vida['text'] = zumbi.vida
    arm['text'] = zumbi.arm
    dano['text'] = zumbi.dano

def personagem():
    global guerreiro
    perso_janela = Toplevel()
    perso_janela.attributes('-alpha', 0.0)
    perso_janela.geometry('473x643')
    center(perso_janela)
    perso_janela.attributes('-alpha', 1.0)
    perso_janela.resizable(height=False, width=False)
    perso = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                            'SagaAdventure/imagens/Guerreiro.png')
    nome = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/Nome.png')
    vida = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Vida.png')
    arm = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                          'SagaAdventure/imagens/Armadura.png')
    dano = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/Dano.png')
    label_perso = Label(perso_janela, image=perso, borderwidth=0)
    label_perso.place(x=0, y=0)

    label_avulsa = Label(perso_janela, text='', bg='black')
    label_avulsa.place(x=0, y=10, width=642, height=28)

    button_warior = Button(perso_janela, text='GUERREIRO', command=lambda: (troca_warior(perso, info_name, info_vida, info_arm, info_dano)), bg='black', fg='white', borderwidth=0, activebackground='red')
    button_warior.place(x=50, y=10, width=80, height=28)

    button_anao = Button(perso_janela, text='ANÃO', bg='black', command=lambda: (troca_anao(perso, info_name,  info_vida, info_arm, info_dano)), fg='white', borderwidth=0, activebackground='red')
    button_anao.place(x=200, y=10, width=80, height=28)

    button_assassin = Button(perso_janela, text='ASSASSINO', command=lambda: (troca_assassin(perso, info_name,  info_vida, info_arm, info_dano)), bg='black', fg='white', borderwidth=0, activebackground='red')
    button_assassin.place(x=350, y=10, width=80, height=28)

    img_name = Label(perso_janela, image=nome, relief='solid')
    img_name.place(x=20, y=400)
    info_name = Label(perso_janela, width='10', height='2', text=guerreiro.name, relief='solid', fg='black', bg='white')
    info_name.place(x=70, y=402)

    img_vida = Label(perso_janela, image=vida, relief='solid')
    img_vida.place(x=20, y=450)
    info_vida = Label(perso_janela, width='10', height='2', text=guerreiro.vida, relief='solid', fg='black', bg='white')
    info_vida.place(x=70, y=452)

    img_arm = Label(perso_janela, image=arm, relief='solid')
    img_arm.place(x=20, y=500)
    info_arm = Label(perso_janela, width='10', height='2', text=guerreiro.arm, relief='solid', fg='black', bg='white')
    info_arm.place(x=70, y=502)

    img_dano = Label(perso_janela, image=dano, relief='solid')
    img_dano.place(x=20, y=550)
    info_dano = Label(perso_janela, width='10', height='2', text=guerreiro.dano, relief='solid', fg='black', bg='white')
    info_dano.place(x=70, y=552)

    button_sair = Button(perso_janela, command=perso_janela.destroy, text='SAIR', relief='solid', fg='black', bg='white')
    button_sair.place(x=70, y=600)

    change(button_warior, 'purple', 'black')
    change(button_anao, 'purple', 'black')
    change(button_assassin, 'purple', 'black')

    perso_janela.mainloop()

def monstros():
    global esqueleto
    monstro_janela = Toplevel()
    monstro_janela.attributes('-alpha', 0.0)
    monstro_janela.geometry('473x643')
    center(monstro_janela)
    monstro_janela.attributes('-alpha', 1.0)
    monstro_janela.resizable(height=False, width=False)
    monstro = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Esqueleto.png')
    nome = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Nome.png')
    vida = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Vida.png')
    arm = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Armadura.png')
    dano = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Dano.png')
    label_perso = Label(monstro_janela, image=monstro, borderwidth=0)
    label_perso.place(x=0, y=0)

    label_avulsa = Label(monstro_janela, text='', bg='black')
    label_avulsa.place(x=0, y=10, width=642, height=28)

    button_esqueleto = Button(monstro_janela, text='ESQUELETO', command=lambda: (troca_esqueleto(monstro, info_name, info_vida, info_arm, info_dano)), bg='black', fg='white', borderwidth=0, activebackground='red')
    button_esqueleto.place(x=50, y=10, width=80, height=28)

    button_afogado = Button(monstro_janela, text='AFOGADO', bg='black', command=lambda: (troca_afogado(monstro, info_name, info_vida, info_arm, info_dano)), fg='white', borderwidth=0, activebackground='red')
    button_afogado.place(x=200, y=10, width=80, height=28)

    button_zumbi = Button(monstro_janela, text='ZUMBI', command=lambda: (troca_zumbi(monstro, info_name, info_vida, info_arm, info_dano)), bg='black', fg='white', borderwidth=0, activebackground='red')
    button_zumbi.place(x=350, y=10, width=80, height=28)

    img_name = Label(monstro_janela, image=nome, relief='solid')
    img_name.place(x=20, y=400)
    info_name = Label(monstro_janela, width='10', height='2', text=esqueleto.name, relief='solid', fg='black', bg='white')
    info_name.place(x=70, y=402)

    img_vida = Label(monstro_janela, image=vida, relief='solid')
    img_vida.place(x=20, y=450)
    info_vida = Label(monstro_janela, width='10', height='2', text=esqueleto.vida, relief='solid', fg='black', bg='white')
    info_vida.place(x=70, y=452)

    img_arm = Label(monstro_janela, image=arm, relief='solid')
    img_arm.place(x=20, y=500)
    info_arm = Label(monstro_janela, width='10', height='2', text=esqueleto.arm, relief='solid', fg='black', bg='white')
    info_arm.place(x=70, y=502)

    img_dano = Label(monstro_janela, image=dano, relief='solid')
    img_dano.place(x=20, y=550)
    info_dano = Label(monstro_janela, width='10', height='2', text=esqueleto.dano, relief='solid', fg='black', bg='white')
    info_dano.place(x=70, y=552)

    button_sair = Button(monstro_janela, command=monstro_janela.destroy, text='SAIR', relief='solid', fg='black', bg='white')
    button_sair.place(x=70, y=600)

    change(button_esqueleto, 'purple', 'black')
    change(button_afogado, 'purple', 'black')
    change(button_zumbi, 'purple', 'black')

    monstro_janela.mainloop()

def sair():
    exit()

def iniciar(tela):
    tela.destroy()
    selecao.main()

def menu():
    menu_janela = Tk()
    menu_janela.attributes('-alpha', 0.0)
    menu_janela.geometry('800x400')
    center(menu_janela)
    menu_janela.attributes('-alpha', 1.0)
    menu_janela.resizable(height=False, width=False)
    warior = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Trono.png')
    label_fundo = Label(menu_janela, image=warior, borderwidth=0)
    label_fundo.place(x=0, y=-140)
    
    inicia = Button(menu_janela, text='INICIAR', command=lambda: (iniciar(menu_janela)), borderwidth=0, bg='black', fg='white', activebackground='purple')
    inicia.place(x=325, y=100, width=150, height=28)
    
    button_perso = Button(menu_janela, text='PERSONAGEM', command=personagem, borderwidth=0, bg='black', fg='white', activebackground='purple')
    button_perso.place(x=325, y=150, width=150, height=28)

    button_monstro = Button(menu_janela, text='MONSTRO', command=monstros, borderwidth=0, bg='black', fg='white', activebackground='purple')
    button_monstro.place(x=325, y=200, width=150, height=28)
    
    button_sair = Button(menu_janela, text='SAIR', command=sair, borderwidth=0, bg='black', fg='white', activebackground='purple')
    button_sair.place(x=325, y=300, width=150, height=28)
    
    change(inicia, 'purple', 'black')
    change(button_perso, 'purple', 'black')
    change(button_monstro, 'purple', 'black')
    change(button_sair, 'purple', 'black')
    
    menu_janela.mainloop()


menu()
