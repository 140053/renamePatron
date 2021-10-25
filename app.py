import os
from os import path
import shutil

Source_Path = 'D:/ken/rename Photo/photo1'
Destination = 'D:/ken/rename Photo/Dest'


# dst_folder = os.mkdir(Destination)


def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst = "PILI-" + filename
        print(filename)

        # rename all the files
        os.rename(os.path.join(Source_Path, filename), os.path.join(Destination, dst))


# Driver Code
if __name__ == '__main__':
    main()
