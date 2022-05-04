# Creating PowerUp Sphere
import bpy

#from .Drivers.RockDrivers import *

def generateEnergySphere():

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.object.shade_smooth()

    powerupspheremat = bpy.data.materials.new(name='powerupspherematerial')
    powerupspheremat.use_nodes = True
    powerupspheremat.blend_method = 'BLEND'
    powerupspheremat.shadow_method = 'NONE'
    #powerupspheremat.show_transparent_back = False
    powerupspheremat.node_tree.nodes.clear()

    nodes = powerupspheremat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 20

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements.new(0.5)
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.045
    colorramp0.color_ramp.elements[2].position = 0.068      
    colorramp0.color_ramp.elements[0].color = [0.0, 0.000000, 0.000000, 1.000000]
    colorramp0.color_ramp.elements[1].color = [1.0, 1.0, 1.0, 1.0]
    colorramp0.color_ramp.elements[2].color = [0.055327, 0.055327, 0.055327, 1.000000]

    linearlight = nodes.new(type='ShaderNodeMixRGB')
    linearlight.blend_type = 'LINEAR_LIGHT'
    linearlight.inputs[0].default_value = 1.0

    fresnel = nodes.new(type='ShaderNodeFresnel')

    wave = nodes.new(type='ShaderNodeTexWave')
    wave.bands_direction = 'Z'
    wave.wave_profile = 'SAW'
    wave.inputs[1].default_value = 0.1
    wave.inputs[2].default_value = 10
    wave.inputs[3].default_value = 15

    wavemapping = nodes.new(type='ShaderNodeMapping')
    wavemapping.inputs[3].default_value = (1, 5, 3)

    gradient = nodes.new(type='ShaderNodeTexGradient')

    gradientmapping = nodes.new(type='ShaderNodeMapping')
    gradientmapping.inputs[2].default_value[1] = 1.5708

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = powerupspheremat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(emission.outputs[0], mixshader.inputs[1]) 
    links.new(colorramp0.outputs[0], emission.inputs[0])

    links.new(linearlight.outputs[0], colorramp0.inputs[0])

    links.new(fresnel.outputs[0], linearlight.inputs[2])

    links.new(texcoord.outputs[1], fresnel.inputs[1])

    links.new(wave.outputs[0], linearlight.inputs[1])
    links.new(wavemapping.outputs[0], wave.inputs[0])
    links.new(texcoord.outputs[3], wavemapping.inputs[0])

    links.new(gradient.outputs[0], mixshader.inputs[0])
    links.new(gradientmapping.outputs[0], gradient.inputs[0])
    links.new(texcoord.outputs[0], gradientmapping.inputs[0])

    bpy.context.object.data.materials.append(powerupspheremat)


class OBJECT_OT_generateEnergySphere(bpy.types.Operator):
    """Create an animated sphere of energy"""
    bl_idname = "mesh.generate_energy_sphere"
    bl_label = "Add Stylized Sphere of Energy"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateEnergySphere()
        #assignDrivers()

        return {'FINISHED'}
