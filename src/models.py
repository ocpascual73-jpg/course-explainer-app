class Course:
    def __init__(self, title, description, instructor, duration, topics=None):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics or []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

courses = [
    Course(
        "Introduction to Python",
        "Learn the basics of Python programming.",
        "John Doe",
        "4 weeks",
        ["Variables & data types", "Control flow", "Functions", "Modules"],
    ),
    Course(
        "Web Development with Flask",
        "Build web applications using Flask.",
        "Jane Smith",
        "6 weeks",
        ["Routing", "Templates", "Forms", "Deployment"],
    ),
    Course(
        "Data Science Fundamentals",
        "An introduction to data science concepts and tools.",
        "Alice Johnson",
        "8 weeks",
        ["NumPy", "pandas", "Visualization", "Machine learning basics"],
    ),
    Course(
        "Go Programming Language",
        "Learn to build fast, reliable software with Go.",
        "Robert Pike",
        "5 weeks",
        ["Goroutines", "Channels", "Interfaces", "Packages & modules"],
    ),
]

def get_course(course_id):
    """Return the course for a 1-based id, or None if it does not exist."""
    try:
        index = int(course_id) - 1
    except (TypeError, ValueError):
        return None
    if 0 <= index < len(courses):
        return courses[index]
    return None

# Static contact details displayed on the /contact page.
# Placeholder social URLs — update to real handles when available.
CONTACT_INFO = {
    "name": "Course Explainer Team",
    "email": "hello@courseexplainer.com",
    "address": "123 Learning Lane, Suite 400, San Francisco, CA 94105",
    "social_links": [
        {"platform": "Twitter/X", "url": "https://twitter.com/courseexplainer", "icon": "twitter"},
        {"platform": "LinkedIn", "url": "https://linkedin.com/company/courseexplainer", "icon": "linkedin"},
        {"platform": "GitHub", "url": "https://github.com/courseexplainer", "icon": "github"},
    ],
}
