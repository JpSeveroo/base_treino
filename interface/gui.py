from service.services import Services


class UI:

    def __init__(self, services):
        self.services = services
    
    def show_principal_menu(self):
        while True:
            print("MENU DE TAREFAS:")
            print("(1) Cadastrar Tarefa")
            print("(3) Listar uma tarefa")
            print("(4) Atualizar tarefa")
            print("(0) Sair")
            
            opcao = input("Escolhe uma aí: ")
            
            if (opcao == "1"):
                self.cadastrar_task()
            elif (opcao == "3"):
                self.read_one_task()
            elif:
                self.update
            elif opcao == "0":
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def update_task(self):
        try:
            task_id = int(input("Identificador da tarefa: "))
        except ValueError:
            print("Informe um identificador inteiro.")
            return

        title = input("Novo título: ")
        description = input("Nova descrição (opcional): ")

        try:
            self.services.update(task_id, title, description)
        except ValueError as error:
            print(f"Error: {error}")
            return
                
    def cadastrar_task(self):
        print("\n--- Nova Tarefa ---")
        title = input("Título: ")
        description = input("Descrição (opcional): ")
        
        try:
            task = self.services.create(title,description)
            print(f"Tarefa cadastrada com sucesso! ID: {task.id}")
        except ValueError as e:
            print(f"Erro: {e}")
            return
    
    def read_one_task(self):
        print("\n--- Informe o Id ---")
        try:
            task_id = int(input("id: "))
            task = self.services.get(task_id)
            status = "Concluída" if task.completed == 1 else "Pendente"
            print("\n--- Tarefa ---")
            print(f"id:{task.id}\ntítulo:{task.title}\ndescrição:{task.description}\ncompleta:{status}")
        except ValueError as e:
            print(e)
            return