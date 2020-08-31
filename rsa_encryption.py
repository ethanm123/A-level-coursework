import math,random

RSA_algorithm = lambda N, e, M: (M ** e) % N  # Defining the encryption algorithm.

class RSA:
    def __init__(self, private_key1=None, private_key2=None, e=False, d=False, message=""):
        self.private_key1 = private_key1
        self.private_key2 = private_key2
        self.e = e
        self.d = d
        self.message = message

    # def prime_checker(self, number: "the number that needs checking to see if it is prime"):
    #     """Checks if a number is prime"""
    #     for i in range(2, int(math.sqrt(number)) + 1):#looping through the numbers that could potentially divide into the number that are above 2.
    #         #if this test is failed then the number is not prime.
    #         if number % i == 0: #If its possible to divide by i with no remainder, then the number is not prime.
    #             return False
    #     return True #if a number could not be found then the number is prime and has passed the check.

    def find_e_value(self, privatekey1, privatekey2):
        """Used to find the exponent value, e, if it isn't provided by the user."""
        try:
            self.private_key1=int(privatekey1)
            self.private_key2=int(privatekey2)
        except:
            return("Please make sure you provide 2 private keys.")
        if self.private_key2 <= 10 or self.private_key1<=10:
            return "Please make sure you enter a prime greater than 10"
        number = (self.private_key1-1)*(self.private_key2-1)
        number_copy = number
        prime_factors = [] #Creating an empty list.
        while number % 2 == 0:#If the number is divisible by 2, the first prime number, we need to find how many 2s actually go into it.
            prime_factors.append(2) #If it is divisible by 2, 2 gets added to the list
            number = number / 2 #Dividing the number by 2

        for i in range(3, int(math.sqrt(number) + 1), 2):#As no other prime numbers are even, we can increment from 3 taking 2 steps each time. Only needs to run to the sqrt of a number+1
            if number % i == 0: #Checking if the number is divisible by i
                prime_factors.append(i) #if it is, adding it to the list.
                number = number / i #Dividing the number by i.

        if number > 2: #if number becomes a prime and its greater than 2 it gets added to the list here.
            prime_factors.append(int(number))

        numbers_to_test = [int(i) for i in range(2, int((math.sqrt(number_copy)+1)))] #Compiling a list of numbers that are between 2 and the specified number.
        print(numbers_to_test)
        temp=0
        for i in prime_factors:
            if temp == i:
                continue
            else:
                pass
            for j in numbers_to_test:
                if j % i == 0: #if it is divisible by any of the prime factors the numbers cannot be coprime.
                    numbers_to_test.remove(j) #Removing any non-coprime numbers from the list.
                    continue
        print(numbers_to_test)
        return str(numbers_to_test[random.randint(0, len(numbers_to_test)-1)])#Returning a random value from the list of coprime numbers.


    def encrypt(self, message, private_key1, private_key2, e) -> "either a list of numbers or a string of hex":
        """Encrypts a number with RSA encryption"""
        if message == "":
            return "Please enter a message"
        if len(private_key2) <= 1 or len(private_key1)<=1:
            return "Please make sure you enter a prime greater than 10"
        try:
            self.private_key1 = int(private_key1)
            self.private_key2 = int(private_key2)
            self.message = message
        except: return("Please make sure you fill all the fields.")
        if e == "": #Incase an e value is needed, it will run the function that generates one.
            e = int(self.find_e_value(self, self.private_key1, self.private_key2))
        message_list = [ord(i) for i in self.message]#Putting the ascii values of the message into a list, one character at a time.
        N = (self.private_key2)*(self.private_key1) #finding the value of N needed for encryption.
        cipher_text = [RSA_algorithm(N,int(e),i) for i in message_list] #Creating the ciphertext by running each item in the message through the RSA algorithm.
        print("e value used: "+str(e))
        print(cipher_text)
        return str(cipher_text) #Returning the ciphertext.

    def find_d(self, number, modulus_operator):
        """Calculates the multiplicative inverse for the modular_operator. The number will be the encryption exponent,
        and the modulus_operator would be the product of the private keys -1. Basically, finds a solution to
        d*e=1%number."""
        number = number % modulus_operator
        for i in range(1,int(modulus_operator)):
            if (number* i)%modulus_operator == 1: #i represents d. This is in the form e*d%number has to =1.
                return i                           #as its finding a solution to d*e=1%number

    def decrypt(self, private_key1, private_key2, e=None, d=None, message=""):
        """Decrypts a list of digits that were encrypted using RSA"""
        if message == "":
            return "Please enter a message"
        if len(private_key2) <= 1 or len(private_key1)<=1:
            return "Please make sure you enter a prime greater than 10"
        try:
            self.private_key1 = int(private_key1)
            self.private_key2 = int(private_key2)
            if e!="":
                self.e = int(e)
            if d!="":
                d = int(d)
            self.message = message
            N = (self.private_key1)*(self.private_key2)#Calculating one of the values needed in the encryption.
            working_message=[]
            temp=""
            for i in self.message:
                if i == " ":
                    working_message.append(int(temp))
                    temp=""
                else:
                    try:
                        int(i)
                        temp += str(i)
                    except:
                        pass
            working_message.append(int(temp))
            self.message = working_message #Putting all of the ascii values of the message into a list.
        except:return("Please make sure you provide all of the variables that are needed.")
        if (not d or d=="") and (self.e or self.e !=""):
            d = self.find_d(self, self.e, ((self.private_key2-1)*(self.private_key1-1)))  # Calculating a value for d using Euclid's algorithm.
        elif (not d or d == "") and(not self.e or self.e == ""):
            print("Please enter a value of e or d")
        decrypted_list = [RSA_algorithm(N,d,i) for i in working_message]#Running the decrypion algorithm
        decrypted_string = ""
        for i in decrypted_list:
            decrypted_string+=str(chr(i))#Putting the decrypted message into a string.
        return decrypted_string#Returning the decrypted message.









