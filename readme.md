## Getting started with YOLOv5 with RealSense camera

Dataset used:
Fruit detection dataset, download from here
https://inkyusa.github.io/deepNIR_dataset/download/obj-detection/#kaggle-11-fruits

```
conda env create -f environment.yml
```

For this only strawberry dataset was used. It is required to modify the `data.yml` as follow. 
Set the train and validate path correctly based on where you download the folder.
```
train: /home/dev/Documents/dataset_training/dataset/strawberry/train/images
val: /home/dev/Documents/dataset_training/dataset/strawberry/valid/images

nc: 1
names: ['strawberry']
```

For training data dir, set the dir where the data.yml is located. `/home/dev/Documents/dataset_training/dataset/strawberry/data.yaml`
```sh
python train.py --img <imgsize> --batch 16 --epochs 600 --data <training data dir> --cfg models/yolov5s.yaml
python train.py --img 416 --batch 16 --epochs 600 --data /home/dev/Documents/dataset_training/dataset/strawberry/data.yaml --cfg models/yolov5s.yaml
```

Trained weights will be saved on `yolov5/runs/train/exp<?>`

To run realsense.py git clone `https://github.com/ultralytics/yolov5` on this dir or create a symbolic link to yolov5 repo;
```sh
ln -s /home/dev/Documents/yolov5 yolov5
```