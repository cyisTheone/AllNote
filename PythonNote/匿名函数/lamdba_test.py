# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals.sort(key=lambda x: x[0])



# 匿名函数 lambda 参数列表: 返回表达式

def test1(a,b):
    return a+b

test2 = lambda a,b :a+b

print(test1(1,2))
print(test2(1,2))

