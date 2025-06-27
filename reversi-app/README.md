# Reversi/Othello Game

A full-stack implementation of the classic Reversi (Othello) board game with a React frontend and Python Flask backend.

## Features

- Interactive 8x8 game board
- Real-time game state management
- Valid move highlighting
- Score tracking
- Win condition detection
- Responsive design

## Setup Instructions

### Backend (Python Flask)

1. Navigate to the backend directory:
```bash
cd reversi-app/backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python app.py
```

The backend server will run on `http://localhost:5000`

### Frontend (React)

1. Navigate to the frontend directory:
```bash
cd reversi-app/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## Game Rules

1. The game starts with 4 pieces in the center of the board (2 black, 2 white)
2. Black moves first
3. Players must place pieces to capture opponent pieces by surrounding them
4. Valid moves are highlighted on the board
5. If a player has no valid moves, their turn is skipped
6. The game ends when neither player can make a move
7. The player with the most pieces wins

## API Endpoints

- `POST /api/game/new` - Start a new game
- `GET /api/game/{id}/state` - Get current game state
- `POST /api/game/{id}/move` - Make a move
- `GET /api/game/{id}/valid-moves` - Get valid moves for current player

## Project Structure

```
reversi-app/
├── backend/
│   ├── app.py          # Flask API server
│   ├── reversi.py      # Game logic implementation
│   └── requirements.txt # Python dependencies
└── frontend/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── App.js      # Main React component
    │   ├── App.css     # Main styles
    │   ├── Board.js    # Game board component
    │   ├── Board.css   # Board styles
    │   ├── index.js    # React entry point
    │   └── index.css   # Global styles
    └── package.json    # Node.js dependencies
```