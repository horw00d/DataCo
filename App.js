import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes, Navigate } from 'react-router-dom';
import PowerBI from './PowerBI';
import Graphs from './Graphs';
import HomePage from './HomePage';

function Home() {
  const [data, setData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get('http://localhost:5000/api/data');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="header-content">
          <div id="title">
            <h1>DataCo</h1>
            <img src="https://konicaminolta.ca/wps/wcm/connect/bca/c6c4b1fd-1299-4d14-ae44-ffd35dcaeda1/Icon_Environment_Blue.png?MOD=AJPERES&CACHEID=ROOTWORKSPACE.Z18_0IDCHAS0L03T10A5N5R0IT3PU6-c6c4b1fd-1299-4d14-ae44-ffd35dcaeda1-lrmlsfD" alt="Logo" width="75" height="75" />
          </div>
          <nav>
            <div style={{ paddingTop: '20px' }}>
              <Link to="/homepage" className="nav-button">Home</Link>
              <Link to="/powerbi" className="nav-button">PowerBI</Link>
              <Link to="/graphs" className="nav-button">Graphs</Link>
            </div>
          </nav>
        </div>
      </header>

      <main className="app-main">
        <h2>Data Metrics</h2>
        {data ? (
          <div className="card">
            <div className="card-content">
              <p><strong>Company:</strong> {data.company}</p>
              <p><strong>Sector:</strong> {data.sector}</p>
              <p><strong>Cost:</strong> {data.cost}</p>
            </div>
          </div>
        ) : (
          <p>Loading...</p>
        )}

        <Routes>
          <Route path="/powerbi" element={<PowerBI />} />
          <Route path="/graphs" element={<Graphs />} />
          <Route path="/homepage" element={<HomePage />} /> {/* Corrected element */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </main>

      <footer className="app-footer">
        <p>&copy; 2024 DataCo. All rights reserved.</p>
      </footer>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Home />
    </Router>
  );
}

export default App;