"""
Quick Reference: Using Data Entry Functions
Run examples from here directly
"""

from data_entry import *

# ============================================================
# EXAMPLE 1: VIEW ALL STUDENTS
# ============================================================
print("1. Viewing all students:")
view_all_students()

# ============================================================
# EXAMPLE 2: ADD A NEW STUDENT
# ============================================================
print("2. Adding a new student:")
add_student("John Doe", 22, "Java")
view_all_students()

# ============================================================
# EXAMPLE 3: SEARCH FOR A STUDENT
# ============================================================
print("3. Searching for students named 'Rahul':")
search_student("Rahul")

# ============================================================
# EXAMPLE 4: UPDATE A STUDENT
# ============================================================
print("4. Updating student ID 1:")
update_student(1, name="Neha Sharma", course="Python Advanced")
view_all_students()

# ============================================================
# EXAMPLE 5: DELETE A STUDENT
# ============================================================
print("5. Deleting student (if exists):")
# delete_student(6)  # Uncomment to delete
# view_all_students()

print("\n" + "="*60)
print("All features are working! Edit this file to add/modify data")
print("="*60)
