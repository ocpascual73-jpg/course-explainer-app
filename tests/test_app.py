import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app
from models import courses

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Course Details', response.data)

    def test_course_renders_course_data(self):
        # Regression test: the course detail page must receive the course
        # object and render its fields (previously raised UndefinedError).
        first = courses[0]
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(first.title.encode(), response.data)
        self.assertIn(first.description.encode(), response.data)
        self.assertIn(first.instructor.encode(), response.data)
        self.assertIn(first.duration.encode(), response.data)
        for topic in first.topics:
            self.assertIn(topic.encode(), response.data)

    def test_unknown_course_returns_404(self):
        response = self.app.get('/course/999')
        self.assertEqual(response.status_code, 404)

    def test_non_numeric_course_returns_404(self):
        response = self.app.get('/course/abc')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
