def run():
    LIMIT = 10
    counter = 0
    pow_2 = 2**counter

    while pow_2 < LIMIT:
        counter = counter + 1
        pow_2 = 2**counter
        print('2 pow ' + str(counter) + " is equal " + str(pow_2))

    while counter < 1000:
        counter += 1
        print(counter)


if __name__ == '__main__':
    run()
