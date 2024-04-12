import os

from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

core_bp = Blueprint("core", __name__)


@core_bp.route("/")
@login_required
def home():
    return render_template("core/index.html")


@core_bp.route("/list_transcripts", methods=["GET", "POST"])
@login_required
def list_transcripts():
    return redirect(url_for("core.transcript_list"))


@core_bp.route("/transcript_list")
@login_required
def transcript_list():
    cwd = os.getcwd()
    transcript_list = os.listdir(f"{cwd}/dttto/transcripts")
    return render_template("core/transcript_list.html", transcript_list=transcript_list)


@core_bp.route("/transcript/<string:transcript_name>")
@login_required
def transcript(transcript_name):
    cwd = os.getcwd()
    with open(f"{cwd}/dttto/transcripts/{transcript_name}") as html_transcript:
        return html_transcript.read()
