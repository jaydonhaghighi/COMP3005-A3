import psycopg2

# Connect to the PostgreSQL database
conn_params = {
    'dbname': 'test',
    'user': 'haghighi',
    'password': 'postgres',
    'host': 'localhost'
}

def get_connection():
    """Establish a connection to the database."""
    return psycopg2.connect(**conn_params)

def getAllStudents():
    """Retrieves and displays all records from the students table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students;")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """Inserts a new student record into the students table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                   (first_name, last_name, email, enrollment_date))
    conn.commit()
    cursor.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    """Updates the email address for a student with the specified student_id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                   (new_email, student_id))
    conn.commit()
    cursor.close()
    conn.close()

def deleteStudent(student_id):
    """Deletes the record of the student with the specified student_id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    getAllStudents()
    #addStudent('Jaydon', 'Haghighi', 'jaydon.haghighi@carleton.ca', '2024-03-18')
    #updateStudentEmail(1, 'john.doe1@example.com')
    #deleteStudent(3)