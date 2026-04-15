"""Find if any string in a list contain whitespaces using Regex"""
import re

def regex1():
    li1 = ["Geeks forgeeks", "Regex", "Python"]
    # Check if any of the items in a list are True
    res = [x.group() if x is not None else None for x in [re.search(r'\s', i) for i in li1]]
    print(res)

    res1 = any([bool(re.search(r"\s", i)) for i in li1]) 
    print(res1)
#regex1()

def search_regex():
    original_string = "Hello and welcome to Bangalore Bangalore"
    search_word = "Bangalore"
    found = re.search(search_word, original_string)
    print(found)
    print(f"Word '{search_word}' is present in '{original_string}' at start index {found.start()} and ends at {found.end()}")
    print(found.group())        #Getting matched substring

#search_regex()

def findall_regex():    # Returns List of all matched pattern
    original_string = "Lello and welcome to Bangalore"
    pattern = "l"
    found = re.findall(pattern, original_string,flags=re.IGNORECASE)
    print(found)

    found1 = re.finditer(r'[A-Z]+', original_string)
    for x in found1:
        print(x)

#findall_regex()

def substitute_regex():
    original_string = "Hello and welcome to Bangalore"
    subs = re.sub('l','H', original_string, flags=re.IGNORECASE) #, count=1)
    print(subs)

substitute_regex()

''' Encora Interview Round 1 :
Write a function to reverse words in the sentence.
Reverse the words only.
Dots, spaces and commas should remain as it is.
Words will contain aA to zZ characters only and will not contain anything else.
Delimiters are only dots, spaces and commas.
Delimiters themselves are not the constituents of the word.
For example:
Input (String): My, name. is Basavaraj
Output (String): yM, eman. si jaravasaB
Input (String): yM, eman, si. rmI.na. hK,na
Output (String): My, name, is. Imr.an. Kh,an
'''
import re

def rev_words(input):
    rev_str = ""

    words = re.findall(r"[A-Za-z]+", input, flags=re.IGNORECASE)
    print(words)

    wl = 0
    i = 0
    while(wl < len(words)):
        #print(i)
        if(re.match("\W+",input[i])):
            #print(input1[i])
            rev_str += input[i]
            i += 1
        else:
            rev_str += str(words[wl])[::-1]
            i += len(words[wl])
            wl += 1

    print(rev_str)

input1 = "My, name. is Basavaraj"
input2 = "yM, e,man, si. rm,I.na. h_Kn.a"
rev_words(input1)


'''
HCLTech : Print the orderid and total
'''
import re

str1 = "Order#12-Total:78.5$"

result1 = re.findall(r'Order#(\d+)',str1)
result2 = re.findall(r'Total:(\d+.\d+)',str1)
print(result1, result2)


# Hackerrank test
'''110000 : (0, 0) and (0, 0) are two alternating digit pairs, index (2,4) and (2,5). Hence, it is an invalid postal code.'''
