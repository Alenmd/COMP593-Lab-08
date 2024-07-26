"""
Name : Alen Mulangan Davi
Student_id : 10332934
Partner : Krishna Prakash 

Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from random import random, choice
from faker import Faker

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()
    print("Successfully created relationship table with 100 fake relationships.")
  

def create_relationships_table():
    """Creates the relationships table in the DB"""
    conection = sqlite3.connect(db_path)
    cursor = conection.cursor()
    relationship_table = """
        CREATE TABLE IF NOT EXISTS relationships
        (
            id INTEGER PRIMARY KEY, 
            person1_id INTEGER NOT NULL,
            person2_id INTEGER NOT NULL,
            relationship_type TEXT NOT NULL,
            start_date DATE NOT NULL,
            FOREIGN KEY (person1_id) REFERENCES people (id),
            FOREIGN KEY (person2_id) REFERENCES people (id)
        );
       """
    cursor.execute(relationship_table)
    conection.commit()

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    conection = sqlite3.connect(db_path)
    cursor = conection.cursor()
    add_relationship = """
        INSERT INTO relationships
        (
            person1_id,
            person2_id,
            relationship_type,
            start_date
        )
        VALUES (?, ?, ?, ?);
        """
    fake = Faker()
    conection.execute("BEGIN TRANSACTION")
    for _ in range(100):
            person1_id = fake.random_int(min=1, max=200)
            person2_id = fake.random_int(min=1, max=200)
            while person1_id == person2_id:
                person2_id = fake.random_int(1, 200)
            relationship_type = choice(['Friend', 'Spouse', 'Girlfriend'])
            start_date = fake.date_between(start_date='-50y', end_date='today')
            new_relationship = (person1_id, person2_id, relationship_type, start_date)
            cursor.execute(add_relationship, new_relationship)
    conection.commit()

if __name__ == '__main__':
   main()