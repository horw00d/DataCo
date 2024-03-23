import React from 'react';
import { Link } from 'react-router-dom';

function PowerBI() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <h2>PowerBI Page</h2>
      <p>This is the PowerBI emission report.</p>
      <iframe title="Combined" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiOTEyMzAxMmMtOGU1Zi00YWEzLThiYTEtYjRmYzY0OTFmNzFlIiwidCI6IjI0NGU2ZWQyLTMzOWEtNDdmMy1iOTVjLWU0NTM1MWMxOThiNyJ9" frameborder="0" allowFullScreen="true"></iframe>
    </div>
  );
}

export default PowerBI;
