def most_frequent(str1):
    freq={}
    for a in str1:
        if a in freq:
            freq[a]+= 1
        else:
            freq[a]= 1
    print(str(freq))

most_frequent("Mississipi")
