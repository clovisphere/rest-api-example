# Demo

> Rest(ful) API built with [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Usage

Make a copy of [env.sample](./env.sample) file named .env, and make sure all the **ENVIRONMENT_VARIABLES** are set.

```console
$ cp env.sample .env  # make a copy of .env.sample called .env
```

### Development

Prerequiste:

- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Docker](https://www.docker.com/)


> Clone project & CD into it
```console
$ git clone git@github.com:clovisphere/rest-api-example.git
$ cd rest-api-example/flask/demo
```

Without [Docker](https://www.docker.com/):

> Set up Flask Environment

```console
$ export PYTHONDONTWRITEBYTECODE=1  # prevent python from writing pyc files
$ export FLASK_ENV=development
$ export SECRET_KEY=$(python -c "import secrets;print(secrets.token_urlsafe(16))")
$ export SQLALCHEMY_DATABASE_URI_DEV=sqlite:///demo-dev.db
```

> Install dependencies

```console
# spaw a shell
$ poetry shell
# resolve dependencies and install them
$ poetry install
```

> Run migrations

```console
# check if they are any new operations to migrate
$ flask db check
# apply the changes described by the migration script
$ flask db upgrade
```

If you need any help with migration, please refer to [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/).

> Create dummy/test user

```console
# run a shell in the app context
$ flask shell
```

```python
# inside the (flask) shell
user = User(username='demo')
user.set_password('demo')
db.session.add(user)
db.session.commit()
exit()
```

> Start the app

```console
$ flask run --debug --host=0.0.0.0 --port=8000
```

#### Test it out

With [httpie](https://httpie.io/):

1.  */health* (health check)

**(Request)**
```console
$ http :8000/health
```

**(Response)**

 ```json
{
    "status": "healthy"
}
 ```

2. */get-auth-token* (obtain/generate **authentication token**)

**(Request)**
```console
$ http --auth demo:demo :8000/get-auth-token
```

**(Response)**
```json
{
    "token": "eyJpZCI6MX0.ZfmhLw.vK1YtdBZmUZLoD55AqKIPGuyOyA"
}
```

3. */farmers* (fetch all farmers, if any)

**(Request)**
```console
$ http -A bearer --auth 'eyJpZCI6MX0.ZfmhLw.vK1YtdBZmUZLoD55AqKIPGuyOyA' GET http://localhost:8000/api/v1/farmers
```

**(Response)**
```json
[]
```
