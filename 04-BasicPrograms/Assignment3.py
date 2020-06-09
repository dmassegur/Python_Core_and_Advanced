# Program to assign the grading of a student:
import math   #in-built scripts

lst = [int(input('Enter the student ID: '))]
lst.append(input('Enter the student\'s name: ')) 
marks = ([float(m) for m in input('Enter the three student\'s marks Maths, Physics and Chemistry (comma separated!): ').split(',')])
lst.append(marks)

# lst.append(float(m) for m in input('Enter the three student\'s marks Maths, Physics and Chemistry (comma separated!): ').split(','))

# l=input('Enter the three student\'s marks Maths, Physics and Chemistry (comma separated!): ').split(',')
# print(l)
# print(lst)

if (marks[0]>=35 and marks[1]>=35 and marks[2]>=35):
#     avg = (marks[0]+marks[1]+marks[2])/len(marks)
    avg = 0.0
    for i in range(0,len(marks),1) :
#         print(i)  
        avg += marks[i]
    
    avg /= len(marks)
#    print('Student',lst[1],'with ID',lst[0],'has passed the exams with grading:',avg)
    print('Student %s, with ID %d, has passed the exams with grading: %0.2f. Congratulations!' %(lst[1], lst[0], avg))
else :
#    print('Student',lst[1],'with ID',lst[0],'has failed the exams!')
    print('Student %s, with ID %d, has failed the exams!' %(lst[1], lst[0]))
