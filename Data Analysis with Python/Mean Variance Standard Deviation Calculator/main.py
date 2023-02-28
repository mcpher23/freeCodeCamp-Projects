# This entrypoint file to be used in development. Start by reading README.md
import p1code
from unittest import main

print(p1code.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)