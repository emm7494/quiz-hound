from app import create_app, db
from app import models

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"mls": models, "db": db, "cfg": app.config}
