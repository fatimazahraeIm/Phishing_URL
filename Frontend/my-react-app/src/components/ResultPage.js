import React from 'react';
import './HomePage.css'; // Import the same CSS file

function ResultPage({ result, setResult }) {
  return (
    <div>
      <div className="overlay"></div>
      <header>
        <h1>Phishing URL Detector</h1>
      </header>
      <main className="container">
        <h2>Result :</h2>
        <p style={{ color: result === 'spam' ? 'red' : 'green', fontSize: '24px' }}>
          <strong>{result === 'spam' ? 'Spam' : 'Not Spam'}</strong>
        </p>
        <br></br>
        <button onClick={() => setResult(null)}>
          <i className="fas fa-redo-alt"></i> Reset
        </button>
      </main>
      <footer>
        <p>&copy; 2024 Phishing URL Detector. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default ResultPage;