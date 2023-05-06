def test_get_authors_no_records(client):
    response = client.get('/api/v1/authors')
    expected_result = {
        'success': True,
        'data': [],
        'pagination': {
            'total_pages': 0,
            'total_records': 0,
            'current_page': '/api/v1/authors?page=1'
        }
    }

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.get_json() == expected_result


def test_get_authors(client, sample_data):
    response = client.get('/api/v1/authors')
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is True
    assert len(response_data['data']) == 5
    assert response_data['pagination'] == {
        'total_pages': 2,
        'total_records': 10,
        'current_page': '/api/v1/authors?page=1',
    }


def test_get_single_author(client, sample_data):
    response = client.get('/api/v1/authors/9')
    response_data = response.get_json()
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is True
    assert response_data['data']['first_name'] == 'Andrzej'
    assert response_data['data']['last_name'] == 'Sapkowski'
    assert response_data['data']['birth_date'] == '21-06-1948'
    assert len(response_data['data']['books']) == 1


def test_get_single_author(client, sample_data):
    response = client.get('/api/v1/authors/25')
    response_data = response.get_json()
    assert response.status_code == 404
    assert response.headers['Content-Type'] == 'application/json'
    assert response_data['success'] is False
    assert 'data' not in response_data
