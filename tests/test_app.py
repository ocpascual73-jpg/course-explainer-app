import unittest
import sys
import os
from markupsafe import escape

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

    def test_index_lists_course_titles(self):
        # The home page links must show each course's title, not "Course 1/2/3".
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'>Course 1<', response.data)
        for course in courses:
            self.assertIn(course.title.encode(), response.data)

    def test_go_course_present(self):
        response = self.app.get('/')
        self.assertIn(b'Go Programming Language', response.data)
        last = self.app.get('/course/{}'.format(len(courses)))
        self.assertEqual(last.status_code, 200)
        self.assertIn(b'Go Programming Language', last.data)

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
        # Jinja2 autoescapes output, so compare against the escaped form
        # (e.g. "Variables & data types" renders as "Variables &amp; data types").
        self.assertIn(str(escape(first.title)).encode(), response.data)
        self.assertIn(str(escape(first.description)).encode(), response.data)
        self.assertIn(str(escape(first.instructor)).encode(), response.data)
        self.assertIn(str(escape(first.duration)).encode(), response.data)
        for topic in first.topics:
            self.assertIn(str(escape(topic)).encode(), response.data)

    def test_contact_status_200(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_heading(self):
        response = self.app.get('/contact')
        self.assertIn(b'Contact Us', response.data)

    def test_contact_name(self):
        response = self.app.get('/contact')
        self.assertIn(b'Course Explainer Team', response.data)

    def test_contact_email_link(self):
        response = self.app.get('/contact')
        self.assertIn(b'mailto:hello@courseexplainer.com', response.data)

    def test_contact_address(self):
        response = self.app.get('/contact')
        self.assertIn(b'123 Learning Lane', response.data)

    def test_contact_social_links(self):
        response = self.app.get('/contact')
        self.assertIn(b'twitter.com', response.data)
        self.assertIn(b'linkedin.com', response.data)
        self.assertIn(b'github.com', response.data)

    def test_contact_link_in_nav(self):
        # The Contact link should appear in the global nav on every page.
        response = self.app.get('/')
        self.assertIn(b'/contact', response.data)

    def test_unknown_course_returns_404(self):
        response = self.app.get('/course/999')
        self.assertEqual(response.status_code, 404)

    def test_non_numeric_course_returns_404(self):
        response = self.app.get('/course/abc')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
