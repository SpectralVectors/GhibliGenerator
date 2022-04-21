# Assign Drivers to the Rock
import bpy

def assignDrivers():

    drivers = []
    
    object = bpy.context.object

    # Rock Color - Red Channel
    d0 = {
        'object': object, 
        'property': 'RockColor',
        'value': [0.100000, 0.200000, 0.300000, 1.000000],
        'driven_value': 'nodes["Mix"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["RockColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d0)

    # Rock Color - Green Channel
    d1 = {
        'object': object, 
        'property': 'RockColor',
        'value': [0.100000, 0.200000, 0.300000, 1.000000],
        'driven_value': 'nodes["Mix"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["RockColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d1)

    # Rock Color - Blue Channel
    d2 = {
        'object': object, 
        'property': 'RockColor',
        'value': [0.100000, 0.200000, 0.300000, 1.000000],
        'driven_value': 'nodes["Mix"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["RockColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d2)

    # # Pattern Mix - Red Channel
    d3 = { 
        'object': object,
        'property': 'PatternMix',
        'value': 1.0,
        'driven_value': 'nodes["Mix.004"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["PatternMix"]', #[0]
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d3)

    # Pattern Mix - Green Channel
    d4 = { 
        'object': object,
        'property': 'PatternMix',
        'value': 1.0,
        'driven_value': 'nodes["Mix.004"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["PatternMix"]', #[1]
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d4)

    # Pattern Mix - Blue Channel
    d5 = { 
        'object': object,
        'property': 'PatternMix',
        'value': 1.0,
        'driven_value': 'nodes["Mix.004"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["PatternMix"]', #[2]
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d5)

    # # Brightness
    # bpy.data.materials["RockMaterial"].node_tree.nodes["Bright/Contrast"].inputs[1].default_value
    d6 = {
        'object': object,
        'property': 'Brightness',
        'value': -0.1,
        'driven_value': 'nodes["Bright/Contrast"].inputs[1].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["Brightness"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -10,
        'max': 10,
    }

    drivers.append(d6)

    # # Contrast
    # bpy.data.materials["RockMaterial"].node_tree.nodes["Bright/Contrast"].inputs[2].default_value
    d7 = {
        'object': object,
        'property': 'Contrast',
        'value': 1.0,
        'driven_value': 'nodes["Bright/Contrast"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["Contrast"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 10,
    }

    drivers.append(d7)

    # # Rock Displace Strength
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
        'min': -100,
        'max': 100,
    }

    drivers.append(d8)

    
    # # Main Pattern Scale
    # bpy.data.materials["RockMaterial"].node_tree.nodes["Voronoi Texture"].inputs[2].default_value
    d9 = {
        'object': object,
        'property': 'MainPatternScale',
        'value': 5.0,
        'driven_value': 'nodes["Voronoi Texture"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["MainPatternScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d9)

    # # Distortion Pattern Scale
    # bpy.data.materials["RockMaterial"].node_tree.nodes["Voronoi Texture.001"].inputs[2].default_value
    d10 = {
        'object': object,
        'property': 'DistortionScale',
        'value': 5.0,
        'driven_value': 'nodes["Voronoi Texture.001"].inputs[2].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["DistortionScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d10)



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
