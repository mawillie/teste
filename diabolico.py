import copy
anime = ['teste']
animes2 = {}
#Aumentando um texto 2
# Criando uma classe Produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Lista original de produtos
produtos = [
    Produto("Caneta", 1.50),
    Produto("Caderno", 5.00),
    Produto("Mochila", 30.00)
]

print(f'oi {anime}')

# Fazendo shallow copies para criar diferentes visualizações dos mesmos produtos

### 

###
produtos_ordenados_por_preco = copy.copy(produtos)
produtos_ordenados_por_nome = copy.copy(produtos)

# Ordenando as visualizações
produtos_ordenados_por_preco.sort(key=lambda p: p.preco)
produtos_ordenados_por_nome.sort(key=lambda p: p.nome)

# Exibindo cada visualização
print("Produtos ordenados por preço:")
for produto in produtos_ordenados_por_preco:
    print(f"{produto.nome}: R${produto.preco:.2f}")

print("\nProdutos ordenados por nome:")
for produto in produtos_ordenados_por_nome:
    print(f"{produto.nome}: R${produto.preco:.2f}")

# Modificando o preço do produto na visualização ordenada por preço
produtos_ordenados_por_preco[0].preco = 0.99

# Agora, imprimimos novamente todas as visualizações para ver o efeito da alteração
print("\nApós alterar o preço na visualização por preço:")
print("Produtos originais:")
for produto in produtos:
    print(f"{produto.nome}: R${produto.preco:.2f}")

print("\nProdutos ordenados por preço:")
for produto in produtos_ordenados_por_preco:
    print(f"{produto.nome}: R${produto.preco:.2f}")

print("\nProdutos ordenados por nome:")
for produto in produtos_ordenados_por_nome:
    print(f"{produto.nome}: R${produto.preco:.2f}")