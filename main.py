try:
    year = int(input("请输入年份："))
    if (year % 4 == 0 和 year % 100!=0) 或year%400==0:
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
except ValueError：
    print("输入的不是有效年份，请输入数字")
