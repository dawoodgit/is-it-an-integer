print("----Welcome---- \n Type something to check whether it's an integer or not- or type q to quit: ", end = "")

number = input()

while True:
    if number == 'q' or number == 'Q':
        print("Thanks for using the app")
        break
    elif len(number) ==0:
        number = input("It's blank. Please type something then hit the Enter key- or type q to quit: ")
    else:
        count = 0
        for i in range(len(number)):
            if number[i] in '1234567890':
              count+=1
        if count == len(number):
           print(f"Yes! {number} is an integer.")
        else:
           print(f"No! {number} is not an integer.")
        number = input("Check for another number or type q to quit: ")