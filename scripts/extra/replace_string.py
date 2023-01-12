import os

#folder = '/home/yipeng_zhou/mAP/input/ground-truth'
folder = '/home/yipeng_zhou/mAP/input/detection-results'
for file in os.listdir(folder):
    file_data = ''
    file_name = os.path.join(folder, file)
    with open(file_name, 'r') as f:
        for line in f:
            if 'traffic light' in line:
                line = line.replace('traffic light', 'traffic_light')
            if 'fire hydrant' in line:
                line = line.replace('fire hydrant', 'fire_hydrant')
            if 'stop sign' in line:
                line = line.replace('stop sign', 'stop_sign')
            if 'parking meter' in line:
                line = line.replace('parking meter', 'parking_meter')
            if 'sports ball' in line:
                line = line.replace('sports ball', 'sports_ball')
            if 'baseball bat' in line:
                line = line.replace('baseball bat', 'baseball_bat')
            if 'baseball glove' in line:
                line = line.replace('baseball glove', 'baseball_glove')
            if 'tennis racket' in line:
                line = line.replace('tennis racket', 'tennis_racket')
            if 'wine glass' in line:
                line = line.replace('wine glass', 'wine_glass')
            if 'hot dog' in line:
                line = line.replace('hot dog', 'hot_dog')
            if 'potted plant' in line:
                line = line.replace('potted plant', 'potted_plant')
            if 'dining table' in line:
                line = line.replace('dining table', 'dining_table')
            if 'cell phone' in line:
                line = line.replace('cell phone', 'cell_phone')
            if 'teddy bear' in line:
                line = line.replace('teddy bear', 'teddy_bear')
            if 'hair drier' in line:
                line = line.replace('hair drier', 'hair_drier')
            file_data += line
    f.close()
        
    with open(file_name, 'w') as f:
        f.write(file_data)
    f.close()



