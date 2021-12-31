# Function argument unpacking

def myFun(x, y, z):
  print(x, y, z)
  
# unpack using tuple
  tuple_vec = (1, 0, 1)
myFun(*tuple_vec)

# unpack using dict
dict_vec = {"x":1, "y":0, "z":1}
myFunc(**dict_vec)
