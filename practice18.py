sentence="coding in python is fun"
sum=0
vowels='a','e','i','o','u'
for char in sentence:
    if(char in vowels):
        sum+=1
        print(f"there are {sum} vowels in the sentence")
       

