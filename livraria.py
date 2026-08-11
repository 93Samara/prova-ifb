#Avaliação1

def addLivro(dicLivros):
        print("=== Adicionar livro ===")
 
        titulo = input("\n Título: ").lower().strip()
        quantidade = int(input("\n Quantidade: "))
 
        if titulo in dicLivros: 
            dicLivros[titulo] += quantidade #adiciona um novo livro ou adiciona a quantidade se o livro já existir
        else:
            dicLivros[titulo] = quantidade
 
        print("Livro adicionado!")
 
def removeLivro(dicLivros):
        print("=== Remover Livro! ===")
        titulo = input("\n Título: ").lower().strip()
 
        if titulo not in dicLivros:
                print("\n O livro não existe no estoque!")
        else:
            quantidade = int(input("\nQuantidade: "))
            if quantidade > dicLivros[titulo]:
                print("Quantidade insuficiente ") 
                print (f"Quantidade disponível :  {dicLivros[titulo]}")
            else:
                dicLivros[titulo] -= quantidade
                print (f"Quantidade atualizada: {dicLivros[titulo]}")  
 
def consulta(dicLivros):
        titulo = input("\n Digite o título do livro: ").lower().strip()
        if titulo in dicLivros:
            print (f"\nLivro: {titulo}")
            print (f"\nQuantidade disponível: {dicLivros[titulo]}")
        else:
            print("O livro não existe no estoque!")
 
def listar(dicLivros):
        print("\n === Livros disponíveis ===")
 
        for titulo, quantidade in dicLivros.items():
            print(f"{titulo} - {quantidade}")
 
def main():
 
    dicLivros = {
            "querido john": 12,
            "a ultima musica": 6,
            "a revoluçao dos bichos": 10,
            "o sol é pra todos": 5,
            "quem pensa enriquece": 7,
            "gatilhos mentais": 9
            }
 
    while True:
 
        print(" \n=== SISTEMA DE GESTÃO DE LIVRARIA ===")
        print(" \n Escolha uma opção" )
        print(" 1 - Adicionar Livro")
        print(" 2 - Remover Livro")
        print(" 3 - Consultar Livro")
        print(" 4 - Listar Livros")
        print(" 5 - Sair")
 
        op = input("\n Digite a opção escolhida: ")
 
        match op:
             case "1":
                  addLivro(dicLivros)
             case "2":
                  removeLivro(dicLivros)
             case "3":
                  consulta(dicLivros)
             case "4":
                  listar(dicLivros)
             case "5":
                  print("\nSaindo...\n\n\n\n")
                  break
             case _:
                  print("\n Opção inválida")
 
main ()