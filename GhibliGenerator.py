# Ghibli Generator

bl_info = {
    "name": "Ghibli Generator",
    "author": "Spectral Vectors",
    "version": (0, 2),
    "blender": (2, 80, 0),
    "location": "View 3D > Properties Panel",
    "description": "Procedural Anime Assets",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy

# Grass Generator

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
    grassmat.node_tree.nodes.clear()

    nodes = grassmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')
    emission = nodes.new(type='ShaderNodeEmission')
    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.elements[0].color = (0, 0.1, 0.04, 1)
    colorramp.color_ramp.elements[1].color = (0, 0.5, 0.15, 1)
    noise = nodes.new(type='ShaderNodeTexNoise')

    links = grassmat.node_tree.links

    links.new(noise.outputs[0], colorramp.inputs[0])
    links.new(colorramp.outputs[0], emission.inputs[0])
    links.new(emission.outputs[0], output.inputs[0])

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


class OBJECT_OT_generateGrassPlane(bpy.types.Operator):
    """Create a stylized grass plane"""
    bl_idname = "mesh.generate_grass_plane"
    bl_label = "Add Stylized Grass"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateGrassPlane()

        return {'FINISHED'}

# Rock Generator

def generateRock():

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    rock = bpy.context.object
    rock.scale[2] = 0.75
    rock.name = 'Rock'
    bpy.ops.object.shade_smooth()

    rocktex = bpy.data.textures.new(name='Clouds', type = 'CLOUDS')
    rocktex.noise_scale = 0.5

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = rock.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.5
    displace.texture = rocktex

    rockmat = bpy.data.materials.new(name='RockMaterial')
    rockmat.use_nodes = True
    rockmat.node_tree.nodes.clear()

    nodes = rockmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    emission = nodes.new(type='ShaderNodeEmission')

    mixrgb1 = nodes.new(type='ShaderNodeMixRGB')
    mixrgb1.inputs[2].default_value = (0.1, 0.2, 0.3, 1)

    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.elements[0].position = 0.25
    colorramp1.color_ramp.elements[1].position = 0.8
    multiply = nodes.new(type='ShaderNodeMixRGB')
    multiply.inputs[0].default_value = 0.9
    multiply.blend_type = 'MULTIPLY'

    colorramp2 = nodes.new(type='ShaderNodeValToRGB')
    colorramp2.color_ramp.elements[0].color = (0.015712, 0.031914, 0.038389, 1.000000)
    colorramp2.color_ramp.elements[1].color = (0.046440, 0.105856, 0.149684, 1.000000)
    colorramp3 = nodes.new(type='ShaderNodeValToRGB')
    colorramp3.color_ramp.elements[0].color = (0.005042, 0.021007, 0.044304, 1.000000)
    colorramp3.color_ramp.elements[1].color = (0.030861, 0.057856, 0.127087, 1.000000)

    mixrgb2 = nodes.new(type='ShaderNodeMixRGB')

    softlight = nodes.new(type='ShaderNodeMixRGB')
    softlight.inputs[0].default_value = 0.3
    softlight.blend_type = 'SOFT_LIGHT'
    gradient = nodes.new(type='ShaderNodeTexGradient')

    voronoi1 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi1.feature = 'SMOOTH_F1'
    voronoi1.inputs[1].default_value = 3
    voronoi2 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi2.feature = 'SMOOTH_F1'
    voronoi2.inputs[1].default_value = 24
    voronoi2.inputs[3].default_value = 1
    mapping1 = nodes.new(type='ShaderNodeMapping')
    mapping1.inputs[2].default_value = (0, 1.5708, 0)

    mapping2 = nodes.new(type='ShaderNodeMapping')
    colorramp4 = nodes.new(type='ShaderNodeValToRGB')
    colorramp4.color_ramp.elements[0].position = 0.3
    colorramp4.color_ramp.elements[1].position = 0.6
    texcoord1 = nodes.new(type='ShaderNodeTexCoord')

    texcoord2 = nodes.new(type='ShaderNodeTexCoord')
    objectinfo = nodes.new(type='ShaderNodeObjectInfo')
    mixrgb3 = nodes.new(type='ShaderNodeMixRGB')
    mixrgb3.inputs[0].default_value = 0.9
    mixrgb3.inputs[2].default_value = (1, 1, 1, 1)
    noise1 = nodes.new(type='ShaderNodeTexNoise')
    noise1.inputs[2].default_value = 100
    noise1.inputs[3].default_value = 15

    noise2 = nodes.new(type='ShaderNodeTexNoise')
    noise2.inputs[2].default_value = 30
    noise2.inputs[3].default_value = 0.01

    links = rockmat.node_tree.links

    links.new(emission.outputs[0], output.inputs[0])

    links.new(mixrgb1.outputs[0], emission.inputs[0])

    links.new(colorramp1.outputs[0], mixrgb1.inputs[0])
    links.new(multiply.outputs[0], mixrgb1.inputs[1])

    links.new(mixrgb2.outputs[0], colorramp1.inputs[0])

    links.new(colorramp2.outputs[0], multiply.inputs[1])
    links.new(colorramp3.outputs[0], multiply.inputs[2])

    links.new(softlight.outputs[0], colorramp2.inputs[0])

    links.new(mixrgb2.outputs[0], colorramp3.inputs[0])

    links.new(softlight.outputs[0], mixrgb2.inputs[1])

    links.new(gradient.outputs[0], mixrgb2.inputs[2])

    links.new(voronoi1.outputs[1], softlight.inputs[1])

    links.new(voronoi2.outputs[1], softlight.inputs[2])

    links.new(mapping1.outputs[0], gradient.inputs[0])

    links.new(mapping2.outputs[0], voronoi1.inputs[0])
    links.new(mapping2.outputs[0], voronoi2.inputs[0])

    links.new(colorramp4.outputs[0], voronoi1.inputs[3])
    links.new(colorramp4.outputs[0], voronoi2.inputs[3])

    links.new(texcoord1.outputs[0], mapping1.inputs[0])

    links.new(texcoord2.outputs[0], mapping2.inputs[0])

    links.new(objectinfo.outputs[0], mapping2.inputs[1])

    links.new(mixrgb3.outputs[0], mapping2.inputs[3])

    links.new(noise1.outputs[1], colorramp4.inputs[0])

    links.new(noise2.outputs[1], mixrgb3.inputs[1])

    bpy.context.object.data.materials.append(rockmat)

class OBJECT_OT_generateRock(bpy.types.Operator):
    """Create a stylized rock"""
    bl_idname = "mesh.generate_rock"
    bl_label = "Add Stylized Rock"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateRock()

        return {'FINISHED'}

# Rain Plane

def generateRainPlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    rainplane = bpy.context.object
    rainplane.name = 'Rain'
    rainplane.rotation_euler[1] = 1.5708
    bpy.ops.object.shade_smooth()

    rainmat = bpy.data.materials.new(name='RainMaterial')
    rainmat.use_nodes = True
    rainmat.node_tree.nodes.clear()
    rainmat.blend_method = 'BLEND'

    nodes = rainmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    mixrgb = nodes.new(type='ShaderNodeMixRGB')

    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.elements[0].position = 0.6
    colorramp1.color_ramp.elements[1].position = 1
    colorramp1.color_ramp.elements[0].color = (1, 1, 1, 1)
    colorramp1.color_ramp.elements[1].color = (0, 0, 0, 1.000000)
    colorramp2 = nodes.new(type='ShaderNodeValToRGB')
    colorramp2.color_ramp.elements[0].position = 0.6
    colorramp2.color_ramp.elements[1].position = 1
    colorramp2.color_ramp.elements[0].color = (1, 1, 1, 1)
    colorramp2.color_ramp.elements[1].color = (0, 0, 0, 1)

    noise1 = nodes.new(type='ShaderNodeTexNoise')
    noise1.inputs[2].default_value = 10

    noise2 = nodes.new(type='ShaderNodeTexNoise')
    noise2.inputs[2].default_value = 15

    mapping1 = nodes.new(type='ShaderNodeMapping')
    mapping1.inputs[3].default_value = (0.5, 10, 1)

    mapping2 = nodes.new(type='ShaderNodeMapping')
    mapping2.inputs[3].default_value = (0.8, 15, 1)

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = rainmat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(mixrgb.outputs[0], mixshader.inputs[0])

    links.new(emission.outputs[0], mixshader.inputs[1])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(colorramp1.outputs[0], mixrgb.inputs[1])

    links.new(colorramp2.outputs[0], mixrgb.inputs[2])

    links.new(noise1.outputs[1], colorramp1.inputs[0])

    links.new(noise2.outputs[1], colorramp2.inputs[0])

    links.new(mapping1.outputs[0], noise1.inputs[0])

    links.new(mapping2.outputs[0], noise2.inputs[0])

    links.new(texcoord.outputs[0], mapping1.inputs[0])
    links.new(texcoord.outputs[0], mapping2.inputs[0])

    bpy.context.object.data.materials.append(rainmat)

class OBJECT_OT_generateRainPlane(bpy.types.Operator):
    """Create a stylized rain plane"""
    bl_idname = "mesh.generate_rain_plane"
    bl_label = "Add Stylized Rain"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateRainPlane()

        return {'FINISHED'}

# Action Planes

def generateActionPlanes():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    nearplane = bpy.context.object
    nearplane.rotation_euler[1] = 1.5708
    nearplane.name = 'NearLines'
    bpy.ops.object.shade_smooth()

    bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(-2, 0, 0), scale=(1, 1, 1))
    farplane = bpy.context.object
    farplane.rotation_euler[1] = 1.5708
    farplane.name = 'FarLines'
    bpy.ops.object.shade_smooth()

    bpy.ops.mesh.primitive_plane_add(size=10, enter_editmode=False, align='WORLD', location=(-5, 0, 0), scale=(1, 1, 1))
    gradientplane = bpy.context.object
    gradientplane.rotation_euler[1] = 1.5708
    gradientplane.name = 'GradientBG'
    bpy.ops.object.shade_smooth()

    actionmat = bpy.data.materials.new(name='ActionMaterial')
    actionmat.use_nodes = True
    actionmat.node_tree.nodes.clear()
    actionmat.blend_method = 'BLEND'

    nodes = actionmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[0].default_value = (0, 0, 0, 1)
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.elements[1].position = 0.635
    colorramp.color_ramp.elements[1].color = (0, 0, 0, 1)
    colorramp.color_ramp.elements[0].color = (1, 1, 1, 1)
    colorramp.color_ramp.interpolation = 'CONSTANT'

    noise = nodes.new(type='ShaderNodeTexNoise')
    noise.inputs[2].default_value = 10

    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.inputs[3].default_value = (0.1, 15, 1)

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = actionmat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(emission.outputs[0], mixshader.inputs[1])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(colorramp.outputs[0], mixshader.inputs[0])

    links.new(noise.outputs[1], colorramp.inputs[0])

    links.new(mapping.outputs[0], noise.inputs[0])

    links.new(texcoord.outputs[3], mapping.inputs[0])

    nearplane.data.materials.append(actionmat)
    farplane.data.materials.append(actionmat)

    gradientmat = bpy.data.materials.new(name='GradientMaterial')
    gradientmat.use_nodes = True
    gradientmat.node_tree.nodes.clear()

    nodes = gradientmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    emission = nodes.new(type='ShaderNodeEmission')

    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.elements.new(0.5)
    colorramp1.color_ramp.elements[0].position = 0
    colorramp1.color_ramp.elements[1].position = 0.1
    colorramp1.color_ramp.elements[2].position = 1
    colorramp1.color_ramp.elements[0].color = (0.000491, 0.000000, 0.134770, 1.000000)
    colorramp1.color_ramp.elements[1].color = (0.000000, 0.080023, 0.567385, 1.000000)
    colorramp1.color_ramp.elements[2].color = (1, 1, 1, 1)

    colorramp2 = nodes.new(type='ShaderNodeValToRGB')
    colorramp2.color_ramp.elements.new(0.5)
    colorramp2.color_ramp.elements[0].position = 0.3
    colorramp2.color_ramp.elements[1].position = 0.5
    colorramp2.color_ramp.elements[2].position = 0.7
    colorramp2.color_ramp.elements[0].color = (0, 0, 0, 1)
    colorramp2.color_ramp.elements[1].color = (0.5, 0.5, 0.5, 1)
    colorramp2.color_ramp.elements[2].color = (0, 0, 0, 1)
    colorramp2.color_ramp.interpolation = 'B_SPLINE'

    gradient = nodes.new(type='ShaderNodeTexGradient')

    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.inputs[1].default_value = (0.5, 0, 0)
    mapping.inputs[2].default_value = (0, 0, 1.5708)
    mapping.inputs[3].default_value = (2, 0.2, 1)

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = gradientmat.node_tree.links

    links.new(emission.outputs[0], output.inputs[0])

    links.new(colorramp1.outputs[0], emission.inputs[0])

    links.new(colorramp2.outputs[0], colorramp1.inputs[0])

    links.new(gradient.outputs[0], colorramp2.inputs[0])

    links.new(mapping.outputs[0], gradient.inputs[0])

    links.new(texcoord.outputs[3], mapping.inputs[0])

    gradientplane.data.materials.append(gradientmat)

    nearplane = bpy.data.objects['NearLines']
    farplane = bpy.data.objects['FarLines']
    gradientplane = bpy.data.objects['GradientBG']

    farplane.parent = nearplane
    farplane.matrix_parent_inverse = nearplane.matrix_world.inverted()
    gradientplane.parent = nearplane
    gradientplane.matrix_parent_inverse = nearplane.matrix_world.inverted()

class OBJECT_OT_generateActionPlanes(bpy.types.Operator):
    """Create a stylized action planes"""
    bl_idname = "mesh.generate_action_planes"
    bl_label = "Add Stylized Action Planes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateActionPlanes()

        return {'FINISHED'}

# Water Planes

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

    nodes = surfacemat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 5
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    transparent.inputs[0].default_value = (0.25, 0.25, 1, 1)

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

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(colorramp2.outputs[0], mixshader.inputs[0])

    links.new(colorramp1.outputs[0], emission.inputs[0])

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

    links.new(colorramp.outputs[0], emission.inputs[0])

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

class GhibliGeneratorPanel(bpy.types.Panel):
    bl_label = "Ghibli Generator"
    bl_category = "Ghibli Generator"
    bl_idname = "VIEW3D_PT_GhibliGeneratorPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        layout = self.layout
        column = layout.column()
        column.label(text="Procedural Anime Assets")
        column.operator(OBJECT_OT_generateGrassPlane.bl_idname, text='Grass Plane', icon='HAIR')
        column.operator(OBJECT_OT_generateRock.bl_idname, text='Rock', icon='MESH_CAPSULE')
        column.operator(OBJECT_OT_generateWaterPlanes.bl_idname, text='Water Planes', icon='MOD_OCEAN')
        column.operator(OBJECT_OT_generateRainPlane.bl_idname, text='Rain Plane', icon='MOD_FLUIDSIM')
        column.operator(OBJECT_OT_generateActionPlanes.bl_idname, text='Action Planes', icon='ALIGN_FLUSH')

classes = (
            OBJECT_OT_generateGrassPlane,
            OBJECT_OT_generateRock,
            OBJECT_OT_generateRainPlane,
            OBJECT_OT_generateActionPlanes,
            OBJECT_OT_generateWaterPlanes,
            GhibliGeneratorPanel
            )

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()