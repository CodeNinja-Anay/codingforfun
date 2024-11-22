"""
Circle plotting module that generates an HTML visualization of numbers positioned on a circle.
Provides functionality to create interactive circular visualizations of numerical data.
"""

from pathlib import Path


def _generate_circle_svg(radius, center_x, center_y):
    """
    Generate SVG circle element.

    Args:
        radius (float): Circle radius
        center_x (float): X coordinate of circle center
        center_y (float): Y coordinate of circle center

    Returns:
        str: SVG circle element
    """
    return f'<circle cx="{center_x}" cy="{center_y}" r="{radius}" fill="none" stroke="black"/>'


def _generate_point_elements(positions, numbers, center_x, center_y):
    """
    Generate SVG elements for points and labels.

    Args:
        positions (list): List of (x,y) coordinate tuples
        numbers (list): List of numbers to display
        center_x (float): X coordinate of circle center
        center_y (float): Y coordinate of circle center

    Returns:
        str: SVG elements for points and labels
    """
    elements = []
    for (x, y), num in zip(positions, numbers):
        # Adjust coordinates relative to center
        plot_x = x + center_x
        plot_y = y + center_y

        # Add point
        elements.append(f'<circle cx="{plot_x}" cy="{plot_y}" r="4" fill="red"/>')
        # Add number label
        elements.append(
            f'<text x="{plot_x}" y="{plot_y}" text-anchor="middle" '
            f'dy="-10">{num}</text>'
        )
    return "\n".join(elements)


def _generate_html_template(svg_content, width, height, title="Circle Plot"):
    """
    Generate complete HTML document with embedded SVG.

    Args:
        svg_content (str): SVG content to embed
        width (int): SVG viewport width
        height (int): SVG viewport height
        title (str): Page title

    Returns:
        str: Complete HTML document
    """
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        .container {{ display: flex; justify-content: center; }}
        svg {{ border: 1px solid #ccc; margin: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <svg width="{width}" height="{height}">
            {svg_content}
        </svg>
    </div>
</body>
</html>"""


def circle_plotter(radius, positions, numbers, output_path="circle_plot.html"):
    """
    Create an HTML visualization of numbers positioned on a circle.

    Args:
        radius (float): Circle radius
        positions (list): List of (x,y) coordinate tuples
        numbers (list): List of numbers to display
        output_path (str): Path for output HTML file
    """
    # Calculate SVG dimensions and center
    padding = 50
    width = int(2 * radius + 2 * padding)
    height = width
    center_x = width // 2
    center_y = height // 2

    # Generate SVG elements
    circle = _generate_circle_svg(radius, center_x, center_y)
    points = _generate_point_elements(positions, numbers, center_x, center_y)

    # Combine SVG elements
    svg_content = f"{circle}\n{points}"

    # Generate complete HTML
    html_content = _generate_html_template(svg_content, width, height)

       # Write to file
    output_file = Path(output_path)
    output_file.write_text(html_content, encoding="utf-8")
