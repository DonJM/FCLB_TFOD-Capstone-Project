#import neccesary python modules and libraries for project
from Setup_Path import Setup_Path
from FCLB_Datasets import FCLB_Datasets

#initialized setup path class
setup = Setup_Path("my_ssd_mobnet", "ssd_mobilenet_v2_320x320_coco17_tpu-8", "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz", "generate_tfrecord.py", "label_map.pbtxt")
dataset = FCLB_Datasets(setup)

#set main paths and images paths
setup.set_main_paths()
setup.set_image_paths()
