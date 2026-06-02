"""
Student Management System - Data Entry Module
Allows users to add, update, and delete student records
"""
from db_connection import connect_with_pyodbc, execute_query, execute_update

def add_student(name, age, course):
    """
    Add a new student to the database
    """
    try:
        conn = connect_with_pyodbc()
        if not conn:
            print("Failed to connect to database")
            return False
        
        query = f"INSERT INTO students (name, age, course) VALUES ('{name}', {age}, '{course}')"
        execute_update(conn, query)
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Error adding student: {e}")
        return False

def view_all_students():
    """
    Display all students in the database
    """
    try:
        conn = connect_with_pyodbc()
        if not conn:
            print("Failed to connect to database")
            return
        
        results = execute_query(conn, "SELECT * FROM students ORDER BY id")
        if not results:
            print("No students found in database")
            return
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Course':<25}")
        print("="*60)
        for row in results:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]:<25}")
        print("="*60 + "\n")
        
        conn.close()
    except Exception as e:
        print(f"✗ Error viewing students: {e}")

def update_student(student_id, name=None, age=None, course=None):
    """
    Update student information
    """
    try:
        conn = connect_with_pyodbc()
        if not conn:
            print("Failed to connect to database")
            return False
        
        updates = []
        if name:
            updates.append(f"name = '{name}'")
        if age:
            updates.append(f"age = {age}")
        if course:
            updates.append(f"course = '{course}'")
        
        if not updates:
            print("No updates provided")
            return False
        
        query = f"UPDATE students SET {', '.join(updates)} WHERE id = {student_id}"
        execute_update(conn, query)
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Error updating student: {e}")
        return False

def delete_student(student_id):
    """
    Delete a student from the database
    """
    try:
        conn = connect_with_pyodbc()
        if not conn:
            print("Failed to connect to database")
            return False
        
        query = f"DELETE FROM students WHERE id = {student_id}"
        execute_update(conn, query)
        conn.close()
        return True
    except Exception as e:
        print(f"✗ Error deleting student: {e}")
        return False

def search_student(name):
    """
    Search for a student by name
    """
    try:
        conn = connect_with_pyodbc()
        if not conn:
            print("Failed to connect to database")
            return
        
        query = f"SELECT * FROM students WHERE name LIKE '%{name}%'"
        results = execute_query(conn, query)
        
        if not results:
            print(f"No students found with name containing '{name}'")
            return
        
        print(f"\nSearch Results for '{name}':")
        print("="*60)
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Course':<25}")
        print("="*60)
        for row in results:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]:<25}")
        print("="*60 + "\n")
        
        conn.close()
    except Exception as e:
        print(f"✗ Error searching student: {e}")

def display_menu():
    """
    Display the main menu
    """
    print("\n" + "="*60)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")
    print("="*60)

def main():
    """
    Main menu loop for student management
    """
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                # Add new student
                print("\n--- Add New Student ---")
                name = input("Student name: ").strip()
                if not name:
                    print("✗ Name cannot be empty")
                    continue
                try:
                    age = int(input("Student age: ").strip())
                    course = input("Course name: ").strip()
                    if not course:
                        print("✗ Course cannot be empty")
                        continue
                    
                    if add_student(name, age, course):
                        print(f"✓ Student '{name}' added successfully!\n")
                    else:
                        print("✗ Failed to add student\n")
                except ValueError:
                    print("✗ Please enter a valid age (number)\n")
            
            elif choice == '2':
                # View all students
                print("\n--- All Students ---")
                view_all_students()
            
            elif choice == '3':
                # Search student
                search_name = input("Enter name to search: ").strip()
                if search_name:
                    search_student(search_name)
                else:
                    print("✗ Please enter a name to search\n")
            
            elif choice == '4':
                # Update student
                print("\n--- Update Student ---")
                view_all_students()
                try:
                    student_id = int(input("Student ID to update: ").strip())
                    print("Leave blank to skip a field:")
                    
                    new_name = input("New name: ").strip() or None
                    
                    age_input = input("New age: ").strip()
                    new_age = int(age_input) if age_input else None
                    
                    new_course = input("New course: ").strip() or None
                    
                    if update_student(student_id, new_name, new_age, new_course):
                        print(f"✓ Student ID {student_id} updated successfully!\n")
                    else:
                        print("✗ Failed to update student\n")
                except ValueError:
                    print("✗ Please enter valid information\n")
            
            elif choice == '5':
                # Delete student
                print("\n--- Delete Student ---")
                view_all_students()
                try:
                    student_id = int(input("Student ID to delete: ").strip())
                    confirm = input(f"Delete student ID {student_id}? (yes/no): ").lower()
                    
                    if confirm == 'yes':
                        if delete_student(student_id):
                            print(f"✓ Student ID {student_id} deleted successfully!\n")
                        else:
                            print("✗ Failed to delete student\n")
                    else:
                        print("Deletion cancelled\n")
                except ValueError:
                    print("✗ Please enter a valid Student ID\n")
            
            elif choice == '6':
                print("\nThank you for using Student Management System!")
                break
            
            else:
                print("✗ Invalid choice. Please enter 1-6\n")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"✗ Error: {e}\n")

if __name__ == "__main__":
    main()
