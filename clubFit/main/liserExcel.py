
''' informacion clubfit '''

import sys
import subprocess as spp

upName = sys.argv[1]
BASE7 = sys.argv[2]
spp.getstatusoutput("base64 -d "+BASE7+"v_"+upName+" > "+BASE7+upName)
spp.getstatusoutput("rm -frv "+BASE7+"v_"+upName)
#spp.getstatusoutput("ffmpeg -i /tmp/ci_"+upName+" -vcodec h264 -acodec aac -strict -2 /var/www/html/pool/"+upName)
#spp.getstatusoutput("rm -frv /tmp/ci_"+upName)

