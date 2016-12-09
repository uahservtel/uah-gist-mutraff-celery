from celery import Celery
# ========================================================================
app = Celery()
app.config_from_object( 'celery_settings_router' )

# -----------------------------------------------------
# API: simple fake route calculation
# -----------------------------------------------------
@app.task
def route_calculate(O, D):
    return O + D

# -----------------------------------------------------
# API: distributed route calculation
# -----------------------------------------------------
@app.task
def mutraff_route_get( vehicle_id, map, node_orig, node_dest ): 
    out = vehicle_id + ":" + map + ":" + node_orig + ":" + node_dest
    return out

