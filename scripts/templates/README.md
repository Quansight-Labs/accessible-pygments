# {{ theme_title }}

{{ theme_description }}

![Screenshot of the {{ theme }} theme in a bash script](./images/{{ theme }}.png)

## Colors

Background color: ![#{{ background_hex }}](https://via.placeholder.com/20/{{ background_hex }}/{{ background_hex }}.png) `#{{ background_hex }}`

Highlight color: ![#{{ highlight_hex }}](https://via.placeholder.com/20/{{ highlight_hex }}/{{ highlight_hex }}.png) `#{{ highlight_hex }}`

**WCAG compliance**

| Color | Hex | Ratio | Normal text | Large text |
| ----- | --- | ----- | ----------- | ---------- |

{%- for c in colors_hex %}
| ![#{{ c.hex }}](https://via.placeholder.com/20/{{ c.hex }}/{{ c.hex }}.png) | `#{{ c.hex }}` | {{ c.contrast_ratio }} : 1 | {{ c.rating_normal_text }} | {{ c.rating_large_text }} |
{% endfor %}
