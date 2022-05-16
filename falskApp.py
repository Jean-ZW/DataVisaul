#flaskApp.py

# from bokeh.client import pull_session
# from bokeh.embed import server_session
from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__, template_folder="templates", static_folder="static")

# locally creates a page

@app.route('/', methods = ['GET', 'POST'])
def index():
#     with pull_session(url="http://localhost:5006/") as session:
#             script_ghge = server_session(session_id=session.id, url='http://localhost:5006/')
#     with pull_session(url="http://localhost:5007/") as session:
#             script_wholesales = server_session(session_id=session.id, url='http://localhost:5007/')
#     with pull_session(url="http://localhost:5008/") as session:
#             script_re = server_session(session_id=session.id, url='http://localhost:5008/')
#     with pull_session(url="http://localhost:5009/") as session:
#             script_tariff = server_session(session_id=session.id, url='http://localhost:5009/')
    # use the script in the rendered page
    return render_template("Dashboard.html", 
                        #     script_ghge=script_ghge,
                        #     script_wholesales=script_wholesales, 
                        #     script_re = script_re,
                        #     script_tariff=script_tariff,
                            template="Flask",)


if __name__ == '__main__':
    # runs app in debug mode
    app.run(port=5000)