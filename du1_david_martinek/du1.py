from turtle import *
print("Vítejte ve hře TIC-TAC-TOE by martineda96.")
prvni_hrac = input("Zadejte jméno prvního hráče:")
druhy_hrac = input("Zadejte jméno druhého hráče:")
#Uživatel si sám nastaví velikost hracího pole (x,y). Délka hrany čtverce a je pevně stanovena.
#Vstupy x a y jsou ošetřeny nekonečným cyklem (pro případ zadání nekladného čísla) a funkcí int().
x = int(input("Zadejte počet sloupců hracího pole:"))
while x < 1:
    x = int(input("Počet sloupců musí být kladné číslo, zkuste to znovu:"))
y = int(input("Zadejte počet řádků hracího pole:"))
while y < 1:
    y = int(input("Počet řádků musí být kladné číslo, zkuste to znovu:"))

#Kreslení čtvercové mřížky prostřednictvím tří for cyklů. První for cyklus udává počet řádků.
#Druhý cyklus udává počet sloupců a třetí cyklus (vnitřní) kreslí jednotlivé čtverce.
STRANA_CTVERCE = 30
speed(0)
for _ in range(y):
    for _ in range (x):
        for _ in range(4):
            forward(STRANA_CTVERCE)
            left(90)
        forward(STRANA_CTVERCE)
    backward(x*STRANA_CTVERCE)
    left(90)
    forward(STRANA_CTVERCE)
    right(90)

#volna_policka udává, kolik mohou hráči dohromady odehrát tahů. Po nakreslení každého symbolu jejich počet klesne o 1.
#Cyklus zajišťuje střídání hráče s křížky a kolečky (včetně vykreslení příslušných symbolů).
volna_policka = int(x*y)
while volna_policka != 0:
    sloupec = int(input(f"Hraje {prvni_hrac}. Zvol sloupec:"))
    while sloupec < 1 or sloupec > x:
        sloupec = int(input("Takový sloupec neexistuje, zkus to znovu:"))
    radek = int(input(f"Hraje {prvni_hrac}. Zvol řádek:"))
    while radek < 1 or radek > y:
        radek = int(input("Takový řádek neexistuje, zkus to znovu:"))
    penup()
    setpos(sloupec*STRANA_CTVERCE-STRANA_CTVERCE/2,radek*STRANA_CTVERCE-STRANA_CTVERCE/2)
    pendown()
    pencolor("blue")
    right(45)
    for _ in range(2):
        forward(STRANA_CTVERCE/2)
        backward(STRANA_CTVERCE)
        forward(STRANA_CTVERCE/2)
        right(90)
    right(135)
    volna_policka = volna_policka-1
    if volna_policka != 0:
        sloupec = int(input(f"{druhy_hrac}. Zvol sloupec:"))
        while sloupec < 1 or sloupec > x:
            sloupec = int(input("Takový sloupec neexistuje, zkus to znovu:"))
        radek = int(input(f"Hraje {druhy_hrac}. Zvol řádek:"))
        while radek < 1 or radek > y:
            radek = int(input("Takový řádek neexistuje, zkus to znovu:"))
        penup()
        setpos(sloupec*STRANA_CTVERCE-STRANA_CTVERCE/2,radek*STRANA_CTVERCE-STRANA_CTVERCE*0.9)
        pendown()
        pencolor("red")
        circle(STRANA_CTVERCE*0.4)
        volna_policka = volna_policka - 1

print("Konec hry. Pokud jste hráli správně, tak v mřížce nezůstalo žádné volné políčko.")
exitonclick()