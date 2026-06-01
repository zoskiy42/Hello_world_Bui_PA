from flask import Flask, render_template, jsonify, send_file
from sqlalchemy import create_engine, text
import pandas as pd
import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

# Подключение к базе данных student_task (замените на свои параметры)
# Пример для PostgreSQL:
# engine = create_engine('postgresql://user:password@localhost/student_task')
# Для SQLite (для тестирования):
engine = create_engine('sqlite:///student_task.db')

def get_data(query):
    """Выполняет SQL-запрос и возвращает DataFrame"""
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)

# ==================== СТАТИСТИЧЕСКИЕ МЕТРИКИ ====================

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/api/metric/mean')
def api_mean():
    """Средний балл по всем оценкам"""
    df = get_data("SELECT grade FROM student_grades")
    mean_val = df['grade'].mean()
    return jsonify({'value': round(mean_val, 2), 'metric': 'Средний балл'})

@app.route('/api/metric/median')
def api_median():
    """Медиана оценок"""
    df = get_data("SELECT grade FROM student_grades")
    median_val = df['grade'].median()
    return jsonify({'value': round(median_val, 2), 'metric': 'Медиана'})

@app.route('/api/metric/count')
def api_count():
    """Количество записей"""
    df = get_data("SELECT grade FROM student_grades")
    return jsonify({'value': len(df), 'metric': 'Количество оценок'})

@app.route('/api/metric/min')
def api_min():
    """Минимальная оценка"""
    df = get_data("SELECT grade FROM student_grades")
    return jsonify({'value': df['grade'].min(), 'metric': 'Минимум'})

@app.route('/api/metric/max')
def api_max():
    """Максимальная оценка"""
    df = get_data("SELECT grade FROM student_grades")
    return jsonify({'value': df['grade'].max(), 'metric': 'Максимум'})

# ==================== ГРАФИКИ ====================

def create_histogram():
    """Гистограмма распределения оценок с медианой"""
    df = get_data("SELECT grade FROM student_grades")
    grades = df['grade'].dropna()
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(grades, bins=10, edgecolor='black', alpha=0.7, color='steelblue')
    
    median_val = grades.median()
    mean_val = grades.mean()
    
    ax.axvline(median_val, color='red', linestyle='--', linewidth=2, label=f'Медиана = {median_val:.2f}')
    ax.axvline(mean_val, color='green', linestyle=':', linewidth=2, label=f'Среднее = {mean_val:.2f}')
    
    ax.set_xlabel('Оценка')
    ax.set_ylabel('Частота')
    ax.set_title('Распределение оценок студентов')
    ax.legend()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return base64.b64encode(buf.getvalue()).decode('utf-8')

@app.route('/api/chart/histogram')
def api_histogram():
    img_base64 = create_histogram()
    return jsonify({'image': img_base64, 'type': 'histogram'})

def create_bar_chart():
    """Столбчатая диаграмма: средний балл по предметам"""
    query = """
        SELECT subject, AVG(grade) as avg_grade 
        FROM student_grades 
        GROUP BY subject 
        ORDER BY avg_grade DESC
    """
    df = get_data(query)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(df['subject'], df['avg_grade'], color='coral', edgecolor='black')
    
    # Добавляем значения на столбцы
    for bar, val in zip(bars, df['avg_grade']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                f'{val:.2f}', ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Предмет')
    ax.set_ylabel('Средний балл')
    ax.set_title('Средний балл по предметам')
    ax.set_ylim(0, 5.5)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return base64.b64encode(buf.getvalue()).decode('utf-8')

@app.route('/api/chart/barchart')
def api_barchart():
    img_base64 = create_bar_chart()
    return jsonify({'image': img_base64, 'type': 'barchart'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)