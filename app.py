from flask import Flask, render_template, request, redirect
from features import Features
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        """
        if "file" not in request.files:
            return redirect(request.url)

        if "machine_type" not in request.form:
            return redirect(request.url)

        file = request.files["file"]
        print(f"File: {file}")
        machine = request.form.get("machine_type")
        print(f"Machine Type: {machine}")
        if file.filename == "":
            return redirect(request.url)
        if machine == "":
            return redirect(request.url)

        if file:
            data = Features.get_features(file)
            df = pd.DataFrame(data, index=[0])
            model = Features.model_type(machine)
            prediction = Features.predict_data(df, model)

            if prediction == 1:
                print("Machine is Abnormal")
                output = f"Machine {machine}: {file.filename} is Abnormal."
            elif prediction == 0:
                print("Machine is Normal")
                output = f"Machine {machine}: {file.filename} is Normal."

            return render_template("index.html", prediction=output)
            """
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

