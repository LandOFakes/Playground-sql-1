import sqlite3


conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    
    person_id = int(input("Enter a person's ID (or -1 to exit): "))
    
    if person_id == -1:
        break
    
    
    cursor.execute('SELECT * FROM person WHERE id = ?', (person_id,))
    person = cursor.fetchone()
    
    if person:
        
        print(f"{person[1]} {person[2]}, {person[3]} years old")

        
        cursor.execute('''
            SELECT pet.name, pet.breed, pet.age 
            FROM pet 
            JOIN person_pet ON pet.id = person_pet.pet_id 
            WHERE person_pet.person_id = ?
        ''', (person_id,))
        
        pets = cursor.fetchall()
        
        if pets:
            print("Pets owned:")
            for pet in pets:
                print(f"{pet[0]} the {pet[1]}, {pet[2]} years old")
        else:
            print("This person has no pets.")
    else:
        print("Person not found.")
    

conn.close()
