---
layout: default
---

<div id="prediction-container">
  <h2>Today's Penguin</h2>
  <p id="loading">Loading latest prediction...</p>
</div>

<script>
// Create a hardcoded sample prediction to ensure the page works
const sampleData = {
  "date": "2023-04-07",
  "prediction": "Adelie",
  "probability": 50.0,
  "measurements": {
    "bill_length_mm": 44.02,
    "bill_depth_mm": 17.23,
    "flipper_length_mm": 199.80,
    "body_mass_g": 5374.90,
    "datetime": "2025-04-07 07:59:00"
  }
};

// Display the prediction data
document.addEventListener('DOMContentLoaded', function() {
  const predDiv = document.getElementById('prediction-container');
  
  try {
    predDiv.innerHTML = `
      <h2>Today's Penguin (${sampleData.date})</h2>
      <p><strong>Species:</strong> ${sampleData.prediction}</p>
      <p><strong>Confidence:</strong> ${sampleData.probability.toFixed(2)}%</p>
      <h3>Measurements:</h3>
      <ul>
        <li>Bill Length: ${sampleData.measurements.bill_length_mm.toFixed(2)} mm</li>
        <li>Bill Depth: ${sampleData.measurements.bill_depth_mm.toFixed(2)} mm</li>
        <li>Flipper Length: ${sampleData.measurements.flipper_length_mm.toFixed(2)} mm</li>
        <li>Body Mass: ${sampleData.measurements.body_mass_g.toFixed(2)} g</li>
        <li>Time: ${sampleData.measurements.datetime}</li>
      </ul>
      <p><em>Note: This is a sample prediction. The GitHub workflow will update this data daily.</em></p>
    `;
  } catch (error) {
    predDiv.innerHTML = `
      <h2>Today's Penguin</h2>
      <p style="color: red;">Error displaying prediction data.</p>
      <p style="color: gray; font-size: 0.8em;">Technical details: ${error.message}</p>
    `;
  }
});
</script>