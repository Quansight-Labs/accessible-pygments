# Copyright (c) Quansight Labs.
# Distributed under the terms of the Modified BSD License.

import pytest
from hypothesis import given
from hypothesis.strategies import floats, tuples

from a11y_pygments.utils import wcag_contrast as wcag

color_channel = floats(0.0, 1.0)
color = tuples(color_channel, color_channel, color_channel)


@pytest.mark.parametrize(
    "rgb1,rgb2,expected",
    [
        [(0.0, 0.0, 0.0), (1.0, 1.0, 1.0), 21.0],
        [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 1.0],
        [(0.0, 198 / 255.0, 0.0), (0.0, 0.0, 198 / 255.0), 5.000229313902297],
    ],
)
def test_luminance(rgb1, rgb2, expected):
    c1 = wcag.contrast_ratio(rgb1, rgb2)
    c2 = wcag.contrast_ratio(rgb2, rgb1)
    assert c1 == expected
    assert c2 == expected


@pytest.mark.parametrize(
    "c1,c2, expected",
    [
        ("#0a1103", "#0a1103", False),
        ("#F1AAC4", "#FEF8FA", False),
        ("#610C2B", "#FEF8FA", 12.55),
        ("#1B78CA", "#FEF8FA", False),
        ("#1B78CA", "#FEF8FA", False),
        ("#2E3A89", "#FEF8FA", 9.61),
        ("#0B3254", "#0B3254", False),
        ("#FBE9F0", "#0B3254", 11.27),
    ],
)
def test_passes_contrast(c1, c2, expected):
    got = wcag.passes_contrast(wcag.hex_to_rgb(c1), wcag.hex_to_rgb(c2), "AA")
    assert got == expected


@given(color, color)
def test_contrast(rgb1, rgb2):
    c1 = wcag.contrast_ratio(rgb1, rgb2)
    c2 = wcag.contrast_ratio(rgb2, rgb1)
    assert 1.0 <= c1 <= 21.0
    assert c1 == c2
