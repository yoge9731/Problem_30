"""Student Data Task:

Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. 
Loop through the list and print each student's information."""

l = [{
    "name":"yogee",
    "age":30,
    "marks":100
},
{
    "name":"rama",
    "age":30,
    "marks":100
}]
for students in l:
    print(students["name"],"-",students["age"],"-",students["marks"])


    



