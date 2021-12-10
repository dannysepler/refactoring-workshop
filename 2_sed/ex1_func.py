def find_koala(*, name) -> str:
    my_koala = f"koala {name}"
    return my_koala

joe = find_koala(name="joe")
jack = find_koala(name="jack")

print(f"found {joe} and {jack}")
