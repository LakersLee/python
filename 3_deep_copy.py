#深度拷贝实现引用计数不同
import copy
a = [1,2,3,4]
b = copy.deepcopy(a)
print(id(a),id(b))
print(a[:])





