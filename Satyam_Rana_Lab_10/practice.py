def create_new_file():
    file_name = "First_Python_File.txt"
    file_path ="Z:\\CMP4266\\Lab10\\"
    file = open(file_path + file_name, "w")
    file.write("First data \n")
    file.close()

def try_exception():
    numbers = ['nine', 'ten', 'eleven']
    sum = 0
    for s in numbers:
        n = int(s)
        sum += n
    print(" Here is sum %d" %sum)

def try_exception():
    numbers = ['nine', 'ten', 'eleven']
    sum = 0
    try:
        for s in numbers:
            n = int(s)
            sum += n
    except ValueError as err:
        print(err)
    print("Here is sum %d" %sum)



fin = open("cities.txt", 'r')
fin.readline()  
line = fin.readline()
maxpop = 0
maxcity = ''
while line != "":
    fields = line.split(';')
    city = fields[0]
    country = fields[1]
    population = int(fields[2])
    if country == 'UK':
        if population > maxpop:
            maxpop = population
            maxcity = city
    line = fin.readline()
if maxpop == 0:
    print ('No cities in input file.\n')
else:
    print(f"Largest city in {country} is {maxcity}.")
fin.close()