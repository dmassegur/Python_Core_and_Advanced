import pickle
import ClassStudentModule as CS   # the module we have created


f = open('student.dat', 'wb')

s = CS.Student(123,'david',90)   # define object s using class from the impored module
pickle.dump(s,f)   # dumps the object s into the file

f.close()

