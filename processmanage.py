import multiprocessing
import time
import sys
def manage(pro_list):
    while 1:
      time.sleep(5)
      i=0
      for proc in pro_list:
          print('process%d状态:'%(i))
          print(proc.is_alive) 
          i=i+1
