---
layout: default
---

<div id="prediction-container">
  <h2>Today's Penguin</h2>
  <p id="loading">Loading latest prediction...</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const predDiv = document.getElementById('prediction-container');
  
  // Update the fetch URL to use the GitHub Pages path
  fetch('/penguin-classifier-1/predictions/latest_prediction.json')
    .then(response => response.json())
    .then(data => {
      predDiv.innerHTML = `
        <h2>Today's Penguin (${data.date})</h2>
        <p><strong>Species:</strong> ${data.prediction}</p>
        <p><strong>Confidence:</strong> ${data.probability.toFixed(2)}%</p>
        <h3>Species Probabilities:</h3>
        <ul>
          <li>Adelie: ${data.species_probabilities.Adelie.toFixed(2)}%</li>
          <li>Chinstrap: ${data.species_probabilities.Chinstrap.toFixed(2)}%</li>
          <li>Gentoo: ${data.species_probabilities.Gentoo.toFixed(2)}%</li>
        </ul>
        <h3>Measurements:</h3>
        <ul>
          <li>Bill Length: ${data.measurements.bill_length_mm.toFixed(2)} mm</li>
          <li>Bill Depth: ${data.measurements.bill_depth_mm.toFixed(2)} mm</li>
          <li>Flipper Length: ${data.measurements.flipper_length_mm.toFixed(2)} mm</li>
          <li>Body Mass: ${data.measurements.body_mass_g.toFixed(2)} g</li>
          <li>Time: ${data.measurements.datetime}</li>
        </ul>
      `;
    })
    .catch(error => {
      console.error('Error:', error);
      predDiv.innerHTML = `
        <h2>Today's Penguin</h2>
        <p style="color: red;">Error loading prediction data. Please try again later.</p>
        <p style="color: gray; font-size: 0.8em;">Technical details: ${error.message}</p>
      `;
    });
});
</script>