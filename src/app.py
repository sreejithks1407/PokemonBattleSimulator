from flask import Flask, request, jsonify
from battle import Fight
import pandas as pd
import uuid
from flask_sqlalchemy import SQLAlchemy


pokemon_df = pd.read_csv("pokemon.csv")
pokemon_df.set_index("name", inplace=True)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class BattleModel(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    player1 = db.Column(db.String(80), nullable=False)
    player2 = db.Column(db.String(80), nullable=False)
    unique_id = db.Column(db.String(80), nullable=False)
    battle_status = db.Column(db.String(80), nullable=False)
    winner = db.Column(db.String(80), nullable=True)
    won_by_margin = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f"Battle(player1 = {self.player1}, player2 = {self.player2}, unique_id = {self.unique_id}, battle_status = {self.battle_status}, winner = {self.winner}, won_by_margin = {self.won_by_margin})"


@app.route("/")
def all_battles():
    all_battles = BattleModel.query.all()
    return str(all_battles)


# Pagination API section
@app.route("/api/pokemon/pagination", methods=["GET"])
def listing_pokemons():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    
    total = len(pokemon_df)
    start = (page - 1) * per_page
    end = start + per_page
    
    data = pokemon_df.iloc[start:end].to_dict(orient='records')
    
    return jsonify({
        'total': total,
        'page': page,
        'per_page': per_page,
        'data': data
    })


# Battle section and upload result into db
@app.route("/api/pokemon/battle", methods=["POST"])
def pokemon_battle():
    data = request.get_json()

    player1 = data.get("player1")
    player2 = data.get("player2")
    unique_id = str(uuid.uuid4())
    battle_status = "BATTLE_INPROGRESS"

    try:
        pokemon_fight = Fight()
        result = pokemon_fight.fight(player1, player2, pokemon_df)
        if result:
            battle_status = "BATTLE_COMPLETED"
            print(battle_status)
            winner = result[0]
            won_by_margin = result[1]

            battle = BattleModel(player1 = player1, player2 = player2, unique_id = unique_id, battle_status = battle_status, winner = winner, won_by_margin = won_by_margin)
            db.session.add(battle)
            db.session.commit()
        else:
            battle = BattleModel(player1 = player1, player2 = player2, unique_id = unique_id, battle_status = battle_status, winner = "NULL", won_by_margin = "NULL")
            db.session.add(battle)
            db.session.commit()
    # battles = BattleModel.query.all()
    except Exception as e:
        print(f'pokemon battle function failed due to {e}')
        battle_status = "BATTLE_FAILED"
        print(battle_status)
        battle = BattleModel(player1 = player1, player2 = player2, unique_id = unique_id, battle_status = battle_status, winner = "NULL", won_by_margin = "NULL")
        db.session.add(battle)
        db.session.commit()

    return jsonify({"Battle ID": unique_id})
    # return battles[-1].unique_id
    # return jsonify({"Winner": winner, "Battle ID": unique_id, "Winning Margin": won_by_margin})


# Retrieve Battle result.
@app.route("/api/pokemon/battle/result/<battle_id>", methods=["GET"])
def battle_result(battle_id):
    
    battle_result = BattleModel.query.filter_by(unique_id=battle_id).order_by(BattleModel.id.desc()).first()
    winner_name = battle_result.winner
    winning_margin = battle_result.won_by_margin
    battle_status = battle_result.battle_status

    return jsonify({"Status": battle_status,"result": {
        "winnerName": winner_name,
        "wonByMargin": winning_margin
    }})


if __name__ == "__main__":
    app.run(debug=True)
