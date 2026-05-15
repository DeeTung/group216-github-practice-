from student import add_student, show_students, search_student
from utils import print_menu

def main():
    while True:
        print_menu()
        choice = input("Chon chuc nang: ")

        if choice == "1":
            student_id = input("Nhap ma sinh vien: ")
            name = input("Nhap ten sinh vien: ")
            age = input("Nhap tuoi: ")
            add_student(student_id, name, age)
            print("Them sinh vien thanh cong.")

        elif choice == "2":
            show_students()

        elif choice == "3":
            keyword = input("Nhap ma hoac ten can tim: ")
            search_student(keyword)

        elif choice == "0":
            print("Tam biet!")
            break

        else:
            print("Lua chon khong hop le.")

if __name__ == "__main__":
    main()