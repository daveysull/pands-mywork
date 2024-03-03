
car = {
    "make" : "toyota",
    "model" : "carola",
    "year" : 2003,
    "owner" : {
        "name" : "dave",
        "driver-number" : 1234
    }
}

for key in car:
    print(key, 'has value', car[key])