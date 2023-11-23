class Prontuario:
    def __init__(self):
        self.historico_medico = []
        self.medicamentos = []
        self.consultas = []

    def adicionar_historico(self, evento):
        self.historico_medico.append(evento)

    def adicionar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def __str__(self):
        historico_str = "\n".join(self.historico_medico)
        medicamentos_str = "\n".join(self.medicamentos)
        consultas_str = "\n".join([str(consulta) for consulta in self.consultas])
        return (f"Histórico Médico: \n{historico_str}\n"
                f"Medicamentos: \n{medicamentos_str}\n"
                f"Consultas: \n{consultas_str}")

class Paciente:
    def __init__(self, nome_completo, data_nascimento, contato_telefonico, email, endereco, cpf):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.contato_telefonico = contato_telefonico
        self.email = email
        self.endereco = endereco
        self.cpf = cpf
        self.prontuario = Prontuario()  # Cria um prontuário vazio para cada paciente

    def __str__(self):
        return (f"Nome Completo: {self.nome_completo}\n"
                f"Data de Nascimento: {self.data_nascimento}\n"
                f"Contato Telefônico: {self.contato_telefonico}\n"
                f"E-mail: {self.email}\n"
                f"Endereço: {self.endereco}\n"
                f"CPF: {self.cpf}\n"
                f"\nProntuário:\n{self.prontuario}")

class Node:
    def __init__(self, paciente):
        self.paciente = paciente
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, paciente):
        self.root = self._insert(self.root, paciente)
        
    def _insert(self, node, paciente):
        # Inserção na BST
        if not node:
            return Node(paciente)
        if paciente.nome_completo < node.paciente.nome_completo:  # Comparação pelo nome
            node.left = self._insert(node.left, paciente)
        else:
            node.right = self._insert(node.right, paciente)
            
        # Atualização da altura do nó
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Balanceamento do nó
        return self._balance(node)
    
    def search(self, cpf):
        node, comparisons = self._search(self.root, cpf, 0)
        if node:
            return node.paciente, comparisons
        return None, comparisons

    def _search(self, node, cpf, comparisons):
        if not node:
            return None, comparisons
        comparisons += 1
        if cpf == node.paciente.cpf:
            return node, comparisons
        elif cpf < node.paciente.cpf:
            return self._search(node.left, cpf, comparisons)
        else:
            return self._search(node.right, cpf, comparisons)
    
    def _get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _balance(self, node):
        balance_factor = self._get_balance_factor(node)
        if balance_factor > 1:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        if balance_factor < -1:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        return node
    
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T3 = x.right
        x.right = y
        y.left = T3
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

pacientes = AVLTree()

def cadastrar_paciente():
    clear_screen()
    print("---- Cadastro de Paciente ----")
    nome_completo = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento (dd/mm/yyyy): ")
    contato_telefonico = input("Contato Telefônico: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    cpf = input("CPF (somente números): ")

    # Aqui pode-se adicionar validações
    paciente = Paciente(nome_completo, data_nascimento, contato_telefonico, email, endereco, cpf)

    pacientes.insert(paciente)  # Insere o paciente na árvore AVL
    input("\nPaciente cadastrado com sucesso! Pressione ENTER para continuar.")

def listar_pacientes():
    clear_screen()
    print("---- Lista de Pacientes ----")

    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            print("\n", "-"*30, "\n", node.paciente, "\n", "-"*30)
            in_order_traversal(node.right)

    in_order_traversal(pacientes.root)
    input("\nPressione ENTER para continuar.")

def clear_screen():
    print("\n" * 50)  # Simplesmente imprime várias linhas em branco para "limpar" a tela.

def adicionar_evento_historico(paciente):
    evento = input("Descrição do evento histórico: ")
    paciente.prontuario.adicionar_historico(evento)
    print("Evento adicionado ao histórico médico.")

def adicionar_medicamento(paciente):
    medicamento = input("Nome do medicamento: ")
    paciente.prontuario.adicionar_medicamento(medicamento)
    print("Medicamento adicionado ao prontuário.")

def adicionar_consulta(paciente):
    consulta = input("Descrição da consulta: ")
    paciente.prontuario.adicionar_consulta(consulta)
    print("Consulta adicionada ao prontuário.")

def formatar_secao(titulo, conteudo):
    if not conteudo:
        conteudo = ["Nenhuma informação disponível"]
    return f"\n{titulo}\n{'-' * len(titulo)}\n" + "\n".join(conteudo) + "\n"

def consultar_prontuario(paciente):
    clear_screen()
    print(f"{'=' * 40}\nProntuário do Paciente: {paciente.nome_completo}\n{'=' * 40}")

    historico = formatar_secao("Histórico Médico", paciente.prontuario.historico_medico)
    medicamentos = formatar_secao("Medicamentos", paciente.prontuario.medicamentos)
    consultas = formatar_secao("Consultas", [str(consulta) for consulta in paciente.prontuario.consultas])

    print(historico)
    print(medicamentos)
    print(consultas)

    input("\nPressione ENTER para retornar ao menu principal.")

def exibir_menu_atualizacao():
    print("\n---- Atualização de Prontuário ----")
    print("Escolha uma opção:")
    print("1. Adicionar evento ao histórico médico")
    print("2. Adicionar medicamento")
    print("3. Adicionar consulta")
    print("4. Exibe Prontuário")
    print("5. Finalizar atualização")
    return input("> ")

def atualizar_prontuario():
    clear_screen()
    print("---- Atualizar Prontuário do Paciente ----")
    cpf_busca = input("Digite o CPF do paciente para atualizar o prontuário: ")

    paciente, _ = pacientes.search(cpf_busca)

    if paciente:
        while True:
            clear_screen()
            print(f"Paciente: {paciente.nome_completo}")
            opcao = exibir_menu_atualizacao()

            if opcao == '1':
                adicionar_evento_historico(paciente)
            elif opcao == '2':
                adicionar_medicamento(paciente)
            elif opcao == '3':
                adicionar_consulta(paciente)
            elif opcao == '4':
                consultar_prontuario(paciente)
            elif opcao == '5':
                clear_screen()
                print("\nFinalizando atualização do prontuário...")
                break
            else:
                print("\nOpção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar.")

        print("\nProntuário atualizado com sucesso!\n")
    else:
        print("\nNenhum paciente com o CPF informado foi encontrado.")

    input("\nPressione ENTER para retornar ao menu principal.")

def main():
    while True:
        clear_screen()
        print("-" * 40)
        print(" Prontuario Digital ".center(40, "-"))
        print("-" * 40)
        print("\n1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Prontuário do Paciente")
        print("4. Sair\n")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            listar_pacientes()
        elif opcao == '3':
            atualizar_prontuario()
        elif opcao == '4':
            print("\nEncerrando o sistema.")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")
            input("Pressione ENTER para continuar.")

if __name__ == '__main__':
    main()