from flask import Flask, render_template, request, send_file
from predictor_api import make_prediction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', prediction='Predict the outcome of your game !')


@app.route('/predict/', methods=['GET'])
def predict():
    blueWardsPlaced = request.args.get('blueWardsPlaced')
    blueWardsDestroyed = request.args.get('blueWardsDestroyed')
    blueFirstBlood = request.args.get('blueFirstBlood')
    blueDragons = request.args.get('blueDragons')
    blueHeralds = request.args.get('blueHeralds')
    blueTowersDestroyed = request.args.get('blueTowersDestroyed')
    blueGoldDiff = request.args.get('blueGoldDiff')
    blueExperienceDiff = request.args.get('blueExperienceDiff')
    redWardsPlaced = request.args.get('redWardsPlaced')
    redWardsDestroyed = request.args.get('redWardsDestroyed')
    redDragons = request.args.get('redDragons')
    redHeralds = request.args.get('redHeralds')
    redTowersDestroyed = request.args.get('redTowersDestroyed')
    return render_template('index.html',
                           prediction=make_prediction(blueWardsPlaced, blueWardsDestroyed, blueFirstBlood, blueDragons,
                                                      blueHeralds, blueTowersDestroyed,
                                                      blueGoldDiff, blueExperienceDiff, redWardsPlaced,
                                                      redWardsDestroyed, redDragons, redHeralds,
                                                      redTowersDestroyed))


if __name__ == '__main__':
    app.run(debug=True)
