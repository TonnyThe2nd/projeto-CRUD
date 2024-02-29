import pyodbc as py
from tkinter import *
from tkinter import ttk

import datetime as dt
import random as rd
#ID
id = rd.randint(10000,99999)

#LISTAS

civil = ['Casado(a)','Solteiro(a)','Viúvo(a)','Divorciado(a)','Separado(a)']
#SQL


dados_conect = (                             
        "Driver={SQL Server};" 
        "Server=localhost\SQLEXPRESS;" #USUÁRIO PODE ALTERAR O SERVER PARA USAR O CÓDIGO EM SEU PROPRIO BANCO DE DADOS!!!!
        "Database=Cliente_Cadastro;"
) 
conect = py.connect(dados_conect)
cursor = conect.cursor()
#TELA
root = Tk()
root.title('Cadastro')
root.geometry("700x600")
root.maxsize(700,600)

#FUNÇÕES
def sair():
    root.destroy()
def registrar():
    cliente = nome_entry.get()
    cliente_social = nome_social_entry.get()
    cpf_cliente = cpf_entry.get()
    cpf_format = f'{cpf_cliente[0:3]}.{cpf_cliente[3:6]}.{cpf_cliente[6:9]}-{cpf_cliente[9:11]}'
    rg_cliente = rg_entry.get()
    rg_format = f'{rg_cliente[0:2]}.{rg_cliente[2:5]}.{rg_cliente[6:9]}-{rg_cliente[8]}'
    email_cliente = email_entry.get()
    email_rec_cliente = email_rec_entry.get()
    ddd_um_cliente = celular_ddd.get()
    celular_um_cliente = celular_num.get()
    num_cliente = '(' +''.join(ddd_um_cliente)+')'+' '+''.join(celular_um_cliente)
    num_um_format = f'{num_cliente[0:5]} {num_cliente[5:10]}-{num_cliente[10:14]}'
    ddd_dois_cliente = celular_dois_ddd.get()
    celular_dois_cliente = celular_dois_num.get()
    numdois_cliente = '(' +''.join(ddd_dois_cliente)+')'+' ' +''.join(celular_dois_cliente)
    num_dois_format = f'{numdois_cliente[0:5]} {numdois_cliente[5:10]}-{numdois_cliente[10:14]}'
    endereco_cliente = endereco_entry.get()
    cidade_cliente = cidade_entry.get()
    estado_cliente = estado_entry.get()
    sit = estado_civil.get()
    data = dt.datetime.today().year
    age = ano_entry.get()
    idade = data - int(age)

    inserir = f"""INSERT INTO informacoes_cliente(id, nome_cliente, nome_social, cpf, rg, idade, endereco, cidade, estado, email, email_rec, civil, celular_um, celular_dois) 
                    VALUES({id},'{cliente}','{cliente_social}','{cpf_format}','{rg_format}',{idade},'{endereco_cliente.title()}','{cidade_cliente.title()}',
                    '{estado_cliente.upper()}','{email_cliente}','{email_rec_cliente}','{sit}','{num_um_format}','{num_dois_format}')"""
    cursor.execute(inserir)
    cursor.commit()
    nome_entry.delete(0, END)
    nome_social_entry.delete(0, END)
    cpf_entry.delete(0, END)
    rg_entry.delete(0, END)
    email_entry.delete(0,END)
    email_rec_entry.delete(0,END)
    estado_civil.delete(0,END)
    ano_entry.delete(0,END)
    mes_entry.delete(0,END)
    dia_entry.delete(0,END)
    cidade_entry.delete(0,END)
    estado_entry.delete(0,END)
    endereco_entry.delete(0,END)
    celular_num.delete(0,END)
    celular_ddd.delete(0,END)
    celular_dois_num.delete(0,END)
    celular_dois_ddd.delete(0,END)
#CUSTOMIZAÇÃO

nome = Label(root, text='Nome do Cliente: ', font=('Aryal 10'))
nome.place(x=10,y=50)
nome_social = Label(root, text='Nome Social: ', font=('Aryal 10'))
nome_social.place(x=370,y=50)
nome_social_entry = Entry(root, width=35, font=('Aryal'))
nome_social_entry.place(x=370, y=70)
nome_entry = Entry(root, width=35, font=('Aryal'))
nome_entry.place(x=10, y=70)

cpf = Label(root, text='CPF : ', font=('Aryal 10'))
cpf.place(x=10,y=100)
cpf_entry = Entry(root, width=20, font=('Aryal'))
cpf_entry.place(x=10,y=120)

rg = Label(root, text='RG : ', font=('Aryal 10'))
rg.place(x=250,y=100)
rg_entry = Entry(root, width=20, font=('Aryal'))
rg_entry.place(x=250,y=120)

email = Label(root, text='E-Mail : ', font=('Aryal 10'))
email.place(x=10,y=160)
email_entry = Entry(root, width=30, font=('Aryal'))
email_entry.place(x=10,y=180)
email_rec = Label(root, text='E-Mail de Recuperação : ', font=('Aryal 10'))
email_rec.place(x=310,y=160)
email_rec_entry = Entry(root, width=30, font=('Aryal'))
email_rec_entry.place(x=310,y=180)

celular = Label(root, text='Celular 1 : ', font=('Aryal 10'))
celular.place(x=10,y=210)
celular_ddd = Entry(root, width=5, font=('Aryal'), justify=CENTER)
celular_ddd.place(x=10,y=230)
celular_num = Entry(root, width=20, font=('Aryal'))
celular_num.place(x=80,y=230)

celular_dois = Label(root, text='Celular 2 : ', font=('Aryal 10'))
celular_dois.place(x=300,y=210)
celular_dois_ddd = Entry(root, width=5, font=('Aryal'), justify=CENTER)
celular_dois_ddd.place(x=300,y=230)
celular_dois_num = Entry(root, width=20, font=('Aryal'))
celular_dois_num.place(x=370,y=230)

endereco = Label(root, text='Endereço(Rua) : ', font=('Aryal 10'))
endereco.place(x=10,y=260)
endereco_entry = Entry(root, width=35, font=('Aryal'))
endereco_entry.place(x=10, y=280)
cidade = Label(root, text='Cidade : ', font=('Aryal 10'))
cidade.place(x=370,y=260)
cidade_entry = Entry(root, width=20, font=('Aryal'))
cidade_entry.place(x=370,y=280)
estado = Label(root, text='Estado : ', font=('Aryal 10'))
estado.place(x=580,y=260)
estado_entry = Entry(root, width=5, font=('Aryal'), justify=CENTER)
estado_entry.place(x=580,y=280)

sit = Label(root, text='Estado Civil : ', font=('Aryal 10'))
sit.place(x=10, y= 320)
estado_civil = ttk.Combobox(root, values=civil)
estado_civil.place(x=10, y= 340)

nascimento = Label(root, text='Data de Nascimento', font=('Aryal 10'))
nascimento.place(x=300, y= 320)
dia = Label(root, text='Dia', font=('Aryal 10'))
dia.place(x=300, y= 350)
mes = Label(root, text='Mês', font=('Aryal 10'))
mes.place(x=370, y= 350)
ano = Label(root, text='Ano', font=('Aryal 10'))
ano.place(x=440, y= 350)
dia_entry = Entry(root, width=5, font=('Aryal'), justify=CENTER)
dia_entry.place(x=300, y= 370)
mes_entry = Entry(root, width=5, font=('Aryal'), justify=CENTER)
mes_entry.place(x=370, y= 370)
ano_entry = Entry(root, width=5, font=('Aryal'), justify=CENTER)
ano_entry.place(x=440, y= 370)
0
button_registro = Button(text='Registrar',font=('Aryal'), width=20, command=registrar)
button_registro.place(x= 130, y=450)

button_sair = Button(text='Sair',font=('Aryal'), width=20, command=sair)
button_sair.place(x= 350, y=450)



root.mainloop()