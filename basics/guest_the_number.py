import random


def run():
    number_rdm = random.randint(1, 100)
    user_number = int(input("Type a number: "))

    while user_number != number_rdm:
        if user_number < number_rdm:
            print("look for a higher number")
        else:
            print("look for a lower number")
        user_number = int(input("Type another number: "))
    print("You win!")


if __name__ == '__main__':
    run()
