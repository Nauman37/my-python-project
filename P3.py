def assign_task(vehicles):
    for vehicle in vehicles:
        if (vehicle["status"]=="available" and vehicle["battery_level"]>= 30):
            return vehicle["id"]
    return None

vehicles=[
    {"id":"V1", "battery_level":85, "status":"available"},
    {"id":"V2", "battery_level":70, "status":"available"},
    {"id":"V3", "battery_level":35, "status":"available"}
]
print("Assigned vehicle ID", assign_task(vehicles))