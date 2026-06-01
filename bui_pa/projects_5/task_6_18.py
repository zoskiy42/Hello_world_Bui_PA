import psycopg2
import pandas as pd


conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="example",
    database="testdb"
)


query = """
    SELECT
        s.student_id,
        s.first_name || ' ' || s.last_name AS student_name,
        s.enrollment_year,
        c.course_name,
        e.grade
    FROM enrollments e
    JOIN students s ON e.student_id = s.student_id
    JOIN courses c ON e.course_id = c.course_id
"""

df = pd.read_sql(query, conn)
conn.close()



print("\n" + "=" * 70)
print(" ОБЩАЯ ИНФОРМАЦИЯ О ДАННЫХ")
print("=" * 70)
print(f" Всего оценок в базе:        {len(df)}")
print(f" Уникальных студентов:       {df['student_id'].nunique()}")
print(f" Уникальных курсов:          {df['course_name'].nunique()}")
print(f" Пропущенных значений:       {df['grade'].isna().sum()}")

print("\n" + "=" * 70)
print(" ОПИСАТЕЛЬНАЯ СТАТИСТИКА ПО ОЦЕНКАМ")
print("=" * 70)
desc = df['grade'].describe()
print(f"(mean):      {desc['mean']:.2f}")
print(f"(median):           {desc['50%']:.2f}")
print(f"(std): {desc['std']:.2f}")
print(f" Минимальная оценка:         {desc['min']:.0f}")
print(f" Максимальная оценка:        {desc['max']:.0f}")
print(f" 25% студентов имеют ≤ {desc['25%']:.0f}")
print(f" 75% студентов имеют ≤ {desc['75%']:.0f}")


q1 = df['grade'].quantile(0.25)
q3 = df['grade'].quantile(0.75)
iqr = q3 - q1
print(f"Межквартильный размах (IQR): {iqr}")
print(f"   (разброс центральных 50% оценок)")

print("\n" + "=" * 70)
print(" УСПЕВАЕМОСТЬ ПО ГОДАМ ПОСТУПЛЕНИЯ")
print("=" * 70)
by_year = df.groupby('enrollment_year')['grade'].mean().round(2)
for year, avg in by_year.items():
    print(f"   {year} год → средний балл: {avg}")

best_year = by_year.idxmax()
worst_year = by_year.idxmin()
print(f"\n Лучший год: {best_year} (средний балл {by_year[best_year]})")
print(f"Худший год: {worst_year} (средний балл {by_year[worst_year]})")

print("\n" + "=" * 70)
print(" РЕЙТИНГ КУРСОВ ")
print("=" * 70)
by_course = df.groupby('course_name')['grade'].mean().round(2).sort_values(ascending=False)
for course, avg in by_course.items():
    print(f"   {course:<20} → {avg}")

best_course = by_course.index[0]
worst_course = by_course.index[-1]
print(f"\n Самый лёгкий (или лучший): {best_course} ({by_course[best_course]})")
print(f" Самый сложный (или худший): {worst_course} ({by_course[worst_course]})")

print("\n" + "=" * 70)
print("АНАЛИЗ ЗАВЕРШЁН")
print("=" * 70)