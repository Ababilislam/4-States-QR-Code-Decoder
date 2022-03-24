import os
import cv2
from image_similarity_measures.quality_metrics import ssim

da = []
ssim_measures = {}


def image_compare(filename):
    test_img = cv2.imread(filename)
    scale_percent = 100  # percent of original img size
    width = int(test_img.shape[1] * scale_percent / 100)
    height = int(test_img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # data_dir hold all image that we are going to compaire
    path = os.path.dirname((os.path.abspath(__file__)))
    img_path = os.path.join(os.path.dirname(path),"raw")
    # print("imcomp path",img_path)
    data_dir = img_path

    for file in os.listdir(data_dir):
        img_path = os.path.join(data_dir, file)
        data_img = cv2.imread(img_path)
        resized_img = cv2.resize(data_img, dim, interpolation=cv2.INTER_AREA)
        ssim_measures[img_path] = ssim(test_img, resized_img)

    ab = cmpr()
    return ab


def calc_closest_val(dict, checkMax):
    result = {}
    if checkMax:
        closest = max(dict.values())
    else:
        closest = min(dict.values())

    for key, value in dict.items():
        # print("The difference between ", key, " and the original image is : \n", value)
        if value == closest:
            result[key] = closest

    # print("The closest value: ", closest)
    # print("######################################################################")
    return result


def cmpr():
    ssim = calc_closest_val(ssim_measures, True)
    path = os.path.dirname((os.path.abspath(__file__)))
    img_path = os.path.join(os.path.dirname(path),"raw")
    if [key for key in ssim.keys()][0] == os.path.join(img_path,"img1.jpg"):
        da = "00"
    elif [key for key in ssim.keys()][0] == os.path.join(img_path,"img2.jpg"):
        da = "01"
    elif [key for key in ssim.keys()][0] == os.path.join(img_path,"img3.png"):
        da = "10"
    elif [key for key in ssim.keys()][0] == os.path.join(img_path,"img4.png"):
        da = "11"
    # print(da)
    return da


# print("The most similar according to SSIM: ", ssim)


# ax = image_compare("/home/ab/Desktop/QRDecoder/image/patch/img0_900.jpg")
# print(ax)
# print(type(ax))
