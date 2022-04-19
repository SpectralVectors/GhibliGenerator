# Rock Generator
import bpy

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

    # Translucent & Normal Node
    translucent = nodes.new(type='ShaderNodeBsdfTranslucent')
    normal = nodes.new(type='ShaderNodeNormal')
    normal.outputs[0].default_value = (0, 0, -1)
    # Ends

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

    links.new(translucent.outputs[0], output.inputs[0])

    links.new(mixrgb1.outputs[0], translucent.inputs[0])
    links.new(normal.outputs[0], translucent.inputs[1])

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
