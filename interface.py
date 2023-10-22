from classes import *
class Interface:
    #validate function is used to check whether valid class and roll numbers are given.
    @staticmethod
    def validate(option):
        c_name = input("\n\tEnter class Name : ").strip()
        #checks whether class is valid or not

        if (len(c_name)!=0 and c_name.isdigit() and int(c_name)>=1 and int(c_name)<=10):
            r_no = input("\tEnter Roll Number : ").strip()
            if (r_no.isdigit()):
                if(option=="1"):
                    School.get_student_details(c_name, r_no)
                elif(option=="3"):
                    School.remove_student(c_name, r_no)
                elif(option=="5"):
                    School.update_student_details(c_name, r_no)
            else:
                print("\tINVALID ROLL NUMBER\n")
                print("\tYOUR REQUEST UNSUCCESSFULL\n\n")
        else:
            print("\tINVALID CLASS\n")
            print("\tYOUR REQUEST UNSUCCESSFULL\n\n")

    @classmethod
    def main(cls):
        print("\n------------------WELCOME TO ",School.school_name.upper()," SCHOOL-------------------\n")
        print("\t1. To get student details")
        print("\t2. To add new student")
        print("\t3. To remove student")
        print("\t4. To update school name")
        print("\t5. To update student details")
        print("\t6. To get number of students in school")
        print("\t7. To get all student details")
        print("\t8. To get any class student details")
        print("\t9. To get Class Teacher Of Class")

        option=input("\n\tEnter any option : ").strip()

        if option=="1":
            cls.validate(option)

        elif option=="2":
            School.add_student()
        elif option=="3":
            print("\n\t-------------------TO REMOVE STUDENT------------------\n")
            print("\tENTER STUDENT DETAILS\n")
            cls.validate(option)

        elif option=="4":
            School.update_school_name()
        elif option=="5":
            print("\n\t---------------------TO UPDATE STUDENT DETAILS---------------------\n")
            print("\tENTER STUDENT DETAILS")
            cls.validate(option)

        elif option=="6":
            School.count_students()
        elif option=="7":
            School.all_student_details()
        elif option=="8":
            c_name=input("\n\tEnter class Name [1,2,3,4,5,6,7,8,9,10] : ").strip()
            if(len(c_name)!=0 and int(c_name)>=1 and int(c_name)<=10):
                School.class_student_details(c_name)
            else:
                print("\tENTER VALID CLASS")
        elif option=="9":
            School.get_class_teacher()
        else:
            print("\t**************ENTER VALID OPTION****************\n")

  # DRIVER CODE

if __name__=="__main__":
    try:
        while(True):
            print("\n\tTO CONTINUE PRESS (y)")
            print("\tTO QUIT PRESS (n)")
            choice=input("\n\tENTER YOUR CHOICE : ")
            if(choice=="y"):
                print()
                Interface.main()
            elif(choice=="n"):
                break
            else:
                print("\tENTER VALID CHOICE...\n")
    # it handles key board interrupt without terminating program abruptly
    except KeyboardInterrupt:
        print("\n\tYOU ABRUPTLY STOPS THE PROGRAM...")