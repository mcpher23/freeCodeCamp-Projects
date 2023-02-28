# This entrypoint file to be used in development. Start by reading README.md
import p2code
from unittest import main

# Test your function by calling it here
p2code.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)