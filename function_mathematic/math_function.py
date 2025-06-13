class math_function:
    # def __init__(self):
        # self.addition()
        # self.soustraction()
        # self.multiplication()
        # self.division()

    '''
    Retire ces appels du constructeur pour garder le contrôle sur ce que tu exécutes.
    Tu peux ensuite appeler uniquement la méthode que tu veux, sans que l’ autre se lance.
    '''
        
    def addition(self):
        a = int(input('entrer un nombre:  '))
        b = int(input('entrer un nombre:  '))
        print(f'le résultat de votre addition est égale à {a + b}')
       

    def soustraction(self):
        a = int(input('entrer un nombre:  '))
        b = int(input('entrer un nombre:  '))
        print(f'le résulat de votre soustraction est égale à {a - b}')


    def multiplication(self):
        a = int(input('entrer un nombre:  '))
        b = int(input('entrer un nombre:  '))
        print(f'le résultat de votre multiplication est égale à {a * b}')


    def division(self):
        a = int(input('entrer un nombre:  '))
        b = int(input('entrer un nombre:  '))
        print(f'le résultat de votre division est égale à {a / b}')


    def modulo(self):
        a = int(input('entrer un nombre:  '))
        b = int(input('entrer un nombre:  '))
        print(f"le reste de votre division est égale à {a % b}")


    def decimal_to_binary(self):
        a = int(float(input("entrer un nombre decimal:  ")))
        print(f"le resultat de votre conversion en binaire est égale à {bin(a)[2:]}")


    def binary_to_decimal(self):
        binaire = input("Entrez un nombre binaire : ")
        decimal = int(binaire, 2)  # ici on dit à Python : "interprète cette chaîne comme du binaire"
        print(f'le resultat de votre conversion en decimal est égale à {decimal}')
        # print("\n Le décimal est :", decimal)

    def decimal_to_hexa(self):
        n = int(input("Entrez un nombre décimal : "))
        hexadecimal = hex(n)[2:]  # On enlève le "0x" du début
        print(f" Le nombre en hexadécimal est :{hexadecimal.upper()}")



    def hexa_to_decimal(self):
        # hexa = input("Entrez un nombre hexadécimal : ")
        # decimal = int(hexa, 16)  # Interpréter la chaîne comme un nombre en base 16
        # print("Le nombre en décimal est :", decimal)
        pass


    def algorithm(self):
        n = int(input("Entrez un nombre : "))
        m = int(input("Entrez un nombre : "))
        nb = n**2 - m * 10
        print(nb)
        
        pass
     








        
        

           



math_function()