from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        # Criar tabela no banco de dados
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0
            )
            """)

        # Inserir dados iniciais (OBRIGATÓRIO!!!!)
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")