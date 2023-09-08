from flask import Flask, request, jsonify, make_response

from flask_cors import CORS  # Import the CORS class

app = Flask(__name__)
CORS(app)

data = {
    "students":[{
        "name": "student1",
        "Maths": 45,
        "Science": 57,
        "English": 66,
        "Computer Science": 50,

    },{
        "name": "student2",
        "Maths": 76,
        "Science": 87,
        "English": 66,
        "Computer Science": 70,

    },{
        "name": "student3",
        "Maths": 96,
        "Science": 97,
        "English": 86,
        "Computer Science": 90,

    },
    ]
}


@app.route("/score", methods=["GET", "POST"])
def get_score():
    if request.method == "GET":
        try:
            score_data = data
            if not score_data:
                return (
                    jsonify(
                        {"error": "Score data not available."}
                    ),
                    404,
                )

            return score_data
        except Exception as e:
            return jsonify({"error": "An error occurred: {}".format(str(e))}), 500


if __name__ == "__main__":
    app.run(debug=True)
