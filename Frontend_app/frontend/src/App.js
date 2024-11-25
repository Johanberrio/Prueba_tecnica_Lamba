import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Registro from './components/RegisterForm';
import Success from './components/success';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/register" element={<Registro />} />
        <Route path="/success" element={<Success />} />
      </Routes>
    </Router>
  );
}

export default App;