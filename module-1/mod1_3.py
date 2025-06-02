# Alexis Mitchell
# June 1, 2025
# This program uses input and counts backwards to 1 while displaying
# lyrics of "100 bottles of beer on the wall"

def countdown(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottles = bottles - 1
            bottle_word = "bottle" if next_bottles == 1 else "bottles"
            print(f"Take one down and pass it around, {next_bottles} {bottle_word} of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1


def main():
    try:
        user_input = int(input("Enter number of bottles: "))
        if user_input < 1:
            print("Please enter a number greater than 0.")
        else:
            countdown(user_input)
            print("Time to buy more bottles of beer.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Run the main program
main()