#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import hashlib as hl
import tkinter.filedialog as fdlg
from tkinter import messagebox as msb
import tkinter.scrolledtext as tkst
from tkinter.constants import END, HORIZONTAL, VERTICAL, NW, N, E, W, S, SUNKEN, LEFT, RIGHT, TOP, BOTH, YES, NE, X, RAISED, SUNKEN, DISABLED, NORMAL, CENTER, WORD
import webbrowser


"""
Definindo funções
"""

# Abrindo link de autoria na web


def callback(url):
    webbrowser.open_new(url)

# Abrindo arquivo


def abrindoArquivo():

    label01['text'] = fdlg.askopenfilename()

# Função que gera as HASH


def gerandoHash():

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


janela = tk.Tk()

# Carregando arquivo
label01 = tk.Label(janela, borderwidth=2, relief="groove", width=70)
label01.grid(row=1, column=0)
label01.configure(state="disabled")

btn01 = tk.Button(janela, text='Arquivo',
                  comman=abrindoArquivo, font='Bold 12', bg="blue", fg='black')
btn01.grid(row=1, column=1, columnspan=4)

# Saida das HASH
saida = tkst.ScrolledText(janela, width=100, height=10)
saida.grid(row=2, column=0,  columnspan=4, sticky=E+W+N+S)

# Autoria
label02 = tk.Label(
    janela, text='Developed by Jackson Osvaldo', fg="blue", width=70)
label02.grid(row=3, column=0)
label02.bind(
    "<Button-1>", lambda e: callback("http://jacksonosvaldo.github.io"))

# Gerando HASH. Botão
btn02 = tk.Button(janela, text='Gerar HASH',
                  comman=gerandoHash, borderwidth=2, relief="groove", bg="green", fg='black', font='Bold 12')
btn02.grid(row=3, column=1, columnspan=4)

# Executando
janela.resizable(0, 0)
janela.title('Create HASH File')
janela.mainloop()
