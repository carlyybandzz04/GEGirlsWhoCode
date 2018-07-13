# --- Define your functions below! ---
def greeting():
    print("Hello")

def intro():
    print("welcome")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        if answer == "hi":
            greeting(answer)
        else:
            print("That's cool!")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
