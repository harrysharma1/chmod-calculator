chmod_map={
    0:"---",
    1:"--x",
    2:"-w-",
    3:"-wx",
    4:"r--",
    5:"r-x",
    6:"rw-",
    7:"rwx"
}
def int_to_chmod(x:int):
    o = x%10
    g = int((x/10)%10)
    u = int((x/100)%10)
    l = [u,g,o]
    s=""
    for i in l:
        if i in chmod_map.keys():
                s+=chmod_map[i]
        else:
            print("Incorrect value")
    return s
   
print(int_to_chmod(170))