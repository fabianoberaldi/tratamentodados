from flask import Flask, jsonify, request
import residencias_controller as rc
import media_preco_controller as mpc

app = Flask(__name__)

# RESIDÊNCIAS -----------------------------------------------------------------------------
@app.route("/residencias/all", methods=["GET"])
def get_residencias_all():
    residencias = rc.get_all()
    return jsonify(residencias)

@app.route("/residencias/neighbourhood_group/<neighbourhood_group>", methods=["GET"])
def get_residencias_by_neighbourhood_group(neighbourhood_group):
    residencias = rc.get_by_neighbourhood_group(neighbourhood_group)
    return jsonify(residencias)

# MÉDIA PREÇO ------------------------------------------------------------------------------
@app.route("/mediapreco/all", methods=["GET"])
def get_media_precos_all():
    media_precos = mpc.get_all()
    return jsonify(media_precos)

@app.route("/mediapreco/neighbourhood_group/<neighbourhood_group>", methods=["GET"])
def get_media_precos_by_neighbourhood_group(neighbourhood_group):
    media_precos = mpc.get_by_neighbourhood_group(neighbourhood_group)
    return jsonify(media_precos)

@app.route("/mediapreco/room_type/<room_type>", methods=["GET"])
def get_media_precos_by_room_type(room_type):
    media_precos = mpc.get_by_room_type(room_type)
    return jsonify(media_precos)

# RESIDÊNCIAS LIKE -------------------------------------------------------------------------
@app.route("/residencias/like", methods=["POST"])
def insert_residencias_like():
    resid_like = request.get_json()
    id_residencia = resid_like['id_residencia']
    valor_like = resid_like['valor_like']
    
    result = rc.insert_like(id_residencia, valor_like)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run()