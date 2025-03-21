from flask import Flask, request, jsonify, render_template
from bfs import bfs
from dfs import dfs
from recursive_dfs import recursive_dfs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_puzzle():
    data = request.json
    start_node = data.get('start_node')
    end_node = data.get('end_node')
    algorithm = data.get('algorithm')

    if algorithm == 'bfs':
        solution = bfs(start_node, end_node)
    elif algorithm == 'dfs':
        solution = dfs(start_node, end_node)
    elif algorithm == 'recursive_dfs':
        solution = recursive_dfs(start_node, end_node)
    else:
        return jsonify({'error': 'Invalid algorithm specified'}), 400

    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)
    