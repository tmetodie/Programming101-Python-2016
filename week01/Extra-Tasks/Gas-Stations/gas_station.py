distance = 320
stations = [50, 80, 140, 180, 220, 290]
tank_size = 90

def gas_stations(distance, tank_size, stations):
    res = [0]
    stations.append(distance)

    for i in range(len(stations) - 1):
        diff = stations[i+1] - stations[i]
        size = tank_size - (stations[i] - res[-1])
        print(size)
        if size < diff:
            res.append(stations[i])
            size = tank_size
    return res[1:]

print(gas_stations(distance, tank_size, stations))
