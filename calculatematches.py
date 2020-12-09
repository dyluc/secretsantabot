from random import randint


def is_valid(name, other_name, matches):  # internal func -> used in return_matches()
    if name == other_name:  # Same person
        return False
    # Declare any other conditions here
    if (name.lower() == "ben") and (other_name.lower() == "emily"):
        return False
    elif (name.lower() == "emily") and (other_name.lower() == "ben"):
        return False

    try:
        if matches[other_name] == name:
            return False
        elif matches[other_name] != name:
            return True
    except KeyError:
        return True


def return_matches(names):
    matches = {}
    remaining_names = names.copy()
    while len(matches) != len(names):
        for name in names:
            rand_index = randint(0, len(remaining_names) - 1)
            valid = is_valid(name, remaining_names[rand_index], matches)
            if (len(remaining_names) == 1) and (valid is False):  # if last iteration
                matches = {}  # empty dictionary
                remaining_names = names.copy()
                break
            while valid is False:
                rand_index = randint(0, len(remaining_names) - 1)
                valid = is_valid(name, remaining_names[rand_index], matches)
            matches[name] = remaining_names[rand_index]
            del remaining_names[rand_index]
    return matches
