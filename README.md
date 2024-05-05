# 3DPackagingProblemSolution
As is known to all, packaging problem is currently a NP-hard question. Inspired by Problem C of 2024 Beijing Intercollegiate Mathematical Modeling Competition, I develop an algorithm attempting to find out one solution of the 3D packaging problem.

This is a program written based on the backtracking algorithm, mainly exploring the existence of solutions by searching the entire solution space.

When calling the function, you can follow the example in the main() function. The try_box function requires two parameters: the first parameter is the dimensions of the box (tuple type), and the second parameter is a list type containing tuples, where each tuple represents the dimensions of a rectangular prism. You can initially assume that the length of the rectangular prism is greater than or equal to its width, and its width is greater than or equal to its height.

After running, if a solution is found, it can be returned immediately. The format of the solution is a list containing multiple tuples, each tuple representing a way of placing a rectangular prism. Each tuple contains two tuples: the first one represents the lengths of the rectangular prism parallel to the length, width, and height of the box, mainly reflecting the rotation of the rectangular prism; the second one represents the coordinates of the lower left front corner of the rectangular prism. These coordinates are in the space rectangular coordinate system established with the lower left front corner of the box as the origin, the length of the box as the x-axis, the width as the y-axis, and the height as the z-axis. If no solution is found, return an empty list [].

It is worth noting that this algorithm can only solve when all the edge length data of the box and rectangular prisms have the minimum resolution value. For example, if their accuracies are all 1 mm, then when entering the data, please convert all length parameters to centimeters, so that inputs with up to one decimal place are acceptable. The unit of the tuple representing the rotation information of each rectangular prism in the output is centimeters, and the unit of the tuple representing the coordinate information is millimeters.

For example:

```
import packing_check_v2 as pc

box_dimensions = (22, 15, 9)  # Unit: centimeters
items = [(15.0, 5.5, 5.5), (15.0, 5.5, 5.5), (19.5, 9.0, 3.1)]  # Unit: centimeters
resulting_solutions = pc.try_box(box_dimensions, items)

if resulting_solutions:
    print(resulting_solutions[0])
else:
    print("They can't be packed by the given box.")
```
    
This example will display` [((19.5, 9.0, 3.1), (0, 0, 0)), ((15.0, 5.5, 5.5), (0, 0, 31)), ((15.0, 5.5, 5.5), (0, 55, 31))]`, which means the rectangular prism (19.5,9.0,3.1) is not rotated and placed at position (0,0,0) (the lower left front corner of the box), and two rectangular prisms (15.0,5.5,5.5) are also not rotated, one placed at coordinates (0,0,31mm)=(0,0,3.1cm), and the other placed at (0, 55mm, 31mm)=(0, 5.5cm, 3.1cm).

## 三维装箱问题使用说明（中文版）

众所周知，装箱问题目前是一个NP问题。受2024年北京高校数学建模校际联赛C题的启发，我开发了一种算法，试图找出三维装箱问题的一个解。

这是一个基于回溯算法编写的程序，主要通过搜索全部解空间来探究解的存在性。
调用函数时，你可以按照main()函数的示例。其中try_box函数需要传入的第一个参数是包装箱的长宽高（tuple类型），第二个参数是一个list类型，里面的元素是tuple，每一个tuple表示一个长方体的长宽高。你可以初始假定长方体的长大于等于宽大于等于高。

运行后，如果找到一个解，可以立即返回这个解。解的格式是一个list，里面有很多个tuple，每个tuple表示一个长方体块的摆放方式。tuple里面包含了两个tuple，第一个是长方体块平行于包装箱长、宽、高三边的长度，主要反映了长方体块的旋转情况；第二个是长方体块左下前角的坐标。这个坐标是以包装箱左下前角为原点，包装箱的长为x轴，宽为y轴，高为z轴建立的空间直角坐标系中的坐标。如果找不到，返回空列表[]。

值得注意的是，这个算法只能解决包装箱和长方体块的所有边长数据有最小分度值的时候。例如，他们的精确度都是1mm，那么输入的时候请将所有的长度参数转化为厘米单位，这样最多能够接受有一位小数的输入。输出的参数中代表每个长方体块的旋转信息的tuple单位是厘米，代表坐标信息的tuple单位是毫米。

例如：

```
import packing_check_v2 as pc

box_dimensions = (22, 15, 9)  #单位：厘米
items = [(15.0, 5.5, 5.5), (15.0, 5.5, 5.5), (19.5, 9.0, 3.1)]  #单位：厘米
resulting_solutions = try_box(box_dimensions, items)

if resulting_solutions:
    print(resulting_solutions[0])
else:
    print('装不进去。')
```

这个例子会显示`[((19.5, 9.0, 3.1), (0, 0, 0)), ((15.0, 5.5, 5.5), (0, 0, 31)), ((15.0, 5.5, 5.5), (0, 55, 31))]`，即长方体块(19.5,9.0,3.1)不用旋转，放在(0,0,0)的位置（包装箱的左下前角），两个长方体块(15.0,5.5,5.5)也不用旋转，一个放在坐标(0,0,31mm)=(0,0,3.1cm)处，另一个放在(0, 55mm, 31mm)=(0, 5.5cm, 3.1cm)处。
