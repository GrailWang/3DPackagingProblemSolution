import time
import sys
# 设置新的递归深度限制
new_limit = 5000  # 设置为您希望的新的递归深度限制
sys.setrecursionlimit(new_limit)

def pick_the_biggest(items_dim):
    # items_dim:[(L1,W1,H1),(L1,W2,H2),...]
    v_max=0
    l_max,w_max,h_max=0,0,0
    for l,w,h in items_dim:
        V=l*w*h
        if V>v_max:
            v_max=V
            l_max,w_max,h_max=l,w,h
    return (l_max,w_max,h_max)
def orient(pqr,o):
    p,q,r=pqr
    if o==1:
        return (p,q,r)
    if o==2:
        return (p,r,q)
    if o==3:
        return (q,p,r)
    if o==4:
        return (q,r,p)
    if o==5:
        return (r,p,q)
    if o==6:
        return (r,q,p)
    print('Error input of o!')
    return None

def change_xyz_into_index(xyz):
    # xyz:(x,y,z)
    x,y,z=xyz
    nx=int(x*10)
    ny=int(y*10)
    nz=int(z*10)
    return (nx,ny,nz)

def check_valid_state(package,latest_xyz,latest_XYZ):
    # package:一个三维空间填充数组(初始化要ZYX)
    # latest_xyz:(latest_x,latest_y,latest_z)
    # latest_XYZ:(latest_X,latest_Y,latest_Z)
    begin_index_x,begin_index_y,begin_index_z=latest_xyz
    add_x,add_y,add_z=change_xyz_into_index(latest_XYZ)
    end_index_x,end_index_y,end_index_z=begin_index_x+add_x,begin_index_y+add_y,begin_index_z+add_z
    x_max=len(package)
    y_max=len(package[0])
    z_max=len(package[0][0])
    # print(begin_index_x,end_index_x)
    # print(begin_index_y,end_index_y)
    # print(begin_index_z,end_index_z)
    if end_index_x > x_max:
        return False
    if end_index_y > y_max:
        return False
    if end_index_z > z_max:
        return False
    for i in range(begin_index_x,end_index_x):
        for j in range(begin_index_y,end_index_y):
            for k in range(begin_index_z,end_index_z):
                # print(i,j,k)
                if package[i][j][k]==1:
                    # print(i,j,k)
                    return False
    return True

def check_filled_space(package,latest_xyz,latest_XYZ):
    # package:一个三维空间填充数组(初始化要ZYX)
    # latest_xyz:(latest_x,latest_y,latest_z)
    # latest_XYZ:(latest_X,latest_Y,latest_Z)
    begin_index_x,begin_index_y,begin_index_z=latest_xyz
    add_x,add_y,add_z=change_xyz_into_index(latest_XYZ)
    end_index_x,end_index_y,end_index_z=begin_index_x+add_x,begin_index_y+add_y,begin_index_z+add_z
    x_max=len(package)
    y_max=len(package[0])
    z_max=len(package[0][0])
    # print(begin_index_x,end_index_x)
    # print(begin_index_y,end_index_y)
    # print(begin_index_z,end_index_z)
    if end_index_x > x_max:
        print('Index out')
        raise IndexError
    if end_index_y > y_max:
        print('Index out')
        raise IndexError
    if end_index_z > z_max:
        print('Index out')
        raise IndexError
    for i in range(begin_index_x,end_index_x):
        for j in range(begin_index_y,end_index_y):
            for k in range(begin_index_z,end_index_z):
                # print(i,j,k)
                if package[i][j][k]==0:
                    # print(i,j,k)
                    return False
    return True

def place_item(package, item_lwh, position):
    # item_lwh: (length, width, height)
    # position: (x, y, z)
    begin_index_x,begin_index_y,begin_index_z=position
    add_x,add_y,add_z=change_xyz_into_index(item_lwh)
    end_index_x,end_index_y,end_index_z=begin_index_x+add_x,begin_index_y+add_y,begin_index_z+add_z
    # print(begin_index_x,end_index_x)
    # print(begin_index_y,end_index_y)
    # print(begin_index_z,end_index_z)
    # package1=package.copy()
    for i in range(begin_index_x,end_index_x):
        for j in range(begin_index_y,end_index_y):
            for k in range(begin_index_z,end_index_z):
                package[i][j][k] = 1

def remove_item(package, item_lwh, position):
    # item_lwh: (length, width, height)
    # position: (x, y, z)
    if not check_filled_space(package, position, item_lwh):
        print('不是放在这的吧？')
        raise
    begin_index_x,begin_index_y,begin_index_z=position
    add_x,add_y,add_z=change_xyz_into_index(item_lwh)
    end_index_x,end_index_y,end_index_z=begin_index_x+add_x,begin_index_y+add_y,begin_index_z+add_z
    # print(begin_index_x,end_index_x)
    # print(begin_index_y,end_index_y)
    # print(begin_index_z,end_index_z)
    # package1=package.copy()
    for i in range(begin_index_x,end_index_x):
        for j in range(begin_index_y,end_index_y):
            for k in range(begin_index_z,end_index_z):
                package[i][j][k] = 0

def find_solution(items, package, solution, solutions):
    if solutions:
        return
    if not items:
        solutions.append(solution[:])
        return
    current_item = pick_the_biggest(items)
    package_size_x = len(package)
    package_size_y = len(package[0])
    package_size_z = len(package[0][0])

    for i in range(package_size_x):
        for j in range(package_size_y):
            for k in range(package_size_z):
                if package[i][j][k]==1:
                    continue
                for o in range(1, 7):
                    if solutions:
                        return
                    current_XYZ = orient(current_item, o)
                    if check_valid_state(package, (i, j, k), current_XYZ):
                        solution1=solution[:]
                        remaining_items=items[:]
                        remaining_items.remove(current_item)
                        place_item(package, current_XYZ, (i, j, k))
                        solution1+=[(current_XYZ,(i,j,k))]
                        find_solution(remaining_items, package, solution1, solutions)
                        remove_item(package, current_XYZ, (i, j, k))
                        if solutions:
                            return
                        

# Main function
def try_box(box_lwh, items):
    L,W,H=box_lwh
    package = [[[0 for _ in range(int(10*H))] for __ in range(int(10*W))] for ___ in range(int(10*L))]
    solutions = []
    #print(package)
    find_solution(items, package, [], solutions)
    return solutions


# Example usage:
def main():
    start_time=time.time()
    box_dimensions = (22, 15, 9) # Example box dimensions (length, width, height)
    items = [(15.0, 5.5, 5.5), (15.0, 5.5, 5.5), (19.5, 9.0, 3.1)]
    resulting_solutions = try_box(box_dimensions, items)
    if resulting_solutions:
        print(resulting_solutions[0])
    else:
        print('装不进去。')
    end_time=time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
# package = [[[0 for _ in range(185)] for __ in range(245)] for ___ in range(345)]
# package=place_item(package,(25,24,8.5),(0,0,0))
# print(check_valid_state(package,(0,0,85),(25,24,8.5)))
# package=place_item(package,(25,24,8.5),(0,0,85))
# print(check_valid_state(package,(250,0,0),(3,24,16.5)))
# package=place_item(package,(3,24,16.5),(250,0,0))
# print(check_valid_state(package,(280,0,0),(3,24,16.5)))
# package=place_item(package,(3,24,16.5),(280,0,0))
# print(check_valid_state(package,(310,0,0),(2.5,11,15)))
# package=place_item(package,(2.5,11,15),(310,0,0))
# print(package[310][110][0])
# print(check_valid_state(package,(310,110,0),(2.5,11,15)))
# package=place_item(package,(2.5,11,15),(310,110,0))


