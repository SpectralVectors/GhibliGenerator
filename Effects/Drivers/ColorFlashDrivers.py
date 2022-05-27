# Assign Drivers to the Color Flash Plane
import bpy

def assignDrivers():

    drivers = []
    
    object = bpy.context.object

    # Color - Red Channel
    d0 = {
        'object': object, 
        'property': 'Color',
        'value': [1.0, 1.0, 1.0, 1.0],
        'driven_value': 'nodes["Emission"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["Color"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d0)

    # Color - Green Channel
    d1 = {
        'object': object, 
        'property': 'Color',
        'value': [1.0, 1.0, 1.0, 1.0],
        'driven_value': 'nodes["Emission"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["Color"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d1)

    # Color - Blue Channel
    d2 = {
        'object': object, 
        'property': 'Color',
        'value': [1.0, 1.0, 1.0, 1.0],
        'driven_value': 'nodes["Emission"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["Color"][2]',
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
        'data_path' : '["Transparency"]', #[1]
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d4)

    # # Scale X
    # d5 = { 
    #     'object': object,
    #     'property': 'ScaleX',
    #     'value': 1.0,
    #     'driven_value': 'scale',
    #     'driven_object' : object,
    #     'index' : 0,
    #     'variable_name' : 'var',
    #     'data_path' : '["ScaleX"][0]',
    #     'id_type' : 'OBJECT',
    #     'subtype': '',
    #     'min': -100,
    #     'max': 100,
    # }

    # drivers.append(d5)

    # # Scale Y
    # d6 = {
    #     'object': object,
    #     'property': 'ScaleY',
    #     'value': 1.0,
    #     'driven_value': 'scale',
    #     'driven_object' : object,
    #     'index' : 1,
    #     'variable_name' : 'var',
    #     'data_path' : '["ScaleY"][1]',
    #     'id_type' : 'OBJECT',
    #     'subtype': '',
    #     'min': -100,
    #     'max': 100,
    # }

    # drivers.append(d6)


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
