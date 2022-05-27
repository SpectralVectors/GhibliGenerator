# Assign Drivers to the Road Plane

import bpy

def assignDrivers():

    drivers = []
    
    object = bpy.context.object

    # Center Line Color - Red Channel
    d0 = {
        'object': object, 
        'property': 'CenterLineColor',
        'value': (1.0, 1.0, 1.0, 10),
        'driven_value': 'nodes["ColorRamp.001"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["CenterLineColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d0)

    # Center Line Color - Green Channel
    d1 = {
        'object': object, 
        'property': 'CenterLineColor',
        'value': (1.0, 1.0, 1.0, 10),
        'driven_value': 'nodes["ColorRamp.001"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["CenterLineColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d1)

    # Center Line Color - Blue Channel
    d2 = {
        'object': object, 
        'property': 'CenterLineColor',
        'value': (1.0, 1.0, 1.0, 10),
        'driven_value': 'nodes["ColorRamp.001"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["CenterLineColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d2)

    # Road Base Color - Red Channel
    d3 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d3)

    # Road Base Color - Green Channel
    d4 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d4)

    # Road Base Color - Blue Channel
    d5 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d5)

    # Road Base Color - Red Channel
    d6 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d6)

    # Road Base Color - Green Channel
    d7 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d7)

    # Road Base Color - Blue Channel
    d8 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d8)

    # Road Base Color - Red Channel
    d9 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[4].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d9)

    # Road Base Color - Green Channel
    d10 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[4].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d10)

    # Road Base Color - Blue Channel
    d11 = { 
        'object': object,
        'property': 'RoadBaseColor',
        'value': [0.063267, 0.063267, 0.063267, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[4].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["RoadBaseColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d11)

    # Outer Line Color - Red Channel
    d12 = { 
        'object': object,
        'property': 'OuterLineColor',
        'value': [0.922121, 1.000000, 0.000000, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["OuterLineColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d12)

    # Outer Line Color - Green Channel
    d13 = { 
        'object': object,
        'property': 'OuterLineColor',
        'value': [0.922121, 1.000000, 0.000000, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["OuterLineColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d13)

    # Outer Line Color - Blue Channel
    d14 = { 
        'object': object,
        'property': 'OuterLineColor',
        'value': [0.922121, 1.000000, 0.000000, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["OuterLineColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d14)

    # Outer Line Color - Red Channel
    d15 = { 
        'object': object,
        'property': 'OuterLineColor',
        'value': [0.922121, 1.000000, 0.000000, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[3].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["OuterLineColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d15)

    # Outer Line Color - Green Channel
    d16 = { 
        'object': object,
        'property': 'OuterLineColor',
        'value': [0.922121, 1.000000, 0.000000, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[3].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["OuterLineColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d16)

    # Outer Line Color - Blue Channel
    d17 = { 
        'object': object,
        'property': 'OuterLineColor',
        'value': [0.922121, 1.000000, 0.000000, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[3].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["OuterLineColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d17)

    # Extend
    d18 = {
        'object': object,
        'property': 'Extend',
        'value': 1,
        'driven_value': 'count',
        'driven_object' : object.modifiers['Array'],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["Extend"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d18)

    # Line Spacing
    d19 = {
        'object': object,
        'property': 'LineSpacing',
        'value': 0.464,
        'driven_value': 'nodes["ColorRamp.002"].color_ramp.elements[1].position',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["LineSpacing"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d19)

    # Displace Strength
    d20 = {
        'object': object,
        'property': 'DisplaceStrength',
        'value': 0.01,
        'driven_value': 'strength',
        'driven_object' : object.modifiers["Displace"],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["DisplaceStrength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d20)

    # Cracks Mix
    d21 = {
        'object': object,
        'property': 'CracksMix',
        'value': 1.0,
        'driven_value': 'nodes["Mix"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["CracksMix"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d21)

    # Road Texture Mix
    d22 = {
        'object': object,
        'property': 'RoadTexture',
        'value': 0.5,
        'driven_value': 'nodes["Mix.001"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["RoadTexture"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d22)

    # Road Texture Scale
    d23 = {
        'object': object,
        'property': 'RoadTextureScale',
        'value': 200.0,
        'driven_value': 'nodes["Noise Texture.001"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["RoadTextureScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1000,
    }

    drivers.append(d23)

    # Cracks Puddles
    d24 = {
        'object': object,
        'property': 'CracksPuddles',
        'value': 1.0,
        'driven_value': 'nodes["Mix.004"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["CracksPuddles"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d24)

    # Road Motion
    d25 = {
        'object': object,
        'property': 'RoadMotion',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["RoadMotion"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -9.40282e+38,
        'max': 9.40282e+38,
    }

    drivers.append(d25)

    for d in drivers:
        d['object'][d['property']] = d['value']

        edit_property = d['object'].id_properties_ui(d['property'])
        edit_property.update(min=d['min'], max=d['max'])

        if d['subtype']:
            edit_property.update(subtype=d['subtype'])

        driver = d['driven_object'].driver_add(d['driven_value'], d['index'])

        variable = driver.driver.variables.new()
        variable.name = d['variable_name']
        variable.targets[0].id_type = d['id_type']
        variable.targets[0].id = d['object']
        variable.targets[0].data_path = d['data_path']

        driver.driver.expression = variable.name

    # Update Driver Dependencies
    d['object'].hide_render = d['object'].hide_render
