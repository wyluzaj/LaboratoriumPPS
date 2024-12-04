import sys
import time

check = input("Wprowadź 'z' jeżeli potrzebujesz zegaru\nWprowadź 'm' jeżeli potrzebujesz minutnika: ")
if check != "z" and check != "m":
    print("Spróbuj jeszcze raz.")
    sys.exit(0)

print("Wpisz początkową godzinę w formacie hh:mm:ss")
h = int(input("hh = "))
m = int(input("mm = "))
s = int(input("ss = "))

if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
    sys.exit("Nieprawidłowa początkowa godzina")

def zegarek(h: int, m: int, s: int):
    while True:
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1
                if h == 24:
                    h = 0
        time.sleep(1)
        print(f"{h:02}:{m:02}:{s:02}")

def minutnik(h: int, m: int, s: int):
    while True:
        if s == 0 and m == 0 and h == 0:
            print("Czas się skończył.")
            break
        if m == 0 and s == 0 and h != 0:
            m = 59
            h -= 1
        if s == 0 and m != 0:
            s = 59
            m -= 1
        else:
            s -= 1
        time.sleep(1)
        print(f"{h:02}:{m:02}:{s:02}")

if check == "z":
    zegarek(h, m, s)
elif check == "m":
    minutnik(h, m, s)
