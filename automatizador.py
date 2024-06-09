import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minimo = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean() , 2)

destinatario = "email@gmail.com"
assunto = "Analise do projeto"

mensagem = f"""
Olá

Segue as análises dos projetos {ticker}:

valor máximo: R$ {maxima}
valor mínimo: R$ {minimo}
média dos valores: R$ {valor_medio}

Estou a disposição

att. 
"""
# Abrir o navegador e ir para o GMAIL
webbrowser.open("www.gmail.com")
time.sleep(5)

# Configure uma pausa de 3 segundos
pyautogui.PAUSE = 3

# Clicar no botão "escrever"
pyautogui.click(x=93, y=249)

# Digitar o email do destinatario e clicar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("TAB")

# Digite o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("TAB")

# Digite a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão enviar
pyautogui.click(x=1221, y=972)

print("Email enviado")