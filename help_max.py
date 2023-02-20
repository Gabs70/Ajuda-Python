# 📌 Valor Padrão 📌

''' Um valor padrão é um valor que será usado para um parâmetro
se nenhum valor for especificado quando a função for chamada.'''

def calcular_volume_comprimento(largura, altura, profundidade=10):
    volume = largura * altura * profundidade
    return volume

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 NoneType 📌

''' None é frequentemente usado para indicar que um valor não foi especificado
ou que um objeto não possui um valor apropriado.'''

def minha_funcao(a, b=None):
    if b is not None:
        return a + b
    else:
        return a

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Args 📌

''' *args é usado para passar um número variável de argumentos posicionais (ou seja, sem nome) para uma função.'''

def minha_funcao(*args):
    for arg in args:
        print(arg)

minha_funcao(1, 2, 3)  # Saída: 1 2 3
minha_funcao("a", "b", "c")  # Saída: a b c

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Kwargs 📌

''' **kwargs é usado para passar um número variável de argumentos nomeados para uma função.'''

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

minha_funcao(nome="João", idade=25)  # Saída: nome João, idade 25
minha_funcao(cor="verde", tamanho="grande", material="algodão")  # Saída: cor verde, tamanho grande, material algodão

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Closure 📌

''' Uma closure é uma função que tem acesso a uma variável de um escopo externo, 
mesmo após esse escopo ter sido finalizado.'''

def contador():
    contador = 0
    def incrementar_contador():
        nonlocal contador
        contador += 1
        print(contador)
    return incrementar_contador

meu_contador = contador()
meu_contador()  # Saída: 1
meu_contador()  # Saída: 2
meu_contador()  # Saída: 3

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Funções de Ordem Superior 📌

''' Funções que retornam outras funções são chamadas de funções de ordem superior.'''

def criar_funcao(mensagem):
    def exibir_mensagem():
        print(mensagem)
    return exibir_mensagem

minha_funcao = criar_funcao("Olá, mundo!")
minha_funcao()  # Saída: Olá, mundo!


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Funções de Primeira Classe 📌

''' As funções em Python são de primeira classe, o que significa que elas podem ser atribuídas a variáveis, 
passadas como argumentos para outras funções e retornadas como resultados de outras funções.'''

def aplicar_funcao(func, argumento):
    return func(argumento)

def dobrar(numero):
    return numero * 2

resultado = aplicar_funcao(dobrar, 5)
print(resultado)  # Saída: 10

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Dicionário e Métodos Úteis 📌

''' Um dicionário é um tipo de coleção que permite armazenar pares chave-valor,
onde cada chave é única e associada a um valor correspondente. É uma estrutura de dado do tipo de mútavel. '''

cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}

''' Para acessar um valor de um dicionário, basta fornecer a chave correspondente entre colchetes. '''

vermelho = cores['vermelho']
print(vermelho)  # Saída: (255, 0, 0)

''' Alguns métodos úteis são: 

> keys(): Retorna uma lista de todas as chaves do dicionário.

> values(): Retorna uma lista de todos os valores do dicionário.

> items(): Retorna uma lista de tuplas contendo todas as chaves e seus valores correspondentes no dicionário.

> get(chave, valor_padrão): Retorna o valor correspondente à chave fornecida. Se a chave não estiver presente no dicionário, 
retorna o valor padrão fornecido (que é None, se nenhum valor padrão for fornecido).

> pop(chave, valor_padrão): Remove e retorna o valor correspondente à chave fornecida. Se a chave não estiver presente no dicionário, 
retorna o valor padrão fornecido (ou levanta uma exceção KeyError, se nenhum valor padrão for fornecido).

> update(outro_dicionário): Atualiza o dicionário atual com os pares chave-valor do outro dicionário fornecido.
Se uma chave existir em ambos os dicionários, o valor correspondente no dicionário atual é substituído pelo valor correspondente no outro dicionário.

> clear(): Remove todos os pares chave-valor do dicionário.'''

#Por exemplo, suponha que tenhamos o seguinte dicionário:

alunos = {'Alice': 8.5, 'Bob': 7.2, 'Charlie': 9.3, 'David': 6.8}

#Podemos usar os métodos acima para realizar várias operações úteis, como a seguinte:

# Obter todas as chaves do dicionário
chaves = alunos.keys()
print(chaves)  # Saída: dict_keys(['Alice', 'Bob', 'Charlie', 'David'])

# Obter todos os valores do dicionário
valores = alunos.values()
print(valores)  # Saída: dict_values([8.5, 7.2, 9.3, 6.8])

# Obter todos os pares chave-valor do dicionário
itens = alunos.items()
print(itens)  # Saída: dict_items([('Alice', 8.5), ('Bob', 7.2), ('Charlie', 9.3), ('David', 6.8)])

# Obter a nota de Charlie
nota_charlie = alunos.get('Charlie')
print(nota_charlie)  # Saída: 9.3

# Obter a nota de Eve (com valor padrão de 0.0)
nota_eve = alunos.get('Eve', 0.0)
print(nota_eve)  # Saída: 0.0

# Remover o par chave-valor correspondente a 'David'
alunos.pop('David')

# Atualizar o dicionário com novos valores
novos_alunos = {'Eve': 8.9, 'Frank': 7.6}
alunos.update(novos_alunos)

# Remover todos os pares chave-valor do dicionário
alunos.clear()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Copy e DeepCopy 📌

''' Uma cópia superficial de um objeto contém uma nova referência aos objetos filhos, portanto, a cópia e o original apontam para os mesmos objetos filhos. 
Por outro lado, uma cópia profunda de um objeto contém novas cópias dos objetos filhos, recursivamente.
'''

import copy

original = [[1, 2], [3, 4]]
copia_superficial = copy.copy(original)
copia_profunda = copy.deepcopy(original)

# Altera um valor no objeto filho compartilhado
original[0][1] = 5

# A alteração é refletida na cópia superficial
print(copia_superficial)  # Saída: [[1, 5], [3, 4]]

# A alteração não é refletida na cópia profunda
print(copia_profunda)  # Saída: [[1, 2], [3, 4]]

''' Observe que a alteração em original é refletida em copia_superficial, mas não em copia_profunda. 
Isso ocorre porque copia_superficial compartilha os objetos filhos com original, enquanto copia_profunda contém novas cópias dos objetos filhos.'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Tipo Set e suas Peculiaridades 📌

''' Em Python, um set é um tipo de coleção de elementos únicos e não ordenados. Um conjunto é criado usando chaves {} ou a função set() e pode conter elementos de 
qualquer tipo imutável, como números, strings e tuplas. O tipo set é mutável, o que significa que você pode adicionar, remover ou atualizar elementos em um conjunto.'''

''' Algumas peculiaridades do tipo set em Python incluem:

> O conjunto não mantém a ordem dos elementos, então você não pode acessar os elementos por índice.

> O conjunto não pode conter elementos duplicados, portanto, se você tentar adicionar um elemento que já está no conjunto, ele não será adicionado novamente.

> Você pode realizar operações de conjunto, como união, interseção e diferença, usando operadores ou métodos (|, &, -).

> O conjunto é bastante eficiente para testar se um elemento está presente nele, pois o Python usa uma tabela de hash para pesquisar o elemento.

> Você pode usar métodos como add(), remove(), discard(), pop() e clear() para adicionar, remover ou atualizar elementos em um conjunto.'''

# Cria um conjunto com alguns elementos
meu_set = {1, 2, 3, "quatro", (5, 6)}

# Adiciona um novo elemento ao conjunto
meu_set.add(7)

# Remove um elemento do conjunto
meu_set.remove(2)

# Imprime o conjunto resultante
print(meu_set)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Lambda 📌

# Uma lambda é uma função anônima que pode ser definida em uma única linha de código e não precisa de um nome associado a ela.

# A sintaxe para definir uma lambda em Python é a seguinte:

lambda argumentos: None

# > Onde argumentos é uma lista separada por vírgulas de parâmetros que a função espera receber, e None é o resultado que a função deve retornar.

# Por exemplo, se você quiser definir uma função que recebe um número como entrada e retorna o dobro desse número, você poderia fazê-lo com a seguinte lambda:

dobro = lambda x: x * 2

# Agora você pode chamar essa função dobro passando um número como argumento e ela retornará o dobro desse número:

resultado = dobro(3)
print(resultado)  # Saída: 6'''

'''As lambdas também podem ser usadas como argumentos de outras funções, como no caso da função map(),
 que aplica uma função a cada elemento de uma sequência e retorna uma nova sequência com os resultados:'''

numeros = [1, 2, 3, 4, 5]
dobro = lambda x: x * 2
resultado = map(dobro, numeros)
print(list(resultado))  # Saída: [2, 4, 6, 8, 10]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Empacotamento e Desempacotamento de Dicionários 📌 

''' > O empacotamento de dicionários ocorre quando você passa um dicionário como argumento para uma função usando o operador ** antes do nome do dicionário. 
Isso faz com que o Python desempacote o dicionário e passe seus pares chave-valor como argumentos nomeados para a função.'''

# Por exemplo, suponha que você tenha a seguinte função que recebe dois argumentos nomeados:

def minha_funcao(a, b):
    print(f"a = {a}")
    print(f"b = {b}")

# Você pode empacotar um dicionário com os valores para a e b e passá-lo como argumento para a função usando o operador **:

meu_dict = {'a': 1, 'b': 2}
minha_funcao(**meu_dict)

# Isso é equivalente a chamar a função com os argumentos nomeados diretamente:

minha_funcao(a=1, b=2)

''' > O desempacotamento de dicionários ocorre quando você atribui os pares chave-valor de um dicionário a variáveis individuais usando o operador **.
Isso é útil quando você deseja passar um dicionário como argumento para uma função que espera argumentos nomeados separados.'''

# Por exemplo, suponha que você tenha o seguinte dicionário:

meu_dict = {'a': 1, 'b': 2}

# Você pode desempacotar esse dicionário em variáveis individuais com os nomes correspondentes usando o operador **:

a, b = meu_dict['a'], meu_dict['b']

''' > Observe que, ao desempacotar um dicionário, os nomes das variáveis devem corresponder exatamente às chaves do dicionário. 
Se o dicionário contiver uma chave que não corresponde a uma variável, o Python lançará uma exceção.'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 List Comprehension 📌

''' List comprehension é uma técnica em Python para criar listas de forma concisa e eficiente. 
Essa técnica permite que você crie uma nova lista baseada em uma ou mais sequências existentes, ou em outras palavras,
é uma forma de criar uma nova lista aplicando uma operação a cada elemento de uma sequência.'''

# Se você quiser criar uma lista com os quadrados dos números de 0 a 9, pode fazer o seguinte:

quadrados = [x**2 for x in range(10)]

# > Nesse caso, a list comprehension cria uma nova lista quadrados contendo os quadrados de cada número na sequência de range(10).

''' É possível adicionar condições à list comprehension usando uma cláusula if, onde a condição é uma expressão booleana que determina 
se o elemento da sequência será incluído na nova lista.'''

pares = [x for x in range(10) if x % 2 == 0]

# > Nesse caso, a list comprehension cria uma nova lista pares contendo apenas os números pares da sequência de range(10).

''' List comprehension também pode ser usado com múltiplas sequências. Por exemplo, se você quiser criar uma lista com todas as combinações de números de 0 a 2
e letras de 'a' a 'c', pode fazer o seguinte: '''

combinacoes = [(x, y) for x in range(3) for y in ['a', 'b', 'c']]

# > Nesse caso, a list comprehension cria uma nova lista combinacoes contendo todas as combinações possíveis de números de 0 a 2 e letras de 'a' a 'c'.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Filtro de Dados em List Comprehension 📌

''' List comprehension também pode ser usado para filtrar dados de uma lista, ou seja, 
criar uma nova lista contendo apenas os elementos que atendem a uma determinada condição.'''

# Por exemplo, se você quiser criar uma nova lista contendo apenas os números pares de uma lista original, pode usar a seguinte list comprehension:

lista_original = []
numeros_pares = [x for x in lista_original if x % 2 == 0]

# > Nesse caso, a nova lista numeros_pares conterá apenas os elementos da lista_original que são divisíveis por 2, ou seja, os números pares.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Dict e Set Comprehension 📌

''' Além de list comprehension, Python também suporta dicionário e set comprehension, que são construções semelhantes à list comprehension, 
mas que criam dicionários e conjuntos em vez de listas.'''

# Por exemplo, se você quiser criar um dicionário contendo o quadrado de cada número de uma lista, pode usar a seguinte dicionário comprehension:

numeros = [1, 2, 3, 4, 5]
quadrados = {x: x**2 for x in numeros}

# > Nesse caso, o novo dicionário quadrados terá chaves correspondentes aos elementos da lista numeros e valores correspondentes aos quadrados desses elementos.

# Já em set comprehension se você quiser criar um conjunto contendo apenas os números pares de uma lista, pode usar a seguinte set comprehension:

numeros = [1, 2, 3, 4, 5]
numeros_pares = {x for x in numeros if x % 2 == 0}

# > Nesse caso, o novo conjunto numeros_pares conterá apenas os elementos da sequência que são divisíveis por 2, ou seja, os números pares.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Isininstance 📌

# Isinstance é uma função embutida do Python que permite verificar se um objeto é de um determinado tipo.

# Por exemplo, para verificar se uma variável x é uma lista, você pode usar o seguinte código:

x = [1, 2, 3]
if isinstance(x, list):
    print("x é uma lista")
else:
    print("x não é uma lista")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 📌 Iterável, Iterator e Generator 📌 

'''Um iterável é qualquer objeto que pode ser percorrido por um loop for. 
Exemplos de iteráveis incluem listas, tuplas, strings, dicionários e conjuntos. 
Esses objetos fornecem um método __iter__() que retorna um iterador, que é usado para percorrer o iterável.

Um iterator é um objeto que produz valores um de cada vez. Ele implementa dois métodos: __next__() e __iter__().
O método __next__() retorna o próximo valor do iterator e levanta a exceção StopIteration quando não há mais valores para serem produzidos. 
O método __iter__() retorna o próprio iterator. '''

''' Uma generator expression é uma sintaxe compacta para criar um objeto generator em uma única linha de código. 
É semelhante a uma list comprehension, mas em vez de criar uma lista, cria um objeto generator.'''

#Por exemplo, a seguinte generator expression cria um generator que produz o quadrado de cada número par em uma lista:

numeros = [1, 2, 3, 4, 5]
quadrados_pares = (x**2 for x in numeros if x % 2 == 0)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------





