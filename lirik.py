import time
import sys

lirik = [
    'Itulah kenapa jatuh cinta.',
    'Dikatakan jatuh.',
    'Karena sebagaimana kita jatuh.',
    'Kita tidak punya kuasa..',
    'Pilih jatuh...',
    'Pada hati yang mana...'
]

print('=' * 25 + 'Dulu Yang Nanti' + '=' * 25)

for baris in lirik:
    for huruf in baris:
        print(huruf, end="", flush = True)
        time.sleep(0.12)
    print()
    time.sleep(1.1)