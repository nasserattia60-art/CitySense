document.addEventListener('DOMContentLoaded', () => {
    const chartsData = {
        'chart-safety': {{ report.safety_score }
},
    'chart-noise': {{ report.noise_level }},
    'chart-rent': {{ report.rent_level }},
    'chart-water': {{ report.water_quality }},
    'chart-ai': {{ report.ai_score }},
    };

Object.keys(chartsData).forEach(id => {
    const ctx = document.getElementById(id);
    if (!ctx) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Value', 'Remaining'],
            datasets: [{
                data: [chartsData[id], 100 - chartsData[id]],
                backgroundColor: ['var(--primary-color, #3498db)', 'rgba(200,200,200,0.3)'],
                borderWidth: 0
            }]
        },
        options: {
            cutout: '70%',
            plugins: { legend: { display: false } },
            responsive: true,
            maintainAspectRatio: false
        }
    });
});
});
