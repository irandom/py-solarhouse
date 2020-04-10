from thermoelement import Element

e = Element(
            name='cube_water',
            temp0=0,
            density=997,
            heat_capacity=4180,
            volume=1
            )
assert e.n == 1
e.start_calc(1000,3600)
assert round(e.temp, 3) == 0.864
# Example calculate of wall from birch with dx = 0.01 meter and 1 kW power coming to inside area of element
e = Element(
        name='birch_wall',
        temp0=20.0,
        density=700.0,
        heat_capacity=1250.0,
        dx=0.01,
        thickness=0.20,
        kappa=0.15,
        area_inside=1.0,
        area_outside=1.1
        )
assert e.n == 20
assert e.dTx_list == [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0,\
                      20.0, 20.0, 20.0, 20.0]
assert round(e.k_area, 3) == 0.5
assert e.get_loss_dx(0) == 0.0
e.start_calc(1000, 1)
assert round(e.dTx_list[0], 3) == 20.114
assert round(e.dTx_list[1], 3) == 20.0
assert round(e.get_loss_dx(0), 3) == 1.723
e.start_calc(1000, 1)
assert round(e.dTx_list[0], 3) == 20.228
assert round(e.dTx_list[1], 4) == 20.0002
# Example element which implementing  thin layer between two areas
e = Element(
        name='glass',
        temp0=20.0,
        area_inside=1.0,
        input_alpha=23,
        )
assert e.calc_loss_input_q(25.0) == 115.0