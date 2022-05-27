# Assign Drivers to the Circular Flash Plane
import bpy

def assignDrivers():

    drivers = []
    
    object = bpy.context.object

    # Color1 - Red Channel
    d0 = {
        'object': object, 
        'property': 'Color1',
        'value': [0.0, 0.0, 0.0, 1.0],
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

    # Color1 - Green Channel
    d1 = {
        'object': object, 
        'property': 'Color1',
        'value': [0.0, 0.0, 0.0, 1.0],
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

    # Color1 - Blue Channel
    d2 = {
        'object': object, 
        'property': 'Color1',
        'value': [0.0, 0.0, 0.0, 1.0],
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

    # Emission Strength
    d3 = { 
        'object': object,
        'property': 'EmissionStrength',
        'value': 20.0,
        'driven_value': 'nodes["Emission"].inputs[1].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["EmissionStrength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 1,
        'max': 100,
    }

    drivers.append(d3)

    # Transparency
    d4 = { 
        'object': object,
        'property': 'Transparency',
        'value': 0.0,
        'driven_value': 'nodes["Mix Shader"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["Transparency"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d4)

    # Color2 R
    d5 = { 
        'object': object, 
        'property': 'Color2',
        'value': [1.0, 1.0, 1.0, 1.0],
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

    drivers.append(d5)

    # Color2 G
    d6 = {
        'object': object, 
        'property': 'Color2',
        'value': [1.0, 1.0, 1.0, 1.0],
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

    drivers.append(d6)

    # Color2 B
    d7 = {
        'object': object, 
        'property': 'Color2',
        'value': [1.0, 1.0, 1.0, 1.0],
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

    drivers.append(d7)

    # Circle Location Y
    d8 = { 
        'object': object,
        'property': 'CircleLocationX',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["CircleLocationX"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -1,
        'max': 1,
    }
    
    drivers.append(d8)

    # Circle Location Y
    d9 = { 
        'object': object,
        'property': 'CircleLocationY',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["CircleLocationY"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -1,
        'max': 1,
    }
    
    drivers.append(d9)

    # Circle Scale X
    d10 = { 
        'object': object,
        'property': 'CircleScaleX',
        'value': 1.0,
        'driven_value': 'nodes["Mapping"].inputs[3].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["CircleScaleX"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -10,
        'max': 10,
    }
    
    drivers.append(d10)

    # Circle Scale Y
    d11 = { 
        'object': object,
        'property': 'CircleScaleY',
        'value': 1.0,
        'driven_value': 'nodes["Mapping"].inputs[3].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["CircleScaleY"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -10,
        'max': 10,
    }
    
    drivers.append(d11)

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
