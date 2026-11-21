

from file_parser import get_data
from quick_select import quickselect_random
from quick_select import quickselect_deterministic

from recorder import save_results

from test_data_structures import test_structures




if __name__ == "__main__":

    choice = input("Choose what do you want to test: \n Quick Select Random(r) \n ------------------ \n Quick select Deterministic(d) \n ------------------ \n Test data structures(s): ")

    

    if choice == "r":
        name = "Quick Select Random"
        select_algorithm = quickselect_random

    elif choice == "d":
        name = "Quick Select Deterministic"
        select_algorithm = quickselect_deterministic

    elif choice == "s":
        test_structures()
        exit()

    else:
        print("Wrong input, please restart the program and choose option \"r\" or \"d\" ")
        exit()


    filename = input("Select a file to get the data from for sorting: ")

    data = get_data(filename)

    k = len(data) // 2          # look for the median   

    

    save_results(name, select_algorithm, data, filename, k)