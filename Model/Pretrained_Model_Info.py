class pretrained_model:

    def __init__(self, custom_name, pretrained_name, model_url, tfrecord_name, map_name):
        self.custom_name = custom_name
        self.pretrained_name = pretrained_name
        self.model_url = model_url,
        self.tfrecord_name = tfrecord_name
        self.map_name = map_name

    def getCustomName(self):
        return self.custom_name

    def getPretrainedName(self):
        return self.pretrained_name

    def getURLModel(self):
        return self.model_url

    def getTFRecordName(self):
        return self.tfrecord_name

    def getMapName(self):
        return self.map_name
