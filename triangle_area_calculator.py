import math

# 读取测试组数 N
N = int(input())

for _ in range(N):
    # 读取一行，按空格拆分，并将所有元素转换为浮点数
    # 例如输入 "0 0 1 1 2 0"，会变成 [0.0, 0.0, 1.0, 1.0, 2.0, 0.0]
    data = list(map(float, input().split()))
    
    # 取出三个点的坐标
    x1, y1 = data[0], data[1]
    x2, y2 = data[2], data[3]
    x3, y3 = data[4], data[5]
    
    # 1. 计算三条边的长度 (两点间距离公式)
    a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
    c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    
    # 2. 判断能否组成三角形
    # 任意两边之和大于第三边。Python 中通常用 1e-6 作为极小值来防止浮点数精度误差
    if a + b > c + 1e-6 and a + c > b + 1e-6 and b + c > a + 1e-6:
        
        # 3. 使用海伦公式计算面积
        p = (a + b + c) / 2.0  # 半周长
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        
        # 输出保留 3 位小数
        # 注意：格式控制符 %.3f 在 Python 中依然可以这样使用
        print(f"{area:.3f}")
    else:
        print("Can not form a triangle.")