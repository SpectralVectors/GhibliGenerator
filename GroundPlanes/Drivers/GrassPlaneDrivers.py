# Assign Drivers to the Grass Plane

import bpy

def assignDrivers():

    drivers = []
    
    object = bpy.context.object

    # Color 1 - Red Channel
    d0 = {
        'object': object, 
        'property': 'Color1',
        'value': (0, 0.1, 0.04, 1),
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
        'value': (0, 0.1, 0.04, 1),
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
        'value': (0, 0.1, 0.04, 1),
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
        'value': (0, 0.5, 0.15, 1),
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
        'value': (0, 0.5, 0.15, 1),
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
        'value': (0, 0.5, 0.15, 1),
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

    # Array - X Count
    d6 = {
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

    drivers.append(d6)

    # Array - Y Count
    d7 = {
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

    drivers.append(d7)

    # Displace Strength
    d8 = {
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
        'max': 100,
    }

    drivers.append(d8)

    # Grass Length
    d9 = {
        'object': object,
        'property': 'GrassLength',
        'value': 0.2,
        'driven_value': 'hair_length',
        'driven_object' : bpy.data.particles["GrassParticleSettings"],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["GrassLength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d9)

    # Render Children 
    d10 = {
        'object': object,
        'property': 'RenderMultiplier',
        'value': 100,
        'driven_value': 'rendered_child_count',
        'driven_object' : bpy.data.particles["GrassParticleSettings"],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["RenderMultiplier"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1000,
    }

    drivers.append(d10)

    # Twist
    d11 = {
        'object': object,
        'property': 'Twist',
        'value': 0.0,
        'driven_value': 'twist',
        'driven_object' : bpy.data.particles["GrassParticleSettings"],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["Twist"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -10,
        'max': 10,
    }

    drivers.append(d11)

    # Displace Scale
    d12 = {
        'object': object,
        'property': 'DisplaceScale',
        'value': 0.25,
        'driven_value': 'noise_scale',
        'driven_object' : bpy.data.textures["GrassTexture"],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["DisplaceScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 2,
    }

    drivers.append(d12)

    # Color 1 - Position
    d13 = {
        'object': object,
        'property': 'Color1Position',
        'value': 0.0,
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].position',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["Color1Position"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d13)

    # Color 2 - Position
    d14 = {
        'object': object,
        'property': 'Color2Position',
        'value': 1.0,
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].position',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["Color2Position"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d14)


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
