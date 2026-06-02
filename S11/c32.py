def count_word_frequency(sentence):
    # Your code goes here
    freq=0
    words=sentence.split()
    freq={}
    for word in words:

        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
str=input("enter any string:")
res=count_word_frequency(str)
print(res)



