from mtcnn.mtcnn import MTCNN
from PIL import Image
import numpy as np
import cv2
import os
from tqdm import tqdm
from skimage import transform as trans

#define read path
image_root_dir="../../FER/NonFER"
#define store path
store_image_dir="../../FER/FER"
list_emotion = ["anger", "contempt", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

if os.path.exists(store_image_dir) is False:
    os.makedirs(store_image_dir)

#define some param for mtcnn
def calculate_src_points(image_size):
    w, h = image_size
    
    src = np.array([
        [w * 0.3, h * 0.35],     # Left eye (30% width, 35% height)
        [w * 0.7, h * 0.35],     # Right eye (70% width, 35% height)
        [w * 0.5, h * 0.45],     # Nose (center, 45% height)
        [w * 0.35, h * 0.65],    # Left mouth (35% width, 65% height)
        [w * 0.65, h * 0.65]     # Right mouth (65% width, 65% height)
    ], dtype=np.float32)
    return src

threshold = [0.6,0.7,0.9]
factor = 0.85
minSize=20
imgSize=[96, 96]
src = calculate_src_points(imgSize)
detector=MTCNN()

#align,crop and resize
keypoint_list=['left_eye','right_eye','nose','mouth_left','mouth_right']

for emo in list_emotion:
    emo_image_root_dir = os.path.join(image_root_dir, emo)
    emo_store_image_dir = os.path.join(store_image_dir, emo)
    if os.path.exists(emo_store_image_dir) is False:
        os.makedirs(emo_store_image_dir)

    for filename in tqdm(os.listdir(emo_image_root_dir)):
        dst = []
        filepath=os.path.join(emo_image_root_dir,filename)
        storepath=os.path.join(emo_store_image_dir,filename)
        npimage=np.array(Image.open(filepath))
        #Image.fromarray(npimage.astype(np.uint8)).show()

        dictface_list=detector.detect_faces(npimage, threshold_pnet=0.6, threshold_rnet=0.7, threshold_onet=0.9, min_face_size=minSize)#if more than one face is detected, [0] means choose the first face

        if len(dictface_list)>1:
            boxs=[]
            for dictface in dictface_list:
                boxs.append(dictface['box'])
            center=np.array(npimage.shape[:2])/2
            boxs=np.array(boxs)
            face_center_y=boxs[:,0]+boxs[:,2]/2
            face_center_x=boxs[:,1]+boxs[:,3]/2
            face_center=np.column_stack((np.array(face_center_x),np.array(face_center_y)))
            distance=np.sqrt(np.sum(np.square(face_center - center),axis=1))
            min_id=np.argmin(distance)
            dictface=dictface_list[min_id]
        else:
            if len(dictface_list)==0:
                continue
            else:
                dictface=dictface_list[0]
        face_keypoint = dictface['keypoints']
        for keypoint in keypoint_list:
            dst.append(face_keypoint[keypoint])
        dst = np.array(dst).astype(np.float32)
        tform = trans.SimilarityTransform()
        tform.estimate(dst, src)
        M = tform.params[0:2, :]
        warped = cv2.warpAffine(npimage, M, (imgSize[1], imgSize[0]), borderValue=0.0)
        warped=cv2.resize(warped,(400,400))
        Image.fromarray(warped.astype(np.uint8)).save(storepath)