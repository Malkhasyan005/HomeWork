# 1 Write a program that takes a sentence and creates a dictionary where each word is a key, and the value is the number of times that word appears. Use a sample sentence and break it into words to fill the dictionary. 

#st = input("Enter the sentence: ")
#words = st.split()
#wordcount = {}
#wordcount = wordcount.fromkeys(words, 0)
#for word in words:
#    wordcount[word] += 1
#
#print(wordcount)
#

# 2 Create a dictionary to store student names as keys and their scores as values. Use a few sample names and scores to populate the dictionary. Print out each student’s name and score on a new line.

#st_dict = {
#        "Jack" : 54,
#        "Alice": 90,
#        "Bob": 88,
#        "Charlie": 76,
#        "Martin": 98,
#        "John": 82
#        }
#
#for name in st_dict:
#    print(f"{name}'s score is {st_dict[name]}")

# 3 Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...}). Use this dictionary to convert a list of numbers into words and print each word on a new line.

#numbers_dict = {
#        1 : "one",
#        2 : "two",
#        3 : "three",
#        4 : "four",
#        5 : "five"
#        }
#
#num_list = input("Enter numbers between 1-5: ").split()
#print(num_list)
#
#for num in num_list:
#    if num.isdigit():
#        if int(num) not in numbers_dict:
#            print(f"{num} is not between 1-5")
#        else:
#            print(f"{num} = {numbers_dict[int(num)]}")
#    else:
#        print(f"{num} is not digit")


# 4 Create a dictionary to represent a store’s inventory with items as keys and quantities as values. Print the quantity of a specific item (e.g., "Apples"). Update the quantity of an item and print the dictionary to show the change.

#products = {
#        "Apples": 50,
#        "Bananas": 30,
#        "Oranges": 20,
#        "Grapes": 15 
#        }
#
#for prod in products:
#    print(f"{prod} = {products[prod]}")
#
#ans = input("Enter item name or stop to end up: ")
#while ans != "stop":
#    print(f"{ans} = {products[ans]}")
#    quant = int(input("Enter how many do you want: "))
#    products[ans] -= quant
#    for prod in products:
#        print(f"{prod} = {products[prod]}")
#    ans = input("Enter item name or stop to end up: ")

# 5 Write a program that takes a sentence and uses a set to find all unique words. Print each unique word on a new line.

#words = input("Enter a sentence: ").split()
#unique_words = set(words)
#print(unique_words)

# 6 Given two lists of numbers, use sets to find and print the common elements between them.

#lt1 = input("Enter the numbers: ").split()
#lt2 = input("Enter the numbers: ").split()
#
#st1 = set(lt1)
#st2 = set(lt2)
#
#print(f"The Intersection of this two list is {st1.intersection(st2)}")

# 7 Given a list of numbers, use a set to find any duplicates in the list and print them. You can add numbers to a set one by one and check if they are already present.

#lt = input("Enter numbers: ").split()
#st = set({})
#res = set({})
#
#for num in lt:
#    if num in st:
#        res.add(num)
#    else:
#        st.add(num)
#
#print(res)

# 8 Use a set to create a list of vocabulary words from a paragraph. Break the paragraph into individual words, add each word to the set, and print the final set of unique words.


words = input("Enter the sentence: ").split()
unique_words = set({})

for word in words:
    unique_words.add(word)

print(unique_words)



















