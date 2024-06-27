from connect_database import driver
from CRUDusuario import input_with_cancel

def create_vendedor():
    print("\nInserindo um novo vendedor")
    nome = input_with_cancel("Nome do vendedor: ")
    if nome is None: return

    sobrenome = input_with_cancel("Sobrenome do vendedor: ")
    if sobrenome is None: return
    
    endereco = input_with_cancel("Endereço: ")
    if endereco is None: return

    while True:
        try:
            cpf = int(input_with_cancel("CPF: "))
            if cpf < 0:
                raise ValueError("CPF não pode ser negativo.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

    while True:
        try:
            cnpj = int(input_with_cancel("CNPJ: "))
            if cnpj < 0:
                raise ValueError("CNPJ não pode ser negativo.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
            break 

    print(f"\n{nome} {sobrenome} - {endereco} - {cpf} - {cnpj}")  

    with driver.session() as session:
        session.write_transaction(
            _create_vendedor_tx, nome, sobrenome, endereco, cpf, cnpj
        )
        print("Vendedor inserido com sucesso!")

def _create_vendedor_tx(tx, nome, sobrenome, endereco, cpf, cnpj):  
    query = """
        CREATE (v:Vendedor {nome: $nome, sobrenome: $sobrenome, endereco: $endereco, cpf: $cpf, cnpj: $cnpj})
        """
    tx.run(query, nome=nome, sobrenome=sobrenome, endereco=endereco, cpf=cpf, cnpj=cnpj)

def read_vendedores():
    with driver.session() as session:
        result = session.run("MATCH (v:Vendedor) RETURN v")
        vendedores = [record["v"] for record in result]

        if not vendedores:
            print("Nenhum vendedor encontrado.")
            return None

        print("Vendedores disponíveis:")
        for i, vendedor in enumerate(vendedores):
            print(f"{i+1}. Nome: {vendedor['nome']}, CPF: {vendedor['cpf']}, Endereço: {vendedor['endereco']}, CNPJ: {vendedor['cnpj']}, Email: {vendedor['email']}")

        while True:
            try:
                index = int(input("Digite o número do vendedor que deseja: ")) - 1
                if 0 <= index < len(vendedores):
                    return vendedores[index]['cpf']  # Retorna o cpf do vendedor selecionado
                else:
                    print("Índice inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
