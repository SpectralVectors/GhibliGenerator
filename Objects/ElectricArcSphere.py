# Creating Electricity Sphere
import bpy

#from .Drivers.RockDrivers import *

def generateElectricArcSphere():

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.object.shade_smooth()
    electricarc = bpy.context.object

    electricarctex = bpy.data.textures.new(name='ElectricityClouds', type = 'CLOUDS')

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = electricarc.modifiers["Subdivision"]
    subsurf.levels = 2
    subsurf.render_levels = 2

    bpy.ops.object.modifier_add(type='SHRINKWRAP')
    shrinkwrap = electricarc.modifiers["Shrinkwrap"]
    shrinkwrap.offset = 0.2

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = electricarc.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.5
    displace.texture = electricarctex

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf1 = electricarc.modifiers["Subdivision.001"]
    subsurf1.levels = 2
    subsurf1.render_levels = 2

    energyspheremat = bpy.data.materials.new(name='energyspherematerial')
    energyspheremat.use_nodes = True
    energyspheremat.blend_method = 'BLEND'
    energyspheremat.shadow_method = 'NONE'
    #energyspheremat.show_transparent_back = False
    energyspheremat.node_tree.nodes.clear()

    nodes = energyspheremat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[0].default_value = [0.032494, 0.249981, 1.000000, 1.000000]
    emission.inputs[1].default_value = 50
    
    invert = nodes.new(type='ShaderNodeInvert')

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.95    
    colorramp0.color_ramp.elements[0].color = [0.0, 0.000000, 0.000000, 1.000000]
    colorramp0.color_ramp.elements[1].color = [1.0, 1.0, 1.0, 1.0]

    wave = nodes.new(type='ShaderNodeTexWave')
    wave.bands_direction = 'Z'
    wave.wave_profile = 'SAW'
    wave.inputs[1].default_value = 0.1
    wave.inputs[2].default_value = 20
    wave.inputs[3].default_value = 15

    wavemapping = nodes.new(type='ShaderNodeMapping')
    wavemapping.inputs[3].default_value = (1, 5, 3)

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = energyspheremat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(emission.outputs[0], mixshader.inputs[1]) 
    links.new(colorramp0.outputs[0], invert.inputs[1])
    links.new(invert.outputs[0], mixshader.inputs[0])

    links.new(wave.outputs[0], colorramp0.inputs[0])
    links.new(wavemapping.outputs[0], wave.inputs[0])
    links.new(texcoord.outputs[3], wavemapping.inputs[0])

    bpy.context.object.data.materials.append(energyspheremat)


class OBJECT_OT_generateElectricArcSphere(bpy.types.Operator):
    """Create an animated sphere of electricity"""
    bl_idname = "mesh.generate_electric_arc_sphere"
    bl_label = "Add Stylized Sphere of Electricity"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateElectricArcSphere()
        #assignDrivers()

        return {'FINISHED'}
