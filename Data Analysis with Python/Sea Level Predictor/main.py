# This entrypoint file to be used in development. Start by reading README.md
import p5code
from unittest import main

# Test your function by calling it here
p5code.draw_plot()

# Run unit tests automatically
main(module='test_module', exit=False)