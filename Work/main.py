import sys
from Scripts import data_collector

for param in sys.argv[1:]:
        if param == '-g':
                data_collector.generate()
        
