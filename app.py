from flask import Flask, render_template, request, redirect
import subprocess
from time import sleep
import os

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if 'up_button' in request.form:
            x = 1.83
            y = 0.03
            z = -1
            w = 0.01
            run_navigation(x, y, z, w)
            print("Navigating up!")
        elif 'down_button' in request.form:
            x = -1.97
            y = 0.01
            z = 0.01
            w = 0.99
            run_navigation(x, y, z, w)
            print("Navigating down!")

        return render_template("index.html")


def run_navigation(x, y, z, w):
    x = str(x)
    y = str(y)
    z = str(z)
    w = str(w)

    python_interpreter = "/usr/bin/python3"

    # Set the path to your Python script
    python_script = "/home/ubuntu/catkin_ws/src/auto_nav/scripts/goal_pose.py"

    # Run the Python script using the specified interpreter
    subprocess.run(
        [python_interpreter, python_script, x, y, z, w])


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)
