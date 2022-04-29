# Circular Flash Plane
import bpy

#from .Drivers.ActionPlanesDrivers import *

def generateCircularFlashPlane():

    bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    circularflash = bpy.context.object
    circularflash.rotation_euler[1] = 1.5708
    circularflash.name = 'CircularFlash'
    bpy.ops.object.shade_smooth()

    circularflashmat = bpy.data.materials.new(name='CircularFlashMaterial')
    circularflashmat.use_nodes = True
    circularflashmat.node_tree.nodes.clear()
    circularflashmat.blend_method = 'BLEND'
    circularflashmat.shadow_method = 'NONE'

    nodes = circularflashmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 20
    
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    
    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.interpolation = 'B_SPLINE'
    colorramp.color_ramp.elements[0].position = 0.4
    colorramp.color_ramp.elements[1].position = 1.0  

    gradient = nodes.new(type='ShaderNodeTexGradient')
    gradient.gradient_type = 'SPHERICAL'
    
    mapping = nodes.new(type='ShaderNodeMapping')
    
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = circularflashmat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(emission.outputs[0], mixshader.inputs[1])

    links.new(transparent.outputs[0], mixshader.inputs[2])
    
    links.new(colorramp.outputs[0], emission.inputs[0])
    
    links.new(gradient.outputs[0], colorramp.inputs[0])
    
    links.new(mapping.outputs[0], gradient.inputs[0])
    
    links.new(texcoord.outputs[3], mapping.inputs[0])

    circularflash.data.materials.append(circularflashmat)


class OBJECT_OT_generateCircularFlashPlane(bpy.types.Operator):
    """Create a circular gradient color plane"""
    bl_idname = "mesh.generate_circular_flash_plane"
    bl_label = "Add a circular gradient color plane"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateCircularFlashPlane()
        #assignDrivers()

        return {'FINISHED'}
