# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:

```bash
$ poetry run flask run
```

You should see output similar to the following:

```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running with Docker

To run the app in a docker container, run from the root directory of the project:

```bash
$ docker build --tag todo-app:dev --target development .
```

then run:

```bash
$ docker run -p 5000:5000 --env-file .env --mount "type=bind,source=$(pwd)/todo_app,target=/opt/app/todo_app" todo-app:dev
```

Alternatively, you can use docker compose to start the app in a container with:

```bash
$ docker compose up
```

## Testing

To run the tests, run:

```bash
$ poetry run pytest
```

To run pytest in a specific directory, provide the path:

```bash
$ poetry run pytest path/to/test
```

To run pytest in a container run:

```bash
$ docker build --target test --tag todo-app:test .
$ docker run todo-app:test
```

## Provisioning a VM from an Ansible Control Node

To run the app in a VM:

1. Connect to your Control Node using `ssh USERNAME@IP-ADDRESS`
2. Copy over contents of the ansible folder to your Control Node
3. Add the IP address of your managed node under the `webservers` group in `ansible_inventory.ini`
4. Run the playbook with `ansible-playbook ansible_playbook.yml -i ansible_inventory.ini`
   - you will be prompted to enter the relevant details from your local .env file
   - after successfully running the playbook, you should be able to run the app by entering `MANAGED-NODE-IP-ADDRESS:5000` in a browser
