from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        connection.execute("BEGIN IMMEDIATE")
        table_exists = connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = 'tasks'"
        ).fetchone()

        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0
            )
            """)

        if table_exists is None:
            connection.executemany(
                "INSERT INTO tasks (title, description) VALUES (?, ?)",
                [
                    ("Revisar o projeto", "Conferir as funcionalidades do menu."),
                    ("Preparar a entrega", "Reunir os arquivos da atividade."),
                ],
            )

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")