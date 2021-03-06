Quick start
==================


After installation of package you can use it in you code. For example:

.. code-block:: python

    import os

    import uuid

    import settings
    from solarhouse.building import Building
    from solarhouse.calculation import Calculation
    import solarhouse.export as export


    def main():
        calc = Calculation(
            tz=settings.TZ,
            geo=settings.GEO,
            building=Building(
                mesh_file=settings.PATH_FILE_OBJECT,
                geo=settings.GEO,
                wall_material=settings.WALL_MATERIAL,
                wall_thickness=settings.WALL_THICKNESS,
                start_temp_in=settings.TEMPERATURE_START,
                power_heat_inside=settings.POWER_HEAT_INSIDE,
                efficiency=settings.EFF,
                heat_accumulator={
                    'volume': 0.032,
                    'material': 'water',
                },
                windows={
                    'area': 0.3,
                    'therm_r': 5.0,
                },
                floor={
                    'area': 1.0,
                    'material': 'adobe',
                    'thickness': 0.2,
                    't_out': 4.0,
                },
            ),
                        )
        data_frame = calc.compute(date=22, month=12, year=2019, with_weather=False)
        calc_id = str(uuid.uuid4())
        output_dir = os.path.join(settings.PATH_OUTPUT, calc_id)
        os.makedirs(output_dir, exist_ok=True)
        csv_file_path = export.as_file(data_frame, 'csv', output_dir)
        export.as_html(data_frame, output_dir)



As result you get two files in folder with calc_id name: data.csv and plot.html