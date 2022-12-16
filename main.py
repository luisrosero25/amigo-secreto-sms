import json
import random
import requests
import base64

friends = [
    ["Andres", "316623141", "M"],
    ["Edier", "321612312312", "M"],
    ["Jose Meli", "310123123", "M"],
    ["Daniel", "32153123123", "M"],
    ["Omar", "31112312330", "M"],
    ["elver", "3151231231267766", "M"],
    ["Deicy", "321123123572", "F"],
    ["Monica", "3212321377", "F"],
    ["Nidia", "31123123067357", "F"],
    ["Alba", "314812312380", "F"],
    ["Clarita", "3231231237", "F"],
    ["Flor", "3156412312330", "F"],
    ["Melisa", "313512312335", "F"],
    ["margarita", "3112312312862", "F"],

]


def generate_friends2():
    friends_copy = friends.copy()
    random.shuffle(friends_copy)
    friends_done = []

    for friend in friends:

        random.shuffle(friends_copy)
        random.shuffle(friends_copy)
        c = 0
        find_friend = False
        for friend_c in friends_copy:
            if friend_c[0] != friend[0] and friend[2] != friend_c[2]:
                find_friend = True
                friends_done.append({'person':friend, 'friend': friend_c})
                break
            c += 1

        if not find_friend:
            c = 0
            random.shuffle(friends_copy)
            random.shuffle(friends_copy)
            for friend_c in friends_copy:
                if friend_c[0] != friend[0]:
                    friends_done.append({'person': friend, 'friend': friend_c})
                    break
                c += 1

        del friends_copy[c]

    friends_file = open('friends_filev2.txt', 'w')
    for friend_d in friends_done:
        person1 = base64.b64encode(friend_d.get('person')[0].encode('ascii'))
        person2 = base64.b64encode(friend_d.get('friend')[0].encode('ascii'))
        friends_file.writelines(F"{person1};{friend_d.get('person')[1]};{person2};{friend_d.get('friend')[1]}\n")
        send_messages(friend_d.get('person')[1], friend_d.get('friend')[0])


def send_messages(number, nombre):
    SMS_SERVICE_PLAN_ID="xxxxxxxxx"
    SMS_API_TOKEN="xxxxxxxxx"
    response = requests.post(f"https://api.clxcommunications.com/xms/v1/{SMS_SERVICE_PLAN_ID}/batches", json={
        "from":  "xxxxxxx",
        "to": [f"57{number}"],
        "body": F"AMIGO SECRETO DEFINITIVO! - Su amigo secreto es: {nombre}"
    }, headers={
        "Content-Type": "application/json",
        'Authorization': F"Bearer {SMS_API_TOKEN}"
    })

    print("Status Code", response.status_code)
    print("JSON Response ", response.json())


if __name__ == '__main__':
    """"""
    generate_friends2()
