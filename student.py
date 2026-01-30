from database import connect_db
class Student:
    def __init__(self, name, phone, instrument):
        self.name = name
        self.phone = phone
        self.instrument = instrument

    def save(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (name, phone, instrument)
        VALUES (?, ?, ?)
        """, (self.name, self.phone, self.instrument))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        conn.close()
        return students