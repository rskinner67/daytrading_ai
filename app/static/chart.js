document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("chart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
      datasets: [{
        label: "Sample Price",
        data: [148, 152, 150, 153, 155],
        backgroundColor: "rgba(13, 110, 253, 0.2)",
        borderColor: "#0d6efd",
      }]
    }
  });
});