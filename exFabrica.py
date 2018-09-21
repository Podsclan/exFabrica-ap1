class Funcionario:
	def _init_(self):
		self.nome = ''
		self.hora = 0
		self.salario = 0
		self.departamento = ''

def exibirMenu():
	print('\n ==== == MENU == ====')
	print('0 - SAIR')
	print('1 - CADASTRAR DEPARTAMENTO')
	print('2 - LISTAR DEPARTAMENTOS')
	print('3 - CADASTRAR FUNCIONÁRIO')
	print('4 - LISTAR FUNCIONÁRIOS')
	print('5 - SALARIO')
	print('6 - RICO DO MÊS')
	print('7 - DEPARTAMENTO MAIS RICO')
	print('8 - EXCLUIR')
	print('==== == ==== == ====')

def cadastrarDepartamento(lista):
	departamento = input('Digite um novo departamento: ')
	departamentoValido = True
	for i in lista:
		if i == departamento:
			departamentoValido = False
	if departamentoValido == True:
		lista.append(departamento)

def listarDepartamento(lista):
	for i in lista:
		print(i)

def cadastrarFuncionario(lista1, lista2):
	novoFuncionario = Funcionario()
	novoFuncionario.nome = input('Digite o nome do funcionário: ')
	valorHora = float(input('Digite o valor da hora de trabalho'))
	if valorHora > 5:
		novoFuncionario.hora = valorHora
		novoFuncionario.salario = int(input('Digite o salário: '))
		departamento = input('Digite o departamento: ')
		departamentoValido = validarDepartamento(listaDepartamentos, departamento)
		if departamentoValido == True:
			novoFuncionario.departamento = departamento
			lista1.append(novoFuncionario)
		else:
			print('Departamento não existe!')
	else:
		print('O valor deve ser maior que R$5,00')

def validarDepartamento(lista, departamento):
	valido = False
	for i in lista:
		if i == departamento:
			valido = True
	return valido

def listarFuncionatios(lista):
	for i in lista:
		print('Nome', i.nome)
		print('Valor da hora Trabalhada R$', i.hora)
		print('Salário R$', i.salario)
		print('Departamento', i.departamento)

def calcularSalario(lista):
	for i in lista:
		nome = ''
		horaExtra = 0
		salarioGanho = 0
		horas = int(input('Quantas horas trabalhadas?'))
		if horas <= 200:
			salarioGanho = (i.hora*horas)
			print('O salário do funcionário {} será de R${}'.format(i.nome, salarioGanho))
		else:
			horaExtra = (horas - 200)*2
			salarioGanho = (200*2)+(horaExtra*2)
			print('O salário do funcionário {} será de R${}'.format(i.nome, salarioGanho))

def maiorSalario(lista):
	nomeMaior = ''
	maior = 0
	for i in lista:
		if i.salario > maior:
			nomeMaior = i.nome
	print('O funcionário com maior salário é {}'.format(nomeMaior))

def departamentoRico(lista1, lista2):
	departamento = ''
	folhaSalario = 0
	for i in lista2:
		cont = 0
		for b in lista1:
			if b.departamento == i:
				cont += b.salario
		if cont > folhaSalario:
			departamento = i
	print('O departamento mais rico é:{}'.format(departamento))

listaDepartamentos = []
listaFuncionarios = []
opc = -1
while opc != 0:
	exibirMenu()
	opc = int(input('Digite uma opção: '))
	if opc == 1:
		cadastrarDepartamento(listaDepartamentos)
	if opc == 2:
		listarDepartamento(listaDepartamentos)
	if opc == 3:
		cadastrarFuncionario(listaFuncionarios, listaDepartamentos)
	if opc == 4:
		listarFuncionatios(listaFuncionarios)
	if opc == 5:
		calcularSalario(listaFuncionarios)
	if opc == 6:
		maiorSalario(listaFuncionarios)
	if opc == 7:
		departamentoRico(listaFuncionarios, listaDepartamentos)