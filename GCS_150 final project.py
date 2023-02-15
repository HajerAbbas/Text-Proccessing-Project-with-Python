
##################################################
#################################################
# File Creator: Hajer Abbas
# Date: Dec 12th, 2020
# Project: Text processing








def main():
    print('WELCOME to user survice')

    repeat = 1 
    while repeat == 1:
        f = input('Please Enter the name of the file that contains the student names:')
        try:
            content = open(f).read().splitlines()
        except:
            print('Please enter a valid file name')
            continue
        print('The names of the students are:', content)    
        print(' \nMENUE:\n 1.Remove a name\n 2.Add a name\n 3.Add new line between each two names\n 4.Remove occurence of a name\n 5.Remove occurence except the first one\n 6.Reverse the order\n 7.Sort in ascending order\n 8.Sort in descending order\n 9.Add a letter at the end of each name\n 10.Replace all capital letters with lowercase\n 11.Check if there are any names starts with a specific letter\n 12.Find the longest name')
        choice = input('What do you want to do with the input file date?')
        if choice == '1':
            try:
                position = int(input('What is the position of the name?:'))
                result = remove_word(content, position)
            except:
                print('this posithion is out of range')
                continue
        elif choice == '2':
                word=input('What is the  name you want to add?:')
                result = add_word(content, word)
        elif choice == '3':
            result = add_newline(content)
        elif choice == '4':
            try:
                word = input('Enter the name:')
                result = remove_occurences(content, word)
            except:
                print('this name does not exist')
                continue
        elif choice == '5':
            try:
                word = input('Enter the name:')
                result = remove_occurences_not_first(content, word)
            except:
                print('this name deos not exist')
                continue
        elif choice == '6':
            result = reverse_list(content)
        elif choice == '7':
            result = sort_list(content)
        elif choice == '8':
            result = sort_list_desc(content)
        elif choice == '9':
            word = input('Enter the letter')
            re = add_letter(content, word)
            return re
        elif choice == '10':
            result = replace_capital_small(content)
        elif choice == '11':
            word = input('Enter the letter you want to check:')
            result2 = start_letter(content, word)
            if result2 == True:
                res = 'yes there is at least one name that starts with this letter'
            else:
                res = 'There is no name starts with this letter' 
            print(res)
        elif choice == '12':
            try:
                 result2 = longest_word(content)
                 print('the longest name is:', result2)
            except:
                print('no data in the file')
                continue
        else:
            print('please enter a number from the menue')
            
        try:
            out_put = open(f,'w')
            for i in result:
                out_put.write(i + '\n')
            out_put.close()
        except:
             print('this process does not need any changes in the file')
             out_put = open(f,'w')
             for i in content:
                 out_put.write(i + '\n')
             out_put.close()             
          
        print('Process done')
        rep = input('Do you want to do another prosecc?(y or n)')
        if rep == 'y':
            continue
        elif rep == 'n':
            break
           
            
    print('We are very glad to help you, have a nice day ! ')
            
        
         
#the function remove_word removes the word at position position_of_word from word_list
def remove_word(word_list, position_of_word):
    word_list.pop(position_of_word)
    return word_list

#the function add_word add the word at the end of the word_list
def add_word(word_list, word):
    word_list.append(word)
    return word_list


#the function add_newline adds an empty word between each two words of the list
def add_newline(word_list):
    result = []
    for e in word_list:
        result.append(e)
        result.append('')
    result.pop()
    return result

#the function remove_occurences remove the occurence of word in word_list
def remove_occurences(word_list,word):
    while word_list.count(word)>0:
        word_list.remove(word)
    return word_list

#the function remove_occurences remove the occurence of word in word_list except the first one
def remove_occurences_not_first(word_list,word):
    for item in word_list:   
    	if(item==word):
	     	word_list.remove(word)
    return word_list

#the function reverse_list reverses the list word_list
def reverse_list(word_list):
    word_list.reverse()
    return word_list


#the function sort_list sorts the list word_list in ascending order
def sort_list(word_list):
    word_list.sort()
    return word_list
    
#the function sort_list_desc sorts the list word_list in descending order
def sort_list_desc(word_list):
    word_list.sort()
    word_list.reverse()
    return word_list    


#the function add_letter adds the letter given in parameter at the end of each word of the list
def add_letter(word_list, letter):
    word_list2 = [i + letter for i in word_list]
    return word_list2

#the function replace_capital_small replaces all capitals letters in the words of the list by the corresponding small letter
def replace_capital_small(word_list):
    re = [i.lower() for i in word_list]
    return re

#the function start_letter checks if there is at least one word of the word list that starts with the letter indicated by the second argument.
#In this case, the function returns true otherwise it returns false (in this case you do not generate an output file since no modification
    #has been done to the input file
def start_letter(word_list, letter):
    re = [idx for idx in word_list if idx[0].lower() == letter.lower()]
    if re == []:
        return False
    else:
        return True
    
#the function displays the longest word of the word_list 
def longest_word(word_list):
    re = max(word_list, key=len)
    return re 

#call to the main function
main() 

