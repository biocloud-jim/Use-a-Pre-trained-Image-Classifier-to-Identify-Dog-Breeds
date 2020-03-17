#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER:Shih Chieh Chen
# DATE CREATED:2020-02-17                                  
# REVISED DATE: 2020-02-17
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    #代表results_dic中的key值是檔案名稱，value值是用檔案名稱，做出來的一個列表。這個dict中每一組key, value 呈現就是 'filename', 'Pet_label' ==> 'Boston_terrier_02259.jpg' : 'boston terrier'
    #第一步：先找到所有檔案在哪裏，同時總成一個list
    in_files = listdir(image_dir) # define in_file and access the file
    #第二部：命名一個dict空集合 也就是常看到的dictName
    results_dic = dict() #define an empty dictionary
    #接下來開始處理 key 和 valeu.
    #key比較簡單，因為是直接把檔名呈現加入，所以後面一定是result_dic[in_files....] = ....
    #再來就是把檔名提取出來處理value的部分。 
    #loop files in image_dir, from 0 to the end<which means total numbers of files> that's why use len().
    for idx in range(0, len(in_files), 1): 
        if in_files[idx][0] !=".": 
            word_list_pet_images = in_files[idx].lower().split("_") 
    #53行skip "." start file, if file name start with ".", skip it<!=>. 先排除隱藏檔
    #54行lower case and split by "_", because the filename look like XXX_xxx_1234123 製作出檔名的字串，並且把字串用"_"分隔。然後都小寫，再來就是要把這一個一個的字串，做出來一後會變成['boston','terrier','02259']指定給一個變數我們以下設定為pet_label 
            pet_label = "" #create a empty string 
            #再來就是指定要放進去pet_label的東西
            for word in word_list_pet_images: #loop to check if word in pet name are all alphabetic characters, not others like ".!@#$" if true append word to pet_label and separate by trailing space.簡單來說就是loop word_list_pet_images ['boston','terrier','02259']
                if word.isalpha():#檢查是不是只有字母，如果loop到的只有字母，就把他丟進去到pet_label中，然後再加入“” 所以會是先 boston > boston terrier 然後停止，因為接下來是數字，處理到這邊就變成乾淨的pet_label了
                    pet_label += word + " " 
#如果檔名key不在resulet_dic中，那就補上key-value ，而key 與value用idx串連起來
        if in_files[idx] not in results_dic:
            results_dic[in_files[idx]] = [pet_label.strip()]#新增key-value進去dict中, dictName[key] = value.同時用strip刪除頭尾符號
        else:
            print("** Warning: Duplicate files exist in directory:",in_files[idx])
            
             
            
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
