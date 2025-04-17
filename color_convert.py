from colorsys import hls_to_rgb

def hsl_convert(r, g, b):
    red = r / 255.0
    green = g / 255.0
    blue = b / 255.0

    brightest = max(red, green, blue)
    darkest = min(red, green, blue)
    difference = brightest - darkest

    lightness = (brightest + darkest) / 2 # this is in a float percentage

    if difference == 0:
        saturation = 0

    else:
        saturation = difference / (1 - abs(2 * lightness - 1))

    if difference == 0:
        hue = 0

    elif brightest == red:
        hue = 60 * (((green - blue) / difference) % 6)

    elif brightest == green:
        hue = 60 * (((blue - red) / difference) + 2)

    elif brightest == blue:
        hue = 60 * (((red - green) / difference) + 4)

    saturation *= 100
    lightness *= 100

    return hue, saturation, lightness

def RGB_convert(h, s, l):
    h /= 360
    s /= 100
    l /= 100

    r, g, b = hls_to_rgb(h, l, s)

    r *= 255
    g *= 255
    b *= 255

    return int(r), int(g), int(b)