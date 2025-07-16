document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("weeklyChart").getContext("2d"); //

  const weeklyChart = new Chart(ctx, { //
    type: "line", //
    data: { //
      labels: window.weeklyLabels, //
      datasets: [ //
        {
          label: "Calories Consumed", //
          data: window.weeklyData, //
          borderColor: "rgba(75, 192, 192, 1)", //
          fill: true, //
          backgroundColor: "rgba(75, 192, 192, 0.2)", //
          tension: 0.4, //
        },
      ],
    },
    options: { //
      responsive: true, //
      scales: { //
        y: { //
          beginAtZero: true, //
        },
      },
    },
  });
});