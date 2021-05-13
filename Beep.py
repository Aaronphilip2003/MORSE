import winsound
frequency_dot = 2500
duration_dot = 250

frequency_dash = 2500
duration_dash = 750

frequency_pause=100
duration_pause=500

def dot():
    winsound.Beep(frequency_dot,duration_dot)

def dash():
    winsound.Beep(frequency_dash,duration_dash)

string_word=input("Enter morse:")

for char in string_word:
    if char=='-':
        dash()
    elif char=='.':
        dot()
    elif char=='/':
        winsound.Beep(frequency_pause,duration_pause)
    elif char==' ':
        winsound.Beep(50,600)

