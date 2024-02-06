#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()


# Example usage:
append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
