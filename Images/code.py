import cv2
import os
path = "Images"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        # print(file_name)
               
        images.append(file_name)
        
# print(len(images))
count = len(images)

frame=cv2.imread(images[0])
height , width, channels = frame.shape
size=(width,height)
print(size)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("Friendship_Day.avi",fourcc,0.8,size)
for i in range(0,count-1,):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()
print("done")