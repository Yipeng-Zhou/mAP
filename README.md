# mAP (mean Average Precision) Calculation
This repository is a simplified version of the repository "https://github.com/Cartucho/mAP" and is used to evaluate the accuracy (mAP50) of object detection models. 

The ground-truth xml files can be provided by the repository "https://github.com/Yipeng-Zhou/yolov3-tf2".

The detection results  can be provided by the repository "https://gitlab.lrz.de/chair-of-cyber-physical-systems-in-production-engineering/nn-rt-bench.git".

## Usage
1. Copy the detection results into the folder "./results_object_detection".

2. Create the ground-truth files

	2.1. Insert ground-truth xml files into the folder "./input/ground-truth".

	2.2. Go to the folder "./scripts/extra": `cd ./scripts/extra`

	2.3. Run the python script: `python convert_gt_xml.py`

	2.4. Delete the ground-truth files of the images with one channel: `bash delete_one_channel_images.sh`

	2.5. Unify the labels of ground-truth: `python replace_string.py`

3. Calculate mAP50: `bash test_mAP_multi_models.sh | tee output.txt`
