# Methods to calculate WCAG contrast ratio and check if it passes AA or AAA
# https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html

import re
from typing import Tuple, Union


def hex_to_rgb(hex: int) -> Tuple[int, int, int]:
    """Convert a hex defined colour to RGB.

    Args:
        hex (string): color in hex format (#rrggbb/#rgb)

    Returns:
        rgb: tuple of rgb values ``(r, g, b, a)``, where each channel (red, green, blue,
        alpha) can assume values between 0 and 1.
    """
    # hex color in #rrggbb format
    match = re.match(r"\A#[a-fA-F0-9]{6}\Z", hex)
    if match:
        return tuple(int(n, 16) / 255 for n in [hex[1:3], hex[3:5], hex[5:7]])
    # hex color in #rgb format, shorthand for #rrggbb.
    match = re.match(r"\A#[a-fA-F0-9]{3}\Z", hex)
    if match:
        return tuple(int(n, 16) / 255 for n in [hex[1] * 2, hex[2] * 2, hex[3] * 2])


def sRGB_channel(v: float) -> float:
    """Colors need to be normalised (from a sRGB space) before computing the relative
    luminance.

    Args:
        v (float): r,g,b channels values between 0 and 1

    Returns:
        float: sRGB channel value for a given rgb color channel
    """
    if v <= 0.04045:
        return v / 12.92
    else:
        return ((v + 0.055) / 1.055) ** 2.4


def relative_luminance(color: Tuple[int, int, int]) -> float:
    """Compute the relative luminance of a color.

    Args:
        color (tuple): rgb color tuple ``(r, g, b)``

    Returns:
        float: relative luminance of a color
    """
    r, g, b = color
    r = sRGB_channel(r)
    g = sRGB_channel(g)
    b = sRGB_channel(b)

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> float:
    """Compute the contrast ratio between two colors.

    Args:
        color1 (tuple): rgb color tuple ``(r, g, b)``
        color2 (tuple): rgb color tuple ``(r, g, b)``

    Returns:
        float: contrast ratio between two colors
    """

    l1 = relative_luminance(color1)
    l2 = relative_luminance(color2)

    if l1 > l2:
        return (l1 + 0.05) / (l2 + 0.05)
    else:
        return (l2 + 0.05) / (l1 + 0.05)


def passes_contrast(
    color1: Tuple[int, int, int], color2: Tuple[int, int, int], level="AA"
) -> Union[bool, float]:
    """Method to verify the contrast ratio between two colours.

    Args:
        color1 (tuple): rgb color tuple ``(r, g, b)``
        color2 (tuple): rgb color tuple ``(r, g, b)``
        level (str, optional): WCAG contrast level. Defaults to "AA".
    """

    if level not in ["AA", "AAA"]:
        raise ValueError("level must be either 'AA' or 'AAA'")

    ratio = contrast_ratio(color1, color2)

    if level == "AA":
        if ratio >= 4.5:
            return round(ratio, 2)
        else:
            return False
    elif level == "AAA":
        if ratio >= 7.0:
            return round(ratio, 2)
        else:
            return False
