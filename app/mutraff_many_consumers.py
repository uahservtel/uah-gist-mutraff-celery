from random import randint
from celery import group, chord
import time
import mutraff_router as mr

# ------------------------------------------------------------
# -- Alvaro 09/12/2016
# DECORATOR FOR TIME MANAGEMENT
def print_computing_time(txt):
  def time_decorator(func):
    def wrapper(*args, **kwargs):
      beg_ts = time.time()
      func(*args, **kwargs)
      end_ts = time.time()
      print(txt+":elapsed time: %f" % (end_ts - beg_ts))
    return wrapper
  return time_decorator

# ------------------------------------------------------------
class SimpleVehicle:
  def __init__(self,id):
    self.id = id
    self.orig = str(randint(0,1000))
    self.dest = str(randint(0,1000))
    self.plate = "M-{0:03d}".format(id)+"-XX"

# ------------------------------------------------------------
@print_computing_time('routeTrafficSync')
def routeTrafficSync( theTraffic ):
  for v in theTraffic:
    # Asynch call
    result = mr.mutraff_route_get.delay(v.plate, 'mapa-CAM', v.orig, v.dest )
    # print(result.backend)

    try:
      # wait for completion
      out = result.get( timeout=100 )
      print("route_calculate: "+ out )
    except:
      result.traceback

# ------------------------------------------------------------
def cb_finished():
  print("TASK HAS FINISHED !\n")

# ------------------------------------------------------------
@print_computing_time('routeTrafficParallel')
def routeTrafficParallel( theTraffic ):
  header = [
  	mr.mutraff_route_get.s(veh.plate, 'mapa-CAM', veh.orig, veh.dest )
  	for veh in theTraffic ]

#  result = chord( header )(cb_finished)

  # wait for completion
  job = group( header )
  result = job.apply_async()
  # result = job()

  try:
    out = result.get( timeout=100 )
    out2 = result.join()
    print("route_calculate: "+ str(out2) )
  except:
    result.traceback

# ------------------------------------------------------------
# MAIN + INIT
# 1. Define traffic: create vehicles
# 2. Router traffic sync and async
# 3. Display computing times.
# ------------------------------------------------------------
num_vehicles = 100
theTraffic = [SimpleVehicle(n) for n in xrange(num_vehicles)]
# routeTrafficSync( theTraffic)
routeTrafficParallel( theTraffic)
