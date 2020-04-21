import glob
import numpy as np
import os
import cv2

# CMP dataset (B, G, R)
# 0 background: (170, 0, 0)
# 1 facade: (255, 0 ,0)
# 2 window:(255, 85, 0)
# 3 door: (255, 170, 0)
# 4 cornice: (170, 255, 85)
# 5 sill: (0, 170, 255)
# 6 balcony: (85, 255, 170)
# 7 blind: (0, 255, 255)
# 8 deco: (255, 255, 0)
# 9 molding: (0, 85, 255)
# 10 pillar: (0, 0, 255)
# 11 shop: (0, 0, 170)


data_dir = './CMP/'

mask_list = glob.glob(os.path.join(data_dir, 'label_color/' + '*.png'))

count = 0
for name in mask_list:
    ano = cv2.imread(name)
    ano_new = np.zeros([ano.shape[0], ano.shape[1], 1], dtype=np.uint8)
    for y in range(ano.shape[0]):
        for x in range(ano.shape[1]):       # color(B, G, R)
            if ((ano[y][x] == np.array([255, 0 ,0])).all()):    # facade: (255, 0 ,0)
                ano_new[y][x] = 1
            elif ((ano[y][x] == np.array([255, 85, 0])).all()): # window:(255, 85, 0)
                ano_new[y][x] = 2
            elif ((ano[y][x] == np.array([255, 170, 0])).all()):  # door: (255, 170, 0)
                ano_new[y][x] = 3
            elif ((ano[y][x] == np.array([170, 255, 85])).all()):  # cornice: (170, 255, 85)
                ano_new[y][x] = 4
            elif ((ano[y][x] == np.array([0, 170, 255])).all()):  # sill: (0, 170, 255)
                ano_new[y][x] = 5
            elif ((ano[y][x] == np.array([85, 255, 170])).all()):  # balcony: (85, 255, 170)
                ano_new[y][x] = 6
            elif ((ano[y][x] == np.array([0, 255, 255])).all()):  # blind:(0, 255, 255)
                ano_new[y][x] = 7
            elif ((ano[y][x] == np.array([255, 255, 0])).all()):  # deco: (255, 255, 0)
                ano_new[y][x] = 8
            elif ((ano[y][x] == np.array([0, 85, 255])).all()):  # molding: (0, 85, 255)
                ano_new[y][x] = 9
            elif ((ano[y][x] == np.array([0, 0, 255])).all()):  # pillar: (0, 0, 255)
                ano_new[y][x] = 10
            elif ((ano[y][x] == np.array([0, 0, 170])).all()):  # shop: (0, 0, 170)
                ano_new[y][x] = 11
            elif ((ano[y][x] == np.array([170, 0, 0])).all()):  # background: (170, 0, 0)
                ano_new[y][x] = 0
    save_name = data_dir + 'label/' + name.split('\\')[-1].split('.')[0] + '.png'
    cv2.imwrite(save_name, ano_new)
    count += 1
    print(str(count) + ': ' + save_name)

print('Done')






