// UploadPage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function UploadPage() {
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      sessionStorage.setItem('result', JSON.stringify(data));
      navigate('/results');
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to upload the file.');
    }
  };

  return (
    <div className="container">
      <h1>Financial Model Analysis</h1>
      <div className="file-upload-container"> {/* Box for file upload */}
        <input type="file" accept=".json" onChange={handleFileChange} />
        <button onClick={handleSubmit}>Submit</button>
      </div>
    </div>
  );
}

export default UploadPage;
