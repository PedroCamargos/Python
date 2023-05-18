import pyautogui
import pygetwindow 
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

# Passo 1: Acessar o sistema da empresa
pyautogui.press("win")
pyautogui.write("Mozilla")
pyautogui.press("enter")
pyautogui.write(r"file:///C:/Users/pedro.camargos/Documents/Intensiv%C3%A3o%20Python/pagina/site.html")
pyautogui.press("enter")

# Esperar a janela abrir
time.sleep(1)

# Obter uma referência para a janela do Mozilla Firefox
janela_mozilla = pygetwindow.getWindowsWithTitle('Mozilla Firefox')[0]

# Maximizar a janela
janela_mozilla.maximize()

time.sleep(1)

# Passo 2: Fazer loguin no sistema
pyautogui.click(x=2610, y=357)
pyautogui.write("pedro.camargos")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.click(x=2648, y=491)

time.sleep(4)

# Passo 3: Baixar a base de dados
ag.click(x=3135, y=116)
time.sleep(3)

import pandas as pd

# Passo 4: Calcular os indicadores

# Importar a base de dados 
#r para infomar que é o texto da forma que ta escrito 
tabela = pd.read_csv(r"C:\Users\pedro.camargos\Downloads\Compras.csv", sep=";")
display(tabela)

# calculo dos indicadores 
# total gasto -> somar a coluna valor final 
total_gasto = tabela["ValorFinal"].sum()

# quantidade -> somar a coluna quantidade 
quantidade = tabela["Quantidade"].sum()

# preço medio -> total gasto / quantidade 
preco_medio = total_gasto / quantidade 

print(total_gasto)
print(quantidade)
print(preco_medio)

import pyperclip 

# Passo 5: Enviar o email para a diretoria

#Acessando o e-mail 
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(8)

#Preenchendo o E-mail 
pyautogui.click(x=2070, y=186)

pyautogui.PAUSE = 1

pyautogui.write("pedroudi2020@gmail.com")

pyautogui.press("enter")
pyautogui.press("tab")

assunto = "Relatório Final do Dia"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

#f para informar que terá uma variavel no meio do texto 

# (.2f) é a quantidade de casas decimais 
# ( , ) é a informação de que havera controle de mil (1.000)

texto = f"""
Prezados, 

Segue o relatório de compras.

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produto: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}
    
Qualquer dúvida estou à disposição. 

Att, 
Pedro Camargos 
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=2782, y=696)
