# lightspot Plane
import bpy

def generateLightSpotPlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    lightspotplane = bpy.context.object
    lightspotplane.name = 'lightspot'
    lightspotplane.rotation_euler[1] = 1.5708
    bpy.ops.object.shade_smooth()

    lightspotmat = bpy.data.materials.new(name='lightspotMaterial')
    lightspotmat.use_nodes = True
    lightspotmat.node_tree.nodes.clear()
    lightspotmat.blend_method = 'BLEND'
    lightspotmat.shadow_method = 'NONE'

    nodes = lightspotmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader0 = nodes.new(type='ShaderNodeMixShader')
    mixshader0.inputs[0].default_value = 0.9
    mixshader1 = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 20
    transparent0 = nodes.new(type='ShaderNodeBsdfTransparent')
    transparent1 = nodes.new(type='ShaderNodeBsdfTransparent')

    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.interpolation = 'EASE'
    colorramp.color_ramp.elements[0].color = [1.000000, 0.002548, 0.000000, 1.000000]
    colorramp.color_ramp.elements[1].color = [1.000000, 0.708078, 0.000000, 1.000000]

    invert = nodes.new(type='ShaderNodeInvert')

    gradient = nodes.new(type='ShaderNodeTexGradient')
    gradient.gradient_type = 'SPHERICAL'

    mapping1 = nodes.new(type='ShaderNodeMapping')

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = lightspotmat.node_tree.links

    links.new(mixshader0.outputs[0], output.inputs[0])

    links.new(mixshader1.outputs[0], mixshader0.inputs[1])
    
    links.new(transparent0.outputs[0], mixshader0.inputs[2])
    
    links.new(transparent1.outputs[0], mixshader1.inputs[2])
    
    links.new(emission.outputs[0], mixshader1.inputs[1])
    
    links.new(colorramp.outputs[0], emission.inputs[0])
    
    links.new(gradient.outputs[0], colorramp.inputs[0])
    
    links.new(gradient.outputs[0], invert.inputs[1])
    
    links.new(invert.outputs[0], mixshader1.inputs[0])
    
    links.new(mapping1.outputs[0], gradient.inputs[0])

    links.new(texcoord.outputs[3], mapping1.inputs[0])

    bpy.context.object.data.materials.append(lightspotmat)


class OBJECT_OT_generateLightSpotPlane(bpy.types.Operator):
    """Create a stylized circle of light"""
    bl_idname = "mesh.generate_lightspot_plane"
    bl_label = "Add Stylized light circle"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateLightSpotPlane()

        return {'FINISHED'}
