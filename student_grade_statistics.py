# 读取输入
n = int(input())
scores = list(map(int, input().split()))

# 1. 计算平均分
total_sum = sum(scores)
avg = total_sum / n

# 2. 成绩降序排序 (使用冒泡排序）

sorted_scores = scores[:]
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_scores[j] < sorted_scores[j + 1]:
            sorted_scores[j], sorted_scores[j + 1] = sorted_scores[j + 1], sorted_scores[j]

# 3. 最值查询
max_score = max(scores)
min_score = min(scores)

# 4. 等级人数统计
excellent = 0  # 90-100
good = 0       # 80-89
medium = 0     # 70-79
pass_count = 0 # 60-69
fail = 0       # 0-59

for score in scores:
    if 90 <= score <= 100:
        excellent += 1
    elif 80 <= score <= 89:
        good += 1
    elif 70 <= score <= 79:
        medium += 1
    elif 60 <= score <= 69:
        pass_count += 1
    else:
        fail += 1

# 5. 计算及格率
# 及格人数 = 优秀 + 良好 + 中等 + 及格
total_pass = excellent + good + medium + pass_count
pass_rate = (total_pass / n) * 100

# 6. 输出结果
print(f"avg={avg:.2f}")
print(" ".join(map(str, sorted_scores)))
print(f"max={max_score}")
print(f"min={min_score}")
print(f"you={excellent}")
print(f"liang={good}")
print(f"zhong={medium}")
print(f"jige={pass_count}")
print(f"buji={fail}")
print(f"pass={pass_rate:.1f}%")