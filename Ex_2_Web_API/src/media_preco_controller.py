from db import get_db

def get_all():
    try:
        db = get_db()
        
        cursor = db.cursor()
        query = "SELECT * FROM media_preco"
        cursor.execute(query)
        return cursor.fetchall()
    
    except Exception as ex:
        raise Exception(f"Falha ao obter média de preços. Erro: {ex}")


def get_by_neighbourhood_group(neighbourhood_group: str):
    try:
        db = get_db()
        
        cursor = db.cursor()
        statement = "SELECT * FROM media_preco WHERE neighbourhood_group = ?"
        cursor.execute(statement, [neighbourhood_group])
        return cursor.fetchall()
    
    except Exception as ex:
        raise Exception(f"Falha ao obter média de preços por 'neighbourhood_group'. Erro: {ex}")

def get_by_room_type(room_type: str):
    try:
        db = get_db()
        
        cursor = db.cursor()
        statement = "SELECT * FROM media_preco WHERE room_type = ?"
        cursor.execute(statement, [room_type])
        return cursor.fetchall()
    
    except Exception as ex:
        raise Exception(f"Falha ao obter média de preços por 'room_type'. Erro: {ex}")