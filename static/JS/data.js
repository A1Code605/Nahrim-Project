  fetch('/rainfall')
    .then(response => response.json())
    .then(function(data) {
      var labels = data.kedah.map(d => d.date);

      var kedahRainfall = data.kedah.map(d => d.rainfall.toFixed(2));
      var selangorRainfall = data.selangor.map(d => d.rainfall.toFixed(2));
    
      var ctx = document.getElementById('myChart').getContext('2d');
      new Chart(ctx,{
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Kedah (mm)',
              data: kedahRainfall,
              borderColor: 'blue',
              backgroundColor: 'blue',
              fill: false,
              tension:0.1
            },
            {
              label: 'Selangor (mm)',
              data: selangorRainfall,
              borderColor: 'red',
              backgroundColor: 'red',
              fill: false,
              tension: 0.1
            }
          ]
        },
          options: {
            responsive: true,
            plugins: {
              title: {
                display: true,
                text: 'Daily Rainfall - Kedah vs Selangor'
              }
            }
          }
        });
    }); 

fetch('/rainfall/openmeteo')
 .then(response => response.json())
 .then(function(data) {
  var labels = data.kedah.map(d => d.date);
  var kedahRainfall = data.kedah.map(d => d.rainfall.toFixed(2));
  var selangorRainfall = data.selangor.map(d => d.rainfall.toFixed(2));

  var ctx = document.getElementById('openmeteoChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
          {
            label: 'Kedah OpenMeteo (mm)',
            data: kedahRainfall,
            borderColor: '#4a90d9',
            backgroundColor: '#4a90d9'
          },
          {
            label: 'Selangor OpenMeteo (mm)',
            data: selangorRainfall,
            borderColor: '#0d1b3e',
            backgroundColor: '#0d1b3e'
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Daily Rainfall'
          }
        }
      }
  });
 });

fetch('/rainfall/nahrim')
  .then(response => response.json())
 .then(function(data) {
  var labels = data.kedah.map(d => d.date);
  
  var ctx = document.getElementById('nahrimChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
          {
            label: 'Kedah Average RCP',
            data: data.kedah.map(d => d.avg),
            borderColor: '#4a90d9',
            backgroundColor: '#4a90d9'
          },
          {
            label: 'Selangor Average RCP',
            data: data.selangor.map(d => d.avg),
            borderColor: '#0d1b3e',
            backgroundColor: '#0d1b3e'
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Average RCP'
          }
        }
      }
  });
 });

