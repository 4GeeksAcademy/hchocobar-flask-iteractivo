from flask import Flask, jsonify, request


app = Flask(__name__)  # creamos la variable app, que es una instancia de Flask


@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)
    return json_text

""" 
@app.route('/todos', methods=['GET'])
def handle_todos():
    response_body = jsonify(todos)
    return response_body


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)
 """


@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = "Listado de Todos"
        response_body['results'] = todos
        return response_body
    if request.method == 'POST':
        request_body = request.json
        print("Incoming request with the following body", request_body)
        todos.append(request_body)
        response_body['message'] = "Tarea agreaga correctamente"
        response_body['results'] = todos
        return response_body


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= len(todos):
        response_body = {'message': 'Tarea fuera de rango'}
        return response_body
    del todos[position]
    return jsonify(todos)




# Supongamos que tienes tus datos en la variable some_data
some_data = {"name": "Bobby", "lastname": "Rixer"}
todos = [{ "label": "My first task", "done": False },
         { "label": "My second task", "done": False }]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
