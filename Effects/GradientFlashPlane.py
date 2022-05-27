# Gradient Flash Plane
import bpy

from .Drivers.GradientFlashDrivers import *

def generateGradientFlashPlane():

    bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    gradientflash = bpy.context.object
    gradientflash.rotation_euler[1] = 1.5708
    gradientflash.name = 'GradientFlash'
    bpy.ops.object.shade_smooth()

    gradientflashmat = bpy.data.materials.new(name='GradientFlashMaterial')
    gradientflashmat.use_nodes = True
    gradientflashmat.node_tree.nodes.clear()
    gradientflashmat.blend_method = 'BLEND'
    gradientflashmat.shadow_method = 'NONE'

    nodes = gradientflashmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 20
    
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    
    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.interpolation = 'B_SPLINE'
    colorramp.color_ramp.elements[0].position = 0.8
    colorramp.color_ramp.elements[1].position = 1.0  

    gradient = nodes.new(type='ShaderNodeTexGradient')
    
    mapping = nodes.new(type='ShaderNodeMapping')
    
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = gradientflashmat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(emission.outputs[0], mixshader.inputs[1])

    links.new(transparent.outputs[0], mixshader.inputs[2])
    
    links.new(colorramp.outputs[0], emission.inputs[0])
    
    links.new(gradient.outputs[0], colorramp.inputs[0])
    
    links.new(mapping.outputs[0], gradient.inputs[0])
    
    links.new(texcoord.outputs[0], mapping.inputs[0])

    gradientflash.data.materials.append(gradientflashmat)


class OBJECT_OT_generateGradientFlashPlane(bpy.types.Operator):
    """Create a linear gradient color plane"""
    bl_idname = "mesh.generate_gradient_flash_plane"
    bl_label = "Add a linear gradient color plane"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateGradientFlashPlane()
        assignDrivers()

        return {'FINISHED'}
