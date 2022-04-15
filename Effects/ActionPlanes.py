# Action Planes
import bpy

def generateActionPlanes():

    bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    nearplane = bpy.context.object
    nearplane.rotation_euler[1] = 1.5708
    nearplane.name = 'NearLines'
    bpy.ops.object.shade_smooth()

    bpy.ops.mesh.primitive_plane_add(size=6, enter_editmode=False, align='WORLD', location=(-2, 0, 0), scale=(1, 1, 1))
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
    mapping.inputs[3].default_value = (0.1, 5, 1)

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
