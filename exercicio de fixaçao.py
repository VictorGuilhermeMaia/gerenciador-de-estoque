"""DESAFIO 1"""
produtos = {}

while True:
    print("\n1. Cadastrar\n2. Listar\n3. Atualizar\n4. Remover\n5. Sair")
    op = input("Opção: ")
    
    if op == '1':
        nome = input("Nome: ")
        if nome in produtos:
            print("Produto já existe!")
            continue
        produtos[nome] = {
            'preco': float(input("Preço: ")),
            'quantidade': int(input("Quantidade: "))
        }
        print("Cadastrado!")
    
    elif op == '2':
        for nome, p in produtos.items():
            print(f"{nome}: R${p['preco']} - {p['quantidade']} unidades")
    
    elif op == '3':
        nome = input("Nome do produto: ")
        if nome not in produtos:
            print("Não encontrado!")
            continue
        produtos[nome]['preco'] = float(input("Novo preço: "))
        produtos[nome]['quantidade'] = int(input("Nova quantidade: "))
        print("Atualizado!")
    
    elif op == '4':
        nome = input("Nome do produto: ")
        if nome in produtos:
            del produtos[nome]
            print("Removido!")
        else:
            print("Não encontrado!")
    
    elif op == '5':
        break
    
    else:
        print("Opção inválida!")

        """DESAFIO 2"""
        alunos = {}

while True:
    print("\n1. Cadastrar\n2. Listar\n3. Atualizar\n4. Remover\n5. Sair")
    op = input("Opção: ")
    
    if op == '1':
        nome = input("Nome: ")
        if nome in alunos:
            print("Aluno já existe!")
            continue
        alunos[nome] = {
            'idade': int(input("Idade: ")),
            'notas': [float(n) for n in input("Notas (separadas por vírgula): ").split(',')]
        }
        print("Cadastrado!")
    
    elif op == '2':
        for nome, a in alunos.items():
            media = sum(a['notas'])/len(a['notas']) if a['notas'] else 0
            print(f"{nome}: {a['idade']} anos - Média: {media:.1f}")
    
    elif op == '3':
        nome = input("Nome do aluno: ")
        if nome not in alunos:
            print("Não encontrado!")
            continue
        alunos[nome]['idade'] = int(input("Nova idade: "))
        alunos[nome]['notas'] = [float(n) for n in input("Novas notas (separadas por vírgula): ").split(',')]
        print("Atualizado!")
    
    elif op == '4':
        nome = input("Nome do aluno: ")
        if nome in alunos:
            del alunos[nome]
            print("Removido!")
        else:
            print("Não encontrado!")
    
    elif op == '5':
        break
    
    else:
        print("Opção inválida!")

        """DESAFIO 3"""
        tarefas = {}

while True:
    print("\n1. Adicionar\n2. Listar\n3. Filtrar\n4. Atualizar\n5. Remover\n6. Sair")
    op = input("Opção: ")
    
    if op == '1':
        desc = input("Descrição: ")
        if desc in tarefas:
            print("Tarefa já existe!")
            continue
        status = input("Status (pendente/concluída): ")
        if status not in ['pendente', 'concluída']:
            print("Status inválido!")
            continue
        tarefas[desc] = status
        print("Adicionada!")
    
    elif op == '2':
        for desc, status in tarefas.items():
            print(f"{desc} - {status}")
    
    elif op == '3':
        status = input("Filtrar por (pendente/concluída): ")
        for desc, s in tarefas.items():
            if s == status:
                print(f"{desc} - {s}")
    
    elif op == '4':
        desc = input("Descrição: ")
        if desc not in tarefas:
            print("Não encontrada!")
            continue
        novo_status = input("Novo status: ")
        if novo_status not in ['pendente', 'concluída']:
            print("Status inválido!")
            continue
        tarefas[desc] = novo_status
        print("Atualizada!")
    
    elif op == '5':
        desc = input("Descrição: ")
        if desc in tarefas:
            del tarefas[desc]
            print("Removida!")
        else:
            print("Não encontrada!")
    
    elif op == '6':
        break
    
    else:
        print("Opção inválida!")

        