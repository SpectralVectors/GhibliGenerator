# Action Planes Drivers

# Assign Drivers to the Action Planes

import bpy

def assignDrivers():

    drivers = []
    
    #object = bpy.context.object
    object = bpy.data.objects['NearLines']
    bg_object = bpy.data.objects['GradientBG']

    # # Line Speed
    # bpy.data.materials["ActionMaterial"].node_tree.nodes["Mapping"].inputs[1].default_value[0]
    d0 = {
        'object': object, 
        'property': 'LineSpeed',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["LineSpeed"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -9.40282e+38,
        'max': 9.40282e+38,
    }

    drivers.append(d0)

    # Line Length
    # bpy.data.materials["ActionMaterial"].node_tree.nodes["Mapping"].inputs[3].default_value[0]
    d1 = {
        'object': object,
        'property': 'LineLength',
        'value': 0.1,
        'driven_value': 'nodes["Mapping"].inputs[3].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["LineLength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d1)

    # Line Thickness
    # bpy.data.materials["ActionMaterial"].node_tree.nodes["Mapping"].inputs[3].default_value[1]
    d2 = {
        'object': object,
        'property': 'LineThickness',
        'value': 2.0,
        'driven_value': 'nodes["Mapping"].inputs[3].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["LineThickness"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d2)

    # Line Color - Red Channel
    # bpy.data.materials["ActionMaterial"].node_tree.nodes["ColorRamp.001"].color_ramp.elements[1].color[0]
    d3 = { 
        'object': object,
        'property': 'LineColor',
        'value': (0.0, 0.0, 0.0, 1),
        'driven_value': 'nodes["ColorRamp.001"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["LineColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d3)

    # Line Color - Green Channel
    d4 = { 
        'object': object,
        'property': 'LineColor',
        'value': (0.0, 0.0, 0.0, 1),
        'driven_value': 'nodes["ColorRamp.001"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["LineColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d4)

    # Line Color - Blue Channel
    d5 = { 
        'object': object,
        'property': 'LineColor',
        'value': (0.0, 0.0, 0.0, 1),
        'driven_value': 'nodes["ColorRamp.001"].color_ramp.elements[1].color',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["LineColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d5)

    # Line Emission Strength
    # bpy.data.materials["ActionMaterial"].node_tree.nodes["Emission"].inputs[1].default_value
    d6 = {
        'object': object,
        'property': 'LineEmitStrength',
        'value': 1,
        'driven_value': 'nodes["Emission"].inputs[1].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["LineEmitStrength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d6)

    # Line Opacity
    # bpy.data.materials["ActionMaterial"].node_tree.nodes["Invert"].inputs[0].default_value
    d7 = {
        'object': object,
        'property': 'LineOpacity',
        'value': 1.0,
        'driven_value': 'nodes["Invert"].inputs[0].default_value',
        'driven_object' : object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["LineOpacity"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 10,
    }

    drivers.append(d7)

    # BG Speed
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["Mapping"].inputs[1].default_value[1]
    d8 = {
        'object': object,
        'property': 'BG_Speed',
        'value': 0.5,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : bpy.data.materials["GradientMaterial"].node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BG_Speed"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -9.40282e+38,
        'max': 9.40282e+38,
    }

    drivers.append(d8)

    # BG Noise Width
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["Mapping"].inputs[3].default_value[1]
    d9 = {
        'object': object,
        'property': 'BG_NoiseWidth',
        'value': 0.5,
        'driven_value': 'nodes["Mapping"].inputs[3].default_value',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BG_NoiseWidth"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d9)

    # BG Noise Length
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["Mapping"].inputs[3].default_value[0] 
    d10 = {
        'object': object,
        'property': 'BG_NoiseLength',
        'value': 0.1,
        'driven_value': 'nodes["Mapping"].inputs[3].default_value',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BG_NoiseLength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1000,
    }

    drivers.append(d10)

    # BG Width
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["Mapping.001"].inputs[3].default_value[1]
    d11 = {
        'object': object,
        'property': 'BG_Width',
        'value': 0.15,
        'driven_value': 'nodes["Mapping.001"].inputs[3].default_value',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BG_Width"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 1,
    }

    drivers.append(d11)

    # BG Emission Strength
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["Emission"].inputs[1].default_value
    d12 = {
        'object': object,
        'property': 'BG_EmitStrength',
        'value': 1.0,
        'driven_value': 'nodes["Emission"].inputs[1].default_value',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["BG_EmitStrength"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 20,
    }

    drivers.append(d12)

    # BG Opacity
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["Invert"].inputs[0].default_value
    d13 = {
        'object': object,
        'property': 'BG_Opacity',
        'value': 1.0,
        'driven_value': 'nodes["Invert"].inputs[0].default_value',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["BG_Opacity"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 10,
    }

    drivers.append(d13)

    # BG Color 1 - Red Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d14 = {
        'object': object,
        'property': 'BG_Color1',
        'value': [0.000491, 0.000000, 0.134770, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BG_Color1"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d14)

    # BG Color 1 - Green Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d15 = {
        'object': object,
        'property': 'BG_Color1',
        'value': [0.000491, 0.000000, 0.134770, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BG_Color1"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d15)

    # BG Color 1 - Blue Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d16 = {
        'object': object,
        'property': 'BG_Color1',
        'value': [0.000491, 0.000000, 0.134770, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["BG_Color1"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d16)

    # BG Color 2 - Red Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d17 = {
        'object': object,
        'property': 'BG_Color2',
        'value': [0.000000, 0.080023, 0.567385, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BG_Color2"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d17)

    # BG Color 2 - Green Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d18 = {
        'object': object,
        'property': 'BG_Color2',
        'value': [0.000000, 0.080023, 0.567385, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BG_Color2"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d18)

    # BG Color 2 - Blue Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d19 = {
        'object': object,
        'property': 'BG_Color2',
        'value': [0.000000, 0.080023, 0.567385, 1.000000],
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["BG_Color2"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d19)

    # BG Color 3 - Red Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d20 = {
        'object': object,
        'property': 'BG_Color3',
        'value': (1.0, 1.0, 1.0, 1),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BG_Color3"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d20)

    # BG Color 3 - Green Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d21 = {
        'object': object,
        'property': 'BG_Color3',
        'value': (1.0, 1.0, 1.0, 1),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BG_Color3"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d21)

    # BG Color 3 - Blue Channel
    # bpy.data.materials["GradientMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color[0]
    d22 = {
        'object': object,
        'property': 'BG_Color3',
        'value': (1.0, 1.0, 1.0, 1),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : bg_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["BG_Color3"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d22)

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
