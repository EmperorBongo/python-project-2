#Flask server setFlask server set up properly.
from flask import Flask, render_template, url_for, redirect
#Cupcakes module imported Cupcakes module imported properly.
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

#Home page tied to main “/” endpoint.
@app.route("/")
def home():
    return render_template('index.html')
#below is simply a route
@app.route("/cupcakes")
#viewfuction that is being called by app.route
def all_cupcakes():
    #VARIBLE SETTING = TO OUR GET_CUPCAKES FUNCTION "STORE CSV IS A ARGUMENT"
    cupcakes = get_cupcakes("store.csv")
    # RESPONSE FROM SERVER THAT IS MY COMPLETE HTML. CUPCAKES=CUPCAKES IS THE CONTEXT THAT JINJA HAS ACCESS TO.
    return render_template("cupcakes.html", cupcakes=cupcakes)

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("store.csv", name)

    if cupcake:
        add_cupcake_dictionary("order.csv", cupcake)
        return redirect(url_for("order"))
    else:
        return "Sorry cupcake not found."


@app.route("/individual-cupcake")
def individual_cupcake():
    return render_template("individual-cupcake.html")


@app.route("/order")
def order():
    cupcakes = get_cupcakes("order.csv")

    total = 0

    for cupcake in cupcakes:
        total += float(cupcake["price"])
    return render_template("order.html", cupcakes=cupcakes, total=total)


if __name__ == "__main__":
    #APP.RUN IS FOR DEVELOPMENT ONLY DEBUG TRUE ON FOR DEV PURPOSES. 
    app.run(debug=True, port=9822)