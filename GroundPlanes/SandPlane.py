# Sand Plane Generator
import bpy

from .Drivers.SandPlaneDrivers import *

def generateSandPlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    sandplane = bpy.context.object
    sandplane.name = 'Sand'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_x = sandplane.modifiers['Array']
    array_x.count = 1

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = sandplane.modifiers['Array.001']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = sandplane.modifiers["Subdivision"]
    subsurf.levels = 4
    subsurf.render_levels = 4
    subsurf.subdivision_type = 'SIMPLE'

    sandtex = bpy.data.textures.new(name='SandTexture', type = 'CLOUDS')
    sandtex.noise_scale = 1

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = sandplane.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.5
    displace.texture = sandtex

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf1 = sandplane.modifiers["Subdivision.001"]
    subsurf1.levels = 3
    subsurf1.render_levels = 3

    sandmat = bpy.data.materials.new(name='sandmaterial')
    sandmat.use_nodes = True
    sandmat.node_tree.nodes.clear()

    nodes = sandmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    # Translucent & Normal Node
    translucent = nodes.new(type='ShaderNodeBsdfTranslucent')
    normal = nodes.new(type='ShaderNodeNormal')
    normal.outputs[0].default_value = (0, 0, -1)
    # Ends

    multiply = nodes.new(type='ShaderNodeMixRGB')
    multiply.blend_type = 'MULTIPLY'

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements[0].color = [0.273416, 0.222385, 0.073390, 1.000000]
    colorramp0.color_ramp.elements[1].color = [0.641803, 0.656629, 0.100958, 1.000000]
    colorramp0.color_ramp.elements[1].position = 0.6
    
    shadertorgb = nodes.new(type='ShaderNodeShaderToRGB')
    
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
    
    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.interpolation = 'CONSTANT'
    colorramp1.color_ramp.elements.new(0.5)
    colorramp1.color_ramp.elements[0].position = 0
    colorramp1.color_ramp.elements[1].position = 0.86
    colorramp1.color_ramp.elements[2].position = 0.88
    colorramp1.color_ramp.elements[0].color = (1.0, 1.0, 1.0, 1.000000)
    colorramp1.color_ramp.elements[1].color = (0.0, 0.0, 0.0, 1.000000)
    colorramp1.color_ramp.elements[2].color = (1.0, 1.0, 1.0, 1.0)
    
    noise = nodes.new(type='ShaderNodeTexNoise')
    noise.inputs[2].default_value = 1000
    noise.inputs[3].default_value = 15
    noise.inputs[4].default_value = 0

    links = sandmat.node_tree.links

    links.new(translucent.outputs[0], output.inputs[0])
    links.new(normal.outputs[0], translucent.inputs[1])
    links.new(multiply.outputs[0], translucent.inputs[0])
    links.new(colorramp0.outputs[0], multiply.inputs[1])
    links.new(shadertorgb.outputs[0], colorramp0.inputs[0])
    links.new(diffuse.outputs[0], shadertorgb.inputs[0])
    
    links.new(colorramp1.outputs[0], multiply.inputs[2])
    links.new(noise.outputs[0], colorramp1.inputs[0])
    
    bpy.context.object.data.materials.append(sandmat)


class OBJECT_OT_generateSandPlane(bpy.types.Operator):
    """Create a stylized sand plane"""
    bl_idname = "mesh.generate_sand_plane"
    bl_label = "Add Stylized Sand Dunes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateSandPlane()
        assignDrivers()

        return {'FINISHED'}
