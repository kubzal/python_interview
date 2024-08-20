from flask import Flask, render_template, request, jsonify, abort
import subprocess
import tempfile
import os

app = Flask(__name__)


@app.route("/")
def index():
    # Display a welcome message or instructions at the root URL
    return "Welcome to the coding platform! Please navigate to a specific problem like /two_sum."


@app.route("/<endpoint_name>")
def serve_endpoint(endpoint_name):
    # Construct paths to the markdown and python files
    markdown_path = os.path.join("static", f"{endpoint_name}.md")
    python_code_path = os.path.join("static", f"{endpoint_name}.py")

    # Check if both files exist, otherwise return 404
    if not os.path.exists(markdown_path) or not os.path.exists(python_code_path):
        abort(404)

    # Render the index.html template, passing the endpoint name to dynamically load content
    return render_template("index.html", filename=endpoint_name)


@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json()
    code = data.get("code", "")

    try:
        # Use a temporary file to execute the code
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp:
            temp.write(code.encode("utf-8"))
            temp.flush()
            result = subprocess.run(
                ["python", temp.name], capture_output=True, text=True, timeout=5
            )

        output = result.stdout if result.returncode == 0 else result.stderr
        return jsonify({"output": output})

    except subprocess.TimeoutExpired:
        return jsonify({"output": "Error: Code execution timed out."})

    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
