import json


l1 = [
    {
        "fullname": "Albert Einstein",
        "born_date": "March 14, 1879",
        "born_location": "in Ulm, Germany"
    },
    {
        "fullname": "Steve Martin",
        "born_date": "August 14, 1945",
        "born_location": "in Waco, Texas, The United States"
    }
]

l2 = [
    {
        "fullname": "Albert Einstein",
        "born_date": "March 14, 1879",
        "born_location": "in Ulm, Germany"
    },
    {
        "fullname": "Steve 02",
        "born_date": "August 14, 1945",
        "born_location": "in Waco, Texas, The United States"
    }
]
# for el in l2:
#     if el["fullname"] not in [name["fullname"] for name in l1]:
#         l1.append(el)

[l1.append(el) for el in l2 if el["fullname"]
 not in [name["fullname"] for name in l1]]

print(json.dumps(l1, indent=4, sort_keys=True))
