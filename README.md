# Prontuário Digital

## Sobre o Projeto
Este repositório contém o código-fonte do **Sistema de Prontuário Digital**, uma solução moderna e segura para a gestão de informações médicas. Nosso sistema foi desenvolvido para facilitar o acesso a dados de pacientes, agilizar processos e garantir a segurança e a privacidade das informações.

## Funcionalidades
- **Cadastro de Pacientes**: Uma interface amigável permite a fácil inserção e atualização de dados dos pacientes, incluindo informações pessoais, histórico médico, e mais.
- **Prontuário do Paciente**: Gestão eficiente do prontuário de cada paciente, com capacidade de registrar e acessar informações detalhadas.

## Tecnologias Utilizadas
- **Linguagem de Programação**: Python

---

## Documentação do Sistema de Prontuário Digital

### Classes Principais

#### Classe `Prontuario`
Responsável por gerenciar o prontuário de um paciente.

##### Atributos
- `historico_medico`: Lista de eventos médicos (como diagnósticos e procedimentos).
- `medicamentos`: Lista de medicamentos prescritos.
- `consultas`: Lista de consultas realizadas.

##### Métodos
- `adicionar_historico(evento)`: Adiciona um evento ao histórico médico.
- `adicionar_medicamento(medicamento)`: Adiciona um medicamento ao prontuário.
- `adicionar_consulta(consulta)`: Adiciona uma consulta ao prontuário.
- `__str__`: Retorna uma representação em string do prontuário.

#### Classe `Paciente`
Representa um paciente no sistema.

##### Atributos
- `nome_completo`: Nome completo do paciente.
- `data_nascimento`: Data de nascimento.
- `contato_telefonico`: Número de telefone para contato.
- `email`: Endereço de e-mail.
- `endereco`: Endereço residencial.
- `cpf`: CPF do paciente.
- `prontuario`: Instância de `Prontuario` associada ao paciente.

##### Métodos
- `__str__`: Retorna uma representação em string do paciente e seu prontuário.

#### Classe `Node`
Utilizada na estrutura da árvore AVL para armazenar pacientes.

##### Atributos
- `paciente`: Objeto `Paciente` armazenado no nó.
- `left`: Referência ao filho esquerdo na árvore.
- `right`: Referência ao filho direito na árvore.
- `height`: Altura do nó na árvore.

#### Classe `AVLTree`
Representa uma árvore AVL para armazenar e gerenciar pacientes.

##### Atributos
- `root`: Raiz da árvore AVL.

##### Métodos
- `insert(paciente)`: Insere um paciente na árvore.
- `search(cpf)`: Procura um paciente na árvore pelo CPF.
- `_insert(node, paciente)`: Auxiliar para inserir um paciente.
- `_search(node, cpf, comparisons)`: Auxiliar para procurar um paciente.
- `_get_height(node)`: Retorna a altura de um nó.
- `_get_balance_factor(node)`: Retorna o fator de balanceamento de um nó.
- `_balance(node)`: Balanceia um nó na árvore.
- `_rotate_left(z)`: Realiza rotação para a esquerda.
- `_rotate_right(y)`: Realiza rotação para a direita.

### Funções do Sistema
- `cadastrar_paciente()`: Permite o cadastro de um novo paciente no sistema.
- `listar_pacientes()`: Exibe uma lista de todos os pacientes cadastrados.
- `clear_screen()`: Limpa a tela para melhor visualização do menu e informações.
- `adicionar_evento_historico(paciente)`: Adiciona um evento ao histórico médico de um paciente.
- `adicionar_medicamento(paciente)`: Adiciona um medicamento ao prontuário de um paciente.
- `adicionar_consulta(paciente)`: Adiciona uma consulta ao prontuário de um paciente.
- `formatar_secao(titulo, conteudo)`: Formata uma seção de informações para exibição.
- `consultar_prontuario(paciente)`: Consulta e exibe o prontuário de um paciente específico.
- `exibir_menu_atualizacao()`: Exibe o menu para atualização de prontuário.
- `atualizar_prontuario()`: Permite atualizar o prontuário de um paciente.
- `main()`: Função principal que executa o menu do sistema.

## Como Usar
O sistema é iniciado chamando a função `main()`. A partir do menu principal, o usuário pode escolher entre cadastrar novos pacientes, listar todos os pacientes, atualizar o prontuário de um paciente específico, ou sair do sistema. As interações com o usuário são feitas através de entradas de texto e escolhas de menu.
