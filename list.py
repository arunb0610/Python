list = [4,1,2,5,3,6,7]
search = int(input('Enter search number :'))
for i in range(0,len(list)):
    if search == list[i]:
        print(str(search)+'Found at Position'+str(i))
    else:
        print('Entered number not found')
