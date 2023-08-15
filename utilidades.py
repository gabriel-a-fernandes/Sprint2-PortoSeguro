"""LISTAS"""

clientes = []
planos = []

'''FUNÇÕES PRINCIPAIS'''


def leiaInt(msg):
    """
    Função que lê a opção desejada e se a opção não estiver correta
    ela retorna uma mensagem de erro.
    :param msg: int
    :return: string
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\n\33[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def linha(tam=55):
    """
    Função que cria uma linha para dividir o menu
    :param tam: int (quantidade de caracteres)
    :return: string (caracteres)
    """
    return "-" * tam


def cabecalho(txt):
    """
    Função que cria um cabecalho entre duas linhas
    :param txt: string (texto que vai aparecer entre as linhas)
    :return: string (cabeçalho com o texto do parâmetro)
    """
    print(linha())
    print(txt.center(55))
    print(linha())


def menu(lista):
    """
    Função que cria uma lista com a quantidade de argumentos escolhidos
    :param lista: strings (opções do menu)
    :return: int (itens do menu) e string (nome dos itens do menu)
    """
    c = 1
    for item in lista:
        print(f"\033[32m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt(f"\033[32mSua Opção:\033[m ")
    return opc


def inicializacao():
    """
    Função que formata o nome do usuário com texto de boas vindas
    para iniciar a conversa no chat
    :return: string (mensagem de boas vindas como o nome do usuário)
    """
    print("\033[034mPor favor, digite seu primeiro nome:\033[m ")
    nome_cliente = str(input())
    print(f"\033[034mOlá {nome_cliente}, como podemos ajudar ?\033[m ")
    return


'''#FUNÇÕES PARA A ABA CADASTRO'''


def cadastrar_cliente():
    """
    Função que cadastra o cliente recebendo os dados como nome, cpf, telefone e email
    :return: string (cliente)
    """
    cabecalho("\033[034mCADASTRO DE CLIENTE\033[m")
    nome = input("\033[034mDigite o seu nome completo:\033[m ")
    cpf = input("\033[034mDigite o seu cpf (somente os números, sem espaços ou caracteres especiais):\033[m ")
    telefone = input("\033[034mDigite o seu telefone(somente os números, sem espaços ou caracteres especiais):\033[m ")
    email = input("\033[034mDigite o seu email:\033[m ")
    cliente = {
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'email': email
    }
    clientes.append(cliente)
    print(f"\033[032m{nome} o seu cadastro foi realizado com sucesso!!\033[m")
    return cliente


def atualizar_cadastro():
    """
    Função que atualiza os dados do cliente cadastrado
    :return: String (dados atualizados)
    """
    cabecalho("\033[034mATUALIZAR CADASTRO\033[m")
    cpf = input("\033[034mDigite o CPF do cliente que deseja atualizar (somente os números, sem caracteres):\033[m ")
    atualizado = False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            novo_nome = input("\033[034mDigite o novo nome:\033[m ")
            novo_telefone = input("\033[034mDigite o novo telefone:\033[m ")
            novo_email = input("\033[034mDigite o novo email:\033[m ")
            cliente['nome'] = novo_nome
            cliente['telefone'] = novo_telefone
            cliente['email'] = novo_email
            print("\033[032mDados do cliente atualizados com sucesso!\033[m")
            atualizado = True
            break
    if not atualizado:
        print("\033[31mCliente não encontrado.\033[m")
        print("")
        print("\033[034mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_cliente()
        if resposta == 2:
            return


def consultar_cadastro():
    """
    Função que consulta os dados do cliente cadastrado
    :return: String (dados do cliente)
    """
    cabecalho("\033[034mCONSULTAR CADASTRO\033[m")
    cpf = input("\033[034mDigite o CPF do cliente que deseja consultar (somente os números, sem caracteres): \033[m")
    encontrado = False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("\033[032mNome:\033[m ", cliente['nome'])
            print("\033[032mTelefone:\033[m ", cliente['telefone'])
            print("\033[032mEmail: \033[m]", cliente['email'])
            encontrado = True
            break
    if not encontrado:
        print("\033[31mCPF não cadastrado.\033[m")
        print("")
        print("\033[034mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_cliente()
        if resposta == 2:
            return


def remover_cadastro():
    """
    Função que remove cliente cadastrado
    :return: String (remove cliente)
    """
    cabecalho("\033[034mREMOVER CADASTRO\033[m")
    cpf = input("\033[034mDigite o CPF do cliente que deseja remover (somente os números, sem caracteres):\033[m ")
    removido = False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            clientes.remove(cliente)
            print("\033[032mCadastro removido com sucesso!!!\033[m")
            removido = True
            break
    if not removido:
        print("\033[31mCliente não encontrado.\033[m")
        print("")
        print("\033[034mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_cliente()
        if resposta == 2:
            return


def menu_cadastro():
    """
    Função que cria um menu com as funções de criar cadastro, atualizar cadastro,
    consultar cadastro e remover cadastro
    :return: Função escolhida
    """
    while True:
        cabecalho("\033[034mCADASTRO\033[m")
        resposta = menu(["Criar Cadastro", "Atualizar Cadastro", "Consultar Cadastro", "Remover Cadastro", \
                         "Voltar ao Menu Anterior"])
        if resposta == 1:
            cadastrar_cliente()
            break
        elif resposta == 2:
            atualizar_cadastro()
            break
        elif resposta == 3:
            consultar_cadastro()
            break
        elif resposta == 4:
            remover_cadastro()
            break
        elif resposta == 5:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")


'''#FUNÇÕES PARA A ABA DE CONTRATAR SEGUROS'''


def tipos_plano():
    """
    Função que mostra os planos disponiveis para contratação
    :return: String (Planos Disponiveis)
    """
    while True:
        cabecalho("\033[034mPLANOS DISPONÍVEIS\033[m")
        resposta = menu(["Plano Básico", "Plano Completo"])
        if resposta == 1:
            cabecalho("\033[034mPLANO BÁSICO\033[m")
            basico_nome = "\033[034mPlano Básico\033[m"
            basico_cobertura = "\033[034mcobertura para dano parcial ou\nintegral ao caminhão por colisão,\033[m" \
                               "\033[034mincêndio, roubo \ne furto.\033[m"
            basico_valor = "\033[034m6.000,00\033[m"
            print(f"\033[034mO {basico_nome} \033[034mtem\033[m {basico_cobertura} \n\033[034mValor: R$\033[m" \
                  f"{basico_valor} \033[034manual.\033[m")
            plano_basico = {
                'nome': basico_nome,
                'cobertura': basico_cobertura,
                'valor': basico_valor,
            }
            return plano_basico
        elif resposta == 2:
            cabecalho("\033[034mPLANO COMPLETO\033[m")
            completo_nome = "\033[034mPlano Completo\033[m"
            completo_cobertura = "\033[034mcobertura para dano parcial ou\nintegral ao caminhão por colisão,\033[m" \
                                 "\033[034mincêndio , roubo,\nfurto,danos materiais e danos corporais \033[m" \
                                 "\033[034mdecorrentes\nde acidentes com terceiros.\033[m"
            completo_valor = "\033[034m10.000,00\033[m"
            print(
                f"\033[034mO {completo_nome}\033[034m tem {completo_cobertura}"\
                f"\n\033[034mValor: R$ {completo_valor} \033[034manual.\033[m")
            plano_completo = {
                'nome': completo_nome,
                'cobertura': completo_cobertura,
                'valor': completo_valor,
            }
            return plano_completo
        else:
            print("\033[31mOpção Inválida.\033[m")


def contrata_plano():
    """
    Função que permite ao cliente escolher e contratar o plano escolhido
    :return: String (Mensagem de confirmação de escolha do plano)
    """
    cabecalho("\033[034mCONTRATAR PLANO\033[m")
    cpf = input(
        "\033[034mDigite o CPF do cliente que deseja contratar o plano (somente os números, sem caracteres):\033[m")
    encontrado = False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("\033[034mDigite o número correspondente ao plano que deseja contratar\033[m")
            resposta = menu(["Plano Básico", "Plano Completo", "Voltar ao Menu Anterior"])
            if resposta == 1:
                print(f"\033[032mParabens {cliente['nome']}\033[032m,você contratou o Plano de Seguro Básico!\033[m")
                encontrado = True
                break
            if resposta == 2:
                print(f"\033[032mParabens {cliente['nome']}\033[032m,você contratou o Plano de Seguro Completo!\033[m")
                encontrado = True
                break
            if resposta == 3:
                return
    if not encontrado:
        print("\033[31mCPF não cadastrado.\033[m")
        print("")
        print("\033[034mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_cliente()
        elif resposta == 2:
            return


def menu_contrata_seguro():
    """
    Função que cria um menu com as funções planos disponiveis e contratar plano
    :return: Função escolhida
    """
    while True:
        cabecalho("\033[034mCONTRATAÇÃO DE SEGUROS\033[m")
        resposta = menu(["Planos Disponiveis", "Contratar Plano", "Voltar ao Menu Anterior"])
        if resposta == 1:
            tipos_plano()
            break
        elif resposta == 2:
            contrata_plano()
            break
        elif resposta == 3:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")


'''FUNÇÕES PARA A ABA DE ACIONAR SEGUROS'''


def acionar_seguro():
    """
    Função que permite ao cliente acionar um seguro para a sua localização atual
    :return: String (aciona o seguro para o local indicado)
    """
    cabecalho("\033[034mACIONAR SEGURO\033[m")
    cpf = input(
        "\033[034mDigite o CPF do cliente que deseja acionar o seguro\n(somente os números, sem caracteres):\033[m ")
    encontrado = False
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print(f"\033[034mOlá {cliente['nome']}!!!\033[m")
            endereco = input("\033[034mDigite o endereço que você precisa do seguro ex:\nRua: .......,\033[m" \
                             "\033[034mnº: ...., bairro:.....,cidade: .......,\nestado:........., CEP:...-...\033[m")
            print(f"\033[032mEstamos mandando um guincho para atendê-lo o mais\nrápido possivel no endereço\033[m" \
                  f"\033[032ma seguir:\n {endereco}\033[m")
            encontrado = True
            break
    if not encontrado:
        print("\033[31mCPF não cadastrado.\033[m")
        print("")
        print("\033[034mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_cliente()
        elif resposta == 2:
            return


def menu_aciona_seguro():
    """
    Função que cria um menu com a função acionar seguro
    :return: Função de acionar seguro
    """
    while True:
        cabecalho("\033[034mACIONAMENTO DE SEGURO\033[m")
        resposta = menu(["Acionar Seguro", "Voltar ao Menu Anterior"])
        if resposta == 1:
            acionar_seguro()
            return
        if resposta == 2:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")


'''FUNÇÃO PARA FALAR COM UM REPRESENTANTE'''


def falar_representante():
    """
    Função que da a opção do cliente falar com um representante da empresa
    :return: String (Chamado para falar com representante)
    """
    while True:
        cabecalho("\033[034mFALAR COM REPRESENTANTE\033[m")
        print("\033[034mDeseja falar com um representante ?\033[m")
        resposta = menu(["Sim", "Voltar ao Menu Anterior"])
        if resposta == 1:
            print("\033[032mEstamos direcionando a sua chamada para um de nossos \nrepresentantes...\033[m")
            return
        if resposta == 2:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")


# Obs:
# SE QUISER QUE A OPÇÃO CONTINUE A RODAR DEPOIS DO CADASTRO, COLOCAR UM WHILE TRUE LOGO ABAIXO DA LINHA DA FUNÇÃO
