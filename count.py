count = 0



print("counter is ready!")
user_action = input("type c to count and q to quit.").lower()
while True:
    if user_action == "q":
        print("farewell!")
        break
    elif user_action == "c":
        count += 1
        print(f"count is {count}")
    else:
        print("invalid action! type c or q.")
    user_action = input("type c to count and q to quit.").lower()
