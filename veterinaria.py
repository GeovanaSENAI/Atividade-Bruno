cadastros = []
quando_seram_os_atendimentos = []

def cor_texto(texto, cor):
    cores = { #os códigos de cada cor modificam o texto
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'reset': '\033[0m'
    }
    return cores.get(cor, '') + texto + cores['reset']

def desenhar_gato():
    gato = r"""
     /\_/\  
    ( o.o ) 
     > ^ <
"""
    return gato

def desenhar_cachorro():
    cachorro = r"""
   / \__
  (    @\____
  /         O
 /   (_____/
/_____/   U
"""
    return cachorro

def exibir_precos():
    print("- Banho para cachorro pequeno: R$ 50,00")
    print("- Banho para cachorro médio: R$ 70,00")
    print("- Banho para cachorro grande: R$ 90,00")
    print("- Banho para gato: R$ 60, 00")
    print("- Tosa para cachorro pequeno: R$ 70, 00")
    print("- Tosa para cachorro médio: R$ 90,00")
    print("- Tosa para cachorro grande: R$ 110,00")
    print("- Tosa para gato: R$ 80, 00")
    print("- Consulta para cachorro pequeno: R$ 100, 00")
    print("- Consulta para cachorro médio: R$ 120,00")
    print("- Consulta para cachorro grande: R$ 140,00")
    print("- Consulta para gato: R$ 110, 00")

def exibir_horarios():
    print("segunda a sexta, das 9h às 18h\nsábados, das 9h às 14h")

def cadastrar_pet():
    nome = str(input("Entre com o nome do pet: ")).lower()
    raca = str(input("Digite qual a raça do animal: ")).lower()
    tipo = str(input("Expecifique o tipo (gato/cachorro): ")).lower()
    sexo = str(input("Qual é o sexo do pet (f/m): ")).lower()
    if tipo == "cachorro":
        porte = str(input("Digite o porte do cão (p/m/g): ")).lower()
    else:
        porte = "não se enquadra"
    atendimento = str(input("Qual será o tipo de atendimento realizado (banho/tosa/consulta): ")).lower()
    if atendimento == "consulta":
        sintoma = str(input("Qual é o sintoma do animal?: "))
    else:
        sintoma = "não se enquadra"
    print("🐕‍🦺Pet cadastrado com sucesso!🐈\n")

    # cadastro_dono
    print(f"{cor_texto("Iniciando o cadastro do dono","verde")}\n")
    dono = str(input("Digite o nome do dono: ")).lower()
    telefone = str(input("Digite o DDD e o telefone do dono _(18)00000-0000_: "))
    endereco = str(input("Adicione o seu endereço: "))

    # especificações
    print(f"{cor_texto("Especificações do atendimento", "verde")}\n")
    print("segunda a sexta, das 9h às 18h\nsábados, das 9h às 14h")
    while True: #adiciona e identifica a ocorrencia da data do atendimento
        quando_sera = str(input("Digite o dia da semana(segunda/terça/quarta/"
                                "quinta/sexta/sábado) e o horário(ex:00h), exemplo:segunda-9h: ")).lower()
        if quando_sera in quando_seram_os_atendimentos:
            print("ja esta ocupado, tente novamente")
        else:
            quando_seram_os_atendimentos.append(quando_sera)
            break
    atendente = str(input("Quem fará o atendimento (joana/marina): ")).lower()
    if tipo == "cachorro" and porte == "p":
        if atendimento == "banho":
            valor = "R$50,00"
        elif atendimento == "tosa":
            valor = "R$70,00"
        else:
            valor = "R$100,00"
    elif tipo == "cachorro" and porte == "m":
        if atendimento == "banho":
            valor = "R$70,00"
        elif atendimento == "tosa":
            valor = "R$90,00"
        else:
            valor = "R$120,00"
    elif tipo == "cachorro" and porte == "g":
        if atendimento == "banho":
            valor = "R$90,00"
        elif atendimento == "tosa":
            valor = "R$110,00"
        else:
            valor = "R$140,00"
    else:
        if atendimento == "banho":
            valor = "R$60,00"
        elif atendimento == "tosa":
            valor = "R$80,00"
        else:
            valor = "R$110,00"
    if endereco == "":
        endereco = "não adicionado"
    cadastro = {
        "nome": nome,
        "raca": raca,
        "tipo": tipo,
        "porte": porte,
        "sexo": sexo,
        "atendimento": atendimento,
        "sintoma": sintoma,
        "dono": dono,
        "telefone": telefone,
        "endereco": endereco,
        "quando": quando_sera,
        "atendente": atendente,
        "valor": valor,
        "realizada": False
    }
    cadastros.append(cadastro) #nessa parte ele inseri dentro da lista
    print("feito\n")

def consultar_cadastros():
    if len(cadastros) == 0:
        print("😕Ainda não há cadastros😕\n")
        return
    numero = 1
    for cadastro in cadastros:
        status = ""
        if cadastro["realizada"] == True:
            status = "✅Realizada"
        else:
            status = "❌Não realizada"
        print(f"[{numero}] Nome: {cadastro['nome']} | Raca: {cadastro['raca']} | "
              f"Tipo: {cadastro['tipo']} | Sexo: {cadastro['sexo']} | Porte: {cadastro['porte']} | "
              f"Atendimento: {cadastro['atendimento']} | Sintoma: {cadastro['sintoma']} | "
              f"Dono: {cadastro['dono']} | Telefone: {cadastro['telefone']} | Endereço: {cadastro['endereco']} | "
              f"Quando: {cadastro['quando']} | Atendente: {cadastro['atendente']} | Valor: {cadastro['valor']} | "
              f"Status: {status}")
        numero += 1
    print()

def marcar_realizada():
    consultar_cadastros()
    if len(cadastros) == 0:
        return
    try:
        numero = int(input("Digite o número da sessão para marcar como realizada: "))
        indice = numero - 1
        if numero <= len(cadastros):
            cadastros[indice]["realizada"] = True
            print("✅ Sessão marcada como realizada! ✅\n")
        else:
            print("❌ Número inválido! ❌\n")
    except ValueError:
        print("❌ Entrada inválida! Digite um número inteiro. ❌\n")
    consultar_cadastros()

def buscar_cadastro():
    termo = str(input("Buscar por nome do pet ou dono: ")).lower()
    encontrados = [] #guardar os dicionários que batem com a busca
    for cadastro in cadastros: #varredura para confirmar se tem a informação
        if (termo in cadastro["nome"].lower()) or (termo in cadastro["dono"].lower()):
                encontrados.append(cadastro)
    if len(encontrados) == 0: #verificar se encontrou algo
        print("😣Nenhuma sessão encontrada😣\n")
        return
    numero = 1
    for cadastro in encontrados: #mostrar informações encontradas
        status = ""
        if cadastro["realizada"] == True:
            status = "✅Realizada"
        else:
            status = "❌Não realizada"
        print(f"[{numero}] Nome: {cadastro['nome']} | Raca: {cadastro['raca']} | "
              f"Tipo: {cadastro['tipo']} | Sexo: {cadastro['sexo']} | Porte: {cadastro['porte']} | "
              f"Atendimento: {cadastro['atendimento']} | Sintoma: {cadastro['sintoma']} | "
              f"Dono: {cadastro['dono']} | Telefone: {cadastro['telefone']} | Endereço: {cadastro['endereco']} | "
              f"Quando: {cadastro['quando']} | Atendente: {cadastro['atendente']} | Valor: {cadastro['valor']} | "
              f"Status: {status}")
        numero += 1
    print()

def exibir_pagina_inicial():
    gatinho = desenhar_gato()
    cachorrinho = desenhar_cachorro()
    while True:
        print(cor_texto(gatinho, "amarelo"))
        print(cor_texto("---Página Inicial---","azul"))
        print(cor_texto("1. 💲Exibir preços💲","vermelho"))
        print(cor_texto("2. 🕐Exibir horários🕝","roxo"))
        print(cor_texto("3. ✍Cadastrar pet✍","vermelho"))
        print(cor_texto("4. 📋Ver todas as sessões📋","roxo"))
        print(cor_texto("5. 🔍Buscar por pet ou dono🔍","vermelho"))
        print(cor_texto("6. ✅Marcar sessão com realizada✅","roxo"))
        print(cor_texto("7. Sair","vermelho"))
        escolha = str(input(f"{cor_texto("Escolha uma opção: ","azul")}"))
        if escolha == "1":
            exibir_precos()
        elif escolha == "2":
            exibir_horarios()
        elif escolha == "3":
            cadastrar_pet()
        elif escolha == "4":
            consultar_cadastros()
        elif escolha == "5":
            buscar_cadastro()
        elif escolha == "6":
            marcar_realizada()
        elif escolha == "7":
            print("👋Saindo do sistema. Até a próxima!👋")
            print(cor_texto(cachorrinho, "amarelo"))
            break
        else:
            print(" Opção inválida... Tente novamente. \n")

exibir_pagina_inicial()