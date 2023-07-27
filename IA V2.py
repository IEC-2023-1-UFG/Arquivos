# Importação das bibliotecas
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import requests
import urllib.parse
import webbrowser
import time


# Criação de objetos para entrada e saída de áudio
audio = sr.Recognizer()
maquina = pyttsx3.init()

# Inicialização padrão da assistente
maquina.say('Olá, eu sou a Lia, sua assistente virtual desenvolvida por alunos da Universidade Federal de Goiás')
maquina.say('Como posso ajudar?')
maquina.runAndWait()

def executa_comando():  # Entrada de áudio
    try:  # Testagem do microfone
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)  # Entrada de áudio da fonte
            comando = audio.recognize_google(voz, language='pt-BR')  # Seleção da biblioteca de voz que irá reconhecer a voz do usuário
            comando = comando.lower()  # Transcrever o que foi dito para letra minúscula
            if 'lia' in comando:  # Verifica se a assistente virtual foi chamada
                comando = comando.replace('lia', '')  # Retira o nome da assistente do comando dito
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

    elif 'toque' in comando:  # Reproduz primeiro vídeo no YouTube
        musica = comando.replace('toque', '')
        pesquisa = musica + ' música'  # Adiciona "música" à pesquisa para melhorar os resultados
        pesquisa_encoded = urllib.parse.quote(pesquisa)
        url = "https://www.youtube.com/results?search_query={}".format(pesquisa_encoded)
        time.sleep(3)
        response = requests.get(url)
        video_id = None
        if response.ok:
            start = response.text.find('{"videoId":"') + len('{"videoId":"')
            end = response.text.find('","webPageType"')
            video_id = response.text[start:end]
        if video_id:
            youtube_url = "https://www.youtube.com/watch?v={}".format(video_id)
            maquina.say('Tocando música')
            webbrowser.open(youtube_url)
            maquina.runAndWait()
        else:
            maquina.say('Nenhum vídeo encontrado')
            maquina.runAndWait()

    elif 'procure vídeos' in comando:  # Procura qualquer vídeo no YouTube
        musica = comando.replace('procure vídeos', '')
        url = 'https://www.youtube.com/results?search_query={}'.format(musica)
        maquina.say('Abrindo resultados da pesquisa')
        webbrowser.open(url)
        maquina.runAndWait()
    
    elif 'procure imagens de' in comando:  # Procura imagens no Google
        termo_pesquisa = comando.replace('procure imagens de', '')
        url = 'https://www.google.com.br/search?q={}&gl=br&tbm=isch&sxsrf=AB5stBhN31bua67Jlg6trgh_zAHiFXDfcA%3A1690422583557&source=hp&biw=1280&bih=907&ei=N83BZKOEIKTK1sQP7p-EwAw&iflsig=AD69kcEAAAAAZMHbRwR-O0rgx2I2QcSdNpnj-u4UmupA&oq=&gs_lp=EgNpbWciACoCCAAyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCdI2TJQAFgAcAF4AJABAJgBAKABAKoBALgBAcgBAIoCC2d3cy13aXotaW1nqAIK&sclient=img'.format(termo_pesquisa)
        maquina.say('Pesquisando imagens de ' + termo_pesquisa)
        webbrowser.open(url)
        maquina.runAndWait()

    elif 'pesquise por' in comando:  # Pesquisar qualquer coisa no Google
        termo_pesquisa = comando.replace('pesquise por', '')
        url = 'https://www.google.com/search?q={}'.format(termo_pesquisa)
        maquina.say('Pesquisando' + termo_pesquisa)
        webbrowser.open(url)
        maquina.runAndWait()

    elif 'abra meu e-mail' in comando:  # Abrindo e-mail
        url = 'https://mail.google.com/mail/?authuser=0'
        maquina.say('Abrindo e-mail')
        webbrowser.open(url)
        maquina.runAndWait()

    elif 'ache' in comando:  # Pesquisando no google maps
        termo_pesquisa = comando.replace('ache', '')
        url = 'https://www.google.com.br/maps/search/{}/'.format(termo_pesquisa)
        maquina.say('Pesquisando no Google Maps'+termo_pesquisa)
        webbrowser.open(url)
        maquina.runAndWait()
    

comando_voz_usuario()