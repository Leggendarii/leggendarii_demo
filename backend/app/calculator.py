import math


def calculate_scr(voltage, power, xr, frequency, ssc):

    # Short Circuit Ratio
    scr = ssc / power

    # Base impedance
    z_base = voltage**2 / power

    # Grid impedance magnitude
    z = z_base / scr

    # Split impedance according to X/R ratio
    r = z / math.sqrt(1 + xr**2)

    x = xr * r

    return {
        "scr": scr,
        "z": z,
        "r": r,
        "x": x
    }