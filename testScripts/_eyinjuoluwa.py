data = {
    "firstname": "Abiodun",
    "lastname": "Sotunde",
    "id": "HNG-04130",
    "language": "Python",
    "email": "barbieadol@gmail.com",
}


def output():
    print(
        "Hello World, this is [{0}] [{1}] with HNGi7 ID [{2}] using [{3}] for stage 2 task. {4}".format(
            data["firstname"],
            data["lastname"],
            data["id"],
            data["language"],
            data["email"],
        )
    )


output()
