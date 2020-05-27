#!/usr/bin/env python

from resources import Threshold_T, Threshold_P
from coapthon.server.coap import CoAP
import sys

import getopt
import socket
import time

from threading import Thread
from sense_emu import SenseHat


class CoAPServer(CoAP):
  def __init__(self, host, port, multicast=False):
    CoAP.__init__(self,(host,port),multicast)
    
    # CREATE temperature threshold resource
    threshold_t = Threshold_T()
    threshold_t.set_server(self)
    self.add_resource('temp/',threshold_t)
    
    # CREATE pressure threshold resource
    threshold_p = Threshold_P()
    threshold_p.set_server(self)
    self.add_resource('pres/',threshold_p)
    
    # Initial values to thresholds
    self.t_lim = sys.maxint
    self.p_lim = sys.maxint
    
    # LOG
    print "CoAP server started on {}:{}".format(str(host),str(port))
    print self.root.dump()
    
def listener(server):
  try:
    server.listen(10)
    print "executed after listen"
  except KeyboardInterrupt:
    print server.root.dump()
    server.close()
    sys.exit()

def main():
  ip = sys.argv[1] 
  port = int(sys.argv[2])
  multicast=False

  # CREATE CoAP server
  server = CoAPServer(ip,port,multicast)
  print server
  
  # Create thread to get client threshold
  thread = Thread(target = listener, args=(server,))
  thread.setDaemon(True)
  thread.start()
  
  # Initialize emulator
  sense = SenseHat()
  
  # Red color
  red = (255, 0, 0)
    
  while True:    
    time.sleep(1)    
    
    # Get values from emulator
    t = sense.get_temperature()
    p = sense.get_pressure()
        
    if t > server.t_lim or p > server.p_lim: # if temperature and pressure values are above threshold
        sense.clear(red) # turn on all red lights
    else:
        sense.clear() # turn off all leds   

if __name__=="__main__":
  main()