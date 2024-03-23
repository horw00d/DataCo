import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Graphs() {
  const [plotUrl, setPlotUrl] = useState(null);

  useEffect(() => {
    async function fetchPlot() {
      try {
        const response = await axios.get('http://localhost:5000/plot', {
          responseType: 'arraybuffer',
        });
        const blob = new Blob([response.data], { type: 'image/png' });
        const imageUrl = URL.createObjectURL(blob);
        setPlotUrl(imageUrl);
      } catch (error) {
        console.error('Error fetching plot:', error);
      }
    }

    fetchPlot();
  }, []);

  return (
    <div>
      <h2>Net Predicted Emissions per Sector for 2024</h2>
      {plotUrl && <img src={plotUrl} alt="Net Predicted Emissions" style={{ width: '50%', height: 'auto' }} />}
    </div>
  );
}

export default Graphs;