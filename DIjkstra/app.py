from flask import Flask, render_template, request, jsonify
import networkx as nx
import matplotlib.pyplot as plt
import io
import base64
import json

app = Flask(__name__)

# Variable global para almacenar el grafo
graph = nx.Graph()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_node', methods=['POST'])
def add_node():
    data = request.json
    node = data['node']
    graph.add_node(node)
    return jsonify({'status': 'success'})

@app.route('/add_edge', methods=['POST'])
def add_edge():
    data = request.json
    node1 = data['node1']
    node2 = data['node2']
    weight = int(data['weight'])
    graph.add_edge(node1, node2, weight=weight)
    return jsonify({'status': 'success'})

@app.route('/calculate_dijkstra', methods=['POST'])
def calculate_dijkstra():
    data = request.json
    start_node = data['start_node']
    end_node = data['end_node']
    
    try:
        # Calcular el camino más corto usando Dijkstra
        path = nx.dijkstra_path(graph, start_node, end_node)
        path_length = nx.dijkstra_path_length(graph, start_node, end_node)
        
        # Generar imagen del grafo con el camino resaltado
        img = plot_graph_with_path(graph, path)
        
        return jsonify({
            'status': 'success',
            'path': path,
            'path_length': path_length,
            'graph_image': img
        })
    except nx.NodeNotFound:
        return jsonify({'status': 'error', 'message': 'Nodo no encontrado'})
    except nx.NetworkXNoPath:
        return jsonify({'status': 'error', 'message': 'No existe camino entre los nodos'})

def plot_graph_with_path(g, path):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(g)
    
    # Dibujar todos los nodos y aristas
    nx.draw_networkx_nodes(g, pos, node_size=700)
    nx.draw_networkx_edges(g, pos, width=1)
    
    # Resaltar el camino
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(g, pos, nodelist=path, node_color='r')
    nx.draw_networkx_edges(g, pos, edgelist=path_edges, edge_color='r', width=2)
    
    # Etiquetas
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(g, pos, font_size=12, font_family='sans-serif')
    
    # Convertir imagen a base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = base64.b64encode(buf.read()).decode('ascii')
    plt.close()
    
    return img

if __name__ == '__main__':
    app.run(debug=True)
    