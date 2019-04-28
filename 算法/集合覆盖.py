# 洲
states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])
#广播电台
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

finnal_stations = set()

while states_needed:
    best_stations = None
    states_covered = set()
    for station , states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered)>len(states_covered):
            best_stations = station
            states_covered = covered
    states_needed-=states_covered
    print(best_stations)
    print(states_covered)
    finnal_stations.add(best_stations)
print(finnal_stations)