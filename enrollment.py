from database import connect_db
class Enrollment:
    def __init__(self, student_id, teacher_id):
        self.student_id = student_id
        self.teacher_id = teacher_id

    def save(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO enrollments (student_id, teacher_id)
        VALUES (?, ?)
        """, (self.student_id, self.teacher_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT students.name, teachers.name
        FROM enrollments
        JOIN students ON enrollments.student_id = students.id
        JOIN teachers ON enrollments.teacher_id = teachers.id
        """)

        result = cursor.fetchall()
        conn.close()
        return result