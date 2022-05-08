# heatripple Plane
import bpy

def generateHeatRipplePlane():

    bpy.context.scene.eevee.use_ssr = True
    bpy.context.scene.eevee.use_ssr_refraction = True

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    heatrippleplane = bpy.context.object
    heatrippleplane.name = 'HeatRipple'
    heatrippleplane.rotation_euler[1] = 1.5708
    bpy.ops.object.shade_smooth()

    heatripplemat = bpy.data.materials.new(name='heatrippleMaterial')
    heatripplemat.use_nodes = True
    heatripplemat.node_tree.nodes.clear()
    heatripplemat.blend_method = 'BLEND'
    heatripplemat.shadow_method = 'NONE'
    heatripplemat.use_screen_refraction = True

    nodes = heatripplemat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')

    refraction = nodes.new(type='ShaderNodeBsdfRefraction')
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    bump = nodes.new(type='ShaderNodeBump')

    noise1 = nodes.new(type='ShaderNodeTexNoise')
    noise1.noise_dimensions = '4D'
    noise1.inputs[2].default_value = 1
    noise1.inputs[4].default_value = 1

    invert = nodes.new(type='ShaderNodeInvert')

    gradient = nodes.new(type='ShaderNodeTexGradient')
    gradient.gradient_type = 'SPHERICAL'

    mapping1 = nodes.new(type='ShaderNodeMapping')

    texcoord = nodes.new(type='ShaderNodeTexCoord')

    links = heatripplemat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])

    links.new(invert.outputs[0], mixshader.inputs[0])

    links.new(refraction.outputs[0], mixshader.inputs[1])

    links.new(transparent.outputs[0], mixshader.inputs[2])

    links.new(gradient.outputs[0], invert.inputs[1])

    links.new(mapping1.outputs[0], gradient.inputs[0])

    links.new(noise1.outputs[1], bump.inputs[2])

    links.new(bump.outputs[0], refraction.inputs[3])

    links.new(mapping1.outputs[0], noise1.inputs[0])

    links.new(texcoord.outputs[3], mapping1.inputs[0])

    bpy.context.object.data.materials.append(heatripplemat)


class OBJECT_OT_generateHeatRipplePlane(bpy.types.Operator):
    """Create a stylized heat distortion effect plane"""
    bl_idname = "mesh.generate_heatripple_plane"
    bl_label = "Add Stylized heat distortion effect"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateHeatRipplePlane()

        return {'FINISHED'}
