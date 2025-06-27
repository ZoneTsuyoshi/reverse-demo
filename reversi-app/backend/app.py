from flask import Flask, jsonify, request
from flask_cors import CORS
from reversi import ReversiGame

app = Flask(__name__)
CORS(app)

games = {}

@app.route('/api/game/new', methods=['POST'])
def new_game():
    game_id = len(games) + 1
    games[game_id] = ReversiGame()
    return jsonify({
        'game_id': game_id,
        'state': games[game_id].get_state()
    })

@app.route('/api/game/<int:game_id>/state', methods=['GET'])
def get_game_state(game_id):
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    return jsonify(games[game_id].get_state())

@app.route('/api/game/<int:game_id>/move', methods=['POST'])
def make_move(game_id):
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    data = request.json
    row = data.get('row')
    col = data.get('col')
    
    if row is None or col is None:
        return jsonify({'error': 'Row and col are required'}), 400
    
    game = games[game_id]
    if game.make_move(row, col, game.current_player):
        return jsonify(game.get_state())
    else:
        return jsonify({'error': 'Invalid move'}), 400

@app.route('/api/game/<int:game_id>/valid-moves', methods=['GET'])
def get_valid_moves(game_id):
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game = games[game_id]
    return jsonify({
        'valid_moves': game.get_valid_moves(game.current_player)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)