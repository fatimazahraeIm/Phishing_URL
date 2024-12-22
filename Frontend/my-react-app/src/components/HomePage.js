import React, { useState } from 'react';
import './HomePage.css';

function HomePage({ setResult }) {
  const [url, setUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }),
    });
    const data = await response.json();
    setResult(data.result);
  };

  return (
    <div>
      <div className="overlay"></div>
      <header>
        <h1>Phishing URL Detector</h1>
      </header>
      <main className="container">
        <section className="description">
        <h2>About This Project</h2>
<p>
  <strong>Phishing</strong> is a common and dangerous form of cyberattack where attackers deceive victims into revealing sensitive information by masquerading as a trustworthy entity. The growing sophistication of phishing tactics has made it critical for organizations and individuals to adopt proactive measures against these threats.
</p>
<p>
  This project implements a <strong>machine learning-based solution</strong> to detect phishing URLs. By analyzing various characteristics of URLs, the system can predict whether a given URL is likely to be legitimate or a phishing attempt. The solution is designed to be easily integrated as a <strong>RESTful API</strong>, making it a valuable tool for real-time phishing detection.
</p>
<p>
  To get started, enter a URL in the input field below and click the <strong>"Start"</strong> button. The system will analyze the URL and provide a prediction on whether it is a phishing attempt or not.
</p>
          <br></br> 
          <br></br> 
        </section>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter URL"
          />
          <button type="submit">Start</button>
        </form>
      </main>
      <footer>
        <p>&copy; 2024 Phishing URL Detector. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default HomePage;