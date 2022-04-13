# Water Planes
import bpy

def generateWaterPlanes():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    surfaceplane = bpy.context.object
    surfaceplane.name = 'SurfacePlane'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_x = surfaceplane.modifiers['Array']
    array_x.count = 1

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = surfaceplane.modifiers['Array.001']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = surfaceplane.modifiers["Subdivision"]
    subsurf.levels = 4
    subsurf.render_levels = 4
    subsurf.subdivision_type = 'SIMPLE'

    watertex = bpy.data.textures.new(name='WaterClouds', type = 'CLOUDS')
    watertex.noise_depth = 6

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = surfaceplane.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.1
    displace.texture = watertex

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, -0.2), scale=(1, 1, 1))
    bottomplane = bpy.context.object
    bottomplane.name = 'BottomPlane'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_x = bottomplane.modifiers['Array']
    array_x.count = 1

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = bottomplane.modifiers['Array.001']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    surfacemat = bpy.data.materials.new(name='SurfaceMaterial')
    surfacemat.use_nodes = True
    surfacemat.node_tree.nodes.clear()
    surfacemat.blend_method = 'BLEND'
    surfacemat.shadow_method = 'NONE'

    nodes = surfacemat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 5
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    transparent.inputs[0].default_value = (0.25, 0.25, 1, 1)

    # Shadow Nodes Start
    shadowmixrgb = nodes.new(type='ShaderNodeMixRGB')
    huesaturation = nodes.new(type='ShaderNodeHueSaturation')
    huesaturation.inputs[0].default_value = 0.7
    huesaturation.inputs[1].default_value = 0.7
    huesaturation.inputs[2].default_value = 0
    shadertorgb = nodes.new(type='ShaderNodeShaderToRGB')
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
    normal = nodes.new(type='ShaderNodeNormal')
    #Shadow Nodes End

    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.elements.new(0.5)
    colorramp1.color_ramp.elements[0].position = 0
    colorramp1.color_ramp.elements[1].position = 0.25
    colorramp1.color_ramp.elements[2].position = 0.5
    colorramp1.color_ramp.elements[0].color = (0.000000, 0.005409, 0.205264, 1.000000)
    colorramp1.color_ramp.elements[1].color = (0.220020, 0.346031, 0.602632, 1.000000)
    colorramp1.color_ramp.elements[2].color = (1, 1, 1, 1)

    colorramp2 = nodes.new(type='ShaderNodeValToRGB')
    colorramp2.color_ramp.elements[0].position = 0.1
    colorramp2.color_ramp.elements[1].position = 0.2
    colorramp2.color_ramp.elements[0].color = (1, 1, 1, 1)
    colorramp2.color_ramp.elements[1].color = (0, 0, 0, 1)

    subtract = nodes.new(type='ShaderNodeMath')
    subtract.operation = 'SUBTRACT'

    voronoi1 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi1.voronoi_dimensions = '2D'
    voronoi1.inputs[2].default_value = 20
    voronoi2 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi2.voronoi_dimensions = '2D'
    voronoi2.feature = 'SMOOTH_F1'
    voronoi2.inputs[2].default_value = 20

    mapping1 = nodes.new(type='ShaderNodeMapping')

    combinexyz = nodes.new(type='ShaderNodeCombineXYZ')

    separatexyz = nodes.new(type='ShaderNodeSeparateXYZ')

    texcoord1 = nodes.new(type='ShaderNodeTexCoord')

    musgrave1 = nodes.new(type='ShaderNodeTexMusgrave')
    musgrave1.inputs[2].default_value = 50
    musgrave1.inputs[3].default_value = 0.005
    mapping2 = nodes.new(type='ShaderNodeMapping')
    texcoord2 = nodes.new(type='ShaderNodeTexCoord')
    add1 = nodes.new(type='ShaderNodeMath')

    musgrave2 = nodes.new(type='ShaderNodeTexMusgrave')
    musgrave2.inputs[2].default_value = 10
    musgrave2.inputs[3].default_value = 0.02
    mapping3 = nodes.new(type='ShaderNodeMapping')
    texcoord3 = nodes.new(type='ShaderNodeTexCoord')
    add2 = nodes.new(type='ShaderNodeMath')

    links = surfacemat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(emission.outputs[0], mixshader.inputs[1])

    links.new(shadowmixrgb.outputs[0], emission.inputs[0])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(colorramp2.outputs[0], mixshader.inputs[0])

    links.new(colorramp1.outputs[0], huesaturation.inputs[4])
    links.new(colorramp1.outputs[0], shadowmixrgb.inputs[2])

    links.new(shadertorgb.outputs[0], shadowmixrgb.inputs[0])
    links.new(huesaturation.outputs[0], shadowmixrgb.inputs[1])
    links.new(diffuse.outputs[0], shadertorgb.inputs[0])
    links.new(normal.outputs[0], diffuse.inputs[2])

    links.new(subtract.outputs[0], colorramp2.inputs[0])

    links.new(voronoi1.outputs[0], subtract.inputs[0])
    links.new(voronoi2.outputs[0], subtract.inputs[1])

    links.new(mapping1.outputs[0], voronoi1.inputs[0])
    links.new(mapping1.outputs[0], voronoi2.inputs[0])

    links.new(combinexyz.outputs[0], mapping1.inputs[0])

    links.new(separatexyz.outputs[0], combinexyz.inputs[0])
    links.new(separatexyz.outputs[2], combinexyz.inputs[2])
    links.new(texcoord1.outputs[0], separatexyz.inputs[0])

    links.new(add1.outputs[0], combinexyz.inputs[1])

    links.new(musgrave1.outputs[0], add1.inputs[1])
    links.new(mapping2.outputs[0], musgrave1.inputs[0])
    links.new(texcoord2.outputs[0], mapping2.inputs[0])

    links.new(add2.outputs[0], add1.inputs[0])
    links.new(musgrave2.outputs[0], add2.inputs[1])
    links.new(mapping3.outputs[0], musgrave2.inputs[0])
    links.new(texcoord3.outputs[0], mapping3.inputs[0])

    links.new(separatexyz.outputs[1], add2.inputs[0])

    surfaceplane.data.materials.append(surfacemat)

    # Create Custom Properties
    object = surfaceplane

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

    driven_object = bpy.data.objects['SurfacePlane'].modifiers['Array']

    driver = driven_object.driver_add(driven_value)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['SurfacePlane']
    var.targets[0].data_path = '["RepeatX"]'

    driver.driver.expression = var.name

    driven_value = "count"

    driven_object = bpy.data.objects['SurfacePlane'].modifiers['Array.001']

    driver = driven_object.driver_add(driven_value)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['SurfacePlane']
    var.targets[0].data_path = '["RepeatY"]'

    driver.driver.expression = var.name 

    bottommat = bpy.data.materials.new(name='BottomMaterial')
    bottommat.use_nodes = True
    bottommat.node_tree.nodes.clear()

    nodes = bottommat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    emission = nodes.new(type='ShaderNodeEmission')

    # Shadow Nodes Start
    shadowmixrgb = nodes.new(type='ShaderNodeMixRGB')
    huesaturation = nodes.new(type='ShaderNodeHueSaturation')
    huesaturation.inputs[0].default_value = 0.5
    huesaturation.inputs[1].default_value = 0.7
    huesaturation.inputs[2].default_value = 0.1
    shadertorgb = nodes.new(type='ShaderNodeShaderToRGB')
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
    normal = nodes.new(type='ShaderNodeNormal')
    #Shadow Nodes End

    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.elements[0].position = 0
    colorramp.color_ramp.elements[1].position = 0.25
    colorramp.color_ramp.elements[0].color = (0.028821, 0.052685, 0.215383, 1.000000)
    colorramp.color_ramp.elements[1].color = (0.000000, 0.001229, 0.034772, 1.000000)

    subtract = nodes.new(type='ShaderNodeMath')
    subtract.operation = 'SUBTRACT'

    voronoi1 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi1.voronoi_dimensions = '2D'
    voronoi1.inputs[2].default_value = 20
    voronoi2 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi2.voronoi_dimensions = '2D'
    voronoi2.feature = 'SMOOTH_F1'
    voronoi2.inputs[2].default_value = 20

    mapping1 = nodes.new(type='ShaderNodeMapping')

    combinexyz = nodes.new(type='ShaderNodeCombineXYZ')

    separatexyz = nodes.new(type='ShaderNodeSeparateXYZ')

    texcoord1 = nodes.new(type='ShaderNodeTexCoord')

    musgrave1 = nodes.new(type='ShaderNodeTexMusgrave')
    musgrave1.inputs[2].default_value = 50
    musgrave1.inputs[3].default_value = 0.005
    mapping2 = nodes.new(type='ShaderNodeMapping')
    texcoord2 = nodes.new(type='ShaderNodeTexCoord')
    add1 = nodes.new(type='ShaderNodeMath')

    musgrave2 = nodes.new(type='ShaderNodeTexMusgrave')
    musgrave2.inputs[2].default_value = 10
    musgrave2.inputs[3].default_value = 0.02
    mapping3 = nodes.new(type='ShaderNodeMapping')
    texcoord3 = nodes.new(type='ShaderNodeTexCoord')
    add2 = nodes.new(type='ShaderNodeMath')

    links = bottommat.node_tree.links

    links.new(emission.outputs[0], output.inputs[0])

    links.new(shadowmixrgb.outputs[0], emission.inputs[0])

    links.new(colorramp.outputs[0], huesaturation.inputs[4])
    links.new(colorramp.outputs[0], shadowmixrgb.inputs[2])

    links.new(shadertorgb.outputs[0], shadowmixrgb.inputs[0])
    links.new(huesaturation.outputs[0], shadowmixrgb.inputs[1])
    links.new(diffuse.outputs[0], shadertorgb.inputs[0])
    links.new(normal.outputs[0], diffuse.inputs[2])

    links.new(subtract.outputs[0], colorramp.inputs[0])

    links.new(voronoi1.outputs[0], subtract.inputs[0])
    links.new(voronoi2.outputs[0], subtract.inputs[1])

    links.new(mapping1.outputs[0], voronoi1.inputs[0])
    links.new(mapping1.outputs[0], voronoi2.inputs[0])

    links.new(combinexyz.outputs[0], mapping1.inputs[0])

    links.new(separatexyz.outputs[0], combinexyz.inputs[0])
    links.new(separatexyz.outputs[2], combinexyz.inputs[2])
    links.new(texcoord1.outputs[0], separatexyz.inputs[0])

    links.new(add1.outputs[0], combinexyz.inputs[1])

    links.new(musgrave1.outputs[0], add1.inputs[1])
    links.new(mapping2.outputs[0], musgrave1.inputs[0])
    links.new(texcoord2.outputs[0], mapping2.inputs[0])

    links.new(add2.outputs[0], add1.inputs[0])
    links.new(musgrave2.outputs[0], add2.inputs[1])
    links.new(mapping3.outputs[0], musgrave2.inputs[0])
    links.new(texcoord3.outputs[0], mapping3.inputs[0])

    links.new(separatexyz.outputs[1], add2.inputs[0])

    bottomplane.data.materials.append(bottommat)

    surfaceplane = bpy.data.objects['SurfacePlane']
    bottomplane = bpy.data.objects['BottomPlane']

    bottomplane.parent = surfaceplane


    # Assign Drivers
    driven_value = "count"

    driven_object = bpy.context.object.modifiers['Array']

    driver = driven_object.driver_add(driven_value)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['SurfacePlane']
    var.targets[0].data_path = '["RepeatX"]'

    driver.driver.expression = var.name

    driven_value = "count"

    driven_object = bpy.context.object.modifiers['Array.001']

    driver = driven_object.driver_add(driven_value)

    var = driver.driver.variables.new()
    var.name = 'var'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = bpy.data.objects['SurfacePlane']
    var.targets[0].data_path = '["RepeatY"]'

    driver.driver.expression = var.name 


class OBJECT_OT_generateWaterPlanes(bpy.types.Operator):
    """Create a stylized water planes"""
    bl_idname = "mesh.generate_water_planes"
    bl_label = "Add Stylized Water Planes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateWaterPlanes()

        return {'FINISHED'}
