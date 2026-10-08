class Residencia:
    def __init__(self):# Lista privada que armazena os cômodos da residência.
        self.__comodos = []

    def adicionar_comodo(self, nome, area):
        comodo = Comodo(nome, area)
        self.__comodos.append(comodo)# Adiciona o cômodo criado à lista da residência.

    def listar_comodos(self):# Verifica se não existem cômodos cadastrados.
        if len(self.__comodos) == 0:
            print("\nNenhum cômodo cadastrado.")
            return

        print("\n--- Cômodos da residência ---")

        for comodo in self.__comodos:# Percorre todos os cômodos armazenados na residência.
            print(f"Nome: {comodo.get_nome()}")
            print(f"Área: {comodo.get_area()} m²")
            print("-----------------------------")

    def calcular_area_total(self):
        area_total = 0

        for comodo in self.__comodos:
            area_total += comodo.get_area()

        return area_total


class Comodo:
    def __init__(self, nome, area):# Atributos privados para proteger os dados do cômodo.
        self.__nome = nome
        self.__area = area

    def get_nome(self):
        return self.__nome

    def get_area(self):
        return self.__area


def menu():
    residencia = Residencia()

    while True:
        print("\n===== MENU =====")
        print("1 - Adicionar cômodo")
        print("2 - Visualizar cômodos")
        print("3 - Calcular área total")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cômodo: ")

            try:
                area = float(input("Digite a área do cômodo em m²: ")) # Converte a área informada pelo usuário para número decimal.

                if area <= 0:# Verifica se a área informada é válida.
                    print("A área deve ser maior que zero.")
                else:
                    residencia.adicionar_comodo(nome, area)
                    print("Cômodo adicionado com sucesso!")

            except ValueError:# Trata o erro caso o usuário digite algo que não seja um número.
                print("Digite uma área válida.")

        elif opcao == "2":
            residencia.listar_comodos()

        elif opcao == "3":
            area_total = residencia.calcular_area_total()
            print(f"\nÁrea total da residência: {area_total:.2f} m²")

        elif opcao == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()