from pet import Pet

def show_menu():
    print("\nChoose an action:")
    print("1. Feed your pet")
    print("2. Let your pet sleep")
    print("3. Play with your pet")
    print("4. Train your pet a trick")
    print("5. Show pet's tricks")
    print("6. Show pet's status")
    print("0. Exit")

def get_valid_choice():
    while True:
        choice = input("Enter your choice (0–6): ").strip()
        if choice.isdigit() and 0 <= int(choice) <= 6:
            return int(choice)
        print("Invalid input. Please enter a number between 0 and 6.")

def main():
    name = input("Name your pet: ").strip()
    pet = Pet(name)

    while True:
        show_menu()
        choice = get_valid_choice()

        if choice == 1:
            pet.eat()
        elif choice == 2:
            pet.sleep()
        elif choice == 3:
            pet.play()
        elif choice == 4:
            trick = input("Enter the trick to teach: ").strip()
            pet.train(trick)
        elif choice == 5:
            pet.show_tricks()
        elif choice == 6:
            pet.get_status()
        elif choice == 0:
            print(f"👋 Goodbye! {name} will miss you 🐾")
            break

if __name__ == "__main__":
    main()
