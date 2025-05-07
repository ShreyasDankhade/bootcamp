def walrus_operator():
    while (line := input("Enter text: ")) != "exit":
        print(f"You typed: {line}")
    print("Exit detected.")

# Enter text: Hello
# You typed: Hello
# Enter text: exit
# Exit detected.
