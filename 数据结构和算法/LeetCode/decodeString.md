# LeetCode 394 字符串解码 —— 栈思路详解

> 嵌套示例 `3[a2[c]]`，核心思想：**遇到左括号，把现在手头的工作先存到栈里，去做括号里面新的小任务；遇到右括号，从栈把之前存的工作拿回来继续做**。
> 
> 

栈相当于备忘录：

- `cur_str`：我**现在正在写的字符串**

- `cur_num`：我**现在读到的重复次数**

- `stack`：备忘录栈，存储元组 `(之前写好的老字符串，对应的重复次数)`

## 完整代码

```python
def decodeString(s: str) -> str:
    stack = []          # 栈：存放元组 (之前保存的字符串, 重复次数)
    cur_str = ""        # 当前正在拼接的字符串
    cur_num = 0         # 当前解析到的数字（支持多位数，比如10、200）

    for char in s:      # 逐个遍历字符串每一个字符
        if char.isdigit():
            # 如果是数字字符，计算完整数字，处理多位数，例如"12[a]"
            cur_num = cur_num * 10 + int(char)
        elif char == '[':
            # 碰到左括号，把当前状态压栈保存，开启括号内新的子串
            stack.append((cur_str, cur_num))
            cur_str = ""   # 重置：括号里面从空字符串开始收集字符
            cur_num = 0   # 数字清零
        elif char == ']':
            # 碰到右括号，括号结束，出栈，进行字符串重复拼接
            prev_str, num = stack.pop()
            # prev_str：括号外面旧的字符串；cur_str：括号里面的内容，重复num次拼回去
            cur_str = prev_str + cur_str * num
        else:
            # 普通字母，直接追加到当前字符串
            cur_str += char
    return cur_str
```

## 示例模拟：`s = "3[a2[c]]"`

字符依次：`'3','[','a','2','[','c',']',']'`

初始化：
`stack = []`，`cur_str=""`，`cur_num=0`

1. char = `'3'`，是数字
`cur_num = 0*10 + 3 =3` → `cur_num=3`

2. char = `'['`，左括号

> 要进入括号内部干活，进括号前保存当前状态到栈
> 
> 

```python
stack.append( ("",3) )
```

栈：`[("", 3)]`
重置现场，括号内部从头开始：
`cur_str=""`，`cur_num=0`

3. char = `'a'`，普通字符
`cur_str += 'a'` → `cur_str = "a"`

4. char = `'2'`，数字
`cur_num =0*10 +2 =2` → `cur_num=2`

5. char = `'['`，嵌套的左括号

> 再次钻进更深一层括号，再次保存当前现场
> 
> 

```python
stack.append( ("a",2) )
```

栈：`[("",3), ("a",2)]`
重置现场：
`cur_str=""`，`cur_num=0`

6. char = `'c'`，普通字符
`cur_str += 'c'` → `cur_str="c"`

7. char = `']'`，内层右括号，第一次出栈

```python
prev_str, num = stack.pop() # pop拿到 ("a", 2)
cur_str = "a" + "c"*2 = "acc"
```

此时：`cur_str="acc"`；栈：`[("",3)]`

8. char = `']'`，外层右括号，再次出栈

```python
prev_str, num = stack.pop() # pop拿到 ("", 3)
cur_str = "" + "acc"*3 = "accaccacc"
```

循环结束，return `cur_str` → `"accaccacc"`

## 核心：栈里面为什么存 `(老字符串,次数)`

通用模型：`Xxxx k[ 里面的内容 ]`

1. 碰到`[`

- 把**括号外面已经拼完的 Xxxx** 和 **k** 存进栈

- `cur_str`清空，专门收集`[]`括号内部字符

2. 碰到`]`

- 取出外面的 Xxxx 和 k

- `cur_str = Xxxx + (括号内的字符串) * k`

- `cur_str`变回当前工作字符串，继续向后解析

> ⚠️栈**不保存括号里面的内容**！栈存的是**括号外面的上下文**，括号内内容一直放在`cur_str`。
> 
> 

### 简单无嵌套例子：`3[a]2[bc]`

1. `3[` →压栈 `("",3)`，cur\_str 清空

2. `a` →cur\_str="a"

3. `]` →pop，cur\_str="" \+ "a"\*3 →`"aaa"`

4. `2[` →压栈 `("aaa",2)`，cur\_str 清空

5. `bc` →cur\_str="bc"

6. `]` →pop，cur\_str = "aaa"\+"bc"\*2 →`"aaabcbc"`

## 常见理解误区

|误区|正确理解|
|---|---|
|❌栈保存括号里面的子串|✅cur\_str 存括号内子串，栈只存括号外面的历史上下文|
|❌栈只存数字|✅必须同时存外层字符串，嵌套结束要拼接回去，只存数字会丢失外层字符|
|❌遇到`]`直接写 `cur_str = cur_str * num`|✅会丢掉外层`prev_str`，嵌套直接崩盘|

> 记忆固定模板
> 
> 

```python
# 左括号 [
stack.append( (cur_str, cur_num) )
cur_str, cur_num = "", 0

# 右括号 ]
prev_str, num = stack.pop()
cur_str = prev_str + cur_str * num
```

## 面试重点

1. `cur_num = cur_num *10 + int(char)` 处理**多位数**，例如`10[ab]`，不能直接`int(char)`只处理个位数。

2. 栈是迭代实现，等价于递归 DFS；超长字符串递归会有栈溢出风险。

3. 每次遇到`[`保存现场；遇到`]`恢复现场。


> （注：内容由 AI 生成）
