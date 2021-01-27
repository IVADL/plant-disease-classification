import os
from shutil import copy

os.makedirs(os.path.join('dataset', 'train'), exist_ok=True)
os.makedirs(os.path.join('dataset', 'test'), exist_ok=True)
data_dir = 'dataset/tywbtsjrjv-1/Plant_leave_diseases_dataset_with_augmentation'
f = open("dataset/label.txt", 'w')
for root, dirs, files in os.walk(data_dir):
    if files:
        label = root.split('\\')[-1]
        f.write(label+'\n')
        os.makedirs(os.path.join('dataset', 'train', label), exist_ok=True)
        os.makedirs(os.path.join('dataset', 'test', label), exist_ok=True)

        data_size = len(files)

        train_data = files[:int(0.8*data_size)]
        test_data = files[int(0.8*data_size):]

        for t in train_data:
            copy(os.path.join(root, t), os.path.join(
                'dataset', 'train', label, t))
            print(f'copied {label}/{t}')

        for t in test_data:
            copy(os.path.join(root, t), os.path.join(
                'dataset', 'test', label, t))
            print(f'copied {label}/{t}')
f.close()
