from tkinter import *
import iniciando
from heroes import Warior, Anao, Assassin

guerreiro = Warior()
assassino = Assassin()
anao = Anao()

def escolhe_guerreiro(tela):
    tela.destroy()
    iniciando.sou_guerreiro()

def escolhe_assassino(tela):
    tela.destroy()
    iniciando.sou_assassino()

def escolhe_anao(tela):
    tela.destroy()
    iniciando.sou_anao()

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

def main():
    global guerreiro, assassino, anao
    menu_janela = Tk()
    menu_janela.attributes('-alpha', 0.0)
    menu_janela.geometry('1373x643')
    center(menu_janela)
    menu_janela.attributes('-alpha', 1.0)
    menu_janela.resizable(height=False, width=False)

    # ------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------

    image_warior = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                                   'SagaAdventure/imagens/Guerreiro.png')
    image_assassin = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                                     'SagaAdventure/imagens/Assassino.png')
    image_anao = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                                 'SagaAdventure/imagens/Anão.png')
    nome = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/Nome.png')
    vida = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/Vida.png')
    arm = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                          'SagaAdventure/imagens/Armadura.png')
    dano = PhotoImage(file='C:/Users/felip/OneDrive/Área de Trabalho/pythonProject/'
                           'SagaAdventure/imagens/Dano.png')

    # ------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------

    label_warior = Button(menu_janela, image=image_warior, command=lambda: (escolhe_guerreiro(menu_janela)), borderwidth=0)
    label_warior.place(x=0, y=0)

    label_assassin = Button(menu_janela, image=image_assassin, command=lambda: (escolhe_assassino(menu_janela)), borderwidth=0)
    label_assassin.place(x=440, y=0)

    label_anao = Button(menu_janela, image=image_anao, command=lambda: (escolhe_anao(menu_janela)), borderwidth=0)
    label_anao.place(x=900, y=0)

    select_label = Label(menu_janela, text='SELECIONE UM CAMPEÃO', bg='black', fg='white')
    select_label.place(x=0, y=1, width=1400, height=28)

    # ------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------

    img_name = Label(menu_janela, image=nome, relief='solid')
    img_name.place(x=20, y=400)
    info_name = Label(menu_janela, width='10', height='2', text=guerreiro.name, relief='solid', fg='black', bg='white')
    info_name.place(x=70, y=402)

    img_vida = Label(menu_janela, image=vida, relief='solid')
    img_vida.place(x=20, y=450)
    info_vida = Label(menu_janela, width='10', height='2', text=guerreiro.vida, relief='solid', fg='black', bg='white')
    info_vida.place(x=70, y=452)

    img_arm = Label(menu_janela, image=arm, relief='solid')
    img_arm.place(x=20, y=500)
    info_arm = Label(menu_janela, width='10', height='2', text=guerreiro.arm, relief='solid', fg='black', bg='white')
    info_arm.place(x=70, y=502)

    img_dano = Label(menu_janela, image=dano, relief='solid')
    img_dano.place(x=20, y=550)
    info_dano = Label(menu_janela, width='10', height='2', text=guerreiro.dano, relief='solid', fg='black', bg='white')
    info_dano.place(x=70, y=552)

    # ------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------

    img_name = Label(menu_janela, image=nome, relief='solid')
    img_name.place(x=470, y=400)
    info_name = Label(menu_janela, width='10', height='2', text=assassino.name, relief='solid', fg='black', bg='white')
    info_name.place(x=520, y=402)

    img_vida = Label(menu_janela, image=vida, relief='solid')
    img_vida.place(x=470, y=450)
    info_vida = Label(menu_janela, width='10', height='2', text=assassino.vida, relief='solid', fg='black', bg='white')
    info_vida.place(x=520, y=452)

    img_arm = Label(menu_janela, image=arm, relief='solid')
    img_arm.place(x=470, y=500)
    info_arm = Label(menu_janela, width='10', height='2', text=assassino.arm, relief='solid', fg='black', bg='white')
    info_arm.place(x=520, y=502)

    img_dano = Label(menu_janela, image=dano, relief='solid')
    img_dano.place(x=470, y=550)
    info_dano = Label(menu_janela, width='10', height='2', text=assassino.dano, relief='solid', fg='black', bg='white')
    info_dano.place(x=520, y=552)

    # ------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------

    img_name = Label(menu_janela, image=nome, relief='solid')
    img_name.place(x=930, y=400)
    info_name = Label(menu_janela, width='10', height='2', text=anao.name, relief='solid', fg='black', bg='white')
    info_name.place(x=980, y=402)

    img_vida = Label(menu_janela, image=vida, relief='solid')
    img_vida.place(x=930, y=450)
    info_vida = Label(menu_janela, width='10', height='2', text=anao.vida, relief='solid', fg='black', bg='white')
    info_vida.place(x=980, y=452)

    img_arm = Label(menu_janela, image=arm, relief='solid')
    img_arm.place(x=930, y=500)
    info_arm = Label(menu_janela, width='10', height='2', text=anao.arm, relief='solid', fg='black', bg='white')
    info_arm.place(x=980, y=502)

    img_dano = Label(menu_janela, image=dano, relief='solid')
    img_dano.place(x=930, y=550)
    info_dano = Label(menu_janela, width='10', height='2', text=anao.dano, relief='solid', fg='black', bg='white')
    info_dano.place(x=980, y=552)

    menu_janela.mainloop()
