from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Users Controller
@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    user_id= Ninja.save(request.form)
    dojo_id = request.form["dojo_id"]
    return redirect(f'/dojo/{dojo_id}')

# Read Users Controller
@app.route('/ninjas')
def new_ninja_page():
    all_dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", all_dojos=all_dojos)

