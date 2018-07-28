# Check if sting is palindromic
#

def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

def main():
    print(is_palindromic("adjfosjojosdjgos"))
    print(is_palindromic("abba"))

if __name__ == '__main__':
    main()
