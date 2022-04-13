# Grass Generator
import bpy

def generateGrassPlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    grassplane = bpy.context.object
    grassplane.name = 'Grass'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_x = grassplane.modifiers['Array']
    array_x.count = 1

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = grassplane.modifiers['Array.001']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = grassplane.modifiers["Subdivision"]
    subsurf.levels = 3
    subsurf.render_levels = 3
    subsurf.subdivision_type = 'SIMPLE'

    grasstex = bpy.data.textures.new(name='Clouds', type = 'CLOUDS')
    grasstex.noise_scale = 1

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = grassplane.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.5
    displace.texture = grasstex

    bpy.ops.object.particle_system_add()
    particle = bpy.context.object.particle_systems[0].settings
    particle.type = 'HAIR'
    particle.count = 5000
    particle.hair_length = 0.2
    particle.hair_step = 2
    particle.render_step = 2
    particle.child_type = 'SIMPLE'
    particle.clump_factor = -1
    particle.use_modifier_stack = True
    bpy.context.scene.render.hair_type = 'STRIP'

    grassmat = bpy.data.materials.new(name='GrassMaterial')
    grassmat.use_nodes = True
    grassmat.shadow_method = 'NONE'
    grassmat.node_tree.nodes.clear()

    nodes = grassmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')
    emission = nodes.new(type='ShaderNodeEmission')
    # Shadow Nodes Start
    shadowmixrgb = nodes.new(type='ShaderNodeMixRGB')
    huesaturation = nodes.new(type='ShaderNodeHueSaturation')
    huesaturation.inputs[0].default_value = 0.7
    huesaturation.inputs[1].default_value = 0.7
    huesaturation.inputs[2].default_value = 0.1
    shadertorgb = nodes.new(type='ShaderNodeShaderToRGB')
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
    normal = nodes.new(type='ShaderNodeNormal')
    #Shadow Nodes End
    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.elements[0].color = (0, 0.1, 0.04, 1)
    colorramp.color_ramp.elements[1].color = (0, 0.5, 0.15, 1)
    noise = nodes.new(type='ShaderNodeTexNoise')

    links = grassmat.node_tree.links

    links.new(emission.outputs[0], output.inputs[0])
    links.new(shadowmixrgb.outputs[0], emission.inputs[0])
    links.new(colorramp.outputs[0], shadowmixrgb.inputs[2])
    links.new(colorramp.outputs[0], huesaturation.inputs[4])
    links.new(shadertorgb.outputs[0], shadowmixrgb.inputs[0])
    links.new(huesaturation.outputs[0], shadowmixrgb.inputs[1])
    links.new(diffuse.outputs[0], shadertorgb.inputs[0])
    links.new(normal.outputs[0], diffuse.inputs[2])
    links.new(noise.outputs[0], colorramp.inputs[0])
    
    bpy.context.object.data.materials.append(grassmat)

    # Create Custom Properties
    object = bpy.context.object

    property1 = 'RepeatX'
    property2 = 'RepeatY'
    value = 1

    object[property1] = value

    edit_property = object.id_properties_ui(property1)
    edit_property.update(
                    #subtype='COLOR',
                    min=1,
                    max=100,
                    description='',
                    #soft_min=0,
                    #soft_max=1,
                    )
    
    object[property2] = value

    edit_property = object.id_properties_ui(property2)
    edit_property.update(
                    #subtype='COLOR',
                    min=1,
                    max=100,
                    description='',
                    #soft_min=0,
                    #soft_max=1,
                    )

    # Assign Drivers
    driven_value = "count"

    driven_object = bpy.context.object.modifiers['Array']

    driver = driven_object.driver_add(driven_value)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.context.object
    var.targets[0].data_path = '["RepeatX"]'

    driver.driver.expression = var.name

    driven_value = "count"

    driven_object = bpy.context.object.modifiers['Array.001']

    driver = driven_object.driver_add(driven_value)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.context.object
    var.targets[0].data_path = '["RepeatY"]'

    driver.driver.expression = var.name 

    # Create Properties
    object = bpy.data.objects['Grass']

    #Color1
    property = 'Color1'

    object[property] = (0, 0.1, 0.04, 1)

    edit_property = object.id_properties_ui(property)
    edit_property.update(subtype='COLOR', min=0, max=1)

    # Add Drivers
    path = 'nodes["ColorRamp"].color_ramp.elements[0].color'

    node_tree = bpy.data.objects['Grass'].material_slots[0].material.node_tree

    driver = node_tree.driver_add(path, 0)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['Grass']
    var.targets[0].data_path = '["Color1"][0]'

    driver.driver.expression = var.name 

    driver = node_tree.driver_add(path, 1)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['Grass']
    var.targets[0].data_path = '["Color1"][1]'

    driver.driver.expression = var.name 

    driver = node_tree.driver_add(path, 2)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['Grass']
    var.targets[0].data_path = '["Color1"][2]'

    driver.driver.expression = var.name 

    # Color2
    property = 'Color2'

    object[property] = (0, 0.5, 0.15, 1)

    edit_property = object.id_properties_ui(property)
    edit_property.update(
                        subtype='COLOR',
                        min=0,
                        max=1,
                        )

    # Add Drivers
    path = 'nodes["ColorRamp"].color_ramp.elements[1].color'

    node_tree = bpy.data.objects['Grass'].material_slots[0].material.node_tree

    driver = node_tree.driver_add(path, 0)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['Grass']
    var.targets[0].data_path = '["Color2"][0]'

    driver.driver.expression = var.name 

    driver = node_tree.driver_add(path, 1)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['Grass']
    var.targets[0].data_path = '["Color2"][1]'

    driver.driver.expression = var.name 

    driver = node_tree.driver_add(path, 2)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['Grass']
    var.targets[0].data_path = '["Color2"][2]'

    driver.driver.expression = var.name 

    # Update Driver Dependencies
    for obj in bpy.context.scene.objects:
        obj.hide_render = obj.hide_render


class OBJECT_OT_generateGrassPlane(bpy.types.Operator):
    """Create a stylized grass plane"""
    bl_idname = "mesh.generate_grass_plane"
    bl_label = "Add Stylized Grass"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateGrassPlane()

        return {'FINISHED'}
