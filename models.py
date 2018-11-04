

class Application(db.Model):
    """ Application Model for storing application related details """
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=False, nullable=False)
    owner = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, name, email, owner):
        self.email = email
        self.name = name
        self.owner = owner

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.name = name
