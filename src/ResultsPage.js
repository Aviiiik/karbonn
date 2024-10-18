// ResultsPage.js
import React, { useEffect, useState } from 'react';

function ResultsPage() {
  const [result, setResult] = useState(null);

  useEffect(() => {
    const data = sessionStorage.getItem('result');
    if (data) {
      setResult(JSON.parse(data));
    }
  }, []);

  if (!result) {
    return <p>No results to display. Please upload a file first.</p>;
  }

  // Extract the result string and format it for display
  const resultsArray = result.result.split('\n').reduce((acc, line) => {
    const [key, value] = line.split(': ');
    if (key && value) {
      acc[key.trim()] = value.trim(); // Store each key-value pair in the accumulator
    }
    return acc;
  }, {});

  return (
    <div>
      <h1>Analysis Results</h1>
      <div>
        <p>Rule 1: Total Revenue 5 Crore Flag: {resultsArray["TOTAL_REVENUE_5CR_FLAG"] || "Not evaluated"}</p>
        <p>Rule 2: Borrowing to Revenue Flag: {resultsArray["BORROWING_TO_REVENUE_FLAG"] || "Not evaluated"}</p>
        <p>Rule 3: ISCR Flag: {resultsArray["ISCR_FLAG"] || "Not evaluated"}</p>
      </div>
    </div>
  );
}

export default ResultsPage;
