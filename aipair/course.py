import sqlite3

class CourseDB:
    def __init__(self, db_name="courses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            fee REAL NOT NULL,
            duration INTEGER NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_course(self, title, fee, duration):
        query = "INSERT INTO Courses (title, fee, duration) VALUES (?, ?, ?)"
        self.conn.execute(query, (title, fee, duration))
        self.conn.commit()

    def delete_course(self, course_id):
        query = "DELETE FROM Courses WHERE id = ?"
        self.conn.execute(query, (course_id,))
        self.conn.commit()

    def update_course(self, course_id, title=None, fee=None, duration=None):
        fields = []
        params = []
        if title is not None:
            fields.append("title = ?")
            params.append(title)
        if fee is not None:
            fields.append("fee = ?")
            params.append(fee)
        if duration is not None:
            fields.append("duration = ?")
            params.append(duration)
        params.append(course_id)
        query = f"UPDATE Courses SET {', '.join(fields)} WHERE id = ?"
        self.conn.execute(query, params)
        self.conn.commit()

    def select_courses(self):
        query = "SELECT id, title, fee, duration FROM Courses"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_aggregate(self):
        query = """
        SELECT 
            COUNT(*) as total_courses,
            AVG(fee) as avg_fee,
            SUM(fee) as total_fee,
            MAX(duration) as max_duration,
            MIN(duration) as min_duration
        FROM Courses
        """
        cursor = self.conn.execute(query)
        return cursor.fetchone()

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db = CourseDB()

    # Insert sample courses
    db.insert_course("Python Basics", 100.0, 30)
    db.insert_course("Data Science", 200.0, 45)

    # Update a course
    db.update_course(1, fee=120.0)

    # Delete a course
    db.delete_course(2)

    # Select all courses
    courses = db.select_courses()
    print("Courses:", courses)

    # Get aggregates
    aggregates = db.get_aggregate()
    print("Aggregates:", aggregates)

    db.close()