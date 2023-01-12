#! /bin/bash
MAIN_PATH=/home/yipeng_zhou/mAP
RESULTS_PATH=${MAIN_PATH}/results_object_detection
INPUT_PATH=${MAIN_PATH}/input/detection-results

for MODEL in `ls ${RESULTS_PATH}`
do  
    # if [ ${MODEL} == "yolov3-tiny.tflite" ]; then
        echo ${MODEL}
        cp -r ${RESULTS_PATH}/${MODEL}/detection_results/* ${INPUT_PATH}
        python ${MAIN_PATH}/scripts/extra/replace_string.py
        cd ${MAIN_PATH}
        python main.py
        rm -rf ${INPUT_PATH}/*
        rm -rf ${MAIN_PATH}/output
        echo "----------------------------------------------------------"
    # fi
done