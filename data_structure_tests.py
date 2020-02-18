import os
import time
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image
import numpy as np

path = "C:\\Users\\yarem\\PycharmProjects\\project_1\\Data\\Python\\"

menu_choice = 111

image_paths_list = []



def get_image_paths(path_directory):
    image_paths_list.clear()
    directory = path_directory
    if os.path.exists(directory):
        dirs = os.listdir(directory)
        for file in dirs:
            if os.path.isfile(directory + file):
                image_paths_list.append(directory + file)
                print('File name - ' + file)
            elif os.path.isdir(directory):
                print('Catalog')
                print(os.listdir(directory))
    else:
        print('File not Found')


def tuple_structure_test():
    get_image_paths(path)
    image_count = 0
    f = open("tuple_structure.txt", "w")
    for image_path in image_paths_list:
        try:
            start_time = time.time()
            cloud_pixels_count = 0
            normal_pixels_count = 0
            image = Image.open(image_path)
            pixel_ndarray = np.array(image.getdata()).reshape(image.size[0], image.size[1])
            pixel_list = image.getdata()
            tpl = tuple(pixel_list)
            width = image.size[0]
            height = image.size[1]
            for i in range(width):
                for j in range(height):
                    if pixel_list[i, j] > 0 & pixel_list[i, j] < 254:
                        normal_pixels_count += 1
                    if pixel_list[i, j] == 0 or pixel_list[i, j] >= 254:
                        cloud_pixels_count += 1
            percent = (normal_pixels_count / 100) * 5
            cloudiness = cloud_pixels_count / (normal_pixels_count + cloud_pixels_count)
            print("───Pixel array is full───")
            print("Photo name - " + image_path)
            print("Normal pixels count = " + str(normal_pixels_count))
            print("Cloud pixels count = " + str(cloud_pixels_count))
            print("Cloudiness = " + str(cloudiness) + "%")
            print("5% of all pixels = " + str(percent))
            if cloudiness < 0.4:
                unique, counts = np.unique(pixel_ndarray, return_counts=True)
                uniq_tuple = tuple(list(unique))
                #counts_tuple = tuple(counts)
                print("555")
                print(uniq_tuple)
            else:
                print("Cloudiness more then 0.4")
            print(tpl)
        except Exception as e:
            print("Something went wrong - " + str(e))
    print("Proceed photos - " + str(image_count))


def dictionary_structure_test():
    get_image_paths(path)
    image_count = 0
    f = open("dictionary_structure.txt", "w")
    for image_path in image_paths_list:
        try:
            start_time = time.time()
            cloud_pixels_count = 0
            normal_pixels_count = 0
            dictionary = {}
            image = Image.open(image_path)
            pixel_ndarray = np.array(image.getdata()).reshape(image.size[0], image.size[1])
            pixels_array = image.load()
            width = image.size[0]
            height = image.size[1]
            for i in range(width):
                for j in range(height):
                    if pixels_array[i, j] > 0 & pixels_array[i, j] < 254:
                        normal_pixels_count += 1
                    if pixels_array[i, j] == 0 or pixels_array[i, j] >= 254:
                        cloud_pixels_count += 1
            percent = (normal_pixels_count / 100) * 5
            cloudiness = cloud_pixels_count / (normal_pixels_count + cloud_pixels_count)
            #print("───Pixel array is full───")
            #print("Photo name - " + image_path)
            #print("Normal pixels count = " + str(normal_pixels_count))
            #print("Cloud pixels count = " + str(cloud_pixels_count))
            #print("Cloudiness = " + str(cloudiness) + "%")
            #print("5% of all pixels = " + str(percent))
            unique, counts = np.unique(pixel_ndarray, return_counts=True)
            if cloudiness < 0.4:
                for i in range(counts.size):
                    dictionary[unique.item(i)] = counts.item(i)
                if 0 in dictionary.keys():
                    del dictionary[0]
                elif 254 in dictionary.keys():
                    del dictionary[254]
                elif 255 in dictionary.keys():
                    del dictionary[255]
                maximum = max(dictionary.keys(), default=0)
                minimum = min(dictionary.keys(), default=0)
                list_d = list(dictionary.items())
                list_d.sort(key=lambda i: i[1])
                z = 0
                dictionary = dict(list_d)
                while z < percent:
                    for key in dictionary.keys():
                        z += dictionary[key]
                        del dictionary[key]
                        break
                sum_value = sum(dictionary.values())
                #print("Sum = " + str(sum_value))
                time_passed = round((time.time() - start_time), 3)
                vi = round(((255 - (maximum - minimum)) / 255), 2)

                f.write("%f %f %f\r" % (vi, sum_value, time_passed))
                image_count += 1
            else:
                print("Cloudiness more then 0.4")
        except Exception as e :
            print("Something went wrong - " + str(e))
        image_count += 1
    print("Proceed Photos - " + str(image_count))


def list_structure_test():
    get_image_paths(path)
    image_count = 0
    f = open("list_structure.txt", "w")
    for image_path in image_paths_list:
        try:
            start_time = time.time()

            cloud_pixels_count = 0
            normal_pixels_count = 0

            image = Image.open(image_path)
            pixels_array = image.load()
            pixels_list = []

            width = image.size[0]
            height = image.size[1]
            for i in range(width):
                for j in range(height):
                    pixels_list.append(pixels_array[i, j])
                    if pixels_array[i, j] > 0 & pixels_array[i, j] < 254:
                        normal_pixels_count += 1
                    if pixels_array[i, j] == 0 or pixels_array[i, j] >= 254:
                        cloud_pixels_count += 1
            percent = (normal_pixels_count / 100) * 5
            cloudiness = cloud_pixels_count / (normal_pixels_count + cloud_pixels_count)
            #print("───Pixel array is full───")
            #print("Photo name - " + image_path)
            #print("Normal pixels count = " + str(normal_pixels_count))
            #print("Cloud pixels count = " + str(cloud_pixels_count))
            #print("Cloudiness = " + str(cloudiness) + "%")
            #print("5% of all pixels = " + str(percent))
            descending_pixels_list = Counter(pixels_list)
            descending_pixels_list2 = Counter(pixels_list)

            rt = []
            r = 0
            if cloudiness <= 0.4:
                values_list = []
                for q in descending_pixels_list:
                    values_list = list(descending_pixels_list.values())
                values_list.sort(reverse=True)

                for l in values_list:
                    listkey = (list(descending_pixels_list2.keys())[list(descending_pixels_list2.values()).index(l)])
                    rt.append(listkey)
                    descending_pixels_list2.pop(listkey)
                for item in reversed(rt):
                    if r <= percent:
                        r += descending_pixels_list[item]
                        descending_pixels_list.pop(item)

                descending_pixels_list.pop(0)
               # print("List without 5%")
               # print(descending_pixels_list)

                values_sum = sum(descending_pixels_list.values())
                keys_list = list(descending_pixels_list.keys())
                max_value = max(keys_list, default=0)
                min_value = min(keys_list, default=0)
                passed_time = round((time.time() - start_time), 3)
                vi = round(((255 - (max_value - min_value)) / 255), 2)
                f.write("%f %f %f\r" % (vi, values_sum, passed_time))

               # print("─────────────────────────────────────────────────────────────────────────────")
            else:
                print("Cloudiness more then 0.4.")
        except Exception as e:
            print("Something went wrong." + str(e))
    print("Count of Processed Photos = " + str(image_count))
    f.close()


def numpy_structure_test():
    file = open("numpy_structure.txt", "w")
    get_image_paths(path)
    image_count = 0
    for image_path in image_paths_list:
        try:
            start_time = time.time()

            cloud_pixels_count = 0
            normal_pixels_count = 0
            im = Image.open(image_path).convert("L")
            pixel_ndarray = np.array(im.getdata()).reshape(im.size[0], im.size[1])

            pixels = im.load()
            width = im.size[0]
            height = im.size[1]

            for i in range(width):
                for j in range(height):
                    if 0 < pixels[i, j] < 254:
                        normal_pixels_count += 1
                    if pixels[i, j] == 0 or pixels[i, j] >= 254:
                        cloud_pixels_count += 1
            percent = (normal_pixels_count / 100) * 5

            cloudiness = (cloud_pixels_count / (normal_pixels_count + cloud_pixels_count))
            #print("───Pixel array is full───")
            #print("Photo name - " + image_path)
            #print("Normal pixels count = " + str(normal_pixels_count))
            #print("Cloud pixels count = " + str(cloud_pixels_count))
            #print("Cloudiness = " + str(cloudiness) + "%")
            #print("5% of all pixels = " + str(percent))
            r = np.array([], int)
            # print(array_mass_pixel)
            indexes = []
            for i in range(pixel_ndarray.size):
                if pixel_ndarray.item(i) == 0:
                    indexes.append(int(i))
            r = np.delete(pixel_ndarray, indexes)
            maximum = max(r, default=0)
            minimum = min(r, default=0)
            unique, counts = np.unique(r, return_counts=True)
            counts = np.sort(counts)
            z = 0
            indexes_to_del = []
            #print(counts.size)
            if cloudiness <= 0.4:
                ind = 0
                while z < percent:
                    z += counts.item(ind)
                    indexes_to_del.append(ind)
                    ind += 1
                changed_ndarray = np.delete(counts, indexes_to_del)
                #print(indexes_to_del)
                #print(changed_ndarray.size)
                #print("Array without 5% - ")
                #print(changed_ndarray)
                sum_value = sum(changed_ndarray)
                #print("Sum = " + str(sum_value))
                time_passed = round((time.time() - start_time), 3)
                vi = round(((255 - (maximum - minimum)) / 255), 2)
                file.write("%f %f %f\r" % (vi, sum_value, time_passed))
                image_count += 1
            else:
                print("Cloudiness is over 0.4")
        except Exception as e:
            print("Something went wrong - " + str(e))
    print("Count of processed photos = " + str(image_count))


def getSum(file):
    sum_list = []
    sum_list1 = []
    vi_list = []
    time_list = []
    time_list1 = []
    try:
        handle = open(file, "r")
        for line in handle:
            words = line.split()
            vi_list.append(float(words[0]))
            sum_list.append(float(words[1]))
            time_list.append(float(words[0]))
        sum_list.sort(reverse=False)
        time_list.sort(reverse=False)
        sum_list1.append(sum_list[0])
        for i in range(len(sum_list)-1):
            value = float(sum_list1[i] + sum_list[i+1])
            sum_list1.append(value)
    except Exception as e:
        print("this went wrong :" + str(e))
    return sum_list1


def getTime(file):
    sum_list = []
    sum_list1 = []
    vi_list = []
    time_list = []
    time_list1 = []
    try:
        handle = open(file, "r")
        for line in handle:
            words = line.split()
            vi_list.append(float(words[0]))
            sum_list.append(float(words[1]))
            time_list.append(float(words[0]))
        sum_list.sort(reverse=False)
        time_list.sort(reverse=False)
        time_list1.append(time_list[0])
        for i in range(len(time_list) - 1):
            value = float(time_list1[i] + time_list[i + 1])
            time_list1.append(value)

    except Exception as e:
        print("this went wrong :" + str(e))
    return time_list1


while menu_choice != 0:

    print("─────────────────────")
    print("1. Find images.")
    print("2. Test structures.")
    print("3. Plot Graphics.")
    menu_choice = int(input("Chosen option:"))

    if menu_choice == 1:
        get_image_paths(path)
    elif menu_choice == 2:
        list_structure_test()
        numpy_structure_test()
        dictionary_structure_test()
        #tuple_structure_test()
    elif menu_choice == 3:
        try:
            sum_list = getSum("list_structure.txt")
            time_list = getTime("list_structure.txt")
            time_np = getTime("numpy_structure.txt")
            time_dict = getTime("dictionary_structure.txt")
            plt.plot(sum_list, time_list, label='list')
            plt.plot(sum_list, time_np, label='numpy')
            plt.plot(sum_list, time_dict, label='dict' )
            plt.title('Info Graphic')
            plt.xlabel('PG')
            plt.ylabel('Time')
            plt.legend(loc='upper left')
            plt.show()
        except Exception as e:
            print("Something went wrong " + str(e))

    else:
        print("Select available value.")