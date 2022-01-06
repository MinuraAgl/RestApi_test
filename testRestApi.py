import requests
def check_status_code_equals_200():
    response = requests.get("http://45.33.71.199:31000/user/subscriptions?uuid=06e2097f-d5b9-407e-aec8-cc2f335708cb")
    assert response.status_code == 200
    print(response.status_code)
    return response

def check_body_json(response, index, title, subsType):
    response_body = response.json()
    assert response_body[index]["title"] == title
    assert response_body[index]["subsType"] == subsType
    print(response_body[index]["title"])
    print(response_body[index]["subsType"])


def check_content_type_equals_json(response):
    assert response.headers["Content-Type"] == "application/json"
    print(response.headers["Content-Type"])

# main
response = check_status_code_equals_200()
check_body_json(response, 0, "batman wallet", "OWNER")
check_body_json(response, 1, "second batman's wallet", "OWNER")
check_body_json(response, 2, "third test wallet3", "OWNER")
check_body_json(response, 3, "Forth wallet1", "OWNER")
check_body_json(response, 4, "Fifth", "OWNER")
check_body_json(response, 5, "Sixth", "OWNER")
check_body_json(response, 6, "Seventh wallet", "OWNER")
check_body_json(response, 7, "Eighth wallet", "OWNER")
check_body_json(response, 8, "Storage 1", "OWNER")
check_body_json(response, 9, "sups second wallet", "ADMIN")
check_body_json(response, 10, "sups second wallet", "ADMIN")
check_body_json(response, 11, "sups third wallet", "USER")

check_content_type_equals_json(response)