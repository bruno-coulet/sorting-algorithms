import random, statistics, os
from sorting import *
from time import time
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.patches import Rectangle
import numpy as np
from time import perf_counter
class CreateList:
    def __init__(self, length, min_value, max_value):
        self.length = length
        self.min_value = min_value
        self.max_value = max_value

    def generate_list(self):
        """
        Generates a list of random numbers.

        Returns:
            list: A list of random real numbers.
        """
        generated_list = [round(random.uniform(self.min_value, self.max_value), 1) for _ in range(self.length)]
        return generated_list

def plot_unordered_list(unordered_list):
    plt.figure(figsize=(10, 5))
    plt.plot(unordered_list, color='gray', label='Non triée')
    plt.xlabel('Indices of elements')
    plt.ylabel('Random values')
    plt.title('Unsorted list')
    plt.legend()
    plt.tight_layout()
    plt.show()
 
if __name__ == "__main__": 

    # Asks the user the size of the list, creates the list
    length = int(input ("\nChoose a list length : ")) 
    min_value = 0.1 
    max_value = 1000.0 
    createList = CreateList(length, min_value, max_value) 
    unordered_list = createList.generate_list() 
    print(f"\nA list of {length} real numbers has been generated.\n")

    # Prints the available sorting methods
    for i in range(1,8):
        print(f"Sort {['selection', 'bubble', 'insertion', 'merge', 'quick', 'heap', 'comb'][i-1]} - \033[94m{i}\033[0m")

    # Asks the user which method he wishes to execute
    sort = int(input("\nChoose the number corresponding to the desired sorting method : "))

    # Mapping the sort methods and their corresponding classes
    sorting_methods = {
        1: (Selection, "selection sort"),
        2: (Bulle, "bubble sort"),
        3: (Insertion, "insertion sort"),
        4: (Fusion, "merge sort"),
        5: (Quick, "quick sort"),
        6: (Heap, "heap sort"),
        7: (Comb, "comb sort")
    }

    # Executes the sorting method & displays the graphic
    if sort in sorting_methods:
        sorting_class, method_name = sorting_methods[sort]
        sorting_instance = sorting_class(unordered_list)
        
        # start_time = time()
        start_time = perf_counter()
        if hasattr(sorting_instance, 'sort_method'):
            sorted_list = sorting_instance.sort_method()
        else:
            sorted_list = sorting_instance.selection_sort() if sort == 1 else sorting_instance.bubble_sort() if sort == 2 else sorting_instance.insertion_sort() if sort == 3 else sorting_instance.fusion_sort(unordered_list) if sort == 4 else sorting_instance.quick_sort(unordered_list) if sort == 5 else sorting_instance.heap_sort(unordered_list) if sort == 6 else sorting_instance.comb_sort(unordered_list) if sort == 7 else None

        # stop_time = time()
        stop_time = perf_counter()
        elapsed_time = (stop_time - start_time) * 1000
        
        print("\n", sorted_list)
        print(f"\nList of \033[94m{length}\033[0m entries sorted in \033[94m{elapsed_time:.2f}\033[0m ms using the \033[94m{method_name}\033[0m method.\n")



# --------------------------------------------------------------------------------------------------

        # Normalize the sorted list to map it to colors
        norm = Normalize(vmin=min(sorted_list), vmax=max(sorted_list))
        # Create a colormap
        cmap = plt.get_cmap('viridis')

# --------------------------------------------------------------------------------------------------

        # Plot the sorted list with colors in a pie chart
        plt.figure(figsize=(10, 10), facecolor='black')
        # fig, ax = plt.subplots(figsize=(12, 6))

        colors = [cmap(norm(value)) for value in sorted_list]
        # plt.title(f"{method_name} from {length} random values ​​between 0 and 1000 inclusive {elapsed_time:.3f} ms.", color='white')
# --------------------------------------------------------------------------------------------------        
        # STATIC VERSION
        # plt.pie(sorted_list, startangle=140, colors=colors)
# --------------------------------------------------------------------------------------------------
        # # PROGRESSIVE VERSION 
        for i in range(len(sorted_list)):
            # Updates the graph at each iteration
            plt.pie(sorted_list[:i+1], startangle=140, colors=colors)
            plt.pause(0.000000001)
# --------------------------------------------------------------------------------------------------
        # ADDS A LEGEND
        max_value = int(max(sorted_list))
        # Divides the values in range 100
        value_ranges = [(i, min(i + 99, max_value)) for i in range(0, max_value, 100)]

        # Value ranges and their corresponding colors
        legend_labels = {f"{start}-{end}": cmap(norm((start + end) / 2)) for start, end in value_ranges}

        # Patch list for the legend with colored squares
        legend_patches = [
            Rectangle((0, 0), 1, 1, color=color, label=label) 
            for label, color in legend_labels.items()
        ]


        plt.legend(handles=legend_patches, loc='upper right', bbox_to_anchor=(1.2, 0.75), facecolor='black', edgecolor='white', fontsize=12, labelcolor='white')

# --------------------------------------------------------------------------------------------------
        # Saves the plot into the project folder
        # plt.savefig('pie_chart.png', transparent=True)

        plt.show()

        # Creates the Markdown table
        table = f"| {length} | {method_name} | {elapsed_time:.3f} ms |\n"

        # Creates the README.md file if needed
        if not os.path.exists("README.md"):
            with open("README.md", "w") as readme_file:
                # readme_file.write("Creating a tool for automating sorting of objects containing the following sorts:\n")
                # readme_file.write("1. Selection sort\n2. Bubble sort\n3. Insertion sort\n4. Merge sort\n5. Quick sort\n6. Heap sort\n7. Comb sort \n")
                # readme_file.write("\n Instructions \n Input a number to determine your list’s length.\nThe program creates a list of random natural numbers.\n Choose a sort within the sorts available.\n The program :\n sorts the list \n displays the ordered list in the terminal\n returns the length of the list, the name of the sorting method and the execution time in a table\n displays a pie graph of the ordered list \n")
                readme_file.write("\n| Number of natural numbers in the list | Sorting method | Execution time |\n")
                readme_file.write("| -------------- | ------------- | ----------------- |\n")
                readme_file.write(table)
        #  Writes a new line in the table in README.md
        else:
            try:
                with open("README.md", "a") as readme_file:
                    readme_file.write(table)
                print("A line has been successfully added to the README.md file.")
            except Exception as e:
                print(f"An error occurred while adding the line to the README.md file : {e}")

    else:
        print("The selected sorting method is not valid.")

