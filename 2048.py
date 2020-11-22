"""

2048小游戏核心算法
"""
# lst=[
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0]
# ]

lst=[
    [2,0,0,0],
    [0,2,0,2],
    [2,2,4,8],
    [0,0,0,0]
]

#对4个列表，每个列表进行相同的操作如下
#降维思想

#左移
#list_=[2,4,4,2]  #[2,8,2,0]
#list_=[2,0,0,2]   #[4,0,0,0]
#list_=[2,2,4,8]   #[4,0,0,0]

def move_left():
    global lst
    for line in lst:
        list_=line
        #将0放在列表最后，非0数字前移
        zero_to_end(list_)
        #将结尾为0的列表,将连续相同的数字相加
        merge(list_)

#右移相比于左移，就是开始和结束做两次反转
def move_right():
    global lst
    # for i in range(len(lst)):
    #     lst[i]=lst[i][::-1]
    # for line in lst:
    #     list_=line
    #     #将0放在列表最后，非0数字前移
    #     zero_to_end(list_)
    #     #将结尾为0的列表,将连续相同的数字相加
    #     merge(list_)
    # for i in range(len(lst)):
    #     lst[i]=lst[i][::-1]
    for line in lst:
        list_=line[::-1] #list_是新列表
        #将0放在列表最后，非0数字前移
        zero_to_end(list_)
        #将结尾为0的列表,将连续相同的数字相加
        merge(list_)
        #这个反转变量名不能更换，不然没有用
        line[::-1]=list_ #将新列表的值倒着赋值给原列表

#上移利用转置思想 转置-->左移-->转置
def move_up():
    transpose_matrix()
    move_left()
    transpose_matrix()

#下移利用转置思想 转置-->右移-->转置
def move_down():
    transpose_matrix()
    move_right()
    transpose_matrix()


def transpose_matrix():
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i > j:
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]

def merge(list_):
    for i in range(len(list_) - 1):
        #列表里面全是0的话，省去后续步骤
        if list_[i] == 0:
            break
        if list_[i] == list_[i + 1]:
            list_[i] = list_[i] + list_[i + 1]
            del list_[i + 1]
            list_.append(0)


def zero_to_end(list_):
    for i in range(len(list_) - 1, -1, -1):
        if list_[i] == 0:
            del list_[i]
            list_.append(0)

#move_left()
#move_right()
#move_up()
move_down()
print(lst)

#右移动
"""
[2,0,2,0] --> [0,2,0,2] --> 左移动[4,0,0,0] --> 倒过去变成[0,0,0,4]
"""
