from src.circle_plotter import (
    _generate_circle_svg,
    _generate_point_elements,
    _generate_html_template,
)


def test_generate_circle_svg():
    result = _generate_circle_svg(50, 100, 100)
    expected = '<circle cx="100" cy="100" r="50" fill="none" stroke="black"/>'
    assert result == expected


def test_generate_point_elements():
    positions = [(0, 0), (50, 50)]
    numbers = [1, 2]
    result = _generate_point_elements(positions, numbers, 100, 100)
    expected = (
        '<circle cx="100" cy="100" r="4" fill="red"/>\n'
        '<text x="100" y="100" text-anchor="middle" dy="-10">1</text>\n'
        '<circle cx="150" cy="150" r="4" fill="red"/>\n'
        '<text x="150" y="150" text-anchor="middle" dy="-10">2</text>'
    )
    assert result == expected


def test_generate_html_template():
    svg_content = '<circle cx="100" cy="100" r="50" fill="none" stroke="black"/>'
    result = _generate_html_template(svg_content, 200, 200)
    assert '<svg width="200" height="200">' in result
