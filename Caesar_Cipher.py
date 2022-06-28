alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_text,shift_amount,direction_type):
  if direction_type=="encode":
    encrypt_text=""
    for letter in user_text:
      if letter not in alphabet:
        encrypt_text+=letter
      else:
        position=alphabet.index(letter)
        encrypt_text+=alphabet[(position+shift_amount)%len(alphabet)]
    print(f"The encoded text is {encrypt_text}")

  elif direction_type=="decode":
    decrypt_text=""
    for letter in user_text:
      if letter not in alphabet:
        decrypt_text+=letter
      else:
        position=alphabet.index(letter)
        decrypt_text+=alphabet[(position-shift_amount)%len(alphabet)]
    print(f"The decoded text is {decrypt_text}")
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(user_text=text,shift_amount=shift,direction_type=direction)
  result=input("Do you want to go again ? Type 'Yes'or 'No'")
  if result=="No":
    should_continue=False
    print("Good Bye!!")
