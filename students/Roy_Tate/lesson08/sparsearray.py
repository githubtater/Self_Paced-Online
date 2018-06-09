



class SparseArray:

    def len(self, my_array):
        return len(my_array)

    def delete(self, array, index):
        del array[index]

    def append(self, item):
        self.my_array.append(item)


sa = SparseArray()
my_array = [4, 0, 2, 2, 0, 7]
print(my_array)
print('length: ' + str(sa.len(my_array)))
sa.delete(my_array, 4)
print(my_array)
sa.delete(my_array, 2)
print(my_array)
sa.delete(my_array, 1)
print(my_array)




