from flask import Flask

app=Flask(__name__)
@app.route("/")
def home():
    return "Wlcome to CICD project"


if __name__=="__main__":
    app.run(debug=True)
