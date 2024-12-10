from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


def connect_to_db():
    connection = mysql.connector.connect(
        host="database-1.czyuyw2i077t.us-east-1.rds.amazonaws.com",
        database="Courses_DB",
        user="admin",
        password="malika88"
    )
    return connection


@app.route('/')
def courses_table():
    database = connect_to_db()
    cursor = database.cursor()
    cursor.execute('SELECT id,course, description, week_day, time, instructor, level FROM courses;')
    courses = cursor.fetchall()

    courses_dict = [
        {
            "id": course[0],
            "course": course[1],
            "description": course[2],
            "week_day": course[3],
            "time": course[4],
            "instructor": course[5],
            "level": course[6]
        }
        for course in courses
    ]

    cursor.close()
    database.close()
    return render_template('table.html', courses=courses_dict)


@app.route('/course/<int:course_id>')
def course_detail(course_id):
    database = connect_to_db()
    cursor = database.cursor()

    cursor.execute('SELECT id,course, description, week_day, time, instructor, level FROM courses WHERE id = %s;',
                   (course_id,))
    course = cursor.fetchone()

    cursor.execute('SELECT description FROM description WHERE id = %s;', (course_id,))
    description = cursor.fetchone()

    cursor.close()
    database.close()

    if not course or not description:
        return "There is no such course"

    course_dict = {
        "id": course[0],
        "course": course[1],
        "description": course[2],
        "week_day": course[3],
        "time": course[4],
        "instructor": course[5],
        "level": course[6]
    }

    description_dict = {
        "description": description[0]
    }

    return render_template('course_detail.html', course=course_dict, description=description_dict)


@app.route('/sort/<order>')
def sort_button(order):
    database = connect_to_db()
    cursor = database.cursor()

    if order == 'asc':
        cursor.execute(
            'SELECT id, course, description, week_day, time, instructor, level FROM courses ORDER BY level ASC;')

    courses = cursor.fetchall()

    courses_dict = [
        {
            "id": course[0],
            "course": course[1],
            "description": course[2],
            "week_day": course[3],
            "time": course[4],
            "instructor": course[5],
            "level": course[6]
        }
        for course in courses
    ]

    cursor.close()
    database.close()
    return render_template('table.html', courses=courses_dict)


@app.route('/reset')
def reset_button():
    database = connect_to_db()
    cursor = database.cursor()

    cursor.execute('SELECT id, course, description, week_day, time, instructor, level FROM courses;')
    courses = cursor.fetchall()

    courses_dict = [
        {
            "id": course[0],
            "course": course[1],
            "description": course[2],
            "week_day": course[3],
            "time": course[4],
            "instructor": course[5],
            "level": course[6]
        }
        for course in courses
    ]

    cursor.close()
    database.close()
    return render_template('table.html', courses=courses_dict)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
