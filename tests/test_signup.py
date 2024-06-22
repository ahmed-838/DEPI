from main import app

def test_index_page():
    """Test the index page loads correctly."""
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Sign Up" in response.data
        print(response.data)


def test_successful_signup():
    """Test a successful sign-up."""
    with app.test_client() as test_client:
        response = test_client.post('/submit', data={
        'username': 'testUser',
        'mobile': '1234567890',
        'password': 'testPassword'
        })
        assert response.status_code == 200
        assert b"Sign up successful!" in response.data
        assert b"welcome : testUser" in response.data


def test_missing_field_signup():
    """Test sign-up with a missing field."""
    with app.test_client() as test_client:
        response = test_client.post('/submit', data={
            'username' : 'username',
            'mobile' : '0123456789'
            })
        assert response.status_code == 400
        assert b"this field is required "


def test_invalid_mobile_signup():
    """Test sign-up with invalid mobile number."""
    with app.test_client() as test_client:
        response = test_client.post('/submit', data={
        'username': 'testUser',
        'mobile': 'invalid_mobile',
        'password': 'testPassword'
        })
    assert response.status_code == 400
    assert b"Invalid mobile number" in response.data
