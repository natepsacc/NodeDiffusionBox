

import os
import time
import subprocess
import glob
import shutil
def fileInDirectory(my_dir):
    return [f for f in os.listdir(my_dir) if os.path.isfile(os.path.join(my_dir, f))]

def listComparison(OriginalList, NewList):
    return [x for x in NewList if x not in OriginalList] #Note if files get deleted, this will not highlight them

def fileWatcher(my_dir, pollTime):
    while True:
        previousFileList = fileInDirectory(my_dir)
        print('First Time')
        print(previousFileList)
        
        time.sleep(pollTime)
        
        newFileList = fileInDirectory(my_dir)
        
        fileDiff = listComparison(previousFileList, newFileList)
        if newFileList != previousFileList:
          print("Files have changed")
          print(fileDiff)

          #i want to print the difference between newFileList and previousFileList
          command = ('python /home/schidtery/stable*/optimizedSD/optimized_img2img.py --prompt  "%s"  --init-img /home/schidtery/diffusionBox/indir/%s --outdir /home/schidtery/diffusionBox/diffusionOut --strength 0.7 --n_iter 2 --n_samples 5 --H 800 --W 800 --ddim_steps 50 && python /home/schidtery/stable*/optimizedSD/optimized_img2img.py --prompt  "%s"  --init-img /home/schidtery/diffusionBox/indir/%s --outdir /home/schidtery/diffusionBox/diffusionOut --strength 0.7 --n_iter 2 --n_samples 5 --H 800 --W 800 --ddim_steps 50' % ((str(fileDiff).strip("[]")).strip(".png"), str(fileDiff).strip("[]"),(str(fileDiff).strip("[]")).strip(".png"), str(fileDiff).strip("[]") ))


          subprocess.call(command, shell=True)
            

        else:
            print("Files have not changed")
            command = ('python /home/schidtery/stable*/optimizedSD/optimized_img2img.py --prompt  "%s"  --init-img /home/schidtery/diffusionBox/indir/%s --outdir /home/schidtery/diffusionBox/diffusionOut --strength 0.4 --n_iter 2 --n_samples 5 --H 800 --W 800 --ddim_steps 50 && python /home/schidtery/stable*/optimizedSD/optimized_img2img.py --prompt  "%s"  --init-img /home/schidtery/diffusionBox/indir/%s --outdir /home/schidtery/diffusionBox/diffusionOut --strength 0.7 --n_iter 2 --n_samples 5 --H 800 --W 800 --ddim_steps 50' % ((str(fileDiff).strip("[]")).strip(".png"), str(fileDiff).strip("[]"),(str(fileDiff).strip("[]")).strip(".png"), str(fileDiff).strip("[]") ))
            subprocess.call(command, shell=True)



fileWatcher('/home/schidtery/diffusionBox/indir', 90)
