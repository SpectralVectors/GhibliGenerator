# fire Plane
import bpy

def generateFirePlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    fireplane = bpy.context.object
    fireplane.name = 'fire'
    fireplane.rotation_euler[1] = 1.5708
    bpy.ops.object.shade_smooth()

    firemat = bpy.data.materials.new(name='fireMaterial')
    firemat.use_nodes = True
    firemat.node_tree.nodes.clear()
    firemat.blend_method = 'BLEND'
    firemat.shadow_method = 'NONE'

    nodes = firemat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 20
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.032
    colorramp0.color_ramp.elements[0].color = (1, 1, 1, 1)
    colorramp0.color_ramp.elements[1].color = (0, 0, 0, 1.000000)

    linearlight = nodes.new(type='ShaderNodeMixRGB')
    linearlight.blend_type = 'LINEAR_LIGHT'
    linearlight.inputs[2].default_value = (0, 0, 0, 1)

    softlight0 = nodes.new(type='ShaderNodeMixRGB')
    softlight0.blend_type = 'SOFT_LIGHT'
    softlight0.inputs[0].default_value = 1

    softlight1 = nodes.new(type='ShaderNodeMixRGB')
    softlight1.blend_type = 'SOFT_LIGHT'
    softlight1.inputs[0].default_value = 1
    
    softlight2 = nodes.new(type='ShaderNodeMixRGB')
    softlight2.blend_type = 'SOFT_LIGHT'
    softlight2.inputs[0].default_value = 1    

    voronoi0 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi0.inputs[2].default_value = 8

    voronoi1 = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi1.inputs[2].default_value = 16

    voronoi2 = nodes.new(type='ShaderNodeTexVoronoi')

    mapping0 = nodes.new(type='ShaderNodeMapping')
    mapping0.inputs[3].default_value = (0.5, 1, 1)

    mapping1 = nodes.new(type='ShaderNodeMapping')

    combinexyz = nodes.new(type='ShaderNodeCombineXYZ')
    
    separatexyz = nodes.new(type='ShaderNodeSeparateXYZ')

    add = nodes.new(type='ShaderNodeMath')
    
    mix = nodes.new(type='ShaderNodeMixRGB')
    mix.inputs[2].default_value = (1, 1, 1, 1)

    screen = nodes.new(type='ShaderNodeMixRGB')
    screen.blend_type = 'SCREEN'

    wave = nodes.new(type='ShaderNodeTexWave')
    wave.inputs[1].default_value = 0.3

    gradient1 = nodes.new(type='ShaderNodeTexGradient')
    
    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.elements.new(0.5)
    colorramp1.color_ramp.elements[0].position = 0
    colorramp1.color_ramp.elements[1].position = 0.5
    colorramp1.color_ramp.elements[2].position = 1
    colorramp1.color_ramp.elements[0].color = [0.166536, 0.000000, 0.000000, 1.000000]
    colorramp1.color_ramp.elements[1].color = [0.354082, 0.078236, 0.000000, 1.000000]
    colorramp1.color_ramp.elements[2].color = [0.708214, 0.718336, 0.000000, 1.000000]
    
    invert = nodes.new(type='ShaderNodeInvert')
    
    gradient0 = nodes.new(type='ShaderNodeTexGradient')
    gradient0.gradient_type = 'SPHERICAL'
    
    mapping2 = nodes.new(type='ShaderNodeMapping')

    mapping3 = nodes.new(type='ShaderNodeMapping')
    mapping3.inputs[1].default_value = (0.5, 0, 0)
    
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = firemat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(colorramp0.outputs[0], mixshader.inputs[0])
    links.new(emission.outputs[0], mixshader.inputs[1])
    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(colorramp1.outputs[0], emission.inputs[0])

    links.new(linearlight.outputs[0], colorramp0.inputs[0])

    links.new(softlight0.outputs[0], linearlight.inputs[1])
    links.new(softlight1.outputs[0], softlight0.inputs[2])
    links.new(softlight2.outputs[0], softlight1.inputs[2])
    links.new(softlight2.outputs[0], colorramp1.inputs[0])
    
    links.new(voronoi0.outputs[0], softlight0.inputs[1])
    links.new(voronoi1.outputs[0], softlight1.inputs[1])
    links.new(voronoi2.outputs[0], softlight2.inputs[1])
    
    links.new(mapping0.outputs[0], voronoi0.inputs[0])
    links.new(mapping0.outputs[0], voronoi1.inputs[0])
    links.new(mapping0.outputs[0], voronoi2.inputs[0])

    links.new(combinexyz.outputs[0], mapping0.inputs[0])
    
    links.new(separatexyz.outputs[0], combinexyz.inputs[0])
    links.new(separatexyz.outputs[1], add.inputs[0])
    links.new(add.outputs[0], combinexyz.inputs[1])
    links.new(separatexyz.outputs[2], combinexyz.inputs[2])
    
    links.new(mix.outputs[0], add.inputs[1])
    links.new(screen.outputs[0], mix.inputs[1])
    links.new(wave.outputs[0], screen.inputs[1])
    links.new(mapping1.outputs[0], wave.inputs[0])

    links.new(gradient1.outputs[0], screen.inputs[2])
    links.new(mapping3.outputs[0], gradient1.inputs[0])

    links.new(texcoord.outputs[0], mapping1.inputs[0])
    links.new(texcoord.outputs[3], mapping2.inputs[0])
    links.new(texcoord.outputs[0], mapping3.inputs[0])
    links.new(texcoord.outputs[0], separatexyz.inputs[0])
    
    links.new(invert.outputs[0], linearlight.inputs[0])
    links.new(gradient0.outputs[0], invert.inputs[1])
    links.new(gradient0.outputs[0], softlight2.inputs[2])
    
    links.new(mapping2.outputs[0], gradient0.inputs[0])

    bpy.context.object.data.materials.append(firemat)


class OBJECT_OT_generateFirePlane(bpy.types.Operator):
    """Create a stylized fire plane"""
    bl_idname = "mesh.generate_fire_plane"
    bl_label = "Add Stylized fire"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateFirePlane()

        return {'FINISHED'}
