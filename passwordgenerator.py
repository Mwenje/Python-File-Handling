#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


if nr_letters > len(letters):
    print(f"You have entered more letters than available letters {len(letters)}")
    
elif nr_symbols > len(symbols):
    print(f"You have entered more symbols than available symbols {len(symbols)}")
elif nr_numbers > len(numbers):
  print(f"You have entered more numbers than available numbers {len(numbers)}")
else:
   random_password = []

   for number in range(0, nr_numbers):
      if number <= len(numbers):
        #  random_number = random.randint(0, len(numbers)-1)
         random_password.append(random.choice(numbers))

   for symbol in range(0,nr_symbols):
       if symbol <= len(symbols):
        #   random_symbol = random.randint(0, len(symbols)-1)
          random_password.append(random.choice(symbols))

   for letter in range(0, nr_letters):
      if letter <= len(letters):
        # random_letter = random.randint(0, len(letters)-1)
        random_password.append(random.choice(letters))
    
   random.shuffle(random_password)
   final_password = ''.join(random_password)
   print(f"\nYour generated password is: {final_password}")



