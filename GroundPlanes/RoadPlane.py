# Road Plane Generator
import bpy

#from .Drivers.roadplaneDrivers import *

def generateRoadPlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    roadplane = bpy.context.object
    roadplane.name = 'Sand'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = roadplane.modifiers['Array']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = roadplane.modifiers["Subdivision"]
    subsurf.levels = 4
    subsurf.render_levels = 4
    subsurf.subdivision_type = 'SIMPLE'

    roadtex = bpy.data.textures.new(name='roadtexture', type = 'CLOUDS')
    roadtex.noise_scale = 1

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = roadplane.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.01
    displace.texture = roadtex

    roadmat = bpy.data.materials.new(name='roadmaterial')
    roadmat.use_nodes = True
    roadmat.node_tree.nodes.clear()

    nodes = roadmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    # Translucent & Normal Node
    translucent = nodes.new(type='ShaderNodeBsdfTranslucent')
    normal = nodes.new(type='ShaderNodeNormal')
    normal.outputs[0].default_value = (0, 0, -1)
    # Ends

    multiply0 = nodes.new(type='ShaderNodeMixRGB')
    multiply0.blend_type = 'MULTIPLY'
    multiply0.inputs[0].default_value = 1

    multiply1 = nodes.new(type='ShaderNodeMixRGB')
    multiply1.blend_type = 'MULTIPLY'

    mix0 = nodes.new(type='ShaderNodeMixRGB')

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements.new(0.5)
    colorramp0.color_ramp.elements.new(0.25)
    colorramp0.color_ramp.elements.new(0.125)
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.05
    colorramp0.color_ramp.elements[2].position = 0.08
    colorramp0.color_ramp.elements[3].position = 0.92
    colorramp0.color_ramp.elements[4].position = 0.95
    colorramp0.color_ramp.elements[0].color = [0.063267, 0.063267, 0.063267, 1.000000]
    colorramp0.color_ramp.elements[1].color = [0.922121, 1.000000, 0.000000, 1.000000]
    colorramp0.color_ramp.elements[2].color = [0.063267, 0.063267, 0.063267, 1.000000]
    colorramp0.color_ramp.elements[3].color = [0.922121, 1.000000, 0.000000, 1.000000]    
    colorramp0.color_ramp.elements[4].color = [0.063267, 0.063267, 0.063267, 1.000000]
    
    gradient = nodes.new(type='ShaderNodeTexGradient')
    
    mapping = nodes.new(type='ShaderNodeMapping')
    
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    multiply2 = nodes.new(type='ShaderNodeMixRGB')
    multiply2.blend_type = 'MULTIPLY'
    multiply2.inputs[0].default_value = 1
    
    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.interpolation = 'CONSTANT'
    colorramp1.color_ramp.elements.new(0.5)
    colorramp1.color_ramp.elements[0].position = 0.48
    colorramp1.color_ramp.elements[1].position = 0.5
    colorramp1.color_ramp.elements[2].position = 0.52
    colorramp1.color_ramp.elements[0].color = (0.0, 0.0, 0.0, 0.000000)
    colorramp1.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.000000)
    colorramp1.color_ramp.elements[2].color = (0.0, 0.0, 0.0, 0.0)

    colorramp2 = nodes.new(type='ShaderNodeValToRGB')
    colorramp2.color_ramp.interpolation = 'CONSTANT'
    colorramp2.color_ramp.elements[1].position = 0.464

    wave = nodes.new(type='ShaderNodeTexWave')
    wave.bands_direction = 'Y'
    wave.inputs[1].default_value = 0.6
    wave.inputs[5].default_value = 1

    colordodge = nodes.new(type='ShaderNodeMixRGB')
    colordodge.blend_type = 'DODGE'
    colordodge.inputs[0].default_value = 1    
    
    noise0 = nodes.new(type='ShaderNodeTexNoise')
    noise0.inputs[2].default_value = 11.1
    noise0.inputs[3].default_value = 15
    noise0.inputs[4].default_value = 0.292

    colorramp3 = nodes.new(type='ShaderNodeValToRGB')
    colorramp3.color_ramp.elements[1].position = 0.005
    
    voronoi = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi.feature = 'DISTANCE_TO_EDGE'
    voronoi.inputs[2].default_value = 6.7

    mix1 = nodes.new(type='ShaderNodeMixRGB')
    mix1.inputs[0].default_value = 0.1

    noise1 = nodes.new(type='ShaderNodeTexNoise')
    noise1.inputs[2].default_value = 200
    noise1.inputs[3].default_value = 3
    noise1.inputs[4].default_value = 1

    noise2 = nodes.new(type='ShaderNodeTexNoise')

    links = roadmat.node_tree.links

    links.new(translucent.outputs[0], output.inputs[0])
    links.new(normal.outputs[0], translucent.inputs[1])
    
    links.new(multiply0.outputs[0], translucent.inputs[0])
    links.new(multiply1.outputs[0], multiply0.inputs[1])
    
    links.new(mix0.outputs[0], multiply1.inputs[1])
    links.new(colorramp0.outputs[0], mix0.inputs[1])
    links.new(gradient.outputs[0], colorramp0.inputs[0])
    links.new(mapping.outputs[0], gradient.inputs[0])
    links.new(texcoord.outputs[0], mapping.inputs[0])

    links.new(multiply2.outputs[0], mix0.inputs[2])
    links.new(colorramp1.outputs[0], multiply2.inputs[1])
    links.new(gradient.outputs[0], colorramp1.inputs[0])
    links.new(mapping.outputs[0], wave.inputs[0])
    
    links.new(colorramp2.outputs[0], multiply2.inputs[2])
    links.new(wave.outputs[0], colorramp2.inputs[0])
    
    links.new(noise1.outputs[0], multiply1.inputs[2])
    links.new(mapping.outputs[0], noise1.inputs[0])
    
    links.new(colordodge.outputs[0], multiply0.inputs[2])
    links.new(noise0.outputs[0], colordodge.inputs[1])
    links.new(colorramp3.outputs[0], colordodge.inputs[2])
    links.new(voronoi.outputs[0], colorramp3.inputs[0])
    links.new(mix1.outputs[0], voronoi.inputs[0])
    links.new(noise2.outputs[0], mix1.inputs[2])
    links.new(mapping.outputs[0], gradient.inputs[0])
    links.new(mapping.outputs[0], mix1.inputs[1])
    links.new(mapping.outputs[0], noise2.inputs[0])
    
    bpy.context.object.data.materials.append(roadmat)


class OBJECT_OT_generateRoadRlane(bpy.types.Operator):
    """Create a stylized road plane"""
    bl_idname = "mesh.generate_road_plane"
    bl_label = "Add Stylized Road"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateRoadPlane()
        #assignDrivers()

        return {'FINISHED'}
