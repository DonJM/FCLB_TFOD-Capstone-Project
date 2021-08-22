import os

class Setup_Path:

    IMAGES_PATHS = ["original_images", "preprocessed_images", "labeled_images"]
    LABELS = ["Fresh_Ripe", "Fresh_Unripe", "Rotten_Ripe", "Rotten_Unripe"]
    MODELS = ["eval", "export", "tjsexport", "train"]
    EXPORT = ["checkpoint", "saved_model"]
    SAVED_MODEL = ["assets", "variables"]
    #API_MODEL = Pretrained_Model("my_ssd_mobnet", "ssd_mobilenet_v2_320x320_coco17_tpu-8", "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz", "generate_tfrecord.py", "label_map.pbtxt")
    SUB_PATHS = ["Train", "Test", "Validation"]
    SUB_DIRS = ["anotations","models", "images", "datasets", "pretrained_model", "detection_images"]
    
    def __init__(self, custom_name, pretrained_model_name, model_url, tfrecord_name, map_name):
        self.custom_name = custom_name
        self.pretrained_name = pretrained_model_name
        self.model_url = model_url,
        self.tfrecord_name = tfrecord_name
        self.map_name = map_name
        MAIN_PATHS = ["workspace", "tensorflow_api_model", "protobuf", "tfrecord_generator", "train_model", "deployment"]
        self.main_paths = MAIN_PATHS

    def get_main_paths(self):
        paths = {
            "WORKSPACE_PATH": "workspace",
            "TENSORFLOW_API_MODEL_PATH": "TFOD_Path",
            "PROTOBUF_PATH": "protobuf",
            "ANOTATIONS_PATH": os.path.join("workspace","anotations"),
            "IMAGES_PATH": os.path.join("workspace","images"),
            "DATASETS_PATH": os.path.join("workspace","datasets"),
            "MODELS_PATH": os.path.join("workspace","models"),
            "PRETRAINED_MODEL_PATH": os.path.join("workspace","pretrained_model"),
            "CHECKPOINT_PATH": os.path.join("workspace", "models", self.custom_name),
            "OUTPUT_PATH": os.path.join("workspace", "anotations", "tjsexport"),
            "TFJS_PATH": os.path.join("workspace", "anotations", "tjsexport"),
            "DEPLOYMENT_PATH":os.path.join("workspace"),#for opencv, testing for computer vision
            "DETECTION_IMAGES_PATH":os.path.join("workspace", "images", "detection_images"),
        }

        return paths

    def set_main_paths(self):
        for path in self.get_main_paths.values():
            if not os.path.exists(path):
                os.makedirs(path)

    def get_image_paths(self):
        path = {
            "ORIGINAL_IMAGES_PATH" : ["workspace\datasets\original_images\Fresh_Ripe", "workspace\datasets\original_images\Fresh_Unripe", "workspace\datasets\original_images\Rotten_Ripe", "workspace\datasets\original_images\Rotten_Unripe"],
            "PREPROCESSED_IMAGES_PATH" : ["workspace\datasets\preprocessed_images\Fresh_Ripe", "workspace\datasets\preprocessed_images\Fresh_Unripe", "workspace\datasets\preprocessed_images\Rotten_Ripe", "workspace\datasets\preprocessed_images\Rotten_Unripe"],
        }

        return path

    def set_image_paths(self):
        for path in self.get_image_paths().values():
            for label in self.get_image_paths().values()[path]:
                if os.path.exists(label):
                    os.makedirs(label)

    def getFiles(self):
        files = {
            'PIPELINE_CONFIG':os.path.join(self.get_paths()['MODELS_PATH'], self.custom_name, 'pipeline.config'),
            'TF_RECORD_SCRIPT':os.path.join(self.get_paths()['TFRECORD_GENERATOR_PATH'], self.tfrecord_name),
            'LABEL_MAP':os.path.join(self.get_paths()['ANOTATIONS_PATH'], self.map_name),
        }
        return files