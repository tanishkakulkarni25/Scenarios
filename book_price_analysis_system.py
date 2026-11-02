#Book Price Analysis System
import numpy as np
import pandas as pd
book_prices = np.array([350, 600, 450, 800, 550])
average_price = np.mean(book_prices)
print("Book Prices:", book_prices)
print("Average Book Price: ₹", average_price)
books = {
    "Book": ["Python", "Java", "C++", "Data Science", "AI"],
    "Price": [350, 600, 450, 800, 550]
}
books_df = pd.DataFrame(books)
print("\nBooks DataFrame:")
print(books_df)
students = {
    "RollNo": [101, 102, 103],
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 90, 78]
}
students_df = pd.DataFrame(students)
print("\nStudent Records DataFrame:")
print(students_df)
print("\nBooks Costing More Than ₹500:")
print(books_df[books_df["Price"] > 500])