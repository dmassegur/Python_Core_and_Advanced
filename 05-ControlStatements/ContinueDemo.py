lst = range(1,21,1)

# for i in lst :
#     if i%3==0 :
#         print('%d number skipped' %i)
#         continue
#     else : 
#         print(i)

i=0
while i<20 :
    i += 1
    if i%3==0 :
        print('%d number skipped' %i)
        continue    # skips the rest of the loop statement to the next iteration
    else : 
        print(i)
        
