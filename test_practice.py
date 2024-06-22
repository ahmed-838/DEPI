def test_index_page(client):
    """Test the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Sign Up" in response.data


def test_successful_signup(client):
    """Test a successful sign-up."""
    response = client.post('/submit', data={
        'username': 'testUser',
        'mobile': '1234567890',
        'password': 'testPassword'
    })
    assert response.status_code == 200
    assert b"Sign up successful!" in response.data
    assert b"welcome : testUser" in response.data


def test_missing_field_signup(client):
    """Test sign-up with a missing field."""
    response = client.post('/submit', data={
        'username': 'testUser',
        'password': 'testPassword'
    })
    assert response.status_code == 400
    assert b"This field is required" in response.data


def test_invalid_mobile_signup(client):
    """Test sign-up with invalid mobile number."""
    response = client.post('/submit', data={
        'username': 'testUser',
        'mobile': 'invalid_mobile',
        'password': 'testPassword'
    })
    assert response.status_code == 400
    assert b"Invalid mobile number" in response.data
