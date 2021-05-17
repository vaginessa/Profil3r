from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

def api(self):
    # create the Flask app
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    CORS(app)

    @app.route('/search/<profile>', methods = ['POST'])
    def search(profile):
        # results inititialization
        self.result = {}

        # parameters : items, separators and modules
        self.items = profile.split(" ")
        self.separators = request.get_json()["separators"]
        self.modules_update(request.get_json()["services"])

        modules = self.get_report_modules()

        self.get_permutations()

        for module in modules:
            thread = threading.Thread(target=self.modules[module]["method"](verbose=False))
            thread.start()
            thread.join()

        return jsonify(self.result)

    app.run(port=8081)