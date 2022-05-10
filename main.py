from flask import Flask, request, render_template

app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        team_num = request.form.get("team-number")
        match_num = request.form.get("match-number")
        alliance = request.form.get("alliance")
        station = request.form.get("station")
        start_position = request.form.get("starting-position")
        taxi = request.form.get("taxi")
        cargo_pickup = request.form.get("cargo-pickup")
        defense = request.form.get("defense")
        disabled = request.form.get("disabled")
        action = request.form.get("endgame-action")
        location = request.form.get("climb-location")
        rung = request.form.get("rung-reached")
        notes = request.form.get("notes")
        print("Name: " + name)
        print("Team #: " + team_num)      
        print("Match #: " + match_num)
        print("Alliance: " + alliance)
        print("Station: " + station)
        print("Start pos: " + start_position)
        if taxi == ("taxi"):
          print("Taxi: True")
        else:
          print("Taxi: False")
        if cargo_pickup == ("cargo-pickup"):
          print("Cargo Pickup: True")
        else:
          print("Cargo Pickup: False")
        if defense == ("defense"):
          print("Defense: True")
        else:
          print("Defense: False")
        if disabled == ("disabled"):
          print("Disabled: True")
        else:
          print("Disabled: False")
        print("Action: " + action)
        print("Location: " + location)
        print("Rung: " + rung)
        print("Notes: " + notes)
    return render_template("scouting.html")



if __name__ == '__main__':
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
