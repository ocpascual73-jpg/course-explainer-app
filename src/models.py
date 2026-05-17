class Course:
    def __init__(self, id, title, description, instructor, duration, topics=None):
        self.id = id
        self.title = title
        self.description = description
        self.instructor = instructor
        self.duration = duration
        self.topics = topics if topics is not None else []

    def __repr__(self):
        return f"<Course {self.title} by {self.instructor}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor,
            "duration": self.duration,
            "topics": self.topics
        }

    @staticmethod
    def get(course_id):
        try:
            # Adjusting for 0-based indexing if IDs are 1-based
            return courses[int(course_id) - 1]
        except (ValueError, IndexError):
            return None

class Video:
    def __init__(self, id, title, url, thumbnail):
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail = thumbnail

    def __repr__(self):
        return f"<Video {self.title}>"

courses = [
    Course(1, "Introduction to Python", "Learn the basics of Python programming.", "John Doe", "4 weeks", ["Variables", "Data Types", "Control Flow", "Functions"]),
    Course(2, "Web Development with Flask", "Build web applications using Flask.", "Jane Smith", "6 weeks", ["Flask Basics", "Templating", "Databases", "REST APIs"]),
    Course(3, "Data Science Fundamentals", "An introduction to data science concepts and tools.", "Alice Johnson", "8 weeks", ["Numpy", "Pandas", "Matplotlib", "Machine Learning Basics"]),
]

videos = [
    Video(1, "Python for Beginners", "https://www.youtube.com/watch?v=bW2bMMdvKHY", "https://img.youtube.com/vi/bW2bMMdvKHY/0.jpg"),
    Video(2, "Flask Web Development", "https://www.youtube.com/watch?v=LuG1hWIAYuk", "https://img.youtube.com/vi/LuG1hWIAYuk/0.jpg"),
    Video(3, "Data Science with Python", "https://www.youtube.com/watch?v=Ep_66a1vqTI", "https://img.youtube.com/vi/Ep_66a1vqTI/0.jpg"),
]