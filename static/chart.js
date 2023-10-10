// chart.js

// Use the data passed from the HTML template
const ctx = document.getElementById('chart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Correct', 'Incorrect'],
        datasets: [{
            data: [correctCount, incorrectCount],
            backgroundColor: ['#81c784', '#e57373'],
        }],
    },
    options: {
        responsive: false, // Disable automatic chart resizing
        maintainAspectRatio: false, // Disable aspect ratio maintenance
        plugins: {
            legend: {
                display: true,
                position: 'bottom',
                labels: {
                    font: {
                        size: 12, // Adjust font size as needed
                    },
                },
            },
        },
        layout: {
            padding: {
                left: 10, // Adjust padding as needed
                right: 10,
                top: 10,
                bottom: 10,
            },
        },
    },
});
