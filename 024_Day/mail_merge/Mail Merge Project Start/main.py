#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

namefile=open('./Input/Names/invited_names.txt')
name_list=namefile.readlines()
namefile.close()

let_file=open('./Input/Letters/starting_letter.txt')
base_letter=let_file.read()
let_file.close()

pop_letters=[]
for name in name_list:
    name=name.strip()
    file_name="./Output/ReadyToSend/"+name.strip()+".txt"

    with open(file_name,'w') as file:
        file.write(base_letter.replace('[name]',name))
                   


