# Flask Google Sheets API Assignment

## Run Locally

1. Clone the Project.
```bash
git clone https://github.com/darshan527/Flask-Assignment.git
```
2. Goto the Project directory
```bash
cd Flask-Assignment
```
3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

4. Create an API Key from Google Console to access Sheets API, Check the following Link for reference. Complete the Prerequisites step from here [https://developers.google.com/sheets/api/quickstart/python](https://developers.google.com/sheets/api/quickstart/python)

5. Create .env file in app/ directory
```bash
touch app/.env
```

6. Paste your API key in .env file
```.env
KEY=<YOUR API KEY>
```

7. Start the program
```bash
python3 app/__init__.py
```
## Usage
Open Postman or any Browser and go to the following URL to test the REST Endpoint.
Replace host-name and port number with respect to your server.
Replace id with ID from database.

[http://localhost:port/credits/id](http://localhost:5000/credits/112)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
