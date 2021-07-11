import numpy as np
import os
import tqdm
import matplotlib.pyplot as plt

def read_label():
    # res = -1
    # folder_path = '/Users/yexinyi/Desktop/VE450.nosync/data/merge/dataset/sequences/07/labels'
    # for root, dirs, files in os.walk(folder_path):
    #     for f in tqdm.tqdm(files):
    #         filepath = os.path.join(root, f)
    #         annotated_data = np.fromfile(filepath, dtype=np.uint32).reshape((-1, 1))
    #         # annotated_data = annotated_data & 0xFFFF0000
    #         instance_id_tmp = annotated_data >> 16
    #         instance_id = instance_id_tmp.astype(np.uint8)
    #         res = max(res, max(instance_id))
    # print(res)

    learning_map = {0: 0, 1: 0, 10: 1, 11: 2, 13: 5, 15: 3, 16: 5, 18: 4, 20: 5, 30: 6, 31: 7, 32: 8, 40: 9, 44: 10,
                    48: 11, 49: 12, 50: 13, 51: 14, 52: 0, 60: 9, 70: 15, 71: 16, 72: 17, 80: 18, 81: 19, 99: 0, 252: 1,
                    253: 7, 254: 6, 255: 8, 256: 5, 257: 5, 258: 4, 259: 5}
    statistc_class_dic = {}
    file_num = 11
    root_path = '/Users/yexinyi/Desktop/VE450.nosync/data/merge/dataset/sequences'

    for j in range(file_num):
        for i in range(20):
            statistc_class_dic[i] = 0
        folder_path = os.path.join(root_path, str(j).zfill(2), 'labels')
        # folder_path = '/Users/yexinyi/Desktop/VE450.nosync/data/merge/dataset/sequences/07/labels'
        for root, dirs, files in os.walk(folder_path):
            for f in tqdm.tqdm(files):
                # filepath='/Users/yexinyi/Desktop/VE450.nosync/data/merge/dataset/sequences/00/labels/003907.label'
                tmp_dic = {}
                for i in range(20):
                    tmp_dic[i] = {}
                filepath = os.path.join(root, f)
                annotated_data = np.fromfile(filepath, dtype=np.uint32).reshape((-1, 1))
                label_id_tmp = annotated_data & 0xFFFF  # delete high 16 digits binary
                instance_id_tmp = annotated_data >> 16
                label_id = label_id_tmp.astype(np.uint8)
                instance_id = instance_id_tmp.astype(np.uint8)
                assert len(label_id) == len(instance_id)
                for i in range(len(label_id)):
                    if label_id[i][0] in learning_map.keys():
                        if learning_map[label_id[i][0]] in tmp_dic.keys():
                            if instance_id[i][0] not in tmp_dic[learning_map[label_id[i][0]]].keys():
                                tmp_dic[learning_map[label_id[i][0]]][instance_id[i][0]] = 1

                for i in tmp_dic.keys():
                    statistc_class_dic[i] += len(tmp_dic[i].keys())


        with open('out_ins' + str(j).zfill(2) + '.txt', 'w') as file:
            for i in statistc_class_dic.values():
                file.write(str(i) + '\n')

def plot():
    file_num = 11
    for j in range(file_num):
        X = [str(i) for i in range(20)]
        Y = []
        fig = plt.figure()
        with open('out' + str(j).zfill(2) + '.txt', 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                Y.append(int(line))
        plt.bar(X, Y, 0.4, color="blue")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title('Sequence' + str(j).zfill(2))

        # plt.show()
        plt.savefig('barChart_instance' + str(j).zfill(2) + '.jpg')

if __name__ == '__main__':
    read_label()