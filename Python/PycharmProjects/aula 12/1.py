nome = str(input('Qua seu nome?')).upper()
if nome == 'MARCELA':
    print('Que nome lindo!')
elif nome == 'JOAO' or nome == 'MARIA' or nome == 'ALICE' or nome == 'PEDRO':
    print('Seu nome é muito popular no Brasil!')
elif nome in ('ANA CLAUDIA JULHIA JADE'):
    print('Belo nome feminino!')
else:#o else e opcional se tirar funciona da mesma forma
    print('Seu nome é bem normal!')
print('\033[1;34mBOM DIA, {}!!.\033[m'.format(nome))
