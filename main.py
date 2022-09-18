if __name__ == '__main__':

    def funcao_inicial(arquivo_json):
        if len(arquivo_json) > 0:
            main()
        else:
            try:
                print('-'*40)
                print('SERÁ NECESSÁRIO CRIAR UM CADASTRO ADMIN')
                print('-'*40)
                nome = input('Insira o nome do seu novo usuário admin: ')
                senha = int(input('Escreva uma senha numérica: '))
                adicionar_novo_admin(arquivo_json, nome, senha)
            except ValueError:
                print('É NECESSARIO QUE A SENHA SEJA NUMÉRICA!')
                funcao_inicial(arquivo_json)

    def main():
        while True:
            try:
                print('-' * 20)
                print('Menu Interativo')
                print('-' * 20)
                print('Opções: ')
                print('[1] - Opções de Visitante')
                print('[2] - Opções internas')
                print('[3] - Sair do programa')

                resposta = int(input('Defina sua opção: '))
                if resposta == 1:
                    print('Você selecionou a opção de visitante')
                    menu_visitante()
                elif resposta == 2:
                    print('Você selecionou as opções internas')
                    verifica_acesso(dic_admins)

                elif resposta == 3:
                    print('Saindo do programa...')
                    exit()
                else:
                    print()
                    print('Escolha um valor dentre as opções do MENU')
                    continue
            except ValueError:
                print('Escolha um valor numérico para opção!')
                continue

    def menu_visitante():
        while True:
            try:
                print('-' * 20)
                print('Menu VISITANTE')
                print('-' * 20)
                print('[1] - COTAÇÃO')
                print('[2] - ESTOQUE ATUAL')
                print('[3] - VOLTAR')
                resposta = int(input('>> '))
                if resposta == 1:
                    cotacao()
                    continue
                elif resposta == 2:
                    estoque()
                    continue
                elif resposta == 3:
                    main()
                else:
                    print('ALTERNATIVA INVALIDA!')
                    continue
            except ValueError:
                continue

    def menu_funcionario():
        while True:
            try:
                print('-' * 20)
                print('Menu FUNCIONÁRIO')
                print('-' * 20)
                print('[1] - ESTOQUE ATUAL')
                print('[2] - CONFERIR VALOR ACUMULADO')
                print('[3] - ADICIONAR MATERIAL')
                print('[4] - COTAÇÃO')
                print('[5] - ALTERAR VALOR')
                print('[6] - EXCLUIR MATERIAL')
                print('[7] - VOLTAR')
                resposta = int(input('>> '))
                if resposta == 1:
                    estoque()
                elif resposta == 2:
                    valor_acumulado()
                elif resposta == 3:
                    incluir_material()
                elif resposta == 4:
                    cotacao()
                elif resposta == 5:
                    alterar_material()
                elif resposta == 6:
                    excluir_material()
                elif resposta == 7:
                    return
                else:
                    print('Opção inválida!')
                    continue

            except ValueError:
                print('Escolha um valor de opção válido!')
                continue
##################################
    def verifica_acesso(arquivo_json):
        id_acesso = input('Insira o ID de funcionário: ')
        if id_acesso in arquivo_json:
            senha_acesso = input('Insira a senha de funcionário: ')
            if senha_acesso == str(arquivo_json[id_acesso]):
                print('SEJA BEM-VINDO!')
                menu_funcionario()
            else:
                print('Senha incorreta!')
                return
        else:
            print('ID de funcionário não encontrado!')
            return

    def adicionar_novo_admin(arquivo_json: dict, id_admin: str, senha: str):
        if id_admin in arquivo_json:
            main()
        else:
            arquivo_json[id_admin] = senha
            print(arquivo_json)
            main()

###########################################
    def alterar_material():
        cotacao()
        resposta = input('DESEJA ALTERAR OS DADOS DE QUAL MATERIAL? ')
        resposta = resposta.lower()
        if resposta not in materiais:
            print('Este material não está cadastrado!')
            return
        else:
            materiais[resposta][0] = input(f'Insira o novo valor por kg de {resposta}: ')
            materiais[resposta][1] = input(f'Insira a nova capacidade de estoque de {resposta}: ')

    def cotacao():
        for k, v in materiais.items():
            print(f'{k}: R${v[0]}')
        return

    def estoque():
        for k, v in materiais.items():
            print(f'{k}: {v[1]}kg')
        return

    def valor_acumulado():
        print('O valor acumulado até o momento é: ')
        for k, v in materiais.items():
            print(f'{k}: R${float(v[0]) * int(v[1])}')

    def excluir_material():
        cotacao()
        resposta = input('Digite o material que você deseja excluir: ')
        resposta = resposta.lower()
        if resposta not in materiais:
            print('Esse material não está cadastrado!')
            return
        else:
            del materiais[resposta]

    def incluir_material():
        escolha = (input('Insira o nome do material que deseja inserir: '))
        escolha = escolha.lower()
        if escolha in materiais:
            return
        else:
            try:
                lista_add = []
                valor_add = float(input(f'Informe o valor de {escolha}: '))
                lista_add.append(valor_add)
                capacidade_add = int(input(f'Informe a capacidade de {escolha}: '))
                lista_add.append(capacidade_add)
                materiais[escolha] = lista_add
            except ValueError:
                incluir_material()

    dic_admins = {}#'junior': '123'}
    materiais = {'ferro': [1.45, 2000], 'plastico': [1.88, 500], 'aluminio': [2.51, 100]}
    funcao_inicial(dic_admins)



