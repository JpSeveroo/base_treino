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
            print("(0) Sair")
            
            opcao = input("Escolhe uma ai: ")
            
            if (opcao == "1"):
                self.cadastrar_task()
            elif (opcao == "2"):
                tasks = self.services.list()
                if not tasks:
                    print("Nao existe nenhuma task cadastrada")
                    
                else:
                    for task in tasks:
                        print(f"Task:{task.title} | descricao:{task.description} | ID:{task.id}")
                
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
        