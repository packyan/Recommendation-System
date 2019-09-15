'''
records[i] = [u, i ,rui, pui]
list records contents users rates, rui is the real rate user u give to item i 
and pui is computed by the models
input records list
output loss
'''
import math
def RMSE(records):
    return math.sqrt(
    sum([(rui - pui)**2 for u, i, rui, pui in records]))\
    /float(len(records))
    
def MAE(records):
    return sum([(rui - pui)**2 for u, i, rui, pui in records])\
    /float(len(records))

if __name__ == '__main__':
    records = [[1,2,8,9],[1,3,7,6]]
    assert RMSE(records) == math.sqrt(2)/2.0
    assert MAE(records) == 1.0