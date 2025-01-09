def create_profile(name, **details):
    res = {"name" : name}
    for key, value in details.items():
        res[key] = value
    return res

profile = create_profile("Alice", age=30, profession="Engineer")
print(profile)
