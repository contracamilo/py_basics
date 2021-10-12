

def palindrome(word):
    string = word
    string = word.strip()
    string = word.replace(' ', '')
    string = string.lower()

    if string[::-1] == string:
        return True
    else:
        return False


def run():
    word = input("please type a word: ")
    is_palindrome = palindrome(word)

    if is_palindrome == True:
        print(word + " is a palindrome")
    else:
        print(word + " isn't a palindrome")


if __name__ == '__main__':
    run()
