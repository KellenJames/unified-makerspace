import yaml
from flask import Flask, session, request
from flask_cors import CORS
import sys

sys.path.append("../../api")
from models import User, Task



app = Flask('__name__')
CORS(app)
app.config['SECRET_KEY'] = "testing"


# todo add auth tokens
# todo implement
# todo update documentation with task_name
# todo refactor files
# todo load user

# todo make this a dict...?
test_user = User(first_name='Joe', last_name='Goldberg',
                 user_id="213", assigned_tasks=[],
                 permissions=[]).__dict__

test_users = [test_user]

# load data

def fetch_tasks():
    with open('./test_data/tasks.yaml') as f:
        data = yaml.safe_load(f)
        return [Task(**task).__dict__ for task in data["tasks"]]



# todo return auth token
@app.route('/api/users', methods=['POST'])
def login():
    return dict(code=200, user=test_user)


@app.route('/api/users', methods=['PUT'])
def create_user():
    return dict(code=200, user=test_user)


@app.route('/api/users', methods=['DELETE'])
def delete_user():
    return dict(code=200, message="User has been successfully deleted.")


@app.route('/api/users', methods=['GET'])
def get_users():
    return dict(code=200, users=test_users)


# todo implement
@app.route('/api/users', methods=['PATCH'])
def update_user():
    pass


# tasks

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    if not 'tasks' in session:
        session['tasks'] = fetch_tasks()
        session.modified = True
    return dict(code=200, tasks=session['tasks'])


@app.route('/api/tasks', methods=['POST'])
def create_task():
    pass


@app.route('/api/tasks', methods=['DELETE'])
def resolve_task():
    tasks = session['tasks']
    # list(filter(lambda t: t.task_id == request.json['task_id'], tasks))
    return dict(code=200)


@app.route('/api/tasks', methods=['UPDATE'])
def update_task():
    pass


# machines
# todo validate with machiense
# todo put this in example server

@app.route('/api/machines', methods=['GET'])
def get_machines_status():
    with open('test_data/machines.yaml') as f:
        machines = yaml.load(f)
    return dict(code=200, machines=machines)