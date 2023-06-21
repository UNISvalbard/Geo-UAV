import pandas as pd

def gsd_calculator(alt, drone):
    drone_data = {
        "mavic2pro": [9.6, 10.35,3648],
        "mavic3hasselblad": [13, 12,3956],
        "mavicair2s": [8.82, 12,3648],
        }
    s, f, im = drone_data[drone]

    gsd = (alt*s)/(f*im)
    return gsd

def shutter_speed_calculator(gsd,v):
    return gsd/v

def calculate_speed_versus_gsd(drone):
    velocity = [1,2,3,4,5,10,15]

    df = pd.DataFrame(index=velocity)

    for height in [15,30,45,60,90,120,150]:
        df[height] = gsd_calculator(height,drone)

    df = df.apply(lambda x: 1/shutter_speed_calculator(x.values, x.index))
    df = df.astype(int)
    df = df.astype(str)
    df = df.apply(lambda x: "1/" + x.values)
    df = df.transpose()
    df.columns = [f"{i} m/s" for i in df.columns]
    df.index = [f"{i} m" for i in df.index]

    return df