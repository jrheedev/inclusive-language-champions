"""CRUD operations"""

from urllib import response
from itsdangerous import TimestampSigner
from model import db, User, Count, Terminology, connect_to_db


def create_user(user_name, password):
    """Create and return a new user."""
    user = User(user_name = user_name, password=password)
    db.session.add(user)
    db.session.commit()

    return user


def create_term(inclus_term, non_inclus_term, term_topic, explainer_desc):
    """Create and return a new term"""

    term = Terminology(inclus_term = inclus_term, non_inclus_term=non_inclus_term, term_topic=term_topic, explainer_desc=explainer_desc, active_status = True)
    db.session.add(term)
    db.session.commit()

    return term

# def add_term_to_db(inclus_term, non_inclus_term):
#     """add new term to the database"""
#     add_term = Terminology(inclus_term= inclus_term, explainer_desc= explainer_desc)
#     db.session.add(add_term)
#     db.session.commit()

def term_frequency():
    """show frequency of term in searches"""
    pass 

def update_term(non_inclus_term, new_explainer):
    """update term"""
    non_inclus_term = Terminology.query.filter(Terminology.non_inclus_term == non_inclus_term).first()  
    #Above line - run a specific query where we get an exact match for non_inclus_term from Term table aka
    #Terminology bookshelf
    non_inclus_term.explainer_desc = new_explainer
    #For the above line, we've gotten our book, changed the chapter, stored this new chapter and now we want to place the forever changed
    #book back on the shelf. 
    db.session.add(non_inclus_term)
    #Remember to return the forever changed book (not just the chapter) back into the database
    db.session.commit(non_inclus_term)
    #Commit the forever changed book to database

    return non_inclus_term 
    #Return non_inclus_term to user in case we want to use it

#As an admin, I want to update an existing term with a new term description or new term name
#I would grab the non_inclus_term to find its current term id
#Use current term_id and update explainer_desc
#To update explainer_desc, overwriting old with new [new_explainer_desc = explainer_desc] 

def delete_user_acct(user_id):
    """delete user account"""
    delete_user_acct = User.query.get(user_id)
    # above line gets us a single user_id from User table and stores it in delete_user_acct
    all_user_acct = Count.query.filter(Count.user_id == user_id).all()
    # above line gets us a stack of books AKA goes through ALL the records in Count table where
    # Count.user_id is an exact match with User.user_id
    # .all() allows us to get ALL records in LIST form 

    for x in all_user_acct:
        db.session.delete(x)
        db.session.commit()
    
    #we create a for loop where we want to iterate through the LIST of all_user_acct records
    #delete and each entry for x

    db.session.delete(delete_user_acct)
    db.session.commit()    
    
    return 

    # for our for loop
    # for every exact record match from Count table for count.user_id
    # delete that record and session commit (delete_user_account)

    # for 

#Things that are associated with a user account
#everything in user table & associated records in Count Table
# when deleted an user account, we also want to delete associated
# records along with user name; look at associated foreign keys
# Another examples - message boards, messages, user profile
# We want to delete all the counts but we can do this using user_id
# May need to create a for loop where 
# we get all the counts where the user_id is X person
# create a for loop where each corresponding record is then deleted
# bc there can be multiple entries by a user_id

def delete_user():
    """delete user"""
    pass 

def update_term_status(inclus_term):
    """update term_id to either active/deactivated status.
    some terms may need to be updated to trigger a message
    to users stating the term is deactivated because it is 
    no longer inclusive """

    term_to_be_updated = Terminology.query.filter(Terminology.inclus_term == inclus_term).first()
    term_to_be_updated.active_status = False
    db.session.add(term_to_be_updated)
    db.session.commit()

# IS THIS TERM STILL ACCESSIBLE ON TABLE - YES
# Step 1 - Add a condition in our Terminology table where default for all 
# terms are designated as 'Active'= True
# Step 2 - Add a function where if term status has to be updated to deactivated/False
# function changes 'Active' status to False in db
# Step 3 - Display a message to user stating that term has been deactivated

# we can write an init method in our Terminology table where the default
# is always true


def update_profile(user_id):
    """update user profile"""
    pass 

def term_topic_frequency():
    """find frequency of term topics that appear in past"""
    pass 

def view_term_replace():
    """view suggested term replacement to user"""
    
    term_suggest = Terminology()
    db.session.add(term_suggest)
    db.session.commit()

    return

def sentence_search_for_db_terms(sentence):
    """take sentence and run it through db for exclusive terms"""

    all_terms = Terminology.query.all() 
    # Terminology.non_inclus_term = Terminology.query.filter(Terminology.non_inclus_term == word).all()

    sentence = sentence.split(' ')
 
    # if term.exclusiveterm in sentence:
    #     # Return new statement 
 
    found_terms_in_sentence = []
    suggest_new_terms = []

    for term in all_terms:
        if term.non_inclus_term in sentence:
            
            found_terms_in_sentence.append(term.non_inclus_term) 
            print("we have found the following non-inclusive terms: ")

            suggest_new_terms.append(term.inclus_term)
            print("consider using these more inclusive terms: ")


    print(f"{found_terms_in_sentence}")       

    response_dictionary = {
        "found_terms_in_sentence": found_terms_in_sentence,
        "suggest_new_terms" : suggest_new_terms,
        "sentence" : sentence,
    }

    return response_dictionary

    #NEXT STEP
    #Return the specific non_inclus terms in the sentence/response to user
    #Also run a loop through the term.inclus_term and test in interactive
    #crud.py mode
    #     # Terminology.query.filter(Terminology.inclus_term == word).all()

    # We can also tap into term.inclus_term in sentence on line 149
    # 

    # for term in sentence:
    #     #Return formatted statement 

#CONSIDER
#Storing all the books in one variable


#STEPS
# Take in the sentence from the use
# Break down the sentence into words; have it account for punctuation. Use a python method
# that contains !, but does not only contain this
# Run a for loop that iterates through the words with a database query
# If there are exact matches
# Store these exact matches into new variables; in such a way that we can use this as
# response objects
# Return a response that 'Your search was found in 'XYZ' terminology table'
# Try these replacements instead

#Additional bonus:
# Connect an action/underline/highlight/CSS styling to those exact matches only


def view_all_terms():
    """view all terms"""
    pass 

def view_terms_by_topic():
    """view terms by topic"""
    pass 

def view_all_topics():
    """view all topics"""
    pass 

# def does_count_exist(inclus_term, non_inclus_term, term_topic, explainer_desc):
#     """Check to see if a term already exists"""
    
#     count_check = count.query.filter(user_id, term_id)

#     return count_check


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    