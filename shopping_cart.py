# 商品及单价字典
products = {
    "矿泉水": 2,
    "饼干": 5,
    "薯片": 6,
    "牛奶": 4
}

# 1. 显示商品名称及单价 (基础字符串拼接)
print("商品及单价：", end="")
for name in products:
    print(name + str(products[name]) + "元", end="，")
print() # 换行

# 2. 使用列表保存购物车
cart = []

# 3. 循环输入商品名称
while True:
    user_input = input("请输入商品名称（输入“结算”结束）：")
    item = user_input.strip() # 去除两端空白
    
    if item == "结算":
        break
        
    # 挑战要求：输入“撤销”
    if item == "撤销":
        if len(cart) > 0:
            # 基础语法：删除列表最后一个元素
            removed_item = cart.pop()
            print("已撤销最后添加的商品：" + removed_item)
        else:
            print("购物车为空，无法撤销。")
        continue # 跳过本次循环，重新输入

    # 判断商品是否存在
    if item in products:
        cart.append(item) # 加入购物车
    else:
        print("没有该商品")

# 4. 如果购物车为空
if len(cart) == 0:
    print("您还没有购买商品")
else:
    print("\n购物清单：")
    
    # 5. 统计每种商品的购买数量 (基础字典统计法)
    item_counts = {}
    for item in cart:
        if item in item_counts:
            item_counts[item] = item_counts[item] + 1
        else:
            item_counts[item] = 1
            
    total_price = 0
    
    # 输出名称、数量和小计
    for name in item_counts:
        count = item_counts[name]
        subtotal = products[name] * count
        total_price = total_price + subtotal
        print(name + " × " + str(count) + "，小计" + str(subtotal) + "元")
        
    print("商品总金额：" + str(total_price) + "元")
    
    # 6. 满 20 元减 3 元，否则不优惠
    discount = 0
    if total_price >= 20:
        discount = 3
        print("优惠金额：" + str(discount) + "元")
        
    final_payment = total_price - discount
    print("实际付款：" + str(final_payment) + "元")