# assignDriver
import bpy

drivers = {}

d0 = { 
    'object': bpy.data.objects['Grass'],
    'property': 'Color1',
    'value': (0, 0.1, 0.04, 1),
    'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
    'driven_object' : bpy.data.objects['Grass'].material_slots[0].material.node_tree,
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["Color1"][0]',
    'id_type' : 'OBJECT',
    'subtype': 'COLOR',
    'min': 0,
    'max': 1,
}

drivers.append(d0)

d1 = {
    'object': bpy.data.objects['Grass'],
    'property': 'Color1',
    'value': (0, 0.1, 0.04, 1),
    'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
    'driven_object' : bpy.data.objects['Grass'].material_slots[0].material.node_tree,
    'index' : 1,
    'variable_name' : 'var',
    'data_path' : '["Color1"][1]',
    'id_type' : 'OBJECT',
    'subtype': 'COLOR',
    'min': 0,
    'max': 1,
}

drivers.append(d1)

d2 = {
    'object': bpy.data.objects['Grass'],
    'property': 'Color1',
    'value': (0, 0.1, 0.04, 1),
    'driven_value': 'nodes["ColorRamp"].color_ramp.elements[0].color',
    'driven_object' : bpy.data.objects['Grass'].material_slots[0].material.node_tree,
    'index' : 2,
    'variable_name' : 'var',
    'data_path' : '["Color1"][2]',
    'id_type' : 'OBJECT',
    'subtype': 'COLOR',
    'min': 0,
    'max': 1,
}

drivers.append(d2)

d3 = {
    'object': bpy.data.objects['Grass'],
    'property': 'ExtendX',
    'value': 1,
    'driven_value': 'count',
    'driven_object' : bpy.context.object.modifiers['Array'],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["ExtendX"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 100,
}

drivers.append(d3)

d4 = {
    'object': bpy.data.objects['Grass'],
    'property': 'ExtendY',
    'value': 1,
    'driven_value': 'count',
    'driven_object' : bpy.context.object.modifiers['Array.001'],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["ExtendY"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 100,
}

drivers.append(d4)

d5 = {
    'object': bpy.data.objects['Grass'],
    'property': 'DisplaceStrength',
    'value': 0.1,
    'driven_value': 'strength',
    'driven_object' : bpy.context.object.modifiers["Displace"],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["DisplaceStrength"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 1,
}

drivers.append(d5)

d6 = {
    'object': bpy.data.objects['Grass'],
    'property': 'NumberOfBlades',
    'value': 5000,
    'driven_value': 'count',
    'driven_object' : bpy.data.particles["ParticleSettings"],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["NumberOfBlades"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 1000000,
}

drivers.append(d6)

d7 = {
    'object': bpy.data.objects['Grass'],
    'property': 'GrassLength',
    'value': 0.2,
    'driven_value': 'hair_length',
    'driven_object' : bpy.data.particles["ParticleSettings"],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["GrassLength"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 100,
}

drivers.append(d7)

d8 = {
    'object': bpy.data.objects['Grass'],
    'property': 'RenderMultiplier',
    'value': 100,
    'driven_value': 'rendered_child_count',
    'driven_object' : bpy.data.particles["ParticleSettings"],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["RenderMultiplier"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 1000,
}

drivers.append(d8)

d9 = {
    'object': bpy.data.objects['Grass'],
    'property': 'Twist',
    'value': 0.0,
    'driven_value': 'twist',
    'driven_object' : bpy.data.particles["ParticleSettings"],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["Twist"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 1,
}

drivers.append(d9)

d10 = {
    'object': bpy.data.objects['Grass'],
    'property': 'DisplaceScale',
    'value': 0.25,
    'driven_value': 'noise_scale',
    'driven_object' : bpy.data.textures["Clouds"],
    'index' : 0,
    'variable_name' : 'var',
    'data_path' : '["DisplaceScale"]',
    'id_type' : 'OBJECT',
    'subtype': '',
    'min': 0,
    'max': 1,
}

drivers.append(d10)


def assignDrivers():
    for i in drivers:
        d = drivers[i]
        d['object'][d['property']] = d['value']

        edit_property = d['object'].id_properties_ui(d['property'])
        edit_property.update(min=d['min'], max=d['max'])

        if d['subtype']:
            edit_property.update(subtype=d['subtype'], min=d['min'], max=d['max'])

        driver = d['driven_object'].driver_add(d['driven_value'], d['index'])

        variable = driver.driver.variables.new()
        variable.name = d['variable_name']
        variable.targets[0].id_type = d['id_type']
        variable.targets[0].id = d['object']
        variable.targets[0].data_path = d['data_path']

        driver.driver.expression = variable.name

    # Update Driver Dependencies
    for obj in bpy.context.scene.objects:
        obj.hide_render = obj.hide_render

