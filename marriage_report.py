"""
Name : Alen Mulangan Davi
Student_id : 10332934


Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path, script_dir
import pandas as pd

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    for name1, name2, start_date in married_couples:
        print(f"{name1} has been a Spouse of {name2} since {start_date}.")

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    conection = sqlite3.connect(db_path)
    cursor = conection.cursor()
    query = """
            SELECT person1.name, person2.name, relationships.start_date 
            FROM relationships
            JOIN people person1 ON relationships.person1_id = person1.id
            JOIN people person2 ON relationships.person2_id = person2.id
            WHERE relationships.relationship_type = 'Spouse';
        """
    cursor.execute(query)
    married_couples = cursor.fetchall()
    return married_couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    df = pd.DataFrame(married_couples, columns=["Person 1", "Person 2", "Anniversary"])
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
   main()