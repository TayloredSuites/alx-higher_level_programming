#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    name_spaces = dir(hidden_4)

    for name in name_spaces:
        if "__" not in name:
            print(name)
