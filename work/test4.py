#利用 辗转除2取余法实现将十进制IPv4地址
# 例如203.179.25.37转换为32位长的二进制地址。
class Stack:
    #栈:先进后出
    def __init__(self):
        self.stack = []

    def length(self): # 返回堆栈长度
        return len(self.stack)

    def isempty(self):  # 返回堆栈是否为空
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def push(self, x):  # 压入堆栈
        self.stack.append(x)

    def pop(self):  # 弹出堆栈，注意需要处理堆栈为空的情况
        if self.stack != []:
            return self.stack.pop()
        else:
            print('ERROR: Stack is empty now!')

def so(n):
    s = Stack()
    while n != 0:
        s.push(n%2)
        n = n // 2 #返回商的整数部分(向下取整)
    while s.length() != 8:
        s.push(0)
    res = '' #创建空字符串
    while s.isempty() == 0:
        res += str(s.pop())#将弹出的数转为字符串，并合并字符串
    return res


#测试
print('地址转换：',' ')
ip_ad = '203.179.25.37'
res = ''
ip_adl = ip_ad.split('.')
for ip in ip_adl:
    res += so(int(ip))
print(res)


#创建一个类模拟实现数据结构中的“队列”，
# 类中应包含入队、出队、取队首/队尾元素等方法
class Queue:
    def __init__(self):
        self.queue = []
    def length(self):
        return len(self.queue)
    def isempty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    def in_queue(self,x):#入队
        self.queue.append(x)
    def out_queue(self):#出队
        if self.queue == []:
            print('ERROR:Queue is empty now!')
        else:
            return self.queue.pop(0)
    def head(self):#取队首
        if self.queue == []:
            print('ERROR:Queue is empty now!')
        else:
            return self.queue[0]
    def tail(self):#取队尾
        if self.queue == []:
            print('ERROR:Queue is empty now!')
        else:
            return self.queue[-1]
    

#测试 
print('队列测试：')
q = Queue()
q.in_queue(1)
q.in_queue(2)
print(q.length())
print(q.isempty())
print(q.head())
print(q.tail()) 
q.out_queue
print(q.length())
print(q.head())
print(q.tail()) 



class tree:
    q = Queue()
    def __init__(self, data = None, left = None, right = None): #树
        self.data = data
        self.left = left
        self.right = right


    def level(self):#实现二叉树的层序遍历的函数
        tree.q.in_queue(self)#根节点进入队列中
        while tree.q.length() > 0:
            node = tree.q.out_queue()
            print(node.data,end=' ')
            if node.left:
                tree.q.in_queue(node.left)
            if node.right:
                tree.q.in_queue(node.right)


    def p_leaf(self):#实现输出叶子节点的函数
        if self.left == None and self.right == None:
            print(self.data,end=' ')
        if self.left != None:
            self.left.p_leaf()
        if self.right != None:
            self.right.p_leaf()

#测试
layer3_2 = tree(2,tree(7),tree(4))
layer2_5 = tree(5,tree(6),layer3_2)
layer2_1 = tree(1,tree(0),tree(8))
layer1_3 = tree(3,layer2_5,layer2_1)

print('层序遍历：')
layer1_3.level()
print('')
print('叶子节点：')
layer1_3.p_leaf()
