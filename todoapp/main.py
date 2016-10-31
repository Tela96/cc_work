import pickle
import io

list_test = [1,2,3,4,5]
pickle.dump(list_test, test)
list_test = pickle.load(test)
print(list_test[3])