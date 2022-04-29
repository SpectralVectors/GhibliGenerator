# Ice Plane Generator
import bpy

#from .Drivers.iceplaneDrivers import *

def generateIcePlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    iceplane = bpy.context.object
    iceplane.name = 'Ice'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_x = iceplane.modifiers['Array']
    array_x.count = 1

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = iceplane.modifiers['Array.001']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = iceplane.modifiers["Subdivision"]
    subsurf.levels = 4
    subsurf.render_levels = 4
    subsurf.subdivision_type = 'SIMPLE'

    icetex = bpy.data.textures.new(name='IceTexture', type = 'CLOUDS')
    icetex.noise_scale = 1

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = iceplane.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.005
    displace.texture = icetex

    icemat = bpy.data.materials.new(name='icematerial')
    icemat.use_nodes = True
    icemat.blend_method = 'BLEND'
    icemat.node_tree.nodes.clear()

    nodes = icemat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader0 = nodes.new(type='ShaderNodeMixShader')
    mixshader1 = nodes.new(type='ShaderNodeMixShader')

    # Translucent & Normal Node
    translucent = nodes.new(type='ShaderNodeBsdfTranslucent')
    translucent.inputs[0].default_value = [0.183718, 0.330284, 0.800000, 1.000000]
    normal = nodes.new(type='ShaderNodeNormal')
    normal.outputs[0].default_value = (0, 0, -1)
    # Ends

    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    
    voronoi0 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi0.inputs[2].default_value = 2

    noise0 = nodes.new(type='ShaderNodeTexNoise')
    noise0.inputs[2].default_value = 2  

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements.new(0.5)
    colorramp0.color_ramp.elements[0].color = [0.094031, 0.292350, 0.604645, 1.000000]
    colorramp0.color_ramp.elements[1].color = [0.211978, 0.482632, 0.818554, 1.000000]
    colorramp0.color_ramp.elements[2].color = [1.0, 1.0, 1.0, 1.000000]
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.859
    colorramp0.color_ramp.elements[2].position = 1.0
    
    shadertorgb = nodes.new(type='ShaderNodeShaderToRGB')
    
    glossy = nodes.new(type='ShaderNodeBsdfGlossy')
    
    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.elements[0].position = 0.141
    colorramp1.color_ramp.elements[1].position = 0.4
    
    screen = nodes.new(type='ShaderNodeMixRGB')
    screen.blend_type = 'SCREEN'
    screen.inputs[0].default_value = 1

    voronoi1 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi1.voronoi_dimensions = '2D'
    voronoi1.feature = 'DISTANCE_TO_EDGE'
    voronoi1.inputs[2].default_value = 50

    noise1 = nodes.new(type='ShaderNodeTexNoise')
    noise1.inputs[2].default_value = 35
    noise1.inputs[4].default_value = 0

    links = icemat.node_tree.links

    links.new(mixshader0.outputs[0], output.inputs[0])
    
    links.new(translucent.outputs[0], mixshader0.inputs[2])
    links.new(normal.outputs[0], translucent.inputs[1])
    
    links.new(mixshader1.outputs[0], mixshader0.inputs[1])
    
    links.new(colorramp0.outputs[0], mixshader1.inputs[1])
    links.new(shadertorgb.outputs[0], colorramp0.inputs[0])
    links.new(glossy.outputs[0], shadertorgb.inputs[0])    
    links.new(colorramp1.outputs[0], glossy.inputs[0])
    links.new(screen.outputs[0], colorramp1.inputs[0])
    links.new(voronoi1.outputs[0], screen.inputs[1])
    links.new(noise1.outputs[0], screen.inputs[2])
    
    links.new(transparent.outputs[0], mixshader1.inputs[2])
    links.new(voronoi0.outputs[0], mixshader1.inputs[0])
    links.new(voronoi0.outputs[0], transparent.inputs[0])
    links.new(noise0.outputs[0], voronoi0.inputs[0])
    
    bpy.context.object.data.materials.append(icemat)


class OBJECT_OT_generateIcePlane(bpy.types.Operator):
    """Create a stylized ice plane"""
    bl_idname = "mesh.generate_ice_plane"
    bl_label = "Add Stylized Ice"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateIcePlane()
        #assignDrivers()

        return {'FINISHED'}
