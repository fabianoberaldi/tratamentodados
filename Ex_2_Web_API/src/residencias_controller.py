from db import get_db

def get_all():
    try:
        db = get_db()
        
        cursor = db.cursor()
        query = "SELECT * FROM residencias"
        cursor.execute(query)
        return cursor.fetchall()
    
    except Exception as ex:
        raise Exception(f"Falha ao obter residências. Erro: {ex}")

def get_by_neighbourhood_group(neighbourhood_group: str):
    try:
        db = get_db()
        
        cursor = db.cursor()
        statement = "SELECT * FROM residencias WHERE neighbourhood_group = ?"
        cursor.execute(statement, [neighbourhood_group])
        return cursor.fetchall()
    
    except Exception as ex:
        raise Exception(f"Falha ao obter residências por 'neighbourhood_group'. Erro: {ex}")
    
def insert_like(id_residencia: int, valor_like: int):
    try:
        db = get_db()
        
        cursor = db.cursor()
        statement = "INSERT INTO residencias_like(id_residencia, like) VALUES (?, ?)"
        cursor.execute(statement, [id_residencia, valor_like])
        db.commit()
        
        return True
        
    except Exception as ex:
        raise Exception(f"Falha ao inserir like em residências. Erro: {ex}") 