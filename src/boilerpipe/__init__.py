import os
import imp
import jpype

jars = []
for top, dirs, files in os.walk(imp.find_module('boilerpipe')[1]+'/data'):
    for nm in files:       
        jars.append(os.path.join(top, nm))
 
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % ':'.join(jars))
