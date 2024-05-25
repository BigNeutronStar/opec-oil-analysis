import sys
from Scripts import data_collector
from Scripts import report_generator
##from Scripts import graphics_generator
for param in sys.argv[1:]:
        if param == '-g':
                data_collector.generate_main()
           
        
