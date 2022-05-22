import glob
import os


def get_latest_file(path_to_folder):
    list_of_files = glob.glob(path_to_folder + "/*")
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file.split("/")[-1]
