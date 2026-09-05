records = [("foo", 1, 2), ("bar", "hello"), ("foo", 3, 4)]

def do_foo(x, y):
    print(f"foo: {x}, {y}")

def do_bar(s):
    print(f"bar: {s}")

if __name__ == "__main__":
    for tag, *args in records:
        if tag == "foo":
            do_foo(*args)
        if tag == "bar":
            do_bar(*args)