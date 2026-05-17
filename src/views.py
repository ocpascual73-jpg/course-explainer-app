from flask import render_template, jsonify
from models import Course, courses, videos

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    course = Course.get(course_id)
    return render_template('course.html', course=course)

def api_course_detail(course_id):
    course = Course.get(course_id)
    if course:
        return jsonify(course.to_dict())
    return jsonify({"error": "Course not found"}), 404

def contact():
    return render_template('contact.html')

def videos_page():
    return render_template('videos.html', videos=videos)