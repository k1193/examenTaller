def averageStudent():
    average = 0
    for j in range(1,6):
        average = average + float(input(f"ingrese nota {j}: ")) 
    average = average / 5   

numAlumnos = 0;
students = []
countWomenSoftware = 0
countMenSoftware = 0
countNotBinarySoftware = 0
countWomenTelecomunications = 0
countMenTelecomunications = 0
countNotBinaryTelecomunications = 0
averageTelecomunocations = 0
averageSoftware = 0
countStudents = 0
averageAge = 0
countWoman = 0
countMen = 0
menu = input("Qué desea hacer - ingrese 'admision(admin) - matrícula(matri)'")
if menu == "admin":
    numAlumnos = int("ingrese numero de alumnos")
    for i  in range(numAlumnos):
        name = input("ingrese nombre") 
        academicProgram = input("Ingrese el programa académico -> s - software - t- telecomunicaciones")
        sex = input("ingrese sexo - m(mujer), h(hombre), nb(no binario)") 
        opciones = ['m', 'M','h','H', 'nb', 'NB']
        while(sex not in opciones){
            sex = input("error al ingresar intente de nuevo: ingrese sexo - m(mujer), h(hombre), nb(no binario)") 
        }
        programDict = {}
        if (programDict[academicProgram]){
            programDict[academicProgram] += 1
        }else{
             programDict[academicProgram] = 1
        }
        

        if academicProgram == "s" or academicProgram == "S":
            if sex == "m" or sex == "M":
                countWomenSoftware+=1
            elif sex == "h" or sex == "H":  
                countMenSoftware+=1
            elif sex == "nb" or sex == "NB":
                countNotBinarySoftware+=1

            average = averageStudent()
            students.append({"name": name, "average": average})   
            averageSoftware+=average  
        else:
            sex = input("ingrese sexo - m(mujer), h(hombre), nb(no binario)")  
            if sex == "m" or sex == "M":
                countWomenTelecomunications+=1
            elif sex == "h" or sex == "H":  
                countMenTelecomunications+=1
            elif sex == "bn" or sex == "NB":
                countNotBinarySoftware+=1

            average = averageStudent()
            students.append({"name": name, "average": average})   
            averageTelecomunocations += average         
    #resultado
    averageSoftware = averageSoftware/(countMenSoftware+countNotBinarySoftware+countWomenSoftware)
    averageTelecomunocations = averageTelecomunocations/(countNotBinaryTelecomunications
    +countWomenTelecomunications+countMenTelecomunications)
    print(f"promedio software:{averageSoftware}")
    print(f"Número de mujeres en software:{countWomenSoftware}")
    print(f"Número de hombres en software:{countMenSoftware}")
    print(f"Número de no binarios en software:{countNotBinarySoftware}")
    print(f"promedio de telecomunicaciones:{averageTelecomunocations}")
    print(f"Número de mujeres en telecomunicaciones:{countWomenTelecomunications}")
    print(f"Número de hombres en telecomunicaciones:{countMenTelecomunications}")
    print(f"Número de no binarios en telecomunicaciones:{countNotBinaryTelecomunications}")

    for i in students:
        print(f"Nombre: {i['name']} - Nota Final: {i['average']}")

       
else:
    while True:
        averageAge+=int(input("Ingrese edad"))
        sex = input("ingrese sexo")
        if sex == "m" or sex == "M":
            countWoman += 1
        elif sex == "h" or sex =="H":
            countMen += 1
        stopAdmission = input("si desea dejar de matricular ingrese 0,de lo contrario cualquer tecla para continuar")
        countStudents+=1
        if stopAdmission == 0:
            break

    averageAge = averageAge/countStudents
    print(f"Número de estudiantes matriculados: {countStudents}")
    print(f"Promedio de edad de matricula: {averageAge}") 
    print(f"Número de mujeres matriculadas: {countWomen}")
    print(f"Número de hombres matriculadas: {countMen}")


     for prog, qty in programDict.items():
            print('el programa:' + prog + 'tiene: ' + qty + 'alumnos')






    