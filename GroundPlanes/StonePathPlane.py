# Stone Path Plane Generator
import bpy

#from .Drivers.stonepathDrivers import *

def generateStonePathPlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    stonepath = bpy.context.object
    stonepath.name = 'StonePath'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_x = stonepath.modifiers['Array']
    array_x.count = 1

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = stonepath.modifiers['Array.001']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = stonepath.modifiers["Subdivision"]
    subsurf.levels = 2
    subsurf.render_levels = 2
    subsurf.subdivision_type = 'SIMPLE'


    stonepathmat = bpy.data.materials.new(name='stonepathmaterial')
    stonepathmat.use_nodes = True
    stonepathmat.node_tree.nodes.clear()

    nodes = stonepathmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    # Translucent & Normal Node
    translucent = nodes.new(type='ShaderNodeBsdfTranslucent')
    normal = nodes.new(type='ShaderNodeNormal')
    normal.outputs[0].default_value = (0, 0, -1)
    # Ends

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'B_SPLINE'
    colorramp0.color_ramp.elements.new(0.5)
    colorramp0.color_ramp.elements[0].color = [0.016370, 0.068727, 0.016674, 1.000000]
    colorramp0.color_ramp.elements[1].color = [0.076728, 0.076728, 0.076728, 1.000000]
    colorramp0.color_ramp.elements[2].color = [0.571661, 0.571661, 0.571661, 1.000000]
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.05
    colorramp0.color_ramp.elements[2].position = 1.0
    
    shadertorgb = nodes.new(type='ShaderNodeShaderToRGB')
    
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')
    
    multiply0 = nodes.new(type='ShaderNodeMixRGB')
    multiply0.blend_type = 'MULTIPLY'
    multiply0.inputs[0].default_value = 1

    multiply1 = nodes.new(type='ShaderNodeMixRGB')
    multiply1.blend_type = 'MULTIPLY'
    multiply1.inputs[0].default_value = 1
    multiply1.inputs[2].default_value = [0.154261, 0.154261, 0.154261, 1.000000]

    voronoi0 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi0.feature = 'DISTANCE_TO_EDGE'
    voronoi0.inputs[2].default_value = 3

    noise0 = nodes.new(type='ShaderNodeTexNoise')
    noise0.inputs[2].default_value = 10

    noise1 = nodes.new(type='ShaderNodeTexNoise')
    noise1.inputs[2].default_value = 1
    noise1.inputs[3].default_value = 15

    mapping0 = nodes.new(type='ShaderNodeMapping')
    
    mapping1 = nodes.new(type='ShaderNodeMapping')

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = stonepathmat.node_tree.links

    links.new(translucent.outputs[0], output.inputs[0])
    links.new(normal.outputs[0], translucent.inputs[1])
    links.new(colorramp0.outputs[0], translucent.inputs[0])
    links.new(shadertorgb.outputs[0], colorramp0.inputs[0])
    links.new(diffuse.outputs[0], shadertorgb.inputs[0])

    links.new(multiply0.outputs[0], diffuse.inputs[0])
    links.new(noise0.outputs[0], multiply0.inputs[1])
    links.new(mapping1.outputs[0], noise0.inputs[0])
    links.new(texcoord.outputs[0], mapping1.inputs[0])
    
    links.new(voronoi0.outputs[0], multiply0.inputs[2])
    links.new(mapping0.outputs[0], voronoi0.inputs[0])
    links.new(mapping1.outputs[0], mapping0.inputs[0])
    links.new(multiply1.outputs[0], mapping0.inputs[1])
    links.new(noise1.outputs[0], multiply1.inputs[1])
    links.new(texcoord.outputs[0], noise1.inputs[0])    
    
    bpy.context.object.data.materials.append(stonepathmat)


class OBJECT_OT_generateStonePathPlane(bpy.types.Operator):
    """Create a stylized stone path plane"""
    bl_idname = "mesh.generate_stone_path_plane"
    bl_label = "Add Stylized Stone Path"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateStonePathPlane()
        #assignDrivers()

        return {'FINISHED'}
