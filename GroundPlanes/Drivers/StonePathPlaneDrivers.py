# Assign Drivers to the Stone Path Plane

import bpy

def assignDrivers():

    drivers = []
    
    object = bpy.context.object

    # Color 1 - Red Channel
    d0 = {
        'object': object, 
        'property': 'Color1',
        'value': [0.016370, 0.068727, 0.016674, 1.000000],
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
        'value': [0.016370, 0.068727, 0.016674, 1.000000],
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
        'value': [0.016370, 0.068727, 0.016674, 1.000000],
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
        'value': [0.076728, 0.076728, 0.076728, 1.000000],
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
        'value': [0.076728, 0.076728, 0.076728, 1.000000],
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
        'value': [0.076728, 0.076728, 0.076728, 1.000000],
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

    # Color 3 - Red Channel
    d6 = { 
        'object': object, 
        'property': 'Color3',
        'value': [0.571661, 0.571661, 0.571661, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["Color3"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d6)

    # Color 3 - Green Channel
    d7 = { 
        'object': object, 
        'property': 'Color3',
        'value': [0.571661, 0.571661, 0.571661, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["Color3"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d7)

    # Color 3 - Blue Channel
    d8 = { 
        'object': object, 
        'property': 'Color3',
        'value': [0.571661, 0.571661, 0.571661, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["Color3"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d8)

    # Extend X
    d18 = {
        'object': object,
        'property': 'ExtendX',
        'value': 1,
        'driven_value': 'count',
        'driven_object' : object.modifiers['Array'],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["ExtendX"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d18)

    # Extend Y
    d19 = {
        'object': object,
        'property': 'ExtendY',
        'value': 1,
        'driven_value': 'count',
        'driven_object' : object.modifiers['Array.001'],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["ExtendY"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d19)

    # Stone Randomness
    d20 = {
        'object': object,
        'property': 'StoneRandom',
        'value': 1.0,
        'driven_value': 'nodes["Voronoi Texture"].inputs[5].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["StoneRandom"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d20)

    # Lines Mix
    d21 = {
        'object': object,
        'property': 'LinesMix',
        'value': 1.0,
        'driven_value': 'nodes["Mix"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["LinesMix"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d21)

    # Noise Scale
    d22 = {
        'object': object,
        'property': 'NoiseScale',
        'value': 10.0,
        'driven_value': 'nodes["Noise Texture"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["NoiseScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d22)

    # Stone Scale
    d23 = {
        'object': object,
        'property': 'StoneScale',
        'value': 3.0,
        'driven_value': 'nodes["Voronoi Texture"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["StoneScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1000,
    }

    drivers.append(d23)

    # Distortion Scale
    d24 = {
        'object': object,
        'property': 'DistortionScale',
        'value': 1.0,
        'driven_value': 'nodes["Noise Texture.001"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["DistortionScale"]',
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
