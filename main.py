def reverse_string():
    text = input("Enter a string: ")
    print("Reversed string:", text[::-1])

def check_prime():
    num = int(input("Enter a number: "))
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    print(f"{num} is prime? {is_prime}")

def fizz_buzz():
    n = int(input("Enter a number: "))
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def count_vowels():
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)

def palindrome_checker():
    text = input("Enter a string: ")
    if text == text[::-1]:
        print("Palindrome!")
    else:
        print("Not a palindrome.")

def main_menu():
    while True:
        print("\n=== Python Code Challenges Menu ===")
        print("1. Reverse String")
        print("2. Check Prime")
        print("3. FizzBuzz")
        print("4. Count Vowels")
        print("5. Palindrome Checker")
        print("6. Exit")
        
        choice = input("Select a challenge (1-6): ")

        if choice == "1":
            reverse_string()
        elif choice == "2":
            check_prime()
        elif choice == "3":
            fizz_buzz()
        elif choice == "4":
            count_vowels()
        elif choice == "5":
            palindrome_checker()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()

