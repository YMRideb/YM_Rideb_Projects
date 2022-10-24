from October_2022.Recipes_cookbook.flask_app import EMAIL_REGEX
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users_crud;"
        results = connectToMySQL('dB').query_db(query)
        users = []
        for row in results:
            users.append(User(row))
        return users

    @classmethod
    def show_user(cls, data):
        query = "SELECT * FROM users_crud WHERE id = %(id)s;"
        results = connectToMySQL('dB').query_db(query, data)
        return results[0]

    @classmethod
    def update(cls, data):
        query = "UPDATE users_crud SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('dB').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users_crud WHERE id = %(id)s;"
        return connectToMySQL('dB').query_db(query, data)

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users_crud (first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL('dB').query_db(query, data)
    
    @classmethod
    def get_email_to_validate(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(dB).query_db(query, data)

        if len(result) > 0:
            current_user = cls(result[0])
            return current_user
        else:
            return None
    
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.", "error_first_name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.", "error_last_name")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", "error_email")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.", "error_pw")
            is_valid= False
        if not data['pwd_confirm'] == data['password']:
            flash("One of these is not like the other!", 'error_pwd_confirm')
            is_valid= False
        return is_valid
