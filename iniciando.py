from tkinter import *
from monster import Esqueleto, Zombie, Afogado
from heroes import Warior, Anao, Assassin


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


def sou_guerreiro():
    print('ola')
    personagem = Warior()
    test1(personagem)


def sou_assassino():
    personagem = Assassin()
    test1(personagem)


def sou_anao():
    personagem = Anao()
    test1(personagem)


def altera_imagem(guerreiro, perso):
    if guerreiro.name == 'Lion':
        perso['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Guerreiro.png'

    if guerreiro.name == 'Katarina':
        perso['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Assassino.png'

    if guerreiro.name == 'Jarl':
        perso['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Anão.png'

def entrando(img, btt, frente):
    img['file'] = 'C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/SagaAdventure/imagens/Corredor.png'
    btt['text'] = ''
    frente['text'] = 'R E T O'

def test1(guerreiro):
    perso_janela = Tk()
    perso_janela.attributes('-alpha', 0.0)
    perso_janela.geometry('1373x643')
    center(perso_janela)
    perso_janela.attributes('-alpha', 1.0)
    perso_janela.resizable(height=False, width=False)
    perso_janela.configure(bg='black')
    perso = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                            'SagaAdventure/imagens/Fundo.png')
    altera_imagem(guerreiro, perso)
    name = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/Nome.png')
    life = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/Vida.png')
    armad = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                            'SagaAdventure/imagens/Armadura.png')
    damage = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                             'SagaAdventure/imagens/Dano.png')
    acao = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/GATE.png')

    label_perso = Label(perso_janela, image=perso, borderwidth=0)
    label_perso.place(x=0, y=0)

    label_acao = Label(perso_janela, image=acao, borderwidth=0)
    label_acao.place(x=900, y=0)

    button_inicia = Button(perso_janela, text='ENTRAR', borderwidth=0, bg='black', fg='white')
    button_inicia.place(x=500, y=700)

    img_name = Label(perso_janela, image=name, relief='solid')
    img_name.place(x=20, y=400)
    info_name = Label(perso_janela, width='10', height='2', text=guerreiro.name, relief='solid', fg='black', bg='white')
    info_name.place(x=70, y=402)

    img_vida = Label(perso_janela, image=life, relief='solid')
    img_vida.place(x=20, y=450)
    info_vida = Label(perso_janela, width='10', height='2', text=guerreiro.vida, relief='solid', fg='black', bg='white')
    info_vida.place(x=70, y=452)

    img_arm = Label(perso_janela, image=armad, relief='solid')
    img_arm.place(x=20, y=500)
    info_arm = Label(perso_janela, width='10', height='2', text=guerreiro.arm, relief='solid', fg='black', bg='white')
    info_arm.place(x=70, y=502)

    img_dano = Label(perso_janela, image=damage, relief='solid')
    img_dano.place(x=20, y=550)
    info_dano = Label(perso_janela, width='10', height='2', text=guerreiro.dano, relief='solid', fg='black', bg='white')
    info_dano.place(x=70, y=552)

    button_inicia = Button(perso_janela, text='E N T R A R', command=lambda: (entrando(acao, button_inicia, button_reto)), borderwidth=0, bg='black', fg='white')
    button_inicia.place(x=650, y=600)

    button_esquerda = Button(perso_janela, text='', borderwidth=0, bg='black', fg='white')
    button_esquerda.place(x=500, y=500)

    button_direita = Button(perso_janela, text='', borderwidth=0, bg='black', fg='white')
    button_direita.place(x=800, y=500)

    button_reto = Button(perso_janela, text='', borderwidth=0, bg='black', fg='white')
    button_reto.place(x=670, y=500)

    perso_janela.mainloop()
