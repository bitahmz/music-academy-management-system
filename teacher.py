from database import connect_db

class Teacher:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def save(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO teachers (name, instrument)
        VALUES (?, ?)
        """, (self.name, self.instrument))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM teachers")
        teachers = cursor.fetchall()

        conn.close()
        return teachers