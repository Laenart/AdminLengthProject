import json

from admin_level.haversine import haversine


def calculation_length_subjects(subject_first_name, subject_second_name):
    with open("admin_level/admin_level_4.geojson", encoding='utf-8') as geojsonFile:
        admin_level_data = json.load(geojsonFile)
        geojsonFile.close()

    subject_coord_first = []
    subject_coord_second = []
    has_subject_first = False
    has_subject_second = False

    for item in admin_level_data['features']:
        if item['name'].lower() == subject_first_name.lower():
            has_subject_first = True
            for coordinate in (item['geometry']['coordinates'][0][0]):
                subject_coord_first.append(coordinate)
        elif item['name'].lower() == subject_second_name.lower():
            has_subject_second = True
            for coordinate in (item['geometry']['coordinates'][0][0]):
                subject_coord_second.append(coordinate)

    if has_subject_first & has_subject_second:
        common_coordinates = []
        for coordinate in subject_coord_first:
            if coordinate in subject_coord_second:
                common_coordinates.append(coordinate)

        distance_sum = 0
        if len(common_coordinates) > 0:
            coordinate_first = common_coordinates[0]
            for coordinate in common_coordinates[1:]:
                coordinate_second = coordinate
                distance = haversine(coordinate_first, coordinate_second)
                distance_sum += distance
                coordinate_first = coordinate_second

        result = f'Длина границы между {subject_first_name} и {subject_second_name}: {distance_sum} км'

    return result
