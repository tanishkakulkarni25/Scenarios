# Course Management System
class Course:
    def __init__(self, name, duration, fee):
        self.name = name
        self.duration = duration   
        self.fee = fee
        self.category = self.categorize()
    def categorize(self):
        if self.duration >= 6:
            return "Long-Term"
        else:
            return "Short-Term"
    def __str__(self):
        return f"{self.name} - {self.duration} months - ₹{self.fee} ({self.category})"
class Institute:
    def __init__(self, name):
        self.name = name
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
        print(f"Added: {course}")
    def display_courses(self):
        print(f"\nCourses offered at {self.name}:")
        for course in self.courses:
            print(course)
institute = Institute("Tanishka's Institute")
institute.add_course(Course("Python Programming", 3, 10000))
institute.add_course(Course("Data Science", 12, 50000))
institute.add_course(Course("Web Development", 6, 30000))
institute.display_courses()
