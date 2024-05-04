# 3DPackingProblemSolution
As is known to all, packing problem is currently a NP-hard question. Inspired by Problem C of 2024 Beijing Intercollegiate Mathematical Modeling Competition, I develop an algorithm attempting to find out one solution of the 3D packing problem.


This is a program written based on the backtracking algorithm, mainly exploring the existence of solutions by searching the entire solution space.

When calling the function, you can follow the example in the main() function. The try_box function requires two parameters: the first parameter is the dimensions of the box (tuple type), and the second parameter is a list type containing tuples, where each tuple represents the dimensions of a rectangular prism. You can initially assume that the length of the rectangular prism is greater than or equal to its width, and its width is greater than or equal to its height.

After running, if a solution is found, it can be returned immediately. The format of the solution is a list containing multiple tuples, each tuple representing a way of placing a rectangular prism. Each tuple contains two tuples: the first one represents the lengths of the rectangular prism parallel to the length, width, and height of the box, mainly reflecting the rotation of the rectangular prism; the second one represents the coordinates of the lower left front corner of the rectangular prism. These coordinates are in the space rectangular coordinate system established with the lower left front corner of the box as the origin, the length of the box as the x-axis, the width as the y-axis, and the height as the z-axis. If no solution is found, return an empty list [].

It is worth noting that this algorithm can only solve when all the edge length data of the box and rectangular prisms have the minimum resolution value. For example, if their accuracies are all 1 mm, then when entering the data, please convert all length parameters to centimeters, so that inputs with up to one decimal place are acceptable. The unit of the tuple representing the rotation information of each rectangular prism in the output is centimeters, and the unit of the tuple representing the coordinate information is millimeters.

For example:

python
Copy code
box_dimensions = (22, 15, 9)  # Unit: centimeters
items = [(15.0, 5.5, 5.5), (15.0, 5.5, 5.5), (19.5, 9.0, 3.1)]  # Unit: centimeters
resulting_solutions = try_box(box_dimensions, items)
if resulting_solutions:
    print(resulting_solutions[0])
else:
    print("They can't be packed by the given box.")
    
This example will display [((19.5, 9.0, 3.1), (0, 0, 0)), ((15.0, 5.5, 5.5), (0, 0, 31)), ((15.0, 5.5, 5.5), (0, 55, 31))], which means the rectangular prism (19.5,9.0,3.1) is not rotated and placed at position (0,0,0) (the lower left front corner of the box), and two rectangular prisms (15.0,5.5,5.5) are also not rotated, one placed at coordinates (0,0,31mm)=(0,0,3.1cm), and the other placed at (0, 55mm, 31mm)=(0, 5.5cm, 3.1cm).
