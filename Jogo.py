num_sec = 50
r = 0

while r != 50:
    r = int(input("Insira o número que o computador está a pensar: "))
    if r > num_sec:
        print("Muito alto!")
    elif r < num_sec:
        print("Muito baixo!")
    elif r == num_sec:
        print("Correto!")
        break