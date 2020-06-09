import pickle
import ClassStudentModule # not sure why this is not necessary


f = open('student.dat','rb')

obj = pickle.load(f)  ## reads the object info from the file
obj.display()  ## displays the object info (defined in class module)

f.close()