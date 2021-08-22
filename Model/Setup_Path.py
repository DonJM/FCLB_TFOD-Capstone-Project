import os
from Pretrained_Model_Info import Pretrained_Model

class Setup_Path:

    IMAGES_PATHS = ["original_images", "preprocessed_images", "labeled_images"]
    LABELS = ["Fresh_Ripe", "Fresh_Unripe", "Rotten_Ripe", "Rotten_Unripe"]
    SUB_DIRS = ["anotations","models", "images", "datasets", "pretrained_model", "detection_images"]
    MODELS = ["eval", "export", "tjsexport", "train"]
    EXPORT = ["checkpoint", "saved_model"]
    SAVED_MODEL = ["assets", "variables"]
    API_MODEL = Pretrained_Model("my_ssd_mobnet", "ssd_mobilenet_v2_320x320_coco17_tpu-8", "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz", "generate_tfrecord.py", "label_map.pbtxt")
    MY_TRAINMODELS = ["image_segmentation", "image_augmentation", "modeling", "train_and_test", "prediction", "realtime_object_detection", "load_dataset"]
    SUB_PATHS = ["Train", "Test", "Validation"]
    
    def __init__(self):
        MAIN_PATHS = ["workspace", "tensorflow_api_model", "protobuf", "tfrecord_generator", "train_model", "deployment"]
        self.main_paths = MAIN_PATHS

    def get_paths(self):
        paths = {
            "WORKSPACE_PATH": os.path.join(self.main_paths[0]),
            "TFRECORD_GENERATOR_PATH": os.path.join(self.main_paths[3]),
            "TENSORFLOW_API_MODEL_PATH": os.path.join(self.main_paths[1]),
            "PROTOBUF_PATH": os.path.join(self.main_paths[2]),
            "ANOTATIONS_PATH": os.path.join(self.main_paths[0],self.SUB_DIRS[0]),
            "IMAGES_PATH": os.path.join(self.main_paths[0],self.SUB_DIRS[2]),
            "DATASETS_PATH": os.path.join(self.main_paths[0],self.SUB_DIRS[3]),
            "MODELS_PATH": os.path.join(self.main_paths[0],self.SUB_DIRS[1]),
            "PRETRAINED_MODEL_PATH": os.path.join(self.main_paths[0],self.SUB_DIRS[4]),
            "CHECKPOINT_PATH": os.path.join(self.main_paths[0], self.SUB_DIRS[1], self.API_MODEL.getCustomName()),
            "OUTPUT_PATH": os.path.join(self.main_paths[0], self.SUB_DIRS[1], self.API_MODEL.getCustomName(), self.MODELS[1]),
            "TFJS_PATH": os.path.join(self.main_paths[0], self.SUB_DIRS[1], self.API_MODEL.getCustomName(), self.MODELS[2]),
            "DEPLOYMENT_PATH":os.path.join(self.main_paths[5]),
            "DETECTION_IMAGES_PATH":os.path.join(self.main_paths[0], self.SUB_DIRS[2], self.SUB_DIRS[5]),
        }

        return paths

    def set_paths_dir(self):
        for path in self.get_paths().values():
            if not os.path.exists(path):
                os.makedirs(path)

    def get_image_paths(self):
        path = {}

        for image_path in self.IMAGES_PATHS:
           i = 0
           for label in self.LABELS:
               path.update({("{}".format(image_path+str(i))):"{}".format(os.path.join(self.main_paths[0], self.SUB_DIRS[3], image_path, label))})
               i += 1

        return path

    def set_image_paths(self):
        for path in self.get_image_paths().values():
            if not os.path.exists(path):
                os.makedirs(path)

    def set_train_model(self):
        for path in self.get_train_model().values():
            if not os.path.exists(path):
                os.makedirs(path)

    def get_dataset_paths(self):
        path = {
            'ORIGINAL_IMAGES_PATH': os.path.join(self.get_paths()['DATASETS_PATH'], self.IMAGES_PATHS[0]),
            'PREPROCESSED_IMAGES_PATH': os.path.join(self.get_paths()['DATASETS_PATH'], self.IMAGES_PATHS[1]),
            'LABELED_IMAGES_PATH': os.path.join(self.get_paths()['DATASETS_PATH'], self.IMAGES_PATHS[2]),
        }
        return path

    def get_train_model(self):
        path = {}

        for train_model in self.MY_TRAINMODELS:
            path.update({"{}_PATH".format(train_model).upper():"{}".format(os.path.join(self.main_paths[4], train_model))})
        
        return path

    def get_sub_images_path(self):
        path = []

        for sub_path in self.SUB_PATHS:
            for label in self.LABELS:
                path.append("{}".format(os.path.join(self.get_paths()['IMAGES_PATH'], sub_path, label)))
        return path

    def set_sub_images_path(self):
        for path in self.get_sub_images_path():
            if not os.path.exists(path):
                os.makedirs(path)

    def getFiles(self):
        files = {
            'PIPELINE_CONFIG':os.path.join(self.get_paths()['MODELS_PATH'], self.API_MODEL.getCustomName(), 'pipeline.config'),
            'TF_RECORD_SCRIPT':os.path.join(self.get_paths()['TFRECORD_GENERATOR_PATH'], self.API_MODEL.getTFRecordName()),
            'LABEL_MAP':os.path.join(self.get_paths()['ANOTATIONS_PATH'], self.API_MODEL.getMapName()),
        }
        return files