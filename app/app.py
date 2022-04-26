from dotenv import dotenv_values
import pandas as pd
import requests
from flask import Flask, jsonify


def get_credits(id: int) -> int:
    """
    Returns the Credit value for given id

        Parameters:
            id (int): An Integer value

        Returns:
            credit_val (int): An Integer value
    """

    # Fetch API Key from .env
    config = dotenv_values("app/.env")
    key = config.get("KEY")

    # Sheet ID is found in sheet url -> https://sheets.googleapis.com/v4/{spreadsheets}/spreadsheetId/values/
    SPREADSHEET_ID = "1YbCifV2AiwBQi30w_pjLjqXngdgAv-FikCvQLgpjQbA"

    # Constructing URL
    url = (
        f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Sheet1"
    )

    # Sending GET request to the URL and converting the response into JSON
    res = requests.get(url, params={"key": key}).json()

    # Extracting and Converting JSON response into a Dataframe
    df = pd.DataFrame(res["values"][1:], columns=res["values"][0])

    # Extracting and Returning Credit value
    tmp2 = df.loc[df.ID == str(id), "Credits"].tolist()
    return tmp2[0]


# ---------FLASK ROUTES------------
app = Flask(__name__)


@app.route("/credits/<id>", methods=["GET"])
def get_credit(id: int):
    """
    get_credit route

    get:
        summary: get_credit endpoint.
        description: Get a single credit with the ID id

        parameters:
            name: id
            in: path
            description: id column in database
            type: integer
            required: true
        responses:
            200:
                description: JSON with credit is returned.
            500:
                description: JSON with error is returned.
    """
    try:
        data = {"credits": get_credits(id)[0]}
        return jsonify(data=data), 200
    except Exception as error:
        return jsonify(message=str(error)), 500


if __name__ == "__main__":
    app.debug = True
    app.run()
