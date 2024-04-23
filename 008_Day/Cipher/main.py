alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from logo import logo
print(logo)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

length_alphabet=int(len(alphabet)/2)


def caesar(task,test_text,shift_amount):
    return_msg=""
    while shift_amount > length_alphabet:
       shift_amount-=length_alphabet
    for letter in test_text:
        if letter not in alphabet:
           return_msg+=letter
        else:
            idx=alphabet.index(letter)
            if task=="encode":
                return_msg+=alphabet[idx+shift_amount]
            elif task=="decode":
                return_msg+=alphabet[idx-shift_amount]
    
    print(f"Your {task}d message is: {return_msg}")
          

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#encrypt(plain_text=text, shift_amount=shift)

keep_going=True
while keep_going==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)

    kg_prompt=input("Would you like to keep going? (Y/N)")
    if kg_prompt=="N":
        keep_going=False