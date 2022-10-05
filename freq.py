count_str = input("Enter a string :")
all_freq = {}
for i in count_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters in", count_str ,"is :" , str(all_freq))
