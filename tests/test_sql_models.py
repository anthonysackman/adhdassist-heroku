from app.models import user_account

def test_new_use_model(client):
    user = user_account(email='test_email')
    user.set_password('test')
    assert user.email
    assert user.check_password('test')