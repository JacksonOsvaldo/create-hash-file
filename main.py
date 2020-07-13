#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import hashlib as hl
import tkinter.filedialog as fdlg
import tkinter.scrolledtext as tkst
import webbrowser
from datetime import datetime
from tkinter import messagebox as msb
from tkinter.constants import END, HORIZONTAL, VERTICAL, NW, N, E, W, S, SUNKEN, LEFT, RIGHT, TOP, BOTH, YES, NE, X, RAISED, SUNKEN, DISABLED, NORMAL, CENTER, WORD


"""
Definindo funções
"""

# Abrindo link de autoria na web


def callback(url):
    webbrowser.open_new(url)

# Abrindo arquivo


def abrindoArquivo():

    saida.delete('1.0', END)

    label01['text'] = fdlg.askopenfilename()

# Função que gera as HASH


def gerandoHash():

    saida.delete('1.0', END)

    # BUF_SIZE pode ser arbitrário. Mude de acordo com seu arquivo.
    BUF_SIZE = 65536  # vamos ler as coisas em blocos 64kb.

    SHA1 = hl.sha1()
    SHA224 = hl.sha224()
    SHA256 = hl.sha256()
    SHA384 = hl.sha384()
    SHA512 = hl.sha512()
    try:
        with open('{}'.format(label01.cget('text')), 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                SHA1.update(data)
                SHA224.update(data)
                SHA256.update(data)
                SHA384.update(data)
                SHA512.update(data)
            msb.showinfo(title='Concluido',
                         message='Operação realizada com sucesso!')
            saida.insert(END, "Arquivo Utilizado: {}\n\nSHA1: {}\n\nSHA224: {}\n\nSHA256: {}\n\nSHA384: {}\n\nSHA512: {}\n".format(
                label01.cget('text'), SHA1.hexdigest(), SHA224.hexdigest(), SHA256.hexdigest(), SHA384.hexdigest(), SHA512.hexdigest()))
    except FileNotFoundError as e:
        msb.showwarning(e, 'Arquivo não encontrado. Selecione um arquivo.')

# Salvando em um arquivo .txt


def salvar():

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y às %H:%M")

    try:
        f = fdlg.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        tex2Save = str(saida.get(1.0, END)) + \
            'Códigos gerados em: '+data_e_hora_em_texto
        f.write(tex2Save)
        msb.showinfo(title='Salvar', message='Dados salvos com sucesso!')
        f.close()
    except NameError as e:
        msb.showwarning(e, 'Alguma coisa aconteceu. Tente novamente.')


# Instanciando janela Tkinte.tk
janela = tk.Tk()

# Carregando arquivo
label01 = tk.Label(janela, borderwidth=2, relief="groove", width=70)
label01.grid(row=1, column=0, columnspan=2)

btn01 = tk.Button(janela, text='Arquivo',
                  comman=abrindoArquivo, font='Bold 12', bg="blue", fg='black')
btn01.grid(row=1, column=1, columnspan=8)

# Saida das HASH
saida = tkst.ScrolledText(janela, width=100, height=20)
saida.grid(row=2, column=0,  columnspan=4, sticky=E+W+N+S)


# Autoria
label02 = tk.Label(
    janela, text='Developed by Jackson Osvaldo', fg="blue", width=70)
label02.grid(row=3, column=0)
label02.bind(
    "<Button-1>", lambda e: callback("http://jacksonosvaldo.github.io"))

# Gerando HASH. Botão
btn02 = tk.Button(janela, text='Gerar HASH',
                  comman=gerandoHash, borderwidth=2, relief="groove", bg="yellow", fg='black', font='Bold 12')
btn02.grid(row=3, column=1)

# Botão para salvar arquivo
btn03 = tk.Button(janela, text='Salvar Arquivo',
                  comman=salvar, borderwidth=2, relief="groove", bg="green", fg='black', font='Bold 12')
btn03.grid(row=3, column=2, columnspan=4)

# Executando
janela.resizable(0, 0)
janela.title('Create HASH File')
janela.mainloop()
