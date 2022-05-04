# Creating Energy Ring
import bpy

#from .Drivers.RockDrivers import *

def generateEnergyRing():

    bpy.ops.mesh.primitive_cylinder_add(radius=2, depth=0.5, end_fill_type='NOTHING')
    bpy.ops.object.shade_smooth()

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='DESELECT')

    bpy.ops.object.editmode_toggle()
    bpy.context.object.data.edges[0].select = True

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.loop_multi_select(ring=False)
    bpy.ops.transform.resize(value=(0.5, 0.5, 0.5))

    #

    bpy.ops.mesh.select_all(action='DESELECT')

    bpy.ops.object.editmode_toggle()
    bpy.context.object.data.edges[20].select = True

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.loop_multi_select(ring=False)

    bpy.ops.object.vertex_group_add()
    bpy.ops.object.vertex_group_assign()

    bpy.ops.object.editmode_toggle()

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf0 = bpy.context.object.modifiers["Subdivision"]
    subsurf0.levels = 2

    energytex = bpy.data.textures.new(name='Energy', type='CLOUDS')

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = bpy.context.object.modifiers['Displace']
    displace.vertex_group = "Group"
    displace.direction = 'Z'
    displace.strength = 5
    displace.mid_level = 0
    displace.texture_coords = 'GLOBAL'
    displace.texture = energytex

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf1 = bpy.context.object.modifiers["Subdivision.001"]
    subsurf1.levels = 2

    energyringmat = bpy.data.materials.new(name='energyringMaterial')
    energyringmat.use_nodes = True
    energyringmat.blend_method = 'BLEND'
    energyringmat.shadow_method = 'NONE'
    #energyringmat.show_transparent_back = False
    energyringmat.node_tree.nodes.clear()

    nodes = energyringmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 20

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements.new(0.5)
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.06
    colorramp0.color_ramp.elements[2].position = 0.56       
    colorramp0.color_ramp.elements[0].color = [0.0, 0.000000, 0.000000, 1.000000]
    colorramp0.color_ramp.elements[1].color = [0.055329, 0.055329, 0.055329, 1.000000]
    colorramp0.color_ramp.elements[2].color = [1.0, 1.0, 1.0, 1.0]

    multiply0 = nodes.new(type='ShaderNodeMixRGB')
    multiply0.blend_type = 'MULTIPLY'
    multiply0.inputs[0].default_value = 0.8

    multiply1 = nodes.new(type='ShaderNodeMixRGB')
    multiply1.blend_type = 'MULTIPLY'

    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.interpolation = 'CONSTANT'
    colorramp1.color_ramp.elements[0].color = [0.0, 0.0, 0.0, 1.0]
    colorramp1.color_ramp.elements[1].color = [1.0, 1.0, 1.0, 1.0]
    colorramp1.color_ramp.elements[0].position = 0.3
    colorramp1.color_ramp.elements[1].position = 0.4

    fresnel = nodes.new(type='ShaderNodeFresnel')

    voronoi = nodes.new(type='ShaderNodeTexVoronoi')

    voronoimapping = nodes.new(type='ShaderNodeMapping')
    voronoimapping.inputs[3].default_value = (20, 0.1, 1)

    wave = nodes.new(type='ShaderNodeTexWave')
    wave.bands_direction = 'Z'
    wave.wave_profile = 'SAW'
    wave.inputs[1].default_value = 0.2
    wave.inputs[2].default_value = 0.5

    wavemapping = nodes.new(type='ShaderNodeMapping')
    wavemapping.inputs[3].default_value = (1, 5, 3)

    gradient = nodes.new(type='ShaderNodeTexGradient')

    gradientmapping = nodes.new(type='ShaderNodeMapping')
    gradientmapping.inputs[2].default_value[1] = 1.5708

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = energyringmat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(emission.outputs[0], mixshader.inputs[1]) 
    links.new(colorramp0.outputs[0], emission.inputs[0])

    links.new(multiply0.outputs[0], colorramp0.inputs[0])
    links.new(multiply1.outputs[0], multiply0.inputs[1])

    links.new(fresnel.outputs[0], multiply1.inputs[2])
    links.new(colorramp1.outputs[0], multiply0.inputs[2])

    links.new(voronoi.outputs[0], colorramp1.inputs[0])
    links.new(voronoimapping.outputs[0], voronoi.inputs[0])
    links.new(texcoord.outputs[2], voronoimapping.inputs[0])

    links.new(wave.outputs[0], multiply1.inputs[1])
    links.new(wavemapping.outputs[0], wave.inputs[0])
    links.new(texcoord.outputs[0], wavemapping.inputs[0])

    links.new(gradient.outputs[0], mixshader.inputs[0])
    links.new(gradientmapping.outputs[0], gradient.inputs[0])
    links.new(texcoord.outputs[0], gradientmapping.inputs[0])

    bpy.context.object.data.materials.append(energyringmat)


class OBJECT_OT_generateEnergyRing(bpy.types.Operator):
    """Create an animated ring of energy"""
    bl_idname = "mesh.generate_energy_ring"
    bl_label = "Add Stylized Ring of Energy"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateEnergyRing()
        #assignDrivers()

        return {'FINISHED'}
