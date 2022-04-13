import bpy

# Blue Sky Background
def BlueSkyBG():
    node_tree = bpy.data.worlds['World'].node_tree

    node_tree.nodes.clear()

    nodes = node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')
    background = nodes.new(type='ShaderNodeBackground')
    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.interpolation = 'B_SPLINE'
    colorramp.color_ramp.elements.new(0.5)
    colorramp.color_ramp.elements[0].position = 0
    colorramp.color_ramp.elements[1].position = 0.3
    colorramp.color_ramp.elements[2].position = 0.7
    colorramp.color_ramp.elements[0].color = [0.639438, 0.775820, 0.390884, 1.000000]
    colorramp.color_ramp.elements[1].color = [0.000000, 0.016061, 1.000000, 1.000000]
    colorramp.color_ramp.elements[2].color = [0.003531, 0.000000, 0.329258, 1.000000]
    gradient = nodes.new(type='ShaderNodeTexGradient')
    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.inputs[1].default_value = (0.3, 0, 0)
    mapping.inputs[2].default_value = (0, 1.5708, 0)
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = node_tree.links

    links.new(background.outputs[0], output.inputs[0])
    links.new(colorramp.outputs[0], background.inputs[0])
    links.new(gradient.outputs[0], colorramp.inputs[0])
    links.new(mapping.outputs[0], gradient.inputs[0])
    links.new(texcoord.outputs[0], mapping.inputs[0])

# Sunset Background
def SunsetBG():
    node_tree = bpy.data.worlds['World'].node_tree

    node_tree.nodes.clear()

    nodes = node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')
    background = nodes.new(type='ShaderNodeBackground')
    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.interpolation = 'B_SPLINE'
    colorramp.color_ramp.elements.new(0.5)
    colorramp.color_ramp.elements.new(0.25)
    colorramp.color_ramp.elements.new(0.125)
    colorramp.color_ramp.elements.new(0.062)
    colorramp.color_ramp.elements[0].position = 0
    colorramp.color_ramp.elements[1].position = 0.2
    colorramp.color_ramp.elements[2].position = 0.4
    colorramp.color_ramp.elements[3].position = 0.6
    colorramp.color_ramp.elements[4].position = 0.8
    colorramp.color_ramp.elements[5].position = 1
    colorramp.color_ramp.elements[0].color = [0.861933, 1.000000, 0.000000, 1.000000]
    colorramp.color_ramp.elements[1].color = [0.500000, 0.089998, 0.000000, 1.000000]
    colorramp.color_ramp.elements[2].color = [0.400000, 0.001788, 0.000000, 1.000000]
    colorramp.color_ramp.elements[3].color = [0.300000, 0.000000, 0.080976, 1.000000]
    colorramp.color_ramp.elements[4].color = [0.192383, 0.000000, 0.200000, 1.000000]
    colorramp.color_ramp.elements[5].color = [0.000000, 0.002117, 0.100000, 1.000000]
    gradient = nodes.new(type='ShaderNodeTexGradient')
    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.inputs[1].default_value = (0.3, 0, 0)
    mapping.inputs[2].default_value = (0, 1.5708, 0)
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = node_tree.links

    links.new(background.outputs[0], output.inputs[0])
    links.new(colorramp.outputs[0], background.inputs[0])
    links.new(gradient.outputs[0], colorramp.inputs[0])
    links.new(mapping.outputs[0], gradient.inputs[0])
    links.new(texcoord.outputs[0], mapping.inputs[0])

# Twilight Background
def TwilightBG():
    node_tree = bpy.data.worlds['World'].node_tree

    node_tree.nodes.clear()

    nodes = node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')
    background = nodes.new(type='ShaderNodeBackground')
    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.interpolation = 'B_SPLINE'
    colorramp.color_ramp.elements.new(0.5)
    colorramp.color_ramp.elements.new(0.25)
    colorramp.color_ramp.elements.new(0.125)
    colorramp.color_ramp.elements[0].position = 0
    colorramp.color_ramp.elements[1].position = 0.2
    colorramp.color_ramp.elements[2].position = 0.4
    colorramp.color_ramp.elements[3].position = 0.7
    colorramp.color_ramp.elements[4].position = 0.9
    colorramp.color_ramp.elements[0].color = [0.000000, 0.029845, 0.007454, 1.000000]
    colorramp.color_ramp.elements[1].color = [0.010390, 0.067757, 0.099999, 1.000000]
    colorramp.color_ramp.elements[2].color = [0.006086, 0.006665, 0.022857, 1.000000]
    colorramp.color_ramp.elements[3].color = [0.004441, 0.010000, 0.007736, 1.000000]
    colorramp.color_ramp.elements[4].color = [0.000000, 0.000000, 0.000000, 1.000000]
    gradient = nodes.new(type='ShaderNodeTexGradient')
    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.inputs[1].default_value = (0.3, 0, 0)
    mapping.inputs[2].default_value = (0, 1.5708, 0)
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = node_tree.links

    links.new(background.outputs[0], output.inputs[0])
    links.new(colorramp.outputs[0], background.inputs[0])
    links.new(gradient.outputs[0], colorramp.inputs[0])
    links.new(mapping.outputs[0], gradient.inputs[0])
    links.new(texcoord.outputs[0], mapping.inputs[0])

# Starry Night Background
def StarryNightBG():
    node_tree = bpy.data.worlds['World'].node_tree

    node_tree.nodes.clear()

    nodes = node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')
    mixshader = nodes.new(type='ShaderNodeMixShader')
    background = nodes.new(type='ShaderNodeBackground')
    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.interpolation = 'B_SPLINE'
    colorramp1.color_ramp.elements.new(0.5)
    colorramp1.color_ramp.elements[0].position = 0
    colorramp1.color_ramp.elements[1].position = 0.1
    colorramp1.color_ramp.elements[2].position = 1
    colorramp1.color_ramp.elements[0].color = [0.000000, 0.000566, 0.050000, 1.000000]
    colorramp1.color_ramp.elements[1].color = [0.000000, 0.000226, 0.020000, 1.000000]
    colorramp1.color_ramp.elements[2].color = [0.000000, 0.000000, 0.000000, 1.000000]
    gradient = nodes.new(type='ShaderNodeTexGradient')
    mapping = nodes.new(type='ShaderNodeMapping')
    mapping.inputs[1].default_value = (0.3, 0, 0)
    mapping.inputs[2].default_value = (0, 1.5708, 0)
    texcoord = nodes.new(type='ShaderNodeTexCoord')

    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 100
    colorramp2 = nodes.new(type='ShaderNodeValToRGB')
    colorramp2.color_ramp.elements[0].position = 0.8
    colorramp2.color_ramp.elements[1].position = 1
    noise = nodes.new(type='ShaderNodeTexNoise')
    noise.inputs[2].default_value = 300

    links = node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])
    links.new(background.outputs[0], mixshader.inputs[1])
    links.new(emission.outputs[0], mixshader.inputs[2])
    links.new(colorramp1.outputs[0], background.inputs[0])
    links.new(gradient.outputs[0], colorramp1.inputs[0])
    links.new(mapping.outputs[0], gradient.inputs[0])
    links.new(texcoord.outputs[0], mapping.inputs[0])

    links.new(colorramp2.outputs[0], emission.inputs[0])
    links.new(noise.outputs[0], colorramp2.inputs[0])

class OBJECT_OT_generateBlueSkyBG(bpy.types.Operator):
    """Create a blue sky background"""
    bl_idname = "mesh.generate_blue_sky"
    bl_label = "Add a blue sky background"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        BlueSkyBG()

        return {'FINISHED'}

class OBJECT_OT_generateSunsetBG(bpy.types.Operator):
    """Create a sunset/sunrise background"""
    bl_idname = "mesh.generate_sunset"
    bl_label = "Add a sunset/sunrise background"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        SunsetBG()

        return {'FINISHED'}

class OBJECT_OT_generateTwilightBG(bpy.types.Operator):
    """Create a twilight background"""
    bl_idname = "mesh.generate_twilight"
    bl_label = "Add a twilight background"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        TwilightBG()

        return {'FINISHED'}

class OBJECT_OT_generateStarryNightBG(bpy.types.Operator):
    """Create a starry night background"""
    bl_idname = "mesh.generate_starry_night"
    bl_label = "Add a starry night background"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        StarryNightBG()

        return {'FINISHED'}
