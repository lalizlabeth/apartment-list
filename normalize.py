# Elizabeth Lin
# Apartment List Coding Test

def normalize(path):
    """ Normalizes a file path. All single dot components must be removed. 
    All double dot components must be removed along with their parent directory.
        args:
            path = string that represents a file path
        returns a normalized path
    """
    if type(path) != str:
        return "Path must be of type string."

    path_lst = path.split("/")

    i = 0
    while i < len(path_lst):
        if path_lst[i] == ".":
            path_lst = path_lst[:i] + path_lst[i+1:]
        elif path_lst[i] == "..":
            path_lst = path_lst[:i-1] + path_lst[i+1:]
        i += 1

    return "/".join(path_lst)

if __name__ == "__main__":

    next = True
    yes = ["yes", "Yes", "YES", "y", "Y"]

    while next == True:
        path = raw_input("> Input path you want to normalize: ")
        print("\nInput Path: " + path)
        print("Normalized Path: " + normalize(path) + "\n")

        repeat = raw_input("> Would you like to normalize another path? ")
        next = repeat in yes

    print("\nNormalizing completed.")








