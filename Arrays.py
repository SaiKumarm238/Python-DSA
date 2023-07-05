# Creation of Array
# importing "array" for array creations
import array as arr

# creating an array with integer type
ar = arr.array('i', [1, 2, 3])

print(ar)

ar.append(4)

print(ar)

ar.extend([5,6,7])

print(ar)

print("pop of", ar.pop())

print(ar)

print(ar[0])

li1 = ar.tolist()
print(li1)

bit = ar.tobytes()
print(bit)
print(ar.buffer_info())
