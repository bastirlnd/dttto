import os

from dttto import app, render_template


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/transcript_list")
def transcript_list():
    cwd = os.getcwd()
    transcript_list = os.listdir(f"{cwd}/transcripts")
    return render_template("transcript_list.html", transcript_list=transcript_list)


@app.route("/transcript/<string:transcript_name>")
def transcript(transcript_name):
    with open(f"transcripts/{transcript_name}") as html_transcript:
        return html_transcript.read()


if __name__ == "dttto":
    app.run(debug=True)
