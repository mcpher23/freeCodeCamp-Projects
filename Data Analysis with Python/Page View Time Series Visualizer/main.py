# This entrypoint file to be used in development. Start by reading README.md
import p4code
from unittest import main

# Test your function by calling it here
p4code.draw_line_plot()
p4code.draw_bar_plot()
p4code.draw_box_plot()

# Run unit tests automatically
main(module='test_module', exit=False)