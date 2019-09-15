
''' 
读取数据
'''
import os
import random
def load_data(path):
    data = dict()  # 数据集以dict的方式存储，key为user id， value为user看过的movie id组成的list
    with open(path, 'r') as dat_data:
        for index, line in enumerate(dat_data):
            line_list = line.split('::')
            user = int(line_list[0])
            movie = line_list[1]
            rating = line_list[2]
            #line_list[3] did not user
            if float(rating) < 4:                   #此处int(rating)会报错；4分以下的评分忽略
                continue
            if user not in data:
                data[user] = []
            data[user].append(movie)
    return data


'''
input data

M, split data to M-1/M train data and 1/M  test data

output train_set and test_set
'''


def split_data(data, M, random_seed):
    print('sliting data\n')
    test_set = dict()
    train_set = dict()
    random.seed(random_seed)
    for user, items in data.items():
        user = int(user)
        for item in items:
            if random.randint(1, M) == 1:
                if user not in test_set:
                    test_set[user] = []
                test_set[user].append(item)
            else:
                if user not in train_set:
                    train_set[user] = []
                train_set[user].append(item)
    return train_set, test_set

        
if __name__ == '__main__':
    M = 4
    file = 'rating.dat'
    file_path = os.path.join(os.getcwd(),'Data','ratings.dat')
    data = load_data(file_path)
    assert data[1] == ['1193', '661', '914', '3408', '2355', '1197', '1287', '2804', '594', '919', '595', '938', '2398', '2918', '1035', '2791', '2687', '2018', '3105', '2797', '2321', '720', '1270', '527', '2340', '48', '1097', '1721', '1545', '745', '2294', '3186', '1566', '588', '1907', '783', '1836', '1022', '2762', '150', '1', '1961', '1962', '2692', '260', '1028', '1029', '1207', '2028', '531', '3114', '608', '1246']  

    train_set, test_set = split_data(data, M, 100)
    #train_set = {user : [movies list] }
    #assert round(len(train_set[1])/len(test_set[1])) == M-1
    #print((len(train_set[3]), len(test_set[3])))
    #print(len(data[3]))