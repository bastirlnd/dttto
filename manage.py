import getpass

from flask.cli import FlaskGroup

from dttto import app, db
from dttto.accounts.models import User

cli = FlaskGroup(app)


@cli.command("create_admin")
def create_admin():
    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return 1
    try:
        user = User(email=email, password=password, is_admin=True)
        db.session.add(user)
        db.session.commit()
        print("Admin user created successfully.")
    except Exception as e:
        print(f"Error creating admin user: {e}")
        return 1


if __name__ == "__main__":
    cli()
