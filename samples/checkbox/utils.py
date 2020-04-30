import json

annotations_path = "/Users/danielantonfernandez/Documents/dev/tfg/Checkbox/Checkbox_annotations/via_region_data.json"
annotations = json.load(open(annotations_path))
annotations = list(annotations.values())
annotations = [a for a in annotations if a['regions']]
for a in annotations:
    # Get the x, y coordinaets of points of the polygons that make up
    # the outline of each object instance. These are stores in the
    # shape_attributes (see json format above)
    # The if condition is needed to support VIA versions 1.x and 2.x.
    if type(a['regions']) is dict:
        polygons = [r['shape_attributes'] for r in a['regions'].values()]
    else:
        polygons = [r['shape_attributes'] for r in a['regions']]
    print(polygons)
