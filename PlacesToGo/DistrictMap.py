import json
import folium
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
map_file_path = os.path.join(current_directory, 'istanbul_district_geodata.geojson')

def create_map():
    with open(map_file_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    main_map = folium.Map(location=[41.0082, 28.9784], tiles="Cartodb Positron")

    district_map = folium.GeoJson(geojson_data,
                    highlight_function= lambda feature: {
                        "fillColor": ("#ffff00") },
                    style_function=lambda feature: {
                        'fillColor': 'blue',
                        'fillOpacity': 0.5,
                        'color': 'black',
                        'weight': 1 }
                                  
    ).add_to(main_map)


    #folium.GeoJsonTooltip(fields=["name"]).add_to(district_map)



    main_map.save("istanbul_map.html")