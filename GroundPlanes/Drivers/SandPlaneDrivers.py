# Assign Drivers to the Ice Plane

import bpy

def assignDrivers():

    drivers = []
    
    object = bpy.context.object

    # Color 1 - Red Channel
    d0 = {
        'object': object, 
        'property': 'Color1',
        'value': [0.273416, 0.222385, 0.073390, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["Color1"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d0)

    # Color 1 - Green Channel
    d1 = {
        'object': object, 
        'property': 'Color1',
        'value': [0.273416, 0.222385, 0.073390, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["Color1"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d1)

    # Color 1 - Blue Channel
    d2 = {
        'object': object, 
        'property': 'Color1',
        'value': [0.273416, 0.222385, 0.073390, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["Color1"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d2)

    # Color 2 - Red Channel
    d3 = { 
        'object': object, 
        'property': 'Color2',
        'value': [0.641803, 0.656629, 0.100958, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["Color2"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d3)

    # Color 2 - Green Channel
    d4 = { 
        'object': object, 
        'property': 'Color2',
        'value': [0.641803, 0.656629, 0.100958, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["Color2"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d4)

    # Color 2 - Blue Channel
    d5 = { 
        'object': object, 
        'property': 'Color2',
        'value': [0.641803, 0.656629, 0.100958, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["Color2"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d5)

    # GrainsDensity
    d20 = {
        'object': object,
        'property': 'GrainsDensity',
        'value': 0.86,
        'driven_value': 'nodes["ColorRamp.001"].color_ramp.elements[1].position',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["GrainsDensity"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d20)

    # Grains Mix
    d21 = {
        'object': object,
        'property': 'GrainsMix',
        'value': 1.0,
        'driven_value': 'nodes["Mix"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["GrainsMix"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d21)

    # Grain Scale
    d22 = {
        'object': object,
        'property': 'GrainScale',
        'value': 1000.0,
        'driven_value': 'nodes["Noise Texture"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["GrainScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -1000,
        'max': 1000,
    }

    drivers.append(d22)

    # Displace Strength
    d24 = {
        'object': object,
        'property': 'DisplaceStrength',
        'value': 0.5,
        'driven_value': 'strength',
        'driven_object' : object.modifiers["Displace"],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["DisplaceStrength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 10,
    }

    drivers.append(d24)
    

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
