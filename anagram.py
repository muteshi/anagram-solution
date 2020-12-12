def create_dictionary():
    """
    Creates a dictionary from text file
    """
    anagram_dict={}
    with open("dictionary.txt") as my_dict:
        for line in my_dict:
            # Strip newlines, convert to list then sort the string
            line = sorted(list(line.rstrip()))
            word = "".join(line) # Re create the string from the list
            # if word in dictionary increment its count
            if word in anagram_dict:
                anagram_dict[word] += 1
            else:
                anagram_dict[word] = 1

        return anagram_dict


def anagram():
    """
    Returns the number of times a string appears in a dictionary
    """

    anagram_list = []
    str_count ={}
    anagram_dict=create_dictionary()
    with open("anagram.txt") as my_anagram:
        for line in my_anagram:
            line = sorted(list(line.rstrip()))
            anagram_list.append("".join(line))
    anagram_list=  anagram_list[1:]

    for str in anagram_list:
        if str in anagram_dict:
            str_count[str] = anagram_dict[str]


    return str_count.values()
    
 
counts = anagram()
for count in counts:
    # subtract 1 since the word itself not included
    print(count-1, end=' ')



        
    
        

       



