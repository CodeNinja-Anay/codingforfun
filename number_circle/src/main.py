"""
Main module that orchestrates the prime number circle visualization process.
Coordinates user input, prime number generation, position calculation, and visualization display.
"""

import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

from src.circle_plotter import circle_plotter
from src.position_calculator import position_calculator
from src.prime_generator import prime_generator
from src.input_validator import get_valid_input


def start_server(port=8000):
    """Start a simple HTTP server in a separate thread"""
    server = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    return server


def main():
    """
    Main Module.

    Args:

    Returns:

    """
    # Get valid range for prime numbers from user
    print("Enter the range for prime numbers:")
    user_value = get_valid_input(min_value=1, max_value=1000)

    # Generate prime numbers
    prime_numbers = prime_generator(user_value)

    if not prime_numbers:
        print(f"No prime numbers found between 1 and {user_value}")
        return

    # Calculate positions for visualization
    radius, positions = position_calculator(prime_numbers)

    # Generate the visualization
    output_file = "prime_circle.html"
    circle_plotter(radius, positions, prime_numbers, output_file)

    # Start local server and open browser
    server = start_server()

    # Open the visualization in the default web browser
    webbrowser.open(f"http://localhost:8000/{output_file}")

    print("\nVisualization server running. Press Ctrl+C to exit.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()


if __name__ == "__main__":
    main()
