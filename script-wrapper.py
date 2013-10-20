#!/usr/bin/python

import commands
import sys
import os
from time import strftime

def script_wrapper(script_to_run,outfile_postfix,startpoint):
   ''' script_wrapper(script_to_run,outfile_postfix,startpoint) -> integer on success, None on failures
       Function takes a text file list of shell commands to execute in ordered sequence.
       Commands N+1 is only executed if Command N is successful.'''

   try:
       f_out=open('/tmp/' + strftime("%Y%m%d_%H%M%S_") + outfile_postfix + '.log', 'w')
   except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return 1
   try:
       f_in=open(script_to_run, 'r')
   except Exception, err:
       sys.stderr.write('ERROR: %s\n' % str(err))

   cmdlines=f_in.readlines()
   if len(cmdlines) < startpoint:
       sys.stderr.write('ERROR: less commands than specified starting point \n')
       return 2
   
   for i in range(startpoint,len(cmdlines)):
       command= cmdlines[i].strip()
       (exitstatus, outtext) = commands.getstatusoutput(command)
       f_out.write('\n\n#########################################\n')
       if command.find('passw') > -1:
          f_out.write('EXECUTING COMMAND N ' + str(i) +':  "' + command[0:command.index('passw')] + '" \n')
       else:
          f_out.write('EXECUTING COMMAND N ' + str(i) +':   "' + command + '" \n')
       f_out.write('COMMAND EXIT STATUS:  ' + str(exitstatus) + '\n')
       f_out.write('FOLLOWS COMMAND OUTPUT: ++++++++++++++++++++\n')
       f_out.writelines(outtext) 
       f_out.flush()      
       if exitstatus:
          sys.stderr.write('ERROR during test at command %s\n' % command )
          f_out.write('\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++\n****************** END OF TEST: FAILURE ***************\n')
          f_out.close()
          sys.exit(-1)
   f_out.write('\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++\n****************** END OF TEST: SUCCESS ***********************\n')    
   f_out.close()   

#SCRIPT EXECUTION
if len(sys.argv) < 3:
   sys.stderr.write('USAGE ERROR: two arguments expected\n 1- file with list of script_to_run\n 2- POSTFIX for test execution logfile\n')
   sys.exit(-1)
if len(sys.argv)==4:
   startpoint = int(sys.argv[3])-1
else:
   startpoint = 0
if ( os.access(sys.argv[1],os.F_OK)==False):
   sys.stderr.write('ERROR: File ' + sys.argv[1] + '   not found.\n\n')
   sys.exit(-1)

script_wrapper(sys.argv[1],sys.argv[2],startpoint)

