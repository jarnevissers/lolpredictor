import joblib

model = joblib.load('static/models/finalized_model.joblib')


def make_prediction(blueWardsPlaced, blueWardsDestroyed, blueFirstBlood, blueDragons, blueHeralds, blueTowersDestroyed,
                    blueGoldDiff, blueExperienceDiff, redWardsPlaced, redWardsDestroyed, redDragons, redHeralds,
                    redTowersDestroyed):
    win = model.predict(
        [[blueWardsPlaced, blueWardsDestroyed, blueFirstBlood, blueDragons, blueHeralds, blueTowersDestroyed,
          blueGoldDiff, blueExperienceDiff, redWardsPlaced, redWardsDestroyed, redDragons, redHeralds,
          redTowersDestroyed]])[0]
    team = 'BLUE' if win else 'RED'
    return team + ' will win!'
