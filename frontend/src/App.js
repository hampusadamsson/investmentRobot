import React from 'react';
import logo from './img/logo.svg';
import './css/App.css';
import Requester from './Requester';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>YOO src/App.js</code> and save to reload.
        </p>
        <Requester />
      </header>
    </div>
  );
}

export default App;
