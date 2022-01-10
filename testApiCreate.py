import requests
import json

data = "06e2097f-d5b9-407e-aec8-cc2f335708cb"
def check_status_code_equals_200():
    response = requests.post("http://45.33.71.199:31000/wallet/recordsOfWallet?walletUuid=da09f43e-3e68-49c9-a971-149dadf8c750", data=data)
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    return response

def check_body_json(response, index, title, userUuid):
    response_body = response.json()
    assert response_body[index]["title"] == title
    assert response_body[index]["userUuid"] == userUuid
    print("")
    print("title-", response_body[index]["title"])
    print("userUuid-", response_body[index]["userUuid"])

def check_content_type_equals_json(response):
    assert response.headers["Content-Type"] == "application/json"
    print("Content-Type:", response.headers["Content-Type"])




response = check_status_code_equals_200()
check_body_json(response, 0, "record 1 in the batman wallet", "06e2097f-d5b9-407e-aec8-cc2f335708cb")
check_body_json(response, 1, "Second2", "06e2097f-d5b9-407e-aec8-cc2f335708cb")
check_body_json(response, 2, "Third", "06e2097f-d5b9-407e-aec8-cc2f335708cb")
check_body_json(response, 3, "Forth", "06e2097f-d5b9-407e-aec8-cc2f335708cb")
check_body_json(response, 4, "Fifth", "06e2097f-d5b9-407e-aec8-cc2f335708cb")
check_body_json(response, 5, "Seventh", "06e2097f-d5b9-407e-aec8-cc2f335708cb")

check_content_type_equals_json(response)

