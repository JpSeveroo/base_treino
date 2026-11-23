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
            print("(4) Atualizar tarefa")
            print("(5) Excluir uma tarefa")
            print("(6) Marcar tarefa como concluída")
            print("(7) Marcar tarefa como pendente")
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
                        status = "Concluída" if task.completed == 1 else "Pendente"
                        print(
                            f"Task:{task.title} | descricao:{task.description} | "
                            f"ID:{task.id} | Situação: {status}"
                        )
            elif (opcao == "3"):
                self.read_one_task()
            elif (opcao == "4"):
                self.update_task()
            elif (opcao == "5"):
                self.delete_task()
            elif (opcao == "6"):
                self._change_task_status(self.services.complete, "concluída")
            elif (opcao == "7"):
                self._change_task_status(self.services.reopen, "pendente")
            elif opcao == "0":
                time.sleep(1)
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def _change_task_status(self, operation, status):
        try:
            task_id = int(input("Identificador da tarefa: "))
        except ValueError:
            print("Informe um identificador inteiro.")
            return

        try:
            changed = operation(task_id)
        except ValueError as error:
            print(f"Erro: {error}")
            return

        if changed:
            print(f"Situação atualizada para {status}.")
        else:
            print(f"A tarefa já está {status}")

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
            print("Tarefa atualizada com sucesso!")
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
