

import tkinter as tk
import tkinter.messagebox


def Input(n, w, v):
    for i in range(0, n):
        if i == 0:
            w[i] = int(w0.get())
        elif i == 1:
            w[i] = int(w1.get())
        elif i == 2:
            w[i] = int(w2.get())
        elif i == 3:
            w[i] = int(w3.get())
        elif i == 4:
            w[i] = int(w4.get())
        elif i == 5:
            w[i] = int(w5.get())
        elif i == 6:
            w[i] = int(w6.get())
        elif i == 7:
            w[i] = int(w7.get())
        elif i == 8:
            w[i] = int(w8.get())
        elif i == 9:
            w[i] = int(w9.get())
    for i in range(0, n):
        if i == 0:
            v[i] = int(v0.get())
        elif i == 1:
            v[i] = int(v1.get())
        elif i == 2:
            v[i] = int(v2.get())
        elif i == 3:
            v[i] = int(v3.get())
        elif i == 4:
            v[i] = int(v4.get())
        elif i == 5:
            v[i] = int(v5.get())
        elif i == 6:
            v[i] = int(v6.get())
        elif i == 7:
            v[i] = int(v7.get())
        elif i == 8:
            v[i] = int(v8.get())
        elif i == 9:
            v[i] = int(v9.get())


def bag():
    # 数量未输入
    if l_input.get() == '':
        tkinter.messagebox.showerror(title='错误', message='请输入数量')
        return
    n = int(l_input.get())
    # 背包容量未输入
    if l_cap_in.get() == '':
        tkinter.messagebox.showerror(title='错误', message='请输入背包容量')
        return
    c = int(l_cap_in.get())
    w = [0 for i in range(0, n)]  # 重量数组
    v = [0 for i in range(0, n)]  # 价值数组
    Input(n, w, v)
    #     w=[2,2,6,5,4]
    #     v=[6,3,5,4,6]
    dp = [[-1 for j in range(c + 1)] for i in range(n + 1)]  # 动态规划数组
    for j in range(c + 1):
        dp[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i - 1] and dp[i][j] < dp[i - 1][j - w[i - 1]] + v[i - 1]:  # 判断是否能装入背包中
                dp[i][j] = dp[i - 1][j - w[i - 1]] + v[i - 1]
                print(dp)
    show(n, c, w, dp)  # 路径显示函数


# 显示函数
def show(n, c, w, dp):
    global var
    # 输出最大价值
    var.set(dp[n][c])
    print('最大价值为:', dp[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if dp[i][j] > dp[i - 1][j]:  # 判断是否装入背包中
            x[i - 1] = True
            j = j - w[i - 1]
    print('选择的物品为:')

    # 用红色背景显示转入背包的物品
    for i in range(n):
        if x[i]:
            print('第', i, '个 ', end='')
            if i == 0:
                w0.config(bg='red'), v0.config(bg='red')
            elif i == 1:
                w1.config(bg='red'), v1.config(bg='red')
            elif i == 2:
                w2.config(bg='red'), v2.config(bg='red')
            elif i == 3:
                w3.config(bg='red'), v3.config(bg='red')
            elif i == 4:
                w4.config(bg='red'), v4.config(bg='red')
            elif i == 5:
                w5.config(bg='red'), v5.config(bg='red')
            elif i == 6:
                w6.config(bg='red'), v6.config(bg='red')
            elif i == 7:
                w7.config(bg='red'), v7.config(bg='red')
            elif i == 8:
                w8.config(bg='red'), v8.config(bg='red')
            elif i == 9:
                w9.config(bg='red'), v9.config(bg='red')
        print('')

    # 清空函数


def clear():
    l_input.delete('0', 'end')  # 数量清空
    l_cap_in.delete('0', 'end')  # 容量清空
    var.set('0')
    w0.delete('0', 'end')
    w0.config(bg='white')
    w1.delete('0', 'end')
    w1.config(bg='white')
    w2.delete('0', 'end')
    w2.config(bg='white')
    w3.delete('0', 'end')
    w3.config(bg='white')
    w4.delete('0', 'end')
    w4.config(bg='white')
    w5.delete('0', 'end')
    w5.config(bg='white')
    w6.delete('0', 'end')
    w6.config(bg='white')
    w7.delete('0', 'end')
    w7.config(bg='white')
    w8.delete('0', 'end')
    w8.config(bg='white')
    w9.delete('0', 'end')
    w9.config(bg='white')
    v0.delete('0', 'end')
    v0.config(bg='white')
    v1.delete('0', 'end')
    v1.config(bg='white')
    v2.delete('0', 'end')
    v2.config(bg='white')
    v3.delete('0', 'end')
    v3.config(bg='white')
    v4.delete('0', 'end')
    v4.config(bg='white')
    v5.delete('0', 'end')
    v5.config(bg='white')
    v6.delete('0', 'end')
    v6.config(bg='white')
    v7.delete('0', 'end')
    v7.config(bg='white')
    v8.delete('0', 'end')
    v8.config(bg='white')
    v9.delete('0', 'end')
    v9.config(bg='white')


window = tk.Tk()
window.title('实验三 软件工程结对项目')
window.geometry('600x300')

var = tk.IntVar()

# 设置个数
l_num = tk.Label(window, text='请输入数量：', font='NewTimesRoman -20 bold')
l_num.place(x=100, y=50, anchor='center')
l_input = tk.Entry(window, show='', width=10)
l_input.place(x=220, y=50, anchor='center')
l_cap = tk.Label(window, text='背包容量：', font='NewTimesRoman -20 bold')
l_cap.place(x=90, y=80, anchor='center')
l_cap_in = tk.Entry(window, show='', width=10)
l_cap_in.place(x=220, y=80, anchor='center')

# 设置重量
P = tk.Label(window, width=5, text='重量')
P.place(x=50, y=130, anchor='center')
w0 = tk.Entry(window, show='', width=5)
w0.place(x=100, y=130, anchor='center')
w1 = tk.Entry(window, show='', width=5)
w1.place(x=150, y=130, anchor='center')
w2 = tk.Entry(window, show='', width=5)
w2.place(x=200, y=130, anchor='center')
w3 = tk.Entry(window, show='', width=5)
w3.place(x=250, y=130, anchor='center')
w4 = tk.Entry(window, show='', width=5)
w4.place(x=300, y=130, anchor='center')
w5 = tk.Entry(window, show='', width=5)
w5.place(x=350, y=130, anchor='center')
w6 = tk.Entry(window, show='', width=5)
w6.place(x=400, y=130, anchor='center')
w7 = tk.Entry(window, show='', width=5)
w7.place(x=450, y=130, anchor='center')
w8 = tk.Entry(window, show='', width=5)
w8.place(x=500, y=130, anchor='center')
w9 = tk.Entry(window, show='', width=5)
w9.place(x=550, y=130, anchor='center')

# 设置单价
l2 = tk.Label(window, width=5, text='价值')
l2.place(x=50, y=170, anchor='center')
v0 = tk.Entry(window, show='', width=5)
v0.place(x=100, y=170, anchor='center')
v1 = tk.Entry(window, show='', width=5)
v1.place(x=150, y=170, anchor='center')
v2 = tk.Entry(window, show='', width=5)
v2.place(x=200, y=170, anchor='center')
v3 = tk.Entry(window, show='', width=5)
v3.place(x=250, y=170, anchor='center')
v4 = tk.Entry(window, show='', width=5)
v4.place(x=300, y=170, anchor='center')
v5 = tk.Entry(window, show='', width=5)
v5.place(x=350, y=170, anchor='center')
v6 = tk.Entry(window, show='', width=5)
v6.place(x=400, y=170, anchor='center')
v7 = tk.Entry(window, show='', width=5)
v7.place(x=450, y=170, anchor='center')
v8 = tk.Entry(window, show='', width=5)
v8.place(x=500, y=170, anchor='center')
v9 = tk.Entry(window, show='', width=5)
v9.place(x=550, y=170, anchor='center')

# 设置动态规划按钮
b1 = tk.Button(window, text='计算', width=10, command=bag)
b1.place(x=50, y=215)

# # 设置递归按钮
b2 = tk.Button(window, text='递归', width=10)
b2.place(x=150, y=215)

# 设置清空按钮
b3 = tk.Button(window, text='清空', width=10, command=clear)
b3.place(x=150, y=215)

# 设置结果
l3 = tk.Label(window, textvariable=var, bg='skyblue', width=10)
l3.place(x=400, y=230, anchor='center')
l4 = tk.Label(window, text='最大价值为', font='NewTimesRoman -20 bold')
l4.place(x=300, y=230, anchor='center')

window.mainloop()