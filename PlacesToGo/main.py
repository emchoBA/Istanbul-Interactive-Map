import webbrowser
import os
from DistrictMap import create_map

create_map()

current_directory = os.path.dirname(os.path.abspath(__file__))
html_page = os.path.join(current_directory, 'istanbul_map.html')
def auto_open(path):
    new = 2
    webbrowser.open(path, new=new)

auto_open(html_page)