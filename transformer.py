import re

def transform_swiftui_colors(code: str) -> str:
    colors = [
        "red", "blue", "green", "orange", "purple", "pink",
        "yellow", "teal", "indigo", "mint", "cyan", "brown"
    ]
    pattern = r'Color\.[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)?'
    color_index = 0

    def replace_color(match):
        nonlocal color_index
        new_color = f"Color.{colors[color_index]}"
        color_index = (color_index + 1) % len(colors)
        return new_color

    transformed_code = re.sub(pattern, replace_color, code)
    return transformed_code
