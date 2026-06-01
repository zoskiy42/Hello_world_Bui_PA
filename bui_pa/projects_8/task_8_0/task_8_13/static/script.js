const resultArea = document.getElementById('result-area');

function showLoading() {
    resultArea.innerHTML = '<div class="loading">⏳ Загрузка... Пожалуйста, подождите</div>';
}

function showError(message) {
    resultArea.innerHTML = `<div class="error-message">❌ Ошибка: ${message}</div>`;
}

function showStat(value, metric) {
    resultArea.innerHTML = `
        <div class="stat-value">${value}</div>
        <div class="stat-label">${metric}</div>
    `;
}

function showChart(base64Image, type) {
    resultArea.innerHTML = `
        <div class="chart-container">
            <img src="data:image/png;base64,${base64Image}" alt="График ${type}">
        </div>
    `;
}

function clearResult() {
    resultArea.innerHTML = '<div class="placeholder">✨ Здесь появится результат ✨</div>';
}

async function fetchStat(endpoint, metricName) {
    showLoading();
    try {
        const response = await fetch(`/api/metric/${endpoint}`);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        showStat(data.value, data.metric || metricName);
    } catch (error) {
        showError(error.message);
    }
}

async function fetchChart(endpoint, chartType) {
    showLoading();
    try {
        const response = await fetch(`/api/chart/${endpoint}`);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const data = await response.json();
        if (data.image) {
            showChart(data.image, chartType);
        } else {
            throw new Error('Не удалось загрузить график');
        }
    } catch (error) {
        showError(error.message);
    }
}

// Обработчики кнопок
document.querySelectorAll('.stat-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const action = btn.getAttribute('data-action');
        const metricNames = {
            mean: 'Средний балл',
            median: 'Медиана',
            count: 'Количество оценок',
            min: 'Минимум',
            max: 'Максимум'
        };
        fetchStat(action, metricNames[action]);
    });
});

document.querySelectorAll('.chart-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const action = btn.getAttribute('data-action');
        fetchChart(action, action);
    });
});

document.querySelector('.clear-btn').addEventListener('click', clearResult);