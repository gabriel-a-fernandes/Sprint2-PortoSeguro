''' O objetivo do projeto é atualizar e automatizar o processo de solicitação e envio do
modal para o cliente, diminuindo o maximo de trabalho humano possível no processo de acionamento do seguro. '''

from utilidades import *

cabecalho("\033[034mOlá, Bem vindo a central de atendimento da Porto\033[m")
inicializacao()

while True:
    cabecalho("\033[034mMENU PRINCIPAL\033[m")
    resposta = menu(["Cadastro", "Contratação de Seguros", "Acionamento de Seguro",
                     "Falar com Representante", "Encerrar Atendimento"])
    if resposta == 1:
        menu_cadastro()
    elif resposta == 2:
        menu_contrata_seguro()
    elif resposta == 3:
        menu_aciona_seguro()
    elif resposta == 4:
        falar_representante()
    elif resposta == 5:
        cabecalho("\033[034mEncerrando o Atendimento... Até Logo!\033[m")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida\033[m")

