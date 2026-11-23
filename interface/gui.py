from service.services import Services
import time

class UI:

    def __init__(self, services):
        self.services = services
    
    def show_principal_menu(self):
        while True:
            print("MENU DE TAREFAS:")
            print("(1) Cadastrar Tarefa")
            print("(2) Listar Tarefas")
            print("(3) Listar uma tarefa")
            print("(4) Excluir uma tarefa")
            print("(0) Sair")
            
            opcao = input("Escolhe uma aí: ")
            
            if (opcao == "1"):
                self.cadastrar_task()
            elif (opcao == "2"):
                tasks = self.services.list()
                if not tasks:
                    print("Nao existe nenhuma task cadastrada")
                    
                else:
                    for task in tasks:
                        print(f"Task:{task.title} | descricao:{task.description} | ID:{task.id}")
            elif (opcao == "3"):
                self.read_one_task()
            elif (opcao == "4"):
                self.delete_task()
            elif opcao == "0":
                time.sleep(1)
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")
                
                
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

    def delete_task(self):
        print("\n--- Informe o Id ---")
        try:
            task_id = int(input("id: "))
            task = self.services.get(task_id)
            print("\n--- Deseja excluir essa task ---")
            print(f"título: {task.title}\ndescrição: {task.description}")
            decision = input("Deseja excluir?(s/n): ")
            if decision.lower() == "s":
                self.services.delete(task_id)
                print("\nTarefa excluída com sucesso")
            else:
                print("\nExclusão cancelada")
        except ValueError as e:
            print(e)
            return
