def is_prime(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def run():
    number = int(input("Type a number"))

    if is_prime(number):
        print(str(number) + "is prime")
    else:
        print(str(number) + "isn´t prime")


if __name__ == '__main__':
    run()
