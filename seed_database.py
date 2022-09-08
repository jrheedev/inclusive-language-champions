"""Script to seed database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb inclusivedb")
os.system("createdb inclusivedb")

model.connect_to_db(server.app)
model.db.create_all()

user = model.User(user_name='jellybean', password='popsicles')
model.db.session.add(user) 
model.db.session.commit()

user1 = model.User(user_name='oprahwinfrey', password='gaylerocks')
model.db.session.add(user1) 
model.db.session.commit()

user2 = model.User(user_name='gayleking', password='oprahrocks')
model.db.session.add(user2) 
model.db.session.commit()

user3 = model.User(user_name='dwaynejohnson', password='therockrocks')
model.db.session.add(user3) 
model.db.session.commit()

#TERMINOLOGY TEST DATA

non_inclus_term = model.Terminology(non_inclus_term = 'tkkk', inclus_term = 'better',  term_topic = 'random', explainer_desc='please')
model.db.session.add(non_inclus_term)
model.db.session.commit()

#COUNT TEST DATA

count_value1 = model.Count(count_value = 1353, term_id = 1, user_id = 1)
model.db.session.add(count_value1)
model.db.session.commit()

count_value2 = model.Count(count_value = 14555, term_id = 1, user_id = 1)
model.db.session.add(count_value2)
model.db.session.commit()


# more manual way is to also create user2, user3... for dummy data 

# to ease creation of new dummy data, also consider
# creating a for loop using range built in function
# to auto-create new user profiles, etc and use concatenation
# inside for loop, take the constructor function as argument
# and supply with concatenated strings
# add and commit as you go

#Create 10 unique users
for n in range(10):
    user_name = f"username{n}"  
    password = "test"

    user = crud.create_user(user_name, password)
    model.db.session.add(user)

model.db.session.commit()
        

# NEXT STEPS
# add enough dummy data to test crud functions
# practice deleting records/adding records in psql inclusivedb
# test all functions as it's being developed, test interactively in the terminal
# python3 -i crud.py, seed_database.py, model.py
# IMPORTANT: any time you use a function in crud.py file, remember to change
# invoke crud file by typing crud.create_term; crud.add_term_to_db
# play interactively with seed_database file using crud functions 

# for n in range(10):
    
#     new_term = crud.create_user(term_id, inclus_term)
#     model.db.session.add(new_term)

term = model.Terminology(non_inclus_term='boogie', inclus_term='beige', term_topic='pastels', explainer_desc='string')
model.db.session.add(term)
model.db.session.commit()

count = model.Count(user_id=1, term_id=1, count_value=1)
model.db.session.add(count)
model.db.session.commit()

