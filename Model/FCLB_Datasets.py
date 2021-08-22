#import neccessary python modules and libraries
import os
import shutil
from PIL import ImageEnhance
from PIL import Image
import uuid
import tarfile

class FCLB_Datasets:
    #class' constructor
    def __init__(self, setup):
        self.setup = setup
    
    #acquiring uncategorized dataset
    def get_original_dataset(self, num1, num2, label):
        images_path = self.setup.get_dataset_paths()['PREPROCESSED_IMAGES_PATH']
        path = os.path.join(images_path, label)

        files = ["{}".format(i) for i in os.listdir(path)[num1:num2]]

        return files

    def copy_image_file(self, subPath, num1, num2):

        for label in self.setup.LABELS:
            for file in self.get_original_dataset(num1, num2, label):
                dst = os.path.join(self.setup.get_main_paths()['IMAGES_PATH'], subPath, label, file)
                src = os.path.join(self.setup.get_dataset_paths()['PREPROCESSED_IMAGES_PATH'], label, file)
                shutil.copyfile(src, dst)

    #define a function that returns path of datasets sub_directories which is a labels
    def getDir(self,path):
        return self.setup.get_dataset_paths()[path]

    #I call it segment function, wala na koy mahunahunaan
    def segment(self):
        original_dir = self.getDir('ORIGINAL_IMAGES_PATH')
        target_dir = self.getDir('PREPROCESSED_IMAGES_PATH')
        sub_dirs = self.getSubDirectories(original_dir)

        for sub_dir in sub_dirs:
            original = os.path.join(original_dir, sub_dir)
            target = os.path.join(target_dir, sub_dir)
            for img in os.listdir(original):
                self.segmentation(original, target, img)
    #this function gets a list of sub directories, ex. fresh unripe, rotten unripe
    def getSubDirectories(self, dir):
        return os.listdir(dir)  

    #this function used to segment an image file, it actually resize image, add contrast and lightness
    #and save it to the target directory
    #the purpose of uuid module is to give unique id or name to an image file
    def segmentation(self, base_dir, target_dir, fname):
        image = Image.open(os.path.join(base_dir, fname))
        size = (400,400)
        image.thumbnail(size)
        image.save(os.path.join(target_dir, '{}.jpg'.format(uuid.uuid1())))

        contrast = ImageEnhance.Contrast(image)
        contrast.enhance(1.8).save(os.path.join(target_dir, '{}.jpg'.format(uuid.uuid1())))

        brightness = ImageEnhance.Brightness(image)
        brightness.enhance(1.2).save(os.path.join(target_dir, '{}.jpg'.format(uuid.uuid1())))

    #compressed file for github upload
    def compressed(self):
        path = self.getDir('PREPROCESSED_IMAGES_PATH')
        sub_paths = self.getSubDirectories(path)
        ARCHIVE_PATH = os.path.join(path, 'preprocessed_images.tar.gz')
        tar = tarfile.open(ARCHIVE_PATH, "w:gz")
        for sub_path in sub_paths:
            dir = os.path.join(path, sub_path)
            tar.add(dir)
        tar.close()