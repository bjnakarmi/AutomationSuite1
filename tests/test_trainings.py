from utils import api_helpers

def test_trainings():
    headers = {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDQ1ODg5MywiZXhwIjoxNzU4MjM0ODkzfQ.NzjwioGdDYDi2ZzJXo0RxkyCD6IYpXZLTJLmNVfBU60'
    }
    response = api_helpers.get_all_training(headers)
    data = response.json()
    assert response.status_code == 200
    assert 'data' in data
