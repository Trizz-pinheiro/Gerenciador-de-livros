import matplotlib.pyplot as plt

class Livro:
    def __init__(self, titulo, autor, qtd_disponivel, genero):
        self.titulo = titulo
        self.autor = autor
        self.qtd_disponivel = qtd_disponivel
        self.genero = genero
        
    def __str__(self): 
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nQuantidade: {self.qtd_disponivel}\n'
    
livros = []

def cadastrar_livro():
    titulo = input('Digite o titulo do livro: ')
    autor = input(f'Digite o autor do livro {titulo}: ')
    genero = input(f'Digite o genero do livro {titulo}: ')
    qtd_disponivel = int(input(f'Digite a quantidade disponivel do livro {titulo}: '))
    
    novo_livro = Livro(titulo, autor, qtd_disponivel, genero)
    livros.append(novo_livro)
    print(f'\n Livro {titulo} cadastrado com sucesso!')
    
def listar_livros():
        if not livros:
            print('Nenhum livro cadastrado ainda.')
            return 
        print('\nLista de livros: ')
        for livro in livros:
            print(livro)
        print()
        
def buscar_livro():
    titulo_busca = input('Digite o titulo do livro que deseja buscar: ')
    encontrados = [livro for livro in livros if livro.titulo.lower() == titulo_busca.lower()]
    
    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print('Livro não encontrado.')
        
def gerar_grafico():
    if not livros:
        print('Não há livros cadastrados para gerar o gráfico.')
        return
    
    generos = {}
    for livro in livros:
        if livro.genero in generos:
            generos[livro.genero] += livro.qtd_disponivel
        else:
            generos[livro.genero] = livro.qtd_disponivel
            
    plt.bar(generos.keys(), generos.values(), color='#ff0000')
    plt.title('Quantidade de livros por Gênero')
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade')
    plt.show()
    
def opcoes():
    while True:
        print('<--- Sistema de gerenciamento de Livros --->')
        print('1. Cadastrar Livro')
        print('2. Listar Livros')
        print('3. Buscar Livro')
        print('4. Gerar Gráfico')
        print('5. Sair')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            gerar_grafico()
        elif opcao == '5':
            print('Saindo do sistema......')
            break
        else: 
            print('Opção inválida! Tente novamente. \n')
            
opcoes()