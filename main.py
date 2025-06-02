from tkinter import *
from tkinter import ttk


# Cores:
co1 = "#EDF2F7"     #branco
co2 = "#E53E3E"     #vermelho
co3 = "#000000"     #preto
co4 = "#424c53"     #cinza
co5 = "#9EFDA9"     #abacate


# Janela:
janela = Tk()
janela.title('BiCalc')
janela.geometry('500x430')
janela.resizable(False,False)
janela.configure(bg=co1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, sticky=EW)


# Divisão da janela em dois frames:
frame_cima = Frame(janela, height=60, bg=co4) #cinza
frame_cima.grid(row=1,column=0,sticky=EW)

frame_baixo = Frame(janela, width=500, height=300, bg=co1, pady=12, padx=20) #branco
frame_baixo.grid(row=2, column=0, sticky='ew')


# Configurando frame de cima:
app_nome = Label(frame_cima, text="* Conversor BiCalc *", relief=FLAT, anchor='center',
                    font=('System 25 bold'), bg=co4, fg=co1) #cinza #branco
app_nome.pack(fill=X,expand=True,pady=10)


# Variáveis para exibição
valor_binario = StringVar()
valor_decimal = StringVar()
valor_octal = StringVar()
valor_hexadecimal = StringVar()


# Função de conversão:
def conversor_BiCalc():
    """
    Converte o valor digitado pelo usuário para binário, decimal, octal e hexadecimal,
    com base na opção selecionada.
    
    Emite mensagem de erro na tela do usuário, caso ocorra.
    
    Utiliza variáveis globais de interface: e_valor (entrada), combo (menu de base),
    e os StringVars para saída.
    """
    
    l_erro['text'] = ""
    valor_binario.set("")
    valor_decimal.set("")
    valor_octal.set("")
    valor_hexadecimal.set("")

    entrada = e_valor.get()
    base_nome = combo.get()

    if not entrada or not base_nome:
        l_erro['text'] = "Selecione uma base e digite um valor"
        return

    match base_nome:
        case 'BINARIO':
            base = 2
        case 'DECIMAL':
            base = 10
        case 'OCTAL':
            base = 8
        case 'HEXADECIMAL':
            base = 16

    try:
        inteiro = int(entrada, base)
        valor_binario.set(bin(inteiro)[2:])
        valor_decimal.set(str(inteiro))
        valor_octal.set(oct(inteiro)[2:])
        valor_hexadecimal.set(hex(inteiro)[2:].upper())
        
    except ValueError:
        l_erro['text'] = "Valor inválido para o tipo selecionado"


# Label da base:
l_instrucao_base = Label(frame_baixo, text="Selecione uma base:", relief=FLAT, anchor='center',
                         font=('Verdana', 11, 'bold'), fg=co3)
l_instrucao_base.place(x=10, y=-10, height=30)

bases = ['BINARIO','DECIMAL','OCTAL','HEXADECIMAL']
combo = ttk.Combobox(frame_baixo, width=17, justify=CENTER, font=('Ivi 12 bold'), state='readonly')
combo['values'] = (bases)
combo.place(x=10, y=25)


# Label da entrada:
l_instrucao_valor = Label(frame_baixo, text="Digite abaixo o valor:",
                        relief=FLAT, anchor='center', font=('Verdana', 11, 'bold'), fg=co3)
l_instrucao_valor.place(x=10, y=56, height=30)

e_valor = Entry(frame_baixo,width=24, justify='left', font=("",14),
                highlightthickness=1, relief='solid')
e_valor.place(x=10, y=88)


# Botão Converter:
b_converter = Button(frame_baixo,command=conversor_BiCalc, text="CONVERTER", relief=RAISED,
                     overrelief=RIDGE,width=15, font=('Ivy 10 bold'), bg=co5, fg=co3)
b_converter.place(x=280, y=88)


# Label de Erro:
l_erro = Label(frame_baixo, text="", relief=FLAT,anchor='w',
               font=('Verdana 10 bold'), fg=co2)
l_erro.place(x=10,y=118)


# Labels com Entry de saída:
def criar_saida(y, titulo, var):
    """
    Cria dinamicamente um par de widgets (Label e Entry) para exibir
    os resultados das conversões na interface gráfica.

    Parâmetros:
    y (int): Posição vertical no frame.
    titulo (str): Texto a ser exibido como título da base (ex: "Binário:").
    var (StringVar): Variável associada ao Entry, onde o valor convertido será exibido.
    """
    
    Label(frame_baixo, text=titulo, width=11, relief=FLAT, anchor='nw',
          font=('Verdana 13 bold'), bg=co4, fg=co1).place(x=-15,y=y)
    Entry(frame_baixo, textvariable=var, state='readonly', width=34,
          readonlybackground=co1, fg=co3, font=('Verdana 11')).place(x=125, y=y)


criar_saida(160, "Binário:", valor_binario)
criar_saida(195, "Decimal:", valor_decimal)
criar_saida(228, "Octal:", valor_octal)
criar_saida(260, "Hexadecimal:", valor_hexadecimal)



janela.mainloop()