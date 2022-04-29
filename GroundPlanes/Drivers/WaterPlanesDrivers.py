# Assign Drivers to the Water Planes
import bpy

def assignDrivers():

    drivers = []
    
    surface_object = bpy.data.objects['SurfacePlane']
    bottom_object = bpy.data.objects['BottomPlane']

    # Surface Color 1 - Red Channel
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color
    d0 = {
        'object': surface_object, 
        'property': 'SurfaceColor1',
        'value': (0.000000, 0.005409, 0.205264, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor1"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d0)

    # Surface Color 1 - Green Channel
    d1 = {
        'object': surface_object, 
        'property': 'SurfaceColor1',
        'value': (0.000000, 0.005409, 0.205264, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor1"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d1)

    # Surface Color 1 - Blue Channel
    d2 = {
        'object': surface_object, 
        'property': 'SurfaceColor1',
        'value': (0.000000, 0.005409, 0.205264, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor1"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d2)

    # Surface Color 2
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[1].color
    d3 = { 
        'object': surface_object,
        'property': 'SurfaceColor2',
        'value': (0.220020, 0.346031, 0.602632, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor2"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d3)

    # Surface Color 2 - Green Channel
    d4 = { 
        'object': surface_object,
        'property': 'SurfaceColor2',
        'value': (0.220020, 0.346031, 0.602632, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor2"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d4)

    # Surface Color 2 - Blue Channel
    d5 = { 
        'object': surface_object,
        'property': 'SurfaceColor2',
        'value': (0.220020, 0.346031, 0.602632, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor2"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d5)

    
    # Surface Color 3 - Red Channel
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[2].color
    d6 = {
        'object': surface_object,
        'property': 'SurfaceColor3',
        'value': (1.0, 1.0, 1.0, 1.0),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor3"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d6)

    # Surface Color 3 - Green Channel
    d7 = {
        'object': surface_object,
        'property': 'SurfaceColor3',
        'value': (1.0, 1.0, 1.0, 1.0),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor3"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d7)

    # Surface Color 3 - Blue Channel
    d8 = {
        'object': surface_object,
        'property': 'SurfaceColor3',
        'value': (1.0, 1.0, 1.0, 1.0),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[2].color',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["SurfaceColor3"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d8)

    # Surface Transparent Color - Red Channel
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["Transparent BSDF"].inputs[0].default_value
    d9 = {
        'object': surface_object,
        'property': 'SurfaceTransparentColor',
        'value': (0.25, 0.25, 1, 1),
        'driven_value': 'nodes["Transparent BSDF"].inputs[0].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["SurfaceTransparentColor"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d9)

    # Surface Transparent Color - Green Channel
    d10 = {
        'object': surface_object,
        'property': 'SurfaceTransparentColor',
        'value': (0.25, 0.25, 1, 1),
        'driven_value': 'nodes["Transparent BSDF"].inputs[0].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["SurfaceTransparentColor"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d10)

    # Surface Transparent Color - Blue Channel
    d11 = {
        'object': surface_object,
        'property': 'SurfaceTransparentColor',
        'value': (0.25, 0.25, 1, 1),
        'driven_value': 'nodes["Transparent BSDF"].inputs[0].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["SurfaceTransparentColor"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d11)

    # Bottom Color 1 - Red Channel
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[0].color
    d12 = {
        'object': surface_object,
        'property': 'BottomColor1',
        'value': (0.028821, 0.052685, 0.215383, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BottomColor1"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d12)

    # Bottom Color 1 - Green Channel
    d13 = {
        'object': surface_object,
        'property': 'BottomColor1',
        'value': (0.028821, 0.052685, 0.215383, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BottomColor1"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d13)

    # Bottom Color 1 - Blue Channel
    d14 = {
        'object': surface_object,
        'property': 'BottomColor1',
        'value': (0.028821, 0.052685, 0.215383, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["BottomColor1"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d14)

    # Bottom Color 2
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["ColorRamp"].color_ramp.elements[1].color
    d15 = {
        'object': surface_object,
        'property': 'BottomColor2',
        'value': (0.000000, 0.001229, 0.034772, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BottomColor2"][0]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d15)

    # Bottom Color 1 - Blue Channel
    d16 = {
        'object': surface_object,
        'property': 'BottomColor2',
        'value': (0.000000, 0.001229, 0.034772, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["BottomColor2"][1]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d16)

    # Bottom Color 1 - Blue Channel
    d17 = {
        'object': surface_object,
        'property': 'BottomColor2',
        'value': (0.000000, 0.001229, 0.034772, 1.000000),
        'driven_value': 'nodes["ColorRamp"].color_ramp.elements[1].color',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 2,
        'variable_name' : 'var',
        'data_path' : '["BottomColor2"][2]',
        'id_type' : 'OBJECT',
        'subtype': 'COLOR',
        'min': 0,
        'max': 1,
    }

    drivers.append(d17)

    # Surface Large Ripples Speed
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["Mapping.002"].inputs[1].default_value[0]
    d18 = {
        'object': surface_object,
        'property': 'BigRippleSpeed',
        'value': 0.0,
        'driven_value': 'nodes["Mapping.002"].inputs[1].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BigRippleSpeed"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -9.40282e+38,
        'max': 9.40282e+38,
    }

    drivers.append(d18)

    # Bottom Large Ripples Speed
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["Mapping.002"].inputs[1].default_value[0]
    d19 = {
        'object': surface_object,
        'property': 'BigRippleSpeed',
        'value': 0.0,
        'driven_value': 'nodes["Mapping.002"].inputs[1].default_value',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["BigRippleSpeed"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -9.40282e+38,
        'max': 9.40282e+38,
    }

    drivers.append(d19)

    # Surface Small Ripples Speed
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["Mapping.001"].inputs[1].default_value[0]
    d20 = {
        'object': surface_object,
        'property': 'SmallRippleSpeed',
        'value': 0.0,
        'driven_value': 'nodes["Mapping.001"].inputs[1].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["SmallRippleSpeed"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -9.40282e+38,
        'max': 9.40282e+38,
    }

    drivers.append(d20)

    # Bottom Small Ripples Speed
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["Mapping.001"].inputs[1].default_value[0]
    d21 = {
        'object': surface_object,
        'property': 'SmallRippleSpeed',
        'value': 0.0,
        'driven_value': 'nodes["Mapping.001"].inputs[1].default_value',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["SmallRippleSpeed"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -9.40282e+38,
        'max': 9.40282e+38,
    }

    drivers.append(d21)

    # Surface Large Ripple Scale
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["Musgrave Texture.001"].inputs[2].default_value
    d22 = {
        'object': surface_object,
        'property': 'BigRippleScale',
        'value': 5.0,
        'driven_value': 'nodes["Musgrave Texture.001"].inputs[2].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["BigRippleScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d22)
    
    # Bottom Large Ripple Scale
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["Musgrave Texture.001"].inputs[2].default_value
    d23 = {
        'object': surface_object,
        'property': 'BigRippleScale',
        'value': 5.0,
        'driven_value': 'nodes["Musgrave Texture.001"].inputs[2].default_value',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["BigRippleScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d23)

    # Surface Small Ripple Scale
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["Musgrave Texture"].inputs[2].default_value
    d24 = {
        'object': surface_object,
        'property': 'SmallRippleScale',
        'value': 1.0,
        'driven_value': 'nodes["Musgrave Texture"].inputs[2].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["SmallRippleScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 10,
    }

    drivers.append(d24)
    
    # Bottom Small Ripple Scale
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["Musgrave Texture"].inputs[2].default_value
    d25 = {
        'object': surface_object,
        'property': 'SmallRippleScale',
        'value': 1.0,
        'driven_value': 'nodes["Musgrave Texture"].inputs[2].default_value',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["SmallRippleScale"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 10,
    }

    drivers.append(d25)
    
    # Surface Motion X
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["Mapping"].inputs[1].default_value[0]
    d26 = {
        'object': surface_object,
        'property': 'MotionX',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["MotionX"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d26)

    # Bottom Motion X
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["Mapping"].inputs[1].default_value[0]
    d27 = {
        'object': surface_object,
        'property': 'MotionX',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 0,
        'variable_name' : 'var',
        'data_path' : '["MotionX"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d27)

    # Surface Motion Y
    # bpy.data.materials["SurfaceMaterial"].node_tree.nodes["Mapping"].inputs[1].default_value[1]
    d28 = {
        'object': surface_object,
        'property': 'MotionY',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : surface_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["MotionY"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d28)

    # Bottom Motion Y
    # bpy.data.materials["BottomMaterial"].node_tree.nodes["Mapping"].inputs[1].default_value[1]
    d29 = {
        'object': surface_object,
        'property': 'MotionY',
        'value': 0.0,
        'driven_value': 'nodes["Mapping"].inputs[1].default_value',
        'driven_object' : bottom_object.material_slots[0].material.node_tree,
        'index' : 1,
        'variable_name' : 'var',
        'data_path' : '["MotionY"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': -100,
        'max': 100,
    }

    drivers.append(d29)

    # Surface Array - X Count
    d30 = {
        'object': surface_object,
        'property': 'ExtendX',
        'value': 1,
        'driven_value': 'count',
        'driven_object' : surface_object.modifiers['Array'],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["ExtendX"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d30)

    # Surface Array - Y Count
    d31 = {
        'object': surface_object,
        'property': 'ExtendY',
        'value': 1,
        'driven_value': 'count',
        'driven_object' : surface_object.modifiers['Array.001'],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["ExtendY"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d31)

    # Bottom Array - X Count
    d32 = {
        'object': surface_object,
        'property': 'ExtendX',
        'value': 1,
        'driven_value': 'count',
        'driven_object' : bottom_object.modifiers['Array'],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["ExtendX"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d32)

    # Bottom Array - Y Count
    d33 = {
        'object': surface_object,
        'property': 'ExtendY',
        'value': 1,
        'driven_value': 'count',
        'driven_object' : bottom_object.modifiers['Array.001'],
        'index' : -1,
        'variable_name' : 'var',
        'data_path' : '["ExtendY"]',
        'id_type' : 'OBJECT',
        'subtype': '',
        'min': 0,
        'max': 100,
    }

    drivers.append(d33)
    
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
