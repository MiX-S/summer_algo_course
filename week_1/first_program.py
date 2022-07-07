# Python module to execute

def sort_array(array):
   sorted_array = sorted(array)
   return sorted_array


if __name__ == "__main__":
    array = [1, 6, 2, 5 , 3]
    print(array)

    sorted_array = sort_array(array)
    print(sorted_array)