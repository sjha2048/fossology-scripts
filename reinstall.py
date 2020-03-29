#this script is intended to run inside fossology folder

import os 


#clean up the old installation of fossology
os.system("sudo utils/fo-cleanold")

#Build fossology
os.system("make")

#Install fossology
os.system("sudo make install")

#Run the post install script
os.system("sudo /usr/local/lib/fossology/fo-postinstall")

#enable fossology service
os.system("sudo systemctl enable --now fossology")
