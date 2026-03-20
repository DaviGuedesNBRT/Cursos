#dicionarios podem ser usados como "banco de dados". usando chaves e valores

#esse dicionario seria uma tabela de um banco de daos
usuario = {id:1,'nome':'davi', 'endereço': 'rua sei lá'}

#acessando valores de um dicionario via chave
print(usuario['nome'])

#acessando valores de um dicionario via função get
print(usuario.get('nome'))

#ao solicitar um valor que não existe no dicionario, ele retorna None
print(usuario.get('telefone'))

#podemos definir um valor padrão para quando o valor não for encontrado
print(usuario.get('telefone', 'não encontrado'))

#aqui busca por uma valor dentro do dicionario usando o metodo values()
print('davi' in usuario.values())

#adicionando um novo valor ao dicionario
usuario['telefone'] = '123456789'

#segunda forma de adicionar um novo valor ao dicionario
sobrenome = {'sobrenome': 'souza'}
usuario.update(sobrenome)

print(usuario)

#remover dados de um dicionario
usuario.pop('telefone')
print(usuario)

#agora vamos fazer uma verdadeira "tabela" de banco de dados
tb_usuarios = [
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},
    {'nome':'davi', 'endereço': 'rua sei lá'},]

#para pegar um valor de um dicionario dentro de uma lista, eu irei usar um for 
for item in tb_usuarios:
    print(item['nome'])
    #dessa forma consigo acessar os valores de cada dicionario dentro da lista

#outra forma de fazer outra tabela
tb_users = {'nome':['davi', 'joao', 'maria'], 'endereço': ['rua sei lá', 'rua sei lá', 'rua sei lá']}

#para acessar os valores dessa tabela, podemos iterar pelos índices
for i in range(len(tb_users['nome'])):
    print(tb_users['nome'][i])
    print(tb_users['endereço'][i])


#posso adicionar em uma tabela dessas usando o input, para o usuario adicionar os valores
lista_new_users = []
while True:
    nome = input('digite o nome: ')
    endereço = input('digite o endereço: ')

    lista_new_users.append({'nome': nome, 'endereço': endereço})
    parar = input('deseja adicionar mais um usuario? (s/n): ')

    if parar[0].lower() == 'n':
        break

print("Novos usuários cadastrados:")
print(lista_new_users)
