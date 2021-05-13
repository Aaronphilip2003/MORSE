import time
morse_to_eng = {
    '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
}

word = input('Enter a sentence : ')
lenword = len(word)
words = ''
for i in word:
    if i != ' ':
        words=words+i
        if i not in morse_to_eng:
            print('Data not formatted properly')
            time.sleep(5)
            break
    elif i == '/':
        print(morse_to_eng[words], end=' ')
    else:
        print(morse_to_eng[words], end='')
        words = ''