from app.models import user_account

def test_new_use_model(client):
    user = user_account(username='test_username', email='test_email', password_hash='test_hash')
    assert user.username
    assert user.email
    assert user.password_hash