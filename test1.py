import requests
def check_status_code_equals_200():
    response = requests.get("http://45.33.71.199:31000/user/subscriptions?uuid=06e2097f-d5b9-407e-aec8-cc2f335708cb")
    assert response.status_code == 200
    print(response.status_code)

check_status_code_equals_200()
