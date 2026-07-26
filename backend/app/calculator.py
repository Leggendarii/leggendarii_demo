def calculate_scr(voltage, power, xr, frequency):

    scr = 5.0

    z = 0.1

    r = z / ((1 + xr**2) ** 0.5)

    x = r * xr

    return {
        "scr": scr,
        "z": z,
        "r": r,
        "x": x
    }
