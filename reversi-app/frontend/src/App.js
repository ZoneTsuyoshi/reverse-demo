import React, { useState, useEffect } from 'react';
import Board from './Board';
import './App.css';

const API_URL = 'http://localhost:5000/api';

function App() {
  const [gameState, setGameState] = useState(null);
  const [gameId, setGameId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const startNewGame = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${API_URL}/game/new`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      const data = await response.json();
      setGameId(data.game_id);
      setGameState(data.state);
    } catch (err) {
      setError('Failed to start new game');
    }
    setLoading(false);
  };

  const makeMove = async (row, col) => {
    if (!gameId || loading || gameState?.game_over) return;

    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${API_URL}/game/${gameId}/move`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ row, col }),
      });
      
      if (response.ok) {
        const data = await response.json();
        setGameState(data);
      } else {
        const errorData = await response.json();
        setError(errorData.error || 'Invalid move');
      }
    } catch (err) {
      setError('Failed to make move');
    }
    setLoading(false);
  };

  const getPlayerName = (player) => {
    return player === 1 ? 'Black' : 'White';
  };

  const getWinnerText = () => {
    if (!gameState?.game_over) return '';
    if (gameState.winner === 0) return 'It\'s a tie!';
    return `${getPlayerName(gameState.winner)} wins!`;
  };

  useEffect(() => {
    startNewGame();
  }, []);

  if (!gameState) {
    return (
      <div className="app">
        <h1>Reversi / Othello</h1>
        <div className="loading">Loading...</div>
      </div>
    );
  }

  return (
    <div className="app">
      <h1>Reversi / Othello</h1>
      
      <div className="game-info">
        <div className="scores">
          <div className="score">
            <div className="score-piece black"></div>
            <span>Black: {gameState.score.black}</span>
          </div>
          <div className="score">
            <div className="score-piece white"></div>
            <span>White: {gameState.score.white}</span>
          </div>
        </div>
        
        {!gameState.game_over && (
          <div className="current-player">
            Current player: {getPlayerName(gameState.current_player)}
          </div>
        )}
        
        {gameState.game_over && (
          <div className="game-over">
            <h2>{getWinnerText()}</h2>
          </div>
        )}
        
        {error && <div className="error">{error}</div>}
      </div>

      <Board
        board={gameState.board}
        validMoves={gameState.valid_moves}
        onCellClick={makeMove}
        currentPlayer={gameState.current_player}
      />

      <div className="controls">
        <button onClick={startNewGame} disabled={loading}>
          {loading ? 'Loading...' : 'New Game'}
        </button>
      </div>

      <div className="rules">
        <h3>How to Play:</h3>
        <ul>
          <li>Click on a highlighted square to place your piece</li>
          <li>Capture opponent pieces by surrounding them</li>
          <li>The game ends when no more moves are possible</li>
          <li>The player with the most pieces wins!</li>
        </ul>
      </div>
    </div>
  );
}

export default App;