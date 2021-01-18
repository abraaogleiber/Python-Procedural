# Conteúdo do Curso Python Full
---
- [x] __Destrinchando o ambiênte de desenvolvimento integrado.__
- [x] __tipos de dados primitivos.__
  - int -> inteiro
  - float -> ponto flutuante
  - bool -> lógicos
  - str -> texto
    
- [x] __Dados de saída.__
  - `print()` -> Imprime algo na tela.
    
- [x] __Dados de Entrada.__
  - `input()` -> Recolhe qualquer valor digitado no teclado.
    
- [x] __Definindo tipos de dados (casting: conversões de dados).__
  - `int()` -> Converte se **possivel** para inteiro.
  - `float()` -> Converte para se **possivel** para ponto flutuante.
  - `complex()` -> Converte se **possivel** um valor para complexo.
  - `str()` -> Converte se **possivel** um valor para texto.
  - `bool()` -> Converte se **possivel** um valor para para True ou False.

- [x] __Processamento dos dados:__
    * _Uso de operadores aritméticos._
      - [+] -> Adição [-] -> Subtração [==] -> Igualdade [*] -> Multiplicação 
      - [/] -> Divisão real [//] -> Divisão inteira [**] -> Expôneciação.
        
    * _Uso de operadores relacionais._
      - [>] -> Maior que [<] -> Menor que [==] -> Igual à [>=] -> Maior ou igual
      - [<=] Menor ou igual [!=] -> Diferente
      
    * _Uso de operadores lógicos._
      - [not] -> Não [and] -> e [or] -> ou
      
    * _Uso de operadores de pertinencia._
      - [is] -> é [in] -> está
      
    * _Uso de operadores de atribuição._
      - [+=] -> Adição [-=] -> Subtração [*=] -> Multiplicação [/=] -> Divisão real
      - [//=] -> Divisão inteira -> [**=] Expôneciação
    
- [x] __Estrutura de Condição (controle de fluxo ou seleção).__
    * _Condição simplificada._
       ```
       print('Sim' **if** condição for True **else** 'Não')
      ```
    * _Condição simples._
        ```
         if condição for True:
            faça isso
        ```
    * _Condição Composta._
      ```
        if condição for True:
           faça isso
        else:
           faça aquilo
      ```
    * _Condição Aninhada_
      ```
        if condição for True:
          if condição for True:
             if condição for True:
                faça isso
             else:
                faça aquilo
          else:
            faça aquilo
        else:
          faça aquilo
      ```
    * _Condição encadeada._
      ```
        if condição for True:
           faça isso
        elif condição for True:
           faça isso 
        elif condição for True:
           faça isso
        else:
           faça aquilo 
      ```
    

- [x] __Estrutura de repetição.__
    - [x] `While`
      * _Repetição com teste lógico._
        ```
        x = 0
        while x <= 10:
           print(x)
           x += 1 
        ```
      * _Repetição infinita._
        ```
        x = 0
        while True:
          print(x)
        ```
      * _Repetição indefinida ou pós-testada._
        ```
        x = "Oi"
        while True:
           print(x)
           if x in 'oi':
              break (saia do laço)
           else:
              continue (Volte para o topo da estrutura)
        ```
    
    - [x] `for`
      * _Repetição definida com variável de controle._
        ```
        for i in range(1, 11):
            print(i)
        ```

 
- [x] __Variáveis compostas.__
    - [x] __Listas__
      * _Lista comprehersion._
      ```
      # é um modelo rápido de criação de listas de valores.
      lista = [x for x in range(100)] # O valor de "x" será armazenado dentro de lista.
      
      ou 
      
      lista = [[x for x in range(100) if x%2 == 0] if x % 16 == 0]
      ```
      * _Declarando uma lista._
      ```
      lista = list()
      lista = []
      lista = [1, 2, 3, 9.9, "Oi", True, 2j]
      ```
      * _Adicionando elementos._
      ```
      lista.append(valor="Oi")
      lista.append(valor=2)
      lista.insert(posição=1, valor=4)
      ```
      * _Acessando elementos._
      ```
      operador de indexação = []
      print(lista[0])
      Oi
      ```  
      * _Atualizando elementos._
      ```
      lista[0] = "Pedro"
      lista[1] = "21" 
      ```
      * _Concatenando listas._
      ```
      lista_a = [1, 2]
      lista_b = [3, 4]
      lista_c = (lista_a + lista_b)
      print(lista_c)
      [1, 2, 3, 4]
      
      ou
      
      lista_a += lista_b
      print(lista_a)
      [1, 2, 3, 4]
      ```
      * _Criando nova instância de lista (clone)._ 
      ```
      a = [1, 2, 3, 4]
      b = a.copy()
      print(b)
      [1, 2, 3, 4]
  
      ou
    
      a = [1, 2, 3, 4]
      b = a[:]
  
      ou 
  
      a = [1, 2, 3, 4]
      b = list(a)
      ```
      * _Criando duas referências para uma lista, apelidagem._
      ```
      a = b = list() # Declaração Multipla.
  
      ou
  
      a = [1, 2, 3]
      b = a # Qualquer alteração realizada na lista "a" afetará a lista "b".
      ```
      * _Removendo ou eliminando elemento de lista._
      ```
      a = [1, 2, 3, 4]
      a.remove(2) # O argumento é o valor a ser excluído.
    
      ou 
  
      a = [1, 3, 4]
      a.pop() # Elimina o ultimo elemento da lista por padrão.
  
      ou
    
      a = [1, 3]
      a.pop(0) # O argumento é a posição do elemento que será excluído.
   
      ou
      
      a = [3]
      del a[0] # Excluindo pela posição, usando a diretiva `del`.
      
      # Podemos excluir uma lista inteira.
      del a[:] # Excluindo toda lista. (tudo é perdido)
      ```
      * _Iterando vetores ou matrizes._
      ```
      a = [1, 2, 3]
      b = [4, 5, 6]
      
      for x in a:
         for y in b:
            print(x, y)
      
      out: 1, 4 -> 1, 5 -> 1, 6
           2, 4 -> 2, 5 -> 2, 6 ... 
      
      matriz = [[0, 0, 0], 
                [0, 0, 0],
                [0, 0, 0],]
      
      for linha in range(len(matriz)):
          for coluna in range(len(matriz[linha])):
              matriz[linha][coluna] = int(input('Digite um valor: ''))
         print('')
      ```
      
      * _Métodos dos objetos listas._
        - `sort()` -> Colaca uma lista emm ordem alfabética ou numerica.
        - `reverse()` -> Inverte a ordem de apresentação da lista. (de trás para frente)
        - `count()` -> Retorna o número de aparições do elemento passado como args.
        - `index()` -> Rertorna a posição do elemento passado como args.
        - `pop()` -> Retorna o ultimo valor de uma lista se não passado args, e elemina o valor.
        - `pop(arg)` ->  Retorna a posição do valor passado como arg, e elimina o valor.
        - `clear()` -> Elimina todo conteúdo da lista.
        - `append()` -> Anexa um valor ao final da lista.
        - `insert()` -> Anexa um valor na posição especificada.
        - `copy()` -> Cria uma copia dos elementos de uma lista.
        - `remove()` -> Remove o elemento repassado como args.
    
    - [x] __Dicionários__
      * _Declando, criando e adicionando valores em um dicionário._
      ```
      dicionario = dict()
      
      ou 
      
      dicionario = {'Nome': 'Abraão'}
      dicionario = {
                    'Nome': 'Abraão'
                    'Idade': 21    
                    }
      dicionario = {
                    'Nome': str(input('Seu nome: ')).strip().title()
                    'Idade': int(input('Sua idade: '))
                    }
      dicionario['Nome'] = 'Ester'
      dicionario['Idade'] = 23
      
      dicionario = {
              'Nomes': [],
              'Idades': [],
              'Cidades': [],
              }

       for pessoa in range(4):
           dicionario['Nomes'].append(str(input('Nome: ')).strip().title())
           dicionario['Idades'].append(int(input('Idade: ')))
           dicionario['Cidades'].append(str(input('Cidade: ')).strip().title())
        
        
       print(dicionario)

      ```
      * _Iterando valores de um dicionário._
      ```
      pessoas = []

      for pessoa in range(3):
          nome = str(input('Nome: ')).strip().title()
          idade = int(input('Idade: '))
          telefone = int(input('Telefone: '))
          pessoas.append({'Nome': nome, 'Idade': idade, 'Telefone': telefone})
    
    
      for idx in range(len(pessoas)):
          print(f"{pessoas[idx]['Nome']} {pessoas[idx]['Idade']} {pessoas[idx]['Telefone']}")
      
      
      
      pessoa = {'Nome': 'Abraão', 'Idade': 21, 'Cidade': 'Fortaleza'}
      
      for i, j in pessoa.items():
          print(f'{i} ---> {j}')
      ```
      * _Referência do endereço de memória (dicionários)._
      ```
      a = {"1": "Paulo"}
      b = a     # Aqui eu estou dizendo que "b" receberá uma referência da alocação do dict na memória. 
      b["1"] = "Estênio"        # Desta forma quando eu altero uma referência a outra automaticamente é modificada.
      print(a)
      
      print(id(a)) # Retorna a posição de alocação do dict na memória.
      print(id(x))
      
      ```
      * _Criando uma copia ou clone de um dicionário._
      ```
      a = {"1": "Abraão"}
      b = a.copy()  # Aqui eu jogo dentro de "b" uma copia de "a", agora são dicionários distintos. 
      b["1"] = "Epafrodito"
      print(b)
      
      ou
      
      x = {"1": 21}
      y = dict(x)
      
      y.update(x)
      print(y)
      ```
      * _Apagando ou eliminando elementos e dict (dicionários)._
      ```
      nomes = {"1": "abraão", "2": "marcos", "3": "elziu"}
      del nomes["3"]  # Apagando o valor da chave "3".
      
      ou
      
      nomes.pop("1")  # Apagando o valor da chave "1".
      
      ou
      
      nomes.popitem()   # Apagando o último elemento do dict.
      
      ou 
      
      del nomes   # Apagandoo todo conteúdo do dict.  
      ```  
      * _Metódos dos objetos dict (dicionários)._
        - `keys()` -> Retorna um objeto `dict_keys` com todas as chaves do dicionário.
        - `values()` -> Retorna um objeto `dict_values` com todos os valores do dicionário.
        - `items()` -> Retorna um objeto `dict_items` com todos os conjutos __chave-valor__ do dicionário.
        - `copy()` -> Cria dentro de um objeto `dict` uma copia dos elementos de outro objeto `dict`.
        - `update()` -> Concatena um dicionário com outro, sem precisar criar uma nova estrutura.
        - `pop()` -> Elimina e retorna o valor da chave repassada como arg.
        - `popitem()` -> Elimina e retorna a última chave e o valor do dict.
        - `get()` -> Retorna o valor da chave repassada como arg.
        - `clear()` -> Limpa um dict, apagando todo seu conteúdo.
        - `del` -> a diretiva "del" elimina uma chave e valor.
    
    - [x] __Conjuntos__
      * _Criando, declarando ou convertendo para um conjunto._
      ```
      a = [1, 2, 3, 1]
      a = set(a)
      print(a)
      >>> {1, 2, 3}  # Conjuntos não aceitam duplicatas.
      
      ou
      
      a = set()
      print(a)
      >>> set()  # Conjunto vazio.
      
      ou 
      
      a = {1, 2, 3, 4, 4, 4}
      print(a)
      >>> {1, 2, 3, 4} 
      ```
      * _União ou concatenação de conjuntos._
      ```
      a = {1, 0, 2}
      b = {3, 5, 2}
      
      a = a.union(b)
      print(a)
      >>> {1, 0, 2, 3, 5}
      ```
      * _Intercecção ou capitação de valores integrantes de dois conjuntos._
      ```
      a = {1, 2, 3}
      b = {2, 0, 4}
      
      c = a.intersection(b)
      print(c)
      >>> {2}
      
      # O inverso da expressão funciona perfeitamente.
      ```
      * _Retornando somente valores diferentes._
      ```
      a = {1, 2, 3, 9}
      b = {1, 5, 7, 9}
      
      c = a.difference(b)
      print(c)
      >>> {2, 3}
      
      ou
      
      c = b.difference(a)
      print(c)
      >>> {5, 7}
      ```
      * _Métodos dos conjuntos._
        - `union()` -> Faz a união de dois conjunto.
        - `intersection()` -> Retorna os elementos que fazem parte dos dois conjuntos.
        - `difference()` -> Retorna os elementos que não se repetem nos dois conjuntos.
        - `symmetric_difference()` -> Retorna um conjunto com todos os elementos dos dois conj; menos os duplicados.
        - `update()` -> Retorna pra dentro de um set() a concatenação de dois conjuntos. 
    
    - [x] __Tuplas.__ 
      * _Declarando e inicializando uma tupla._
      ```
      VALORES_CONSTANTES = (1, 2, 3.14, 8.9)
      
      ou 
      
      VALORES_FIXOS = 1, 2, 3.14, 10.2
      
      ou
      
      VALORES_INALTERAVEIS = tuple()
      ```
      * _Adicionando valores á uma tupla._
      ```
      # Só conseguimos adicionar valores a uma tupla de duas maneiras.
      
      VALORES = (1, 2, 2,14, 10.0, True)  # Manualmente.
      
      ou 
      
      VALORES = (1, 2)      # Gambiará
      VALORES = list(VALORES)
      
      VALORES.append(3.14)
      VALORES.append(True)
      
      VALORES = tuple(VALORES)
      print(VALORES)
      >>>  (1, 2, 3.14, True)
      ```
      * _Metódos das tuplas._
        - `count(item)` -> Retorna a quantidade de vezes que o item se repete.
        - `index(item)` -> Retona a posição de alocação de item repassado.
        - `tupla[2]` -> retorna o elemento alocado na posição ressada.

- [x] __Funções.__      
    - [x] __Funções NÃO Frutíferas.__
      * _Declarando ou criando uma função._
      ```
      def printa(): # comando composto.
          print('Hello Word...')
      ```
      * _Chamando ou invocando uma função._
      ```
      printa()
      >>> Hello Word...
      
      # Funções Não Frutiferas, não retornam valores e sim padrões.
      # Ou seja, executam uma serie de instruções. 
      ```
    - [x] __Funções Frutíferas.__
      * _Retornando valores manipulaveis._
      ```
      def potencia():
         retorn 5 ** 2
      
      potencia()
      >>> 25  # Pode ser manipulado dentro do meu programa.
      ```
      * _Passagem de argumentos e definição de parâmetros._
      ```
      def potencia(x, y)  # x e y são parâmetros formais. ou seja a função só funcionará se receber o
          return x ** y   # que pede nos parâmetros.
      
      
      potencia(x=5, y=2)  # Passagem de arg no padrão chave e valor ou argumentos nomeados.
      >>> 25
      ```
      * _Passando argumentos pelo padrão chave-valor (argumentos nomeados)._ 
      ```
      def mostra():
         print(f'{n1} e {n2}')
      
      
      mostra(n2=3, n1=5)
      >>> 5 e 3
      ```
      * _Definindo parâmetros indeterminado._
      ```
      def soma(*args):
         valores = list(args)
         s = int()
         for item in valores:
             s += item
      
         return s
      
      
      result = soma(1, 2, 5, 2)
      print(result)
      >>> 10
      ```
      * _Definindo parâmetros indeterminados e passando args arbitrários._
      ```
      def soma(**args):
          s = 0
          for valor in args.values():
              s += valor
          return s
      
      
      result = soma(n1=3, n2=5, n3=4, n4=10)
      print(result)
      >>> 22
      
      ou 
      
      def nome_completo(**nome):
          print(f'Meu nome é {nome["n"]} {nome["s"]}')
      
      
      nome_completo(n='Abraão', s='Alves da Silva')
      >>> Meu nome é Abraão Alves da Silva
      ```
      * _Documentando ou comentando funções._
      ```
      def soma(n1, n2):
          "A função recebe dois argumentos e soma-os, por fim retorna o resultado da soma."
          return (n1 + n2)
      
      
      <Terminal>
      >>> __doc__.soma()  # Assim acessamos a mini documentação da função.
      ```
      * _Definindo parâmetros opcionais e padrão._
      ```
      # Opcional.
      def soma(n1, n2, opcional=False):
          if opcional:
             print(f'{n1} e {n2} = {n1+n2}')
          else:
             print(n1+n2)
      
      soma(n1=2, n2=4, opcional=True)
    
      # Padrão.
      def soma(n1=0, n2=0):
         print(n1+n2)
      
      
      soma()
      >>> 0
      
      soma(3, 5)
      >>> 8
      ```
    - [x] __Funções Puras.__
      ```
      funções puras não alteram a estrutura de variaveis globais.
      def soma(*args):
          s = sum(args)
      return s
      # Retorna um valor, mas não altera nada em meu programa.    
      ```
    - [x] __Funções Modificadoras.__
      ```
      lista = []
      
      def guardando():
          n = int(input('Digite um valor: '))
          lista.append(n)
      
      guardando()
      print(lista) # A lista é uma estrutura global que foi modificada dentro da função.
      ```
    - [x] __Variáveis globais e locais.__
      ```
      a = 1
      
      def soma(a, b):
         print(a + b)   <-- "a" vale 2, é uma variável simples de escopo local, pois só existe dentro da função.
      
      soma(2, 3)
      print(a)  <-- "a" vale  1, pois é de escopo global, "a" e "a" são diferentes.
      >>> 5
      >>> 1
      ```
      * _Modificando uma variável global, localmente._
      ```
      resultado = 1
      
      def soma(a, b)
          global resultado
          resultado = (a + b)
      
      
      soma(2, 5)
      print(resultado) 
      >>> 7
      ```
    - [x] __Retorno de funções.__
      ```
      def soma(*args):
          s = sum(args)
      
          return (s, args)
      
      
      resultado, valores = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
      print(valores)
      print(resultado)
      >>> 55
      >>> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
      
      
      ou 
      
      resultado = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
      print(resultado[0])
      print(resultado[1])
      >>> 55
      >>> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)        
      ```
      
- [x] __Modularização.__
    * _O que é modularização._
    >  É o processo onde dividimos o programa em varios scripts (pedaços), 
    >  com o objetivo de simplificar a leitura, o processo de depuração e refactoração de um programa.
    >  nós acessamos módulos importando os mesmos.
  
    ```
     programa.py
     def soma(x, y):
        return (x + y)
  
     
     programa_principal.py
     import programa.py
     
     print(programa.soma(5, 3))
     >>> 8
    ```

- [x] __Tratamento de Exceções.__
    * `try \ except \ finally`.
    ```
    while True:
        try:
           n = int(input('Digite um valor: '))
           print(n ** n)
        except ValuesError:
           print('Digite somente números.')
        finally:
            print('Muito obrigado pela colaboração.')
    ```
    * _Formatando o tipo de erro._
     ```
      try:
         n = int(input('Digitr um número: '))
         print(n)
      except Exception as erro:
         print(f'O erro é {erro}')
     ```
  
- [x] __Funções Lambda. (função anônima)__
    > "As funções lambda são pouco utilizadas para o desenvolvimento, creio que o uso delas é na necessidade
    > do processamento de valores com o objetivo de retorno de um resultado simples e rápido, são sintáticamente 
    > pequenas, faceis de criar e são muito elegantes. Recebe quantos parâmetros quiser-mos, mas só recebe uma 
    > expressão que resulta em um valor de retorno."
  
    * _Declaração de uma função lambda._
    ```
    quadrado = (lambda n: n*2)
    print(quadrado(5))
    >>> 25
    ```

- [x] __map, filter e reduce__
    * `map()` -> É uma função interna do python que tem o objetivo de aplicar computações em listas. 
                 O map() retorna uma lista com valores especifico, tipo: valores dos produtos de uma lista,
                 nome de clientes, telefone, ou o email de pessoas cadastradas, enfim.
      
    * _`map()`_
    ```
    pessoas = [{'Nome': 'Tiago', 'Idade': 23}, {'Nome': 'Gil', 'Idade': 45}]
    idades_grupo = list(map((lambda l, l['Idades']), pessoas))
    print(idades_grupo)
    ```
    
    * `filter()` -> É uma função que filtra os elementos de uma lista, exemplo: retorne todas as pessoas com menos de 
                    20 anos, ou pessoas com peso acima de 85kg, ou pessoas que começam com a letra "z".
    
    * `filter()`  
    ```
    pessoas = [{'Nome': 'Tiago', 'Idade': 23}, {'Nome': 'Gil', 'Idade': 45}]
    pessoas_com_idade_maior_30 = list(filter((lambda x: x['Idade'] > 30), pessoas))
    print(pessoas_com_idade_maior_30)
    ```
  
    * `reduce()` -> É uma função do pacote ou módulo `functools`, e consegue reduzir uma sequencia de valores
                    realizando alguma computação, tipo: subtraindo valores, somando, multiplicando, enfim.
      
    * `reduce()`
    ```
    from functools import reduce

    lista = [1, 2, 3, 4]
    soma = reduce(lambda x, j: x+j, lista)
    print(soma)
    >>> 10
    ```

- [x] __Arquivos.__
    > Tudo na computação é um arquivo...
  
    * _Tipos de arquivos._
       - Arquivos simples -> Documentos de texto.
       - Arquivos Binários -> imagens, gits, audios, videos...
    
    * _Como abrir e fechar um arquivo._
    ```
    arquivo = open('endereço do arquivo na mémoria', 'modo')
    arquivo.close()
    ```
  
    * _Endereço do arquivo._
      - Caminho absoluto -> É o local de armazenamento do arquivo, diretórios por diretório atá o arquivo.
      _ Caminho relativo -> É quando o arquivo está na mesma pasta do projeto.
    ```
     arquivo = open('C:\\Principal\Projeto\arquivos.txt')
  
     ou
  
     arquivo = open('arquivo.txt')
    ```
    
    * _Modo de abertura de um arquivo._
      - x (__) -> Método usado unicamente para criar um arquivo. (se já existir, retorna um erro.)
      - w (write) -> Método para escrever em um arquivo (se não existir ele cria.)(se houver conteúdo ele apaga.)
        * `write()` -> Método que escreve uma linha string.
        * `writelines()` -> Método que escreve um conjunto de strings, tipo: lista
          
      - a (append) -> Método para adicionar conteúdo ao arquivo (se não existir ele cria) (não apaga o conteúdo.)
      - r (read) -> Método para leitura de arquivos.
        * `read()` -> Retorna o arquivo no formato texto por extenso.
        * `readline()` -> Retorna o arquivo linha por linha.
        * `readlines()` -> Retorna o arquivo dentro de uma lista, onde cada linha representa um elemento da lista.
    
      - r+ -> Permite a manipulação dupla, ou seja, leitura e escrita (não apaga o conteúdo.)
    
