import numpy as np
import os
import shutil
from shutil import copy



# so there are 24*2 =48 +45 normal so that gives me a total of 45+48=93 so each main character has weight of 2/93
# while each secondary has a weight of 1/93

mainw=np.repeat((2/93),24)
secondw=np.repeat((1/93),45)

weight=np.concatenate([mainw,secondw])

indices=np.arange(0,69)


# This is the random selection of the indices based on the weights we made above
choices=np.random.choice(indices,24,replace=False,p=weight)

photoar=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg',
	'9.jpg','10.jpg','11.jpg','12.jpg','13.jpg','14.jpg','15.jpg',
	'16.jpg','17.jpg','18.jpg','19.jpg','20.jpg','21.jpg','22.jpg',
	'23.jpg','24.jpg','25.jpg','26.jpg','27.jpg','28.jpg','29.jpg',
	'30.jpg','31.jpg', '32.jpg','33.jpg','34.jpg','35.jpg','36.jpg',
	'37.jpg','38.jpg','39.jpg','40.jpg','41.jpg','42.jpg','43.jpg',
	'44.jpg','45.jpg','46.jpg','47.jpg','48.jpg','49.jpg','50.jpg',
	'51.jpg','52.jpg','53.jpg','54.jpg','55.jpg','56.jpg','57.jpg',
	'58.jpg','59.jpg','60.jpg','61.jpg','62.jpg','63.jpg','64.jpg',
	'65.jpg','66.jpg','67.jpg','68.jpg','69.jpg']


# this is actually making the array with the names of the photos we want
chosen=[]
for i in choices:
    chosen.append(photoar[i])

# if an old file path exists with images delete the entire file (this allows us to rerun for new randomness)

if os.path.exists('./GleeImages'):
	shutil.rmtree('./GleeImages')


# Make the new directory to

os.makedirs('./GleeImages')

# populate the directory with the images we chose

for image in chosen:
	copy(image,"./GleeImages")

# at this point you can just call collage_maker.py and put in the parameters "-f GleeImages" (as well as the size)
# and this should do it










