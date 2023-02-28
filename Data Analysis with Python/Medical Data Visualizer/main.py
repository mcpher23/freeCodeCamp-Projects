# This entrypoint file to be used in development. Start by reading README.md
import p3code
from unittest import main

# Test your function by calling it here
p3code.draw_cat_plot()
p3code.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)