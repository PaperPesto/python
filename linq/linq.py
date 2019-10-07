# https://viralogic.github.io/py-enumerable/

from py_linq import Enumerable
my_collection = Enumerable([1,2,3,2,3,1,2,1,3,2,1,4,3,2,0,1,2,3])

my_collection.group_by(key_names=['id'], key=lambda x: x).to_list()

print(my_collection)