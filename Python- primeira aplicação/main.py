import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False}, {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo':True}, {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo':False}]


 # Exibe o nome do programa
def exibir_nome_do_programa():
    print('Sabor Express\n')


 # Exibe as opções disponíveis do menu 
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair')


# Exibe mensagem de finalização do aplicativo
def finalizar_app():
     exibir_subtitulo('Finalizando app...')


# Solicita uma tecla para voltar ao menu 
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()


# Exibe mensagem de opção inválida e retorna ao menu 
def opcao_invalida():
    print('Opção Inválida')
    voltar_ao_menu()

# Limpa a tela e exibe um subtítulo estilizado na tela 
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' *(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# Cadastra novos restaurantes
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu()

# Lista os restaurantes na lista
def listar_restaurantes():
    exibir_subtitulo('Listando os Restaurantes :')
    # Itera sobre a lista de restaurantes e exibe o estado de cada um
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()


# Altera o estado ativo/desativado do restaurante
def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']     
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O resturante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu()

# Função para escolher a opção do menu
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
           alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# Função que inicia o programa
def main():
    os.system('cls')  # Limpa a tela (no Windows)
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

# Executa a função principal se este arquivo for executado diretamente
if __name__ == '__main__':
    main()
