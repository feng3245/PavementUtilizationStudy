# PavementUtilizationStudy
An in depth study of how autonomous vehicles might change utilization of pavement in both Urban/Rural areas.
Reusing code from https://github.com/CosmiQ/basiss all credits to owner for creation of model pipeline.

model is trained using  nohup python -u src/basiss.py --path ./ --model unet --mode train --file_list fileloc.csv --slice_x 400 --slice_y 400 --stride_x 250 --stride_y 250 --n_bands 3 --n_classes 2 --batchsize 32 --validation_split 0.1 --early_stopping_patience 2 --epochs 1 --gpu 4 --prefix pavementCV > pavementCV.log & tail -f pavementCV.log 
command
