
stack=[]
status_=True
list1 = []
while status_ ==True:
    a = input()
    if a.split()[0] == 'push':
        new_a = int(a.split()[-1])
        stack.append(new_a)
        list1.append('ok')
        #print('ok')
    elif a == 'pop':
        if not stack:
            print('error')
        list1.append(stack.pop())
        #print(stack.pop())
    elif a == 'back':
        if not stack:
            print('error')
        list1.append(stack[-1])
        #print(stack[-1])
    elif  a== 'size':
        list1.append(len(stack))
        #print(len(stack))
    elif a == 'clear':
        stack.clear()
        list1.append('ok')
        #print('ok')
    elif a == 'exit':
        list1.append('bye')
        #print('bye')
        break
print(*list1, sep='\n')