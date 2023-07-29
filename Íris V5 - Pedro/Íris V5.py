import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import requests
import pywhatkit as pwk
import time
import random
import os
import requests
import customtkinter
from translate import Translator
from langdetect import detect
from bardapi import Bard
import tkinter
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
from PIL import Image, ImageTk


token = "{YwiZ-gRyevqsq161v7ek2fgAvbjWPkHNGOaGnVQIlSi_OYpHsent4ONkAr12jgUAVf44Xw.}" ##Token de autenticação do Google Bard


"""Observações de desenvolvedor:
o que foi dito irá ser transformado em letra MINÚSCULA pois esse é o padrão pra que ela realize o comando desejado"""



palavroes = ['retardada','idiota','caralho','cu','cuzona','filha da puta','filho da puta','desgraçado','desgraçada',
             'merda','piranha','porra','bosta']

#lista de piadas:
piadas = [
            "Por que a mulher do Hulk divorciou-se dele? Porque ela queria um homem mais maduro.",
            "Qual é o contrário de volátil? Vem cá sobrinho!",
            "Você conhece a piada do pônei? Pô nei eu...",
            "Por que o livro de matemática cometeu suicídio? Porque tinha muitos problemas.",
        ]
def codigo():
    audio = sr.Recognizer()
    maquina = pyttsx3.init()

    def executa_comando():  # Entrada de áudio
        try:  # Testagem do microfone
            with sr.Microphone() as source:
                print('Ouvindo..')
                voz = audio.listen(source)  # Entrada de áudio da fonte
                comando = audio.recognize_google(voz, language='pt-BR')  # Seleção da biblioteca de voz que irá reconhecer a voz do usuário
                comando = comando.lower()  # Transcrever o que foi dito para letra minúscula
                if 'iris' in comando:  # Verifica se a assistente virtual foi chamada
                    comando = comando.replace('iris', '')  # Retira o nome da assistente do comando dito
                    maquina.say(comando)
                    maquina.runAndWait()

        except:  # Microfone não está entregando o áudio
            print('Microfone não está ok')

        return comando

#### Funções para converter hora em algarismos para hora em texto, necessário para o comando de voz que diz as horas
    def numero_para_palavra(numero):
        unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
                "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
                "dezoito", "dezenove"]
        dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        if 0 <= numero < 20:
            return unidades[numero]
        elif 20 <= numero < 100:
            dezena, unidade = divmod(numero, 10)
            return dezenas[dezena] + (" e " + unidades[unidade] if unidade != 0 else "")
        else:
            return str(numero)
    def hora_para_texto(hora):
        horas, minutos = hora.split(':')
        horas_texto = numero_para_palavra(int(horas))
        minutos_texto = numero_para_palavra(int(minutos))
        return horas_texto + ' e ' + minutos_texto
####
#função pra verificar se tem palavrão:
    def palavrao (comando):
        def palavrao1(palavroes):
            comando
            if palavroes in comando:
                return True
            else:
                return False
    
        resposta = list(map(palavrao1,palavroes))
    
        if True in resposta:
            return True
        else: 
            return False

#função pra tradução automática:

    def traduzir(texto):
        idioma_detectado = detect(texto)
        translator = Translator(from_lang= str(idioma_detectado), to_lang='pt')
        resultado = translator.translate(texto)
        return resultado

    def comando_voz_usuario():  # Saída de áudio
        comando = executa_comando()
        if 'horas' in comando:  # Retorna a hora
            hora_atual = datetime.datetime.now().strftime('%H:%M')
            hora_texto = hora_para_texto(hora_atual)
            maquina.say('Agora são ' + hora_texto)
            maquina.runAndWait()

        elif 'procure por' in comando: #Retorna informações dadas pelo resumo do Wikipédia
            procurar = comando.replace('procure por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()
    
        elif 'bem' in comando:
            maquina.say('Poderia estar melhor se tivesse passado em lógica...')
            maquina.runAndWait()

        
        elif 'piada' in comando: #fazendo uma piada
        
        # Selecionar uma piada aleatória
            piada = random.choice(piadas)

        # Falar a piada
            maquina.say(piada)
            maquina.runAndWait()
    
        elif palavrao(comando) is True: #verificando se tem palavrão
            maquina.say("Por favor pare de usar palavras chulas, fale novamente com mais educação")
            maquina.runAndWait()
        
        elif 'traduza' in comando:
            comando = comando.replace('íris','')
            comando = comando.replace('traduza','')
            frase = traduzir(comando)
        
            if palavrao(frase) is True: #verificando se tem palavrão
                maquina.say("Você achou que eu ia falar um palavrão não é?! Mas eu não sou burra. Me dê outro comando")
                print("Você achou que eu ia falar um palavrão não é?! Mas eu não sou burra. Me dê outro comando")
                maquina.runAndWait()
            else:
                maquina.say("A frase traduzida é: "+ frase)
                print("A frase traduzida é:" + frase)
                maquina.runAndWait()
    
        elif 'toque' in comando:  # Reproduzir música no YouTube
                musica = comando.replace('toque', '').strip()
                pesquisa = musica + ' música'  # Adiciona "música" à pesquisa para melhorar os resultados
                pwk.playonyt(pesquisa)
                maquina.runAndWait()

        elif 'pesquise' in comando: #Pesquisa no Bard
                comando = comando.replace('íris','')
                comando = comando.replace('pesquise','')
                input_text = (comando)
                maquina.say(Bard().get_answer(input_text)['content'])
                maquina.runAndWait()
    
    comando_voz_usuario() 

def codigo2():
    nome_assistente = "iris"  # Defina o nome da sua assistente aqui
    parada = "pare" #defina o comando de parada

        #lista de piadas:
    piadas = [
            "Por que a mulher do Hulk divorciou-se dele? Porque ela queria um homem mais maduro.",
            "Qual é o contrário de volátil? Vem cá sobrinho!",
            "Você conhece a piada do pônei? Pô nei eu...",
            "Por que o livro de matemática cometeu suicídio? Porque tinha muitos problemas.",
        ]   
    def palavrao (comando):
        def palavrao1(palavroes):
            comando
            if palavroes in comando:
                return True
            else:
                return False
    
        resposta = list(map(palavrao1,palavroes))
    
        if True in resposta:
            return True
        else: 
            return False
    def traduzir(texto):
        idioma_detectado = detect(texto)
        translator = Translator(from_lang= str(idioma_detectado), to_lang='pt')
        resultado = translator.translate(texto)
        return resultado
    #### Funções para converter hora em algarismos para hora em texto, necessário para o comando de voz que diz as horas
    def numero_para_palavra(numero):
        unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
                    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
                    "dezoito", "dezenove"]
        dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        if 0 <= numero < 20:
            return unidades[numero]
        elif 20 <= numero < 100:
            dezena, unidade = divmod(numero, 10)
            return dezenas[dezena] + (" e " + unidades[unidade] if unidade != 0 else "")
        else:
            return str(numero)
    def hora_para_texto(hora):
        horas, minutos = hora.split(':')
        horas_texto = numero_para_palavra(int(horas))
        minutos_texto = numero_para_palavra(int(minutos))
        return horas_texto + ' e ' + minutos_texto
    ####

    def comando_voz_usuario():  # Saída de áudio
        comando = comando_sem_nome
        if 'horas' in comando:  # Retorna a hora
            hora_atual = datetime.datetime.now().strftime('%H:%M')
            hora_texto = hora_para_texto(hora_atual)
            maquina.say('Agora são ' + hora_texto)
            maquina.runAndWait()

        elif 'procure por' in comando: #Retorna informações dadas pelo resumo do Wikipédia
            procurar = comando.replace('procure por', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            print(resultado)
            maquina.say(resultado)
            maquina.runAndWait()
    
        elif 'bem' in comando:
            maquina.say('Poderia estar melhor se tivesse passado em lógica...')
            maquina.runAndWait()

        
        elif 'piada' in comando: #fazendo uma piada
        
        # Selecionar uma piada aleatória
            piada = random.choice(piadas)

        # Falar a piada
            maquina.say(piada)
            maquina.runAndWait()
    
        elif palavrao(comando) is True: #verificando se tem palavrão
            maquina.say("Por favor pare de usar palavras chulas, fale novamente com mais educação")
            maquina.runAndWait()
        
        elif 'traduza' in comando:
            comando = comando.replace('íris','')
            comando = comando.replace('traduza','')
            frase = traduzir(comando)
        
            if palavrao(frase) is True: #verificando se tem palavrão
                maquina.say("Você achou que eu ia falar um palavrão não é?! Mas eu não sou burra. Me dê outro comando")
                print("Você achou que eu ia falar um palavrão não é?! Mas eu não sou burra. Me dê outro comando")
                maquina.runAndWait()
            else:
                maquina.say("A frase traduzida é: "+ frase)
                print("A frase traduzida é:" + frase)
                maquina.runAndWait()
    
        elif 'toque' in comando:  # Reproduzir música no YouTube
                musica = comando.replace('toque', '').strip()
                pesquisa = musica + ' música'  # Adiciona "música" à pesquisa para melhorar os resultados
                pwk.playonyt(pesquisa)
                maquina.runAndWait()

        elif 'pesquise' in comando: #Pesquisa no Bard
                comando = comando.replace('íris','')
                comando = comando.replace('pesquise','')
                input_text = (comando)
                maquina.say(Bard().get_answer(input_text)['content'])
                maquina.runAndWait()
        
        
    def escutar():
        reconhecimento = sr.Recognizer()
        with sr.Microphone() as source:
            print("Aguardando comando...")
            reconhecimento.adjust_for_ambient_noise(source)  # Ajustar ruído ambiente
            audio = reconhecimento.listen(source)

        try:
            comando = reconhecimento.recognize_google(audio, language='pt-BR')
            print("Você disse: " + comando)
            return comando.lower()
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
            return ""
        except sr.RequestError:
            print("Não foi possível acessar o serviço de reconhecimento de voz. Verifique sua conexão com a internet.")
            return ""


    while True:
        maquina = pyttsx3.init()
        comando = escutar()
        if parada in comando:
            print(f"Vou descansar um pouco")
            maquina.say("Vou descansar um pouco")
            maquina.runAndWait()
            break
                
        elif nome_assistente in comando:
            print("Assistente ativada...")
            comando_sem_nome = comando.replace(nome_assistente, '').strip().lower()
            print("Comando: " + comando_sem_nome)
            comando_voz_usuario()

def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

largura = 550
altura = 350

def abrir_nova_janela():
    def centralizar_janela(janela, largura, altura):
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        janela.geometry(f"{largura}x{altura}+{x}+{y}")

    largura = 550
    altura = 240
    nova_janela = customtkinter.CTk()
    nova_janela.geometry("550x200")
    nova_janela.configure(bg="gray")  # Definir uma cor de fundo diferente para a nova janela

    texto_nova_janela = customtkinter.CTkLabel(nova_janela, text="Essa é a nova janela!")
    texto_nova_janela.pack(padx=20, pady=10)

    nova_janela.option_add("*Font", "Roboto 20 bold")
    icone_path = r"C:\Users\Pedro\Desktop\cyclone_1f300.ico"
    nova_janela.iconbitmap(icone_path)

    nova_janela = customtkinter.CTk()
    centralizar_janela(nova_janela, largura, altura)
    nova_janela.title("Sobre a Íris")

    nova_janela.mainloop()

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    
    janela = customtkinter.CTk()
    janela.geometry("700x160")
    centralizar_janela(janela, largura, altura)
    janela.title("Íris")
    
    #Colocando ícone personalizado
    janela.option_add("*Font", "Roboto 20 bold")
    icone_path = r"C:\Users\Pedro\Desktop\cyclone_1f300.ico"
    janela.iconbitmap(icone_path)

    # Criação do CTkLabel com nova fonte e tamanho
    texto = customtkinter.CTkLabel(janela, text="Olá, eu sou a Íris, sua assistente virtual, como posso ajudar?")
    texto.configure(font=("Calibri", 20))  # Defina a fonte e o tamanho do texto
    texto.pack(padx=20, pady=10)
    texto.place(x=30,y=180)

    # Criação do CTkButton com nova fonte e tamanho
    botao = customtkinter.CTkButton(janela, text="Falar comando", command=codigo)
    botao.configure(font=("Calibri", 14, "bold"))  # Defina a fonte e o tamanho do texto do botão
    botao.pack(padx=10, pady=10)
    botao.place(x=210,y=220)

    # Criação do CTkButton com nova fonte e tamanho
    botao = customtkinter.CTkButton(janela, text="Manter assistente ativa", command=codigo2)
    botao.configure(font=("Calibri", 14, "bold"))  # Defina a fonte e o tamanho do texto do botão
    botao.pack(padx=10, pady=10)
    botao.place(x=200,y=260)

    # Botão que abre a nova janela
    botao_nova_janela = customtkinter.CTkButton(janela, text="Sobre a Íris ", command=abrir_nova_janela)
    botao_nova_janela.configure(font=("Roboto", 10))
    botao_nova_janela.pack(padx=10, pady=14)
    botao_nova_janela.place(x=30,y=300)

    # Botão que fecha tudo
    botao_sair = customtkinter.CTkButton(janela, text="SAIR ", command=sys.exit)
    botao_sair.configure(font=("Roboto", 10))
    botao_sair.pack(padx=40, pady=10)
    botao_sair.place(x=400,y=300)


    imagem = Image.open(r"C:\Users\Pedro\Desktop\slogan.png")
    largura_desejada = 300
    altura_desejada = 150
    imagem_redimensionada = imagem.resize((largura_desejada, altura_desejada), Image.ANTIALIAS)
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
    widget_imagem = tkinter.Label(janela, image=imagem_tk, borderwidth=0)
    widget_imagem.pack_forget()
    widget_imagem.pack()
    widget_imagem.place(x=140,y=10)
    janela.mainloop()