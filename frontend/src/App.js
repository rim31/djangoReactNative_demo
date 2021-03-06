import React, { useState } from 'react';
import './App.css';
import Layout from './layouts/Layout';
import Login from './components/Login';
import Thing from './components/Thing';
// import BaseRouter from './routes';
// import { BrowserRouter as Router } from 'react-router-dom';
function App() {

  const [token, setToken] = useState([]);

  const userLogin = (tok) => {
    console.log("Login", tok)
    setToken(tok);
  }

  return (
    <div>
      <Layout />
      <Login userLogin={userLogin} />
      {token}
      <Thing token={token} />
    </div>
  );
}

export default App;
