students = []

def add_student(student_id, name, age):
    student = {
        "id": student_id,
        "name": name,
        "age": age
    }
    students.append(student)

def show_students():
    if not students:
        print("Danh sach sinh vien rong.")
        return

    print("\nDanh sach sinh vien:")
    for student in students:
        print(f"ID: {student['id']} | Ten: {student['name']} | Tuoi: {student['age']}")

# ==== search ==== #
def search_student(keyword):
    found = False

    for student in students:
        if keyword.lower() in student["name"].lower() or keyword == student["id"]:
            print(f"ID: {student['id']} | Ten: {student['name']} | Tuoi: {student['age']}")
            found = True

    if not found:
        print("Khong tim thay sinh vien.")
