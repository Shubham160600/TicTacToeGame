import React, { useState } from 'react';

const TicTacToeGame = () => {
  const [board, setBoard] = useState(Array(9).fill(''));
  const [currentPlayer, setCurrentPlayer] = useState('X');
  const [player1Name, setPlayer1Name] = useState('');
  const [player2Name, setPlayer2Name] = useState('');
  const [gameStarted, setGameStarted] = useState(false);
  const [gameOver, setGameOver] = useState(false);
  const [winner, setWinner] = useState('');
  const [moveCount, setMoveCount] = useState(0);

  const checkWinner = (newBoard) => {
    const winPatterns = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
      [0, 4, 8], [2, 4, 6] // diagonals
    ];

    for (let pattern of winPatterns) {
      const [a, b, c] = pattern;
      if (newBoard[a] && newBoard[a] === newBoard[b] && newBoard[a] === newBoard[c]) {
        return newBoard[a];
      }
    }
    return null;
  };

  const handleCellClick = (index) => {
    if (board[index] !== '' || gameOver) return;

    const newBoard = [...board];
    newBoard[index] = currentPlayer;
    setBoard(newBoard);

    const winnerPlayer = checkWinner(newBoard);
    const newMoveCount = moveCount + 1;
    setMoveCount(newMoveCount);

    if (winnerPlayer) {
      setWinner(currentPlayer === 'X' ? player1Name : player2Name);
      setGameOver(true);
    } else if (newMoveCount === 9) {
      setWinner('Tie');
      setGameOver(true);
    } else {
      setCurrentPlayer(currentPlayer === 'X' ? 'O' : 'X');
    }
  };

  const startGame = () => {
    if (player1Name.trim() && player2Name.trim()) {
      setGameStarted(true);
    }
  };

  const resetGame = () => {
    setBoard(Array(9).fill(''));
    setCurrentPlayer('X');
    setGameOver(false);
    setWinner('');
    setMoveCount(0);
  };

  const newGame = () => {
    setBoard(Array(9).fill(''));
    setCurrentPlayer('X');
    setPlayer1Name('');
    setPlayer2Name('');
    setGameStarted(false);
    setGameOver(false);
    setWinner('');
    setMoveCount(0);
  };

  if (!gameStarted) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-400 to-purple-600 flex items-center justify-center p-4">
        <div className="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md">
          <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">
            Tic-Tac-Toe
          </h1>
          <div className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Player 1 Name (X)
              </label>
              <input
                type="text"
                value={player1Name}
                onChange={(e) => setPlayer1Name(e.target.value)}
                className="w-full px-4 py-3 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none transition-colors"
                placeholder="Enter player 1 name"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Player 2 Name (O)
              </label>
              <input
                type="text"
                value={player2Name}
                onChange={(e) => setPlayer2Name(e.target.value)}
                className="w-full px-4 py-3 border-2 border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none transition-colors"
                placeholder="Enter player 2 name"
              />
            </div>
            <button
              onClick={startGame}
              disabled={!player1Name.trim() || !player2Name.trim()}
              className="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white py-3 px-6 rounded-lg font-semibold text-lg hover:from-blue-600 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all transform hover:scale-105"
            >
              Start Game
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-400 to-purple-600 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-lg">
        <h1 className="text-4xl font-bold text-center mb-6 text-gray-800">
          Tic-Tac-Toe
        </h1>
        
        <div className="text-center mb-6">
          <div className="flex justify-between items-center mb-4">
            <div className="text-lg font-semibold text-gray-700">
              {player1Name} (X)
            </div>
            <div className="text-lg font-semibold text-gray-700">
              {player2Name} (O)
            </div>
          </div>
          
          {!gameOver && (
            <div className="text-xl font-bold text-blue-600 mb-4">
              Current Player: {currentPlayer === 'X' ? player1Name : player2Name} ({currentPlayer})
            </div>
          )}
          
          {gameOver && (
            <div className="text-2xl font-bold mb-4">
              {winner === 'Tie' ? (
                <span className="text-orange-600">Game Tied!</span>
              ) : (
                <span className="text-green-600">{winner} Wins! 🎉</span>
              )}
            </div>
          )}
        </div>

        <div className="grid grid-cols-3 gap-3 mb-6 max-w-xs mx-auto">
          {board.map((cell, index) => (
            <button
              key={index}
              onClick={() => handleCellClick(index)}
              className="w-20 h-20 bg-gray-100 border-2 border-gray-300 rounded-lg text-3xl font-bold hover:bg-gray-200 transition-colors flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-blue-500"
              disabled={gameOver || cell !== ''}
            >
              <span className={cell === 'X' ? 'text-blue-600' : 'text-red-600'}>
                {cell || index}
              </span>
            </button>
          ))}
        </div>

        <div className="flex gap-4 justify-center">
          <button
            onClick={resetGame}
            className="bg-green-500 text-white py-2 px-6 rounded-lg font-semibold hover:bg-green-600 transition-colors"
          >
            Reset Game
          </button>
          <button
            onClick={newGame}
            className="bg-gray-500 text-white py-2 px-6 rounded-lg font-semibold hover:bg-gray-600 transition-colors"
          >
            New Game
          </button>
        </div>

        {gameOver && (
          <div className="text-center mt-6">
            <p className="text-lg text-gray-600">
              Game Over! Thanks For Playing
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default TicTacToeGame;
