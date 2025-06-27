import React from 'react';
import './Board.css';

const Board = ({ board, validMoves, onCellClick, currentPlayer }) => {
  const isValidMove = (row, col) => {
    return validMoves.some(([r, c]) => r === row && c === col);
  };

  const getCellClass = (row, col, value) => {
    let className = 'cell';
    if (value === 1) className += ' black';
    if (value === 2) className += ' white';
    if (isValidMove(row, col)) className += ' valid-move';
    return className;
  };

  return (
    <div className="board">
      {board.map((row, rowIndex) => (
        <div key={rowIndex} className="row">
          {row.map((cell, colIndex) => (
            <div
              key={`${rowIndex}-${colIndex}`}
              className={getCellClass(rowIndex, colIndex, cell)}
              onClick={() => onCellClick(rowIndex, colIndex)}
            >
              {cell !== 0 && <div className="piece" />}
              {isValidMove(rowIndex, colIndex) && (
                <div className="valid-indicator" />
              )}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Board;