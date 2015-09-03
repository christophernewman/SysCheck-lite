#!/usr/bin/python

#
#   Author: Chris Newman 
#   Version: 1.1.8 Lite (Final)
#   Application: SysCheck
#   Language: Python
#
#   Copyright 2015 Xnet Project
#   All Rights Reserved.

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

	
# Program variables
Header = 'The SysCheck Utility is checking your system...\n\n';
Break = '\n';
Space = 'Checking System Space...\n\n';
SysInfo = 'Checking System Information...\n\n';
SysMem = 'Checking System Memory...\n\n';
SysClean = 'Running System Cleanup...\n\n';
SysUpdate = 'Checking and Installing System Updates...\n\n';
SysHw = 'Checking System Hardware...\n\n';
Version = ' Version: 1.1.7 (Final)';
Complete = 'SysCheck Complete! Please review check.log for details.\n\n';

# Import text time controls

import sys
import os
import platform
from time import sleep
	
# Case parameters

case0 = Break;
case1 = Header;
case2 = Break;
case3 = Space;
case4 = Break;
case5 = SysInfo;
case6 = Break;
case7 = SysMem;
case8 = Break;
case9 = SysHw;
case10 = Break;
case11 = SysUpdate;
case12 = Break;
case13 = SysClean;
case14 = Break;
case15 = Complete;
case16 = Break;

# OS distribution

dist = platform.linux_distribution(
                    supported_dists=('redhat', 'debian', 'SuSE', 'mandrake', 'Ubuntu'))[0];



# Controls for each character line


for char in case0:
	sleep(0.04)
	os.system("echo >> check.log")
	os.system("echo ----- >> check.log")
	os.system("echo >> check.log")
	os.system("echo +---------------------------+ >> check.log")
	os.system("echo + Author: Chris Newman >> check.log")
	os.system("echo + Version: 1.1.8 Lite Final >> check.log")
	os.system("echo + Application: SysCheck >> check.log")
	os.system("echo + Language: Python >> check.log")
	os.system("echo +---------------------------+ >> check.log")
	os.system("echo >> check.log")
	os.system("echo SysCheck Utility >> check.log")
	os.system("echo ------------------------- >> check.log")
	os.system("echo >> check.log")
	os.system("echo SysCheck started >> check.log")
	os.system("echo >> check.log")
	os.system("echo The SysCheck Utility is checking your system on: >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case1:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case2:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("date >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case3:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case4:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking System Space: >> check.log")
	os.system("echo >> check.log")
	os.system("df -h >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case5:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case6:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking System Information: >> check.log")
	os.system("echo >> check.log")
	os.system("python version.py >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case7:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case8:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking System Memory: >> check.log")
	os.system("echo >> check.log")
	os.system("free -m >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case9:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case10:
	sleep(0.09)
if dist == ('CentOS'):
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("yum install lshw -y >> check.log")
	os.system("echo >> check.log")
	os.system("lshw -short >> check.log")
	os.system("echo >> check.log")
elif dist == ('redhat'):
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("yum install lshw -y >> check.log")
	os.system("echo >> check.log")
	os.system("lshw -short >> check.log")
	os.system("echo >> check.log")
elif dist == ('Fedora'):
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("yum install lshw -y >> check.log")
	os.system("echo >> check.log")
	os.system("lshw -short >> check.log")
	os.system("echo >> check.log")
elif dist == ('debian'):
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("sudo apt-get install lshw -y >> check.log")
	os.system("echo >> check.log")
	os.system("lshw -short >> check.log")
	os.system("echo >> check.log")
elif dist == ('Ubuntu'):
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("sudo apt-get install lshw -y >> check.log")
	os.system("echo >> check.log")
	os.system("lshw -short >> check.log")
	os.system("echo >> check.log")
else:
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list. >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case11:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case12:
	sleep(0.09)
if dist == ('CentOS'):
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("yum update -y >> check.log")
	os.system("echo >> check.log")
elif dist == ('redhat'):
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("yum update -y >> check.log")
	os.system("echo >> check.log")
elif dist == ('Fedora'):
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("yum update -y >> check.log")
	os.system("echo >> check.log")
elif dist == ('debian'):
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("sudo apt-get update -y >> check.log")
	os.system("echo >> check.log")
elif dist == ('Ubuntu'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("sudo apt-get update -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	sys.stdout.write(char)
	sys.stdout.flush()
else:
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list. >> check.log")
	os.system("echo")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case13:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case14:
	sleep(0.09)
if dist == ('CentOS'):
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("yum install yum utils -y >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --leaves --all >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --problems >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --orphans --all >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --cleandupes >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --oldkernels >> check.log")
	os.system("echo >> check.log")
	os.system("/usr/sbin/yum-complete-transaction --cleanup-only >> check.log")
	os.system("echo >> check.log")
elif dist == ('redhat'):
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("yum install yum utils -y >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --leaves --all >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --problems >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --orphans -all >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --cleandupes >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --oldkernels >> check.log")
	os.system("echo >> check.log")
	os.system("/usr/sbin/yum-complete-transaction --cleanup-only >> check.log")
	os.system("echo >> check.log")
elif dist == ('Fedora'):
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("yum install yum utils -y >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --leaves --all >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --problems >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --orphans -all >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --cleandupes >> check.log")
	os.system("echo >> check.log")
	os.system("package-cleanup --oldkernels >> check.log")
	os.system("echo >> check.log")
	os.system("/usr/sbin/yum-complete-transaction --cleanup-only >> check.log")
	os.system("echo >> check.log")
elif dist == ('debian'):
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("apt-get autoremove -y >> check.log")
	os.system("echo >> check.log")
	os.system("apt-get clean -y >> check.log")
	os.system("echo >> check.log")
	os.system("apt-get autoclean -y >> check.log")
	os.system("echo >> check.log")
elif dist == ('Ubuntu'):
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("apt-get autoremove -y >> check.log")
	os.system("echo >> check.log")
	os.system("apt-get clean -y >> check.log")
	os.system("echo >> check.log")
	os.system("apt-get autoclean -y >> check.log")
	os.system("echo >> check.log")
else:
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list. >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case15:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case16:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo SysCheck Completed on: >> check.log")
	os.system("echo >> check.log")
	os.system("date >> check.log")
	os.system("echo >> check.log")
	os.system("echo ----- >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
