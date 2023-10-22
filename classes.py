class School:
    '''
    school_name,std_dict,count are static variables in Class School.
    school_name holds the name of school.
    count holds the number of students in school.
    std_dict holds the roll number and objects of Classes(One,Two,Three,....Ten) as key value pairs.
    '''
    school_name="ABC"
    std_dict={"1":{},"2":{},"3":{},"4":{},"5":{},"6":{},"7":{},"8":{},"9":{},"10":{}}
    count=0
    def __init__(self,name,age,rno,cls):
        self.name=name
        self.age=age
        self.rno=rno
        self.cls=cls
        # Add the roll number and object as key value pair
        School.std_dict[cls].update({rno:self})
        School.count+=1


    @classmethod
    def get_student_details(cls,c_name,r_no):
        try:
            # obj holds object of Class returned by get_class
            obj=cls.get_class(c_name).list[r_no]
            print("\t\t{0:<28}{1:<27}{2:<28}{3:<28}".format("Roll Number","NAME","CLass","Age"))
            print("_"*100)
            print("\t\t{0:<28}{1:<28}{2:<28}{3:<28}".format(obj.rno, obj.name, obj.cls,obj.age))
            print()
        except Exception:
            print("\n\tSTUDENT DOESN'T EXIST\n")

    '''
    validate_student_details() method checks the details of student to be added are in the valid format.
    '''
    @staticmethod
    def validate_student_details():
        class_name = input("\tEnter Student class : ").strip()
        if(not(len(class_name)!=0 and class_name.isdigit() and int(class_name)>=1 and int(class_name)<=10)):
            print("\n\tINVALID CLASS")
            return tuple()
        rno = input("\tEnter Student rno : ").strip()
        if(not(len(rno)>0 and rno.isdigit())):
            print("\n\tINVALID ROLL NUMBER\n")
            return tuple()
        name = input("\tEnter Student Name(only alphabets) : ")
        if(not name.isalpha()):
            print("\n\tINVALID NAME")
            return tuple()
        print("\tEnter Student Age valid(",int(class_name)+5,"-",int(class_name)+7,") : ",end="")
        age = input().strip()
        if(not(age.isdigit() and int(age)>=int(class_name)+5 and int(age)<=int(class_name)+7)):
            print("AGE NOT SUPPORTED FOR CLASS ",class_name)
            return tuple()
        # returns tuple of student details if they satisfy valid criteria
        return tuple([class_name,rno,name,age])

    '''
    add_student() method calls the constructor of a class based on the class name of student to be added.
    '''
    @classmethod
    def add_student(cls):
        print("\n\n--------------------TO ADD STUDENT----------------------")
        print("\tENTER THE DETAILS\n")
        details=cls.validate_student_details()
        if(len(details)==0):
            print("\n\tSTUDENT NOT ADDED\n")

        else:
            class_name,rno,name,age=details
            obj=None
            if rno not in cls.std_dict[class_name].keys():
                if(class_name=="1"):
                    obj=One(name,age,rno,class_name)
                elif (class_name == "2"):
                    obj = Two(name, age, rno, class_name)
                elif (class_name == "3"):
                    obj = Three(name, age, rno, class_name)
                elif (class_name == "4"):
                    obj = Four(name, age, rno, class_name)
                elif (class_name == "5"):
                    obj = Five(name, age, rno, class_name)
                elif (class_name == "6"):
                    obj = Six(name, age, rno, class_name)
                elif (class_name == "7"):
                    obj = Seven(name, age, rno, class_name)
                elif (class_name == "8"):
                    obj = Eight(name, age, rno, class_name)
                elif (class_name == "9"):
                    obj = Nine(name, age, rno, class_name)
                elif (class_name == "10"):
                    obj = Ten(name, age, rno, class_name)
                print("\n\tSTUDENT ADDED SUCCESSFULLY\n")

                # After adding it prints details of student that get added
                cls.get_student_details(obj.cls, obj.rno)
            else:
                print("\nSTUDENT WITH ROLL NUMBER-", rno, " ALREADY EXISTS IN CLASS-", class_name, "\n")

    @classmethod
    def remove_student(cls,c_name,r_no):
        try:
            obj=cls.std_dict[c_name].pop(r_no)
            c=cls.get_class(c_name)
            c.list.pop(r_no)
            c.count=c.count-1
            cls.count-=1
            del obj
            print("\n\tSTUDENT REMOVED SUCCESSFULLY\n")
        except:
            print("\n\tSTUDENT DOESN'T EXIST\n")

    @classmethod
    def update_school_name(cls):
        print("\tChange School Name from ",cls.school_name," to : ",end="")
        x=input().strip()
        if(len(x)!=0 and x.isalpha()):
            cls.school_name=x
            print("\tSCHOOL NAME CHANGED")
        else:
            print("\tINVALID SCHOOL NAME\n")
            print("\n\tYOUR REQUEST UNSUCCESSFULL\n")

    @classmethod
    def update_student_details(cls, c_name, r_no):
        try:
            obj = cls.std_dict[c_name][r_no]
            print("\t1. Change Student Name")
            print("\t2. Change Student Class")
            print(("\t3. Change Student Age"))

            option = input("\n\tEnter an Option : ")
            if (option == "1"):
                cls.change_sname(obj)
            elif (option == "2"):
                cls.change_sclass(obj)
            elif (option == "3"):
                cls.change_sage(obj)
            else:
                print(("\tINVALID OPTION\n"))
        except:
            print("\n\tSTUDENT DOESN'T EXIST\n")
    @classmethod
    def change_sname(cls,obj):
        name=input("\tEnter New Name(contains only alphabets) : ")
        if(len(name)>0 and name.isalpha()):
            obj.name=name
            print("\tNAME UPDATED SUCCESSFULLY!")
            print("\n\tTHE UPDATED STUDENT DETAILS ARE ")
            cls.get_student_details(obj.cls,obj.rno)
        else:
            print("\n\tINVALID NAME")
            print("\n\tNAME CAN'T UPDATED\n")
    @classmethod
    def change_sclass(cls,obj):
        t=input("\n\tEnter New Class : ").strip()
        rno=input("\tEnter New Roll Number : ").strip()
        name=obj.name
        obj1=None
        if(rno.isdigit() and len(t)!=0 and t.isdigit() and int(t)>=1 and int(t)<=10):
            print("\n\tEnter Student Age valid(", int(t) + 5, "-", int(t) + 7, ") : ")
            age = input("\tEnter New Age : ").strip()
            if(age.isdigit() and int(age)>=int(t)+5 and int(age)<=int(t)+7):
                # it holds new class
                c1=cls.get_class(t)
                # it holds old class
                c2=cls.get_class(obj.cls)
                # it holds old roll number
                r_no=obj.rno
                c=obj.cls
                if(rno not in c1.list.keys()):
                    if (t == "1"):
                        obj1 = One(name, age, rno, t)
                    elif (t == "2"):
                        obj1 = Two(name, age, rno, t)
                    elif (t == "3"):
                        obj1 = Three(name, age, rno, t)
                    elif (t == "4"):
                        obj1 = Four(name, age, rno, t)
                    elif (t == "5"):
                        obj1 = Five(name, age, rno, t)
                    elif (t == "6"):
                        obj1 = Six(name, age, rno, t)
                    elif (t == "7"):
                        obj1 = Seven(name, age, rno, t)
                    elif (t == "8"):
                        obj1 = Eight(name, age, rno, t)
                    elif (t == "9"):
                        obj1 = Nine(name, age, rno, t)
                    elif (t == "10"):
                        obj1 = Ten(name, age, rno, t)

                    cls.std_dict[c].pop(r_no)
                    cls.count-=1
                    c2.list.pop(r_no)
                    c2.count=c2.count-1
                    print("\tCLASS UPDATE SUCCESSFULLY!")

                    del obj
                else:
                    print("\n\tSTUDENT WITH ROLL NUMBER-",obj.rno," IS ALREADY EXISTS IN CLASS-",t)
            else:
                print("\n\tAGE DOESN'T SUPPORT FOR NEW CLASS")
        else:
            print("\n\tCLASS CAN'T UPDATED")
    @classmethod
    def change_sage(cls,obj):
        t=input("\tEnter New Age : ").strip()
        if(len(t)>0 and t.isdigit ()and int(t)>=int(obj.cls)+5 and int(t)<=int(obj.cls)+7):
            obj.age=t
            print("\tAGE UPDATED SUCCESSFULLY!")
            print("\n\tTHE UPDATED STUDENT DETAILS ARE")
            cls.get_student_details(obj.cls,obj.rno)
        else:
            print("\n\tAGE CAN'T UPDATED")



    @classmethod
    def count_students(cls):
        print("\n\tNUMBER OF STUDENTS IN SCHOOL : ",cls.count)
        print()
        for i in range(1,11):
            t=cls.get_class(str(i))
            print("\tNUMBER OF STUDENTS IN CLASS ",i," : ",t.count)


    @classmethod
    def all_student_details(cls):
        for i in range(1,11):
            # l holds list of student objects of class i
            l=list(cls.std_dict[str(i)].values())
            # it sorts list l on basis of roll number
            l.sort(key=lambda i:i.rno)
            print("\n\n")
            if(len(l)!=0):
                print("\t---------------------------THE STUDENTS DETAILS OF CLASS ",i,"-------------------------------")
                print("\t\t{0:<28}{1:<27}{2:<28}{3:<28}".format("Roll Number", "NAME", "CLass", "Age"))
                print("_" * 100,"\n")
                for j in l:
                    print("\t\t{0:<28}{1:<28}{2:<28}{3:<28}".format(j.rno, j.name, j.cls, j.age))
            elif(len(l)==0):
                print("\n\t********************************** NO STUDENTS IN CLASS ",i," ****************************************")
    @classmethod
    def class_student_details(cls,c_name):
        l = list(cls.get_class(c_name).list.values())
        l.sort(key=lambda i:i.rno)
        print("\t\t{0:<28}{1:<27}{2:<28}{3:<28}".format("Roll Number", "NAME", "CLass", "Age"))
        print("_" * 100, "\n")
        for j in l:
            print("\t\t{0:<28}{1:<28}{2:<28}{3:<28}".format(j.rno, j.name, j.cls, j.age))

    @classmethod
    def get_class_teacher(cls):
        x=input("\tEnter Class : ").strip()
        if(x.isdigit() and int(x)>=1 and int(x)<=10):
            c_name=cls.get_class(x)
            print("\n\tTHE CLASS TEACHER OF CLASS ",x," IS : ",c_name.class_teacher)
            print("\n")
        else:
            print("\n\tENTER VALID CLASS")

    @staticmethod
    def get_class(c_name):
        l=[One,Two,Three,Four,Five,Six,Seven,Eight,Nine,Ten]
        return l[int(c_name)-1]
class One(School):
    class_teacher="Teacher1"
    count=0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        One.count+=1
        One.list[rno]=self

class Two(School):
    class_teacher="Teacher2"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Two.count+=1
        Two.list[rno] = self

class Three(School):
    class_teacher="Teacher3"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Three.count+=1
        Three.list[rno] = self

class Four(School):
    class_teacher="Teacher4"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Four.count+=1
        Four.list[rno] = self

class Five(School):
    class_teacher="Teacher5"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Five.count+=1
        Five.list[rno] = self

class Six(School):
    class_teacher="Teacher6"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Six.count+=1
        Six.list[rno] = self

class Seven(School):
    class_teacher="Teacher7"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Seven.count+=1
        Seven.list[rno] = self

class Eight(School):
    class_teacher="Teacher8"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Eight.count+=1
        Eight.list[rno] = self
class Nine(School):
    class_teacher="Teacher9"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Nine.count+=1
        Nine.list[rno] = self

class Ten(School):
    class_teacher="Teacher10"
    count = 0
    list={}
    def __init__(self,name,age,rno,cls):
        School.__init__(self, name, age, rno, cls)
        Ten.count+=1
        Ten.list[rno] = self