
def test_signup_new_account(app):
    username = "user1122"
    password = "test"
    app.james.ensure_user_exists(username, password)