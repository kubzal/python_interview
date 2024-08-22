from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    flash,
    abort,
)
import subprocess
import tempfile
import os
import sys
import builtins
import re

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Initialize a variable to store the message
current_message = ""


# Function to validate URLs
def is_valid_url(url):
    url_regex = re.compile(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", re.IGNORECASE)
    return re.match(url_regex, url) is not None


# Context manager to temporarily disable dangerous functions and modules
class Sandbox:
    def __enter__(self):
        # Backup original functions
        self._original_open = builtins.open

        # Disable dangerous functions/modules
        builtins.open = self._restricted_open
        sys.modules["requests"] = None
        sys.modules["urllib"] = None
        sys.modules["urllib3"] = None
        sys.modules["http"] = None

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore original functions
        builtins.open = self._original_open

    def _restricted_open(self, *args, **kwargs):
        raise PermissionError("The use of 'open' is restricted in this environment.")


# @app.route("/")
# def index():
#     return "Welcome to the coding platform! Please navigate to a specific problem like /two_sum."


@app.route("/")
def index():
    # Redirect the root URL to /default
    return redirect(url_for("default"))


@app.route("/default")
def default():
    return render_template("default.html")


@app.route("/<endpoint_name>")
def serve_endpoint(endpoint_name):
    markdown_path = os.path.join("static", f"{endpoint_name}.md")
    python_code_path = os.path.join("static", f"{endpoint_name}.py")

    if not os.path.exists(markdown_path) or not os.path.exists(python_code_path):
        abort(404)

    return render_template("python_interview.html", filename=endpoint_name)


@app.route("/execute", methods=["POST"])
def execute():
    data = request.get_json()
    code = data.get("code", "")

    try:
        # Use a temporary file to execute the code
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp:
            temp.write(code.encode("utf-8"))
            temp.flush()

            with Sandbox():
                # Run the code with a timeout of 30 seconds
                result = subprocess.run(
                    ["python", temp.name],
                    capture_output=True,
                    text=True,
                    timeout=30,  # Timeout after 30 seconds
                )

        output = result.stdout if result.returncode == 0 else result.stderr
        return jsonify({"output": output})

    except subprocess.TimeoutExpired:
        return jsonify({"output": "Error: Code execution timed out after 30 seconds."})

    except PermissionError as e:
        return jsonify({"output": f"Security Error: {str(e)}"})

    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}"})


@app.route("/get_message", methods=["GET"])
def get_message():
    global current_message
    message_to_send = current_message
    current_message = ""
    return jsonify(message=message_to_send)


@app.route("/send_message_form", methods=["GET", "POST"])
def send_message_form():
    global current_message
    if request.method == "POST":
        message = request.form.get("message", "")
        url = request.form.get("url", "")
        link_text = request.form.get("link_text", "")
        password = request.form.get("password", "")

        if password != os.environ.get("MESSAGE_PASSWORD"):
            flash("Invalid password. Please try again.", "danger")
            return redirect(url_for("send_message_form"))

        if url and not is_valid_url(url):
            flash("Invalid URL. Please enter a valid URL.", "danger")
            return redirect(url_for("send_message_form"))

        if url and link_text:
            current_message = f'{message} <a href="{url}">{link_text}</a>'
        else:
            current_message = message

        flash("Message sent successfully!", "success")
        return redirect(url_for("send_message_form"))

    return render_template("send_message.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
