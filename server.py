from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
import crud
import os 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def home():
    """View homepage"""

    #User should insert their sentence
    #Show user their original sentence
    #Show user the database findings for non_inclus_terms
    #Show those non_inclus_terms
    #Show term replacements instead without refreshing the page

    #REFER TO AJAX DEMO 

    return render_template('home.html')

@app.route("/createuser", methods=['POST'])
def create_user():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)

    crud.create_user(username, password)

@app.route("/createterm", methods =['POST'])
def create_term():
    non_inclus_term = request.form.get("non_inclus_term")
    inclus_term = request.form.get("inclus_term")
    term_topic = request.form.get("term_topic")
    explainer_desc = request.form.get("explainer_desc")

    crud.create_term(non_inclus_term, inclus_term, term_topic, explainer_desc)

@app.route("/sentencequery", methods=["POST"])
def run_sentence_query():
    """Receive sentence from user and return a response"""
    user_gave_sentence= request.json.get("sentence")
    print(user_gave_sentence)

    db_word_search = crud.sentence_search_for_db_terms(user_gave_sentence)


    # Invoke function in Crud.py -> sentence_search_for_db_terms(sentence)
    # This function will return a dictionary but we want to store it in a variable
    # (...) that we can use
    # Add dictionary in our return jsonify response objects (close to line 56)
    # 
    # Take their sentence, pass it through database
    #Return non_inclus terms

    return jsonify({
        "success": True,
        "status": f"{user_gave_sentence}",
        "search_complete": db_word_search

    })

@app.route("/base")
def show_base():
    return render_template("base.html")

@app.route("/terms")
def show_view_all_terms():
    return render_template("terms.html")

@app.route("/how-it-works")
def show_how_it_works():
    return render_template("how-it-works.html")

# if crud.search_count(x,y,z) == None:
#     crud.create_count(x,y,z)
# else:
#     crud.delete_count()
#     crud.create_count()with updated count num

@app.route('/flash')
def show_flash_message():
    """Display flash confirmation message back to user"""
    flash('Welcome {name}')
    return render_template("homepage.html")

@app.route('/get-name')
def get_name():
    """Display user name on page and store in session"""

    name = request.args.get('name')
    session['name'] = name
    return redirect('/')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)