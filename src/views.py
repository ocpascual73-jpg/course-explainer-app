from flask import render_template, abort
from models import get_course, courses

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    selected_course = get_course(course_id)
    if selected_course is None:
        abort(404)
    return render_template('course.html', course=selected_course, course_id=course_id)
