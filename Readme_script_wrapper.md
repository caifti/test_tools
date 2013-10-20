

Author: Danilo Dongiovanni 

## script-wrapper.py 

This is a python wrapper which executes an ordered list of bash shell commands stored in a TESTSCENARIO.txt file. 

### Requires: 
* directory  /root/siteinfo/

\# ls /root/siteinfo/* -lr
-rw-r--r-- 1 root root 3728 Apr 10 15:18 /root/siteinfo/users.conf   <i>---> conf file for yaim </i>

-rw-r--r-- 1 root root 1140 Apr 10 15:18 /root/siteinfo/site-info.def     <i>---> conf file for yaim </i> <br>
-rw-r--r-- 1 root root 2451 Apr 10 15:20 /root/siteinfo/script-wrapper.py    <i>---> script itself </i><br>
-rw-r--r-- 1 root root  221 Apr 10 15:18 /root/siteinfo/groups.conf  <i>---> conf file for yaim </i><br>
-rw-r--r-- 1 root root  614 Apr 10 15:23 /root/siteinfo/EMI2_SL5-64_WMS_deployement_command_list.txt  <i>---> TESTSCENARIO.txt </i><br>
-rw-r--r-- 1 root root 1078 Apr 10 15:23 /root/siteinfo/EMI1_UPDATE_TO_EMI2_SL5-64_WMS_deployement_command_list.txt       <i>---> TESTSCENARIO2.txt </i>

/root/siteinfo/vo.d: <br>
total 8 <br>
-rw-r--r-- 1 root root 616 Apr 10 15:18 testers.eu-emi.eu                                                                 <i>---> EMITESTBED VO conf file </i><br>
-rw-r--r-- 1 root root 387 Apr 10 15:18 testers2.eu-emi.eu                                                                <i>---> EMITESTBED VO conf file</i><br>

/root/siteinfo/services:<br>
total 8<br>
-rw-r--r-- 1 root root 305 Apr 10 15:18 glite-wms                                                                         <i>---> conf file for yaim</i><br>
-rw-r--r-- 1 root root 238 Apr 10 15:18 glite-bdii_site                                                                   <i>---> conf file for yaim</i><br>

+ host certificates under /etc/grid-security/

### Usage: 
* from /root/siteinfo/ directory run

$>python script-wrapper.py EMI1_UPDATE_TO_EMI2_SL5-64_WMS_deployement_command_list.txt WMS-EMI1_UPDATE_EMI2_SL5x64-RC4_DEPLOYMENT_TEST NUMLINE

where:

* EMI1_UPDATE_TO_EMI2_SL5-64_WMS_deployement_command_list.txt is the TESTSCENARIO.txt to use
* WMS-EMI1_UPDATE_EMI2_SL5x64-RC4_DEPLOYMENT_TEST is the postfix to use for the report log file which will be named as: 20120410_152530_WMS-EMI1_UPDATE_EMI2_SL5x64-RC4_DEPLOYMENT_TEST.log
* NUMLINE optional:ex. 3 starting with command at line 3

### Note:
* The script exit on first command with non zero exit status.
*  It produces a log report file 20120410_152530_WMS-EMI1_UPDATE_EMI2_SL5x64-RC4_DEPLOYMENT_TEST.log
* It tries to remove from command line in report.log possible passwords provided at command line, but better to check before publishing reports
