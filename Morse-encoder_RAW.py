import time

eng_to_morse = {
    'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/'
}
outstr = ''
space = ' '
senc = 0
wordprocces = 0
word = input('Enter a sentence : ')
lenword = len(word)

for i in word:
    if i not in eng_to_morse:
        print('Data not formatted properly')
        time.sleep(5)
        break
    else:
        print(eng_to_morse[i], end=' ')