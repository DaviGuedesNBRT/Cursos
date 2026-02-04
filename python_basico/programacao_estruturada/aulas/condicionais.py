#estruturas condicionais python

nome = str(input('informe seu nome :'))
ativo = False
loging = False

print('')
print(f'olá {nome}, deseja fazer login ?')
resposta = str(input('fazer login [S/N] :'))

if resposta[0] == "s":
    loging = True
    print('')
    print(f'{nome}, você fez login com sucesso. agora, para entrar no sistema ative sua conta ! ')
    resposta2 = str(input('deseja ativar sua conta [S/N] :'))

    if resposta2[0] == "s":
        ativo = True
        print('')
        print(f'{nome}, sua conta agora esta ativa!')

else:
    loging =False
    print(f'{nome}, você não fez login.')

#estrutura "AND"
if ativo and loging == True:
    print('')
    print(f'{nome}, você acessou o sistema !')

#estrutura "NOT"
if not ativo:
    #pelo oque observei, o if vai inverte-se. antes ele funcionava se o valor fosse True, mas agora funciona quando é falso
    print(f'ativo :{ativo}')

if not loging:
    print(f'login :{loging}')


