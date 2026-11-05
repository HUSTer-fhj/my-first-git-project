def main():
    # 1. 读取数组大小 n
    n = int(input())
    
    # 2. 读取 n 个已排序的数组元素（使用 list 存储）
    # input().split() 会自动按空格分割，map(int, ...) 将字符串转换为整数
    arr = list(map(int, input().split()))
    
    # 3. 读取查询次数 q
    q = int(input())
    
    # 4. 读取 q 个查询值
    queries = list(map(int, input().split()))
    
    # 5. 依次处理每一次查询
    for x in queries:
        left = 0
        right = n - 1
        ans = -1  # 默认没找到，初始化为 -1
        
        # 二分查找核心逻辑
        while left <= right:
            mid = (left + right) // 2  # 在 Python 中，// 表示整除
            
            if arr[mid] == x:
                ans = mid          # 找到了，先记录下来
                right = mid - 1    # 因为要找最小下标，继续向左收缩查找
            elif arr[mid] < x:
                left = mid + 1     # 目标值在右半部分
            else:
                right = mid - 1    # 目标值在左半部分
                
        # 输出结果，每次输出占一行
        print(ans)

if __name__ == "__main__":
    main()