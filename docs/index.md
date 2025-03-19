---
layout: default
---

<div id="prediction-container">
  <h2>Today's Penguin</h2>
  <p id="loading">Loading latest prediction...</p>
</div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
    $.getJSON('https://raw.githubusercontent.com/Markushenriksson13/penguin-classifier-1/main/predictions/latest_prediction.json')
        .done(function(data) {
            $('#prediction-container').html(`
                <h2>Today's Penguin (${data.date})</h2>
                <p><strong>Species:</strong> ${data.prediction}</p>
                <p><strong>Confidence:</strong> ${data.probability.toFixed(2)}%</p>
                <h3>Measurements:</h3>
                <ul>
                    <li>Bill Length: ${data.measurements.bill_length_mm} mm</li>
                    <li>Bill Depth: ${data.measurements.bill_depth_mm} mm</li>
                    <li>Flipper Length: ${data.measurements.flipper_length_mm} mm</li>
                    <li>Body Mass: ${data.measurements.body_mass_g} g</li>
                </ul>
            `);
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            $('#prediction-container').html(`
                <h2>Today's Penguin</h2>
                <p style="color: red;">Error loading prediction data. Please try again later.</p>
            `);
        });
});
</script>