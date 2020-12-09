def day1_part1():

    data_file = open("day1input.sql", "r")
    #Lista de datos obtenidos del archivo
    data = data_file.readlines()
    for line1 in range(0,len(data) -1 ):
        for line2 in range(line1+1,len(data)):
            #Se obtienen los numeros para las operaciones
            n1 = int(data[line1])
            n2 = int(data[line2])
            if (n1 + n2 == 2020):
                print("Resultado: " + str(n1*n2))
    data_file.close()

def day1_part2():
    data_file = open("day1input.sql", "r")
    #Lista de datos obtenidos del archivo
    data = data_file.readlines()
    for line1 in range(0,len(data) -2 ):
        for line2 in range(line1+1,len(data)-1):
            for line3 in range(line1+2,len(data)):
                #Se obtienen los numeros para las operaciones
                n1 = int(data[line1])
                n2 = int(data[line2])
                n3 = int(data[line3])
                if (n1 + n2 + n3 == 2020):
                    print("Resultado: " + str(n1*n2*n3))
    data_file.close()

def day2_part1():
    data_file = open("day2input.sql", "r")
    valid = 0
    for line in data_file.readlines():
        #División que tiene la contraseña y policy
        split1 = line.split(": ")
        #Se divide el numero de repeticiones y la letra a revisar
        split2 = split1[0].split(" ")
        #Se divide el rango de apariciones
        split3 = split2[0].split("-")
        #Número de repeticiones de la letra en la contraseña
        rep = 0
        
        for i in range (0, len(split1[1])):
            if split1[1][i] == split2[1] :
                rep +=1
        if int(split3[0])<= rep and rep <= int(split3[1]):
            valid +=1
    print(str(valid))
    data_file.close()

def day2_part2():
    data_file = open("day2input2.sql", "r")
    valid = 0
    for line in data_file.readlines():

        #División que tiene la contraseña y policy
        split1 = line.split(": ")
        password = split1[1]
        #Se divide el numero de repeticiones y la letra a revisar
        split2 = split1[0].split(" ")
        letter = split2[1]
        #Se divide el rango de apariciones
        split3 = split2[0].split("-")
        n1 = int(split3[0])
        n2 = int(split3[1])
        #Número de repeticiones de la letra en la contraseña
        rep = 0
        if (password[n1-1] == letter):
            rep+=1
        if (password[n2-1] == letter):
            rep+=1
        
        if rep == 1:
            valid +=1
    print(str(valid))
    data_file.close()


def main():
    #day1_part1()
    #day1_part2()
    #day2_part1()
    day2_part2()
if __name__ == "__main__":
    main()



