# Color Flash Plane
import bpy

from .Drivers.ColorFlashDrivers import *

def generateColorFlashPlane():

    bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    colorflash = bpy.context.object
    colorflash.rotation_euler[1] = 1.5708
    colorflash.name = 'ColorFlash'
    bpy.ops.object.shade_smooth()

    colorflashmat = bpy.data.materials.new(name='ColorFlashMaterial')
    colorflashmat.use_nodes = True
    colorflashmat.node_tree.nodes.clear()
    colorflashmat.blend_method = 'BLEND'
    colorflashmat.shadow_method = 'NONE'

    nodes = colorflashmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 20
    
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    links = colorflashmat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(emission.outputs[0], mixshader.inputs[1])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    colorflash.data.materials.append(colorflashmat)


class OBJECT_OT_generateColorFlashPlane(bpy.types.Operator):
    """Create a single color plane"""
    bl_idname = "mesh.generate_color_flash_plane"
    bl_label = "Add single color plane"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateColorFlashPlane()
        assignDrivers()

        return {'FINISHED'}
