import os

from flask_migrate import Migrate
from src import create_app, db

app = create_app(os.environ.get("FLASK_ENV", "default"))
migrate = Migrate(app, db, include_schemas=True)
