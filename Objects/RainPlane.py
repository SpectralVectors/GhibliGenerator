# Rain Plane
import bpy

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
