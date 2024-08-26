## Python Interview Task Platform

This repository contains a Flask-based platform for running and testing Python interview tasks. The platform allows you to dynamically load problem descriptions and corresponding Python code into a web-based editor, execute the code, and view the output. It is designed to be secure, preventing the code from making external API calls or performing other restricted actions.

### Features

- **Dynamic Task Loading**: Tasks are dynamically loaded based on the URL endpoint.
- **Code Execution with Timeout**: Python code execution is limited to 30 seconds to prevent long-running tasks.
- **Security**: Restricts access to external URLs and certain built-in functions to ensure the safe execution of user code.
- **Dockerized**: Easily deploy the application using Docker.
- **Broadcast Messages**: Send pop-up messages to all users who have the app open via a dedicated endpoint.

### Getting Started

#### Custom Task Setup

To add a new task:

1. Place your Markdown file (e.g., `custom_task.md`) containing the problem description in the `tasks` directory.
2. Place the corresponding Python code file (e.g., `custom_task.py`) in the `tasks` directory.
3. Access the task by navigating to `http://localhost:5000/custom_task` after starting the Flask app.

#### Running the Application Locally with Docker

To run the platform locally using Docker:

1. Clone the repository:

    ```bash
    git clone https://github.com/kubzal/python_interview.git
    cd python_interview
    ```

2. Build the Docker image:

    ```bash
    docker build -t python_interview .
    ```

3. Run the Docker container with environment variables for `SECRET_KEY` and `MESSAGE_PASSWORD`:

    ```bash
    docker run -d -p 5000:5000 --name python_interview \
    -e SECRET_KEY="your_secret_key_here" \
    -e MESSAGE_PASSWORD="your_message_password_here" \
    python_interview
    ```

4. Access the platform in your browser at `http://localhost:5000/`.

Replace `"your_secret_key_here"` and `"your_message_password_here"` with your desired values for the secret key and message password.

#### Sending Broadcast Messages

The platform includes a tool that allows administrators to send pop-up messages to all users who have the app open. This can be accessed via the `/send_message_form` endpoint.

- Navigate to `http://localhost:5000/send_message_form` to access the form.
- Enter the message you wish to broadcast, and if desired, include a URL and hyperlink text.
- Validate the message with the password defined in the `MESSAGE_PASSWORD` environment variable.
- Once sent, the message will pop up for all users currently viewing the platform.

#### Example Task

A working demo of the platform is available at: [https://kubzal.cytr.us/two_sum](https://kubzal.cytr.us/two_sum).

This demo shows the `two_sum` task, where you can see how the task description is loaded from `two_sum.md` and the code is loaded from `two_sum.py`.

### Contributing

If you would like to contribute to the project, feel free to open an issue or submit a pull request. Contributions to improve the security, performance, or functionality of the platform are welcome.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

If you have any questions or need further assistance, feel free to contact me through the issue tracker or via email at jakub.zalewski93@gmail.com.
