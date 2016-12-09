# from mutraff_router import route_calculate
import mutraff_router as mr

# ------------------------------------------------------------
# Asynch call
result = mr.route_calculate.delay(4, 4)
# print(result.backend)

try:
  # wait for completion
  out = result.get( timeout=100 )
  print("route_calculate: ", out )
except:
  result.traceback

# ------------------------------------------------------------
# Asynch call
result = mr.mutraff_route_get.delay('M-5436-FRT','mapa-CAM','Meco','Pinto')
# print(result.backend)

try:
  # wait for completion
  out = result.get( timeout=100 )
  print("route_calculate: ", out )
except:
  result.traceback
