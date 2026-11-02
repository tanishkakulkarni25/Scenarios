#Course Fee Analysis System
import numpy as np
import pandas as pd
course_fees = np.array([20000, 30000, 25000, 40000, 35000])
average_fee = np.mean(course_fees)
maximum_fee = np.max(course_fees)
minimum_fee = np.min(course_fees)
print("Course Fees:", course_fees)
print("Average Fee:", average_fee)
print("Maximum Fee:", maximum_fee)
print("Minimum Fee:", minimum_fee)
courses = {
    "Course": ["Python", "Data Science", "Java", "AI", "Machine Learning"],
    "Fee": [20000, 30000, 25000, 40000, 35000]
}
df = pd.DataFrame(courses)
print("\nCourse DataFrame:")
print(df)
print("\nCourses with Fee Greater Than ₹25,000:")
print(df[df["Fee"] > 25000])