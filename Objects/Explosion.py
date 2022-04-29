# explosion Cloud Generator
import bpy

#from .Drivers.explosionDrivers import *

def generateExplosion():

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    explosion = bpy.context.object
    explosion.name = 'Explosion'
    bpy.ops.object.shade_smooth()

    explosiontex = bpy.data.textures.new(name='ExplosionClouds', type = 'CLOUDS')
    explosiontex.noise_scale = 1.0

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = explosion.modifiers["Subdivision"]
    subsurf.levels = 2
    subsurf.render_levels = 2

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace0 = explosion.modifiers["Displace"]
    displace0.texture_coords = 'GLOBAL'
    displace0.texture = explosiontex

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace1 = explosion.modifiers["Displace.001"]

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf1 = explosion.modifiers["Subdivision.001"]
    subsurf1.levels = 2
    subsurf1.render_levels = 2

    explosionmat = bpy.data.materials.new(name='explosionMaterial')
    explosionmat.use_nodes = True
    explosionmat.blend_method = 'BLEND'
    explosionmat.shadow_method = 'NONE'
    explosionmat.show_transparent_back = False
    explosionmat.node_tree.nodes.clear()

    nodes = explosionmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')
    
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')
    
    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs[1].default_value = 10

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements.new(0.5)
    colorramp0.color_ramp.elements.new(0.25)
    colorramp0.color_ramp.elements.new(0.125)
    colorramp0.color_ramp.elements[0].position = 0.0
    colorramp0.color_ramp.elements[1].position = 0.034
    colorramp0.color_ramp.elements[2].position = 0.056
    colorramp0.color_ramp.elements[3].position = 0.114
    colorramp0.color_ramp.elements[4].position = 0.5        
    colorramp0.color_ramp.elements[0].color = [1.000000, 1.000000, 1.000000, 1.000000]
    colorramp0.color_ramp.elements[1].color = [1.000000, 0.990743, 0.000000, 1.000000]
    colorramp0.color_ramp.elements[2].color = [1.000000, 0.250716, 0.000000, 1.000000]
    colorramp0.color_ramp.elements[3].color = [0.119114, 0.119114, 0.119114, 1.000000]
    colorramp0.color_ramp.elements[4].color = [0.024727, 0.024727, 0.024727, 1.000000]

    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.interpolation = 'CONSTANT'
    colorramp1.color_ramp.elements[0].color = [0.0, 0.0, 0.0, 1.0]
    colorramp1.color_ramp.elements[1].color = [1.0, 1.0, 1.0, 1.0]
    colorramp1.color_ramp.elements[1].position = 1.0

    voronoi = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi.voronoi_dimensions = '2D'

    fresnel = nodes.new(type='ShaderNodeFresnel')

    links = explosionmat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])
    
    links.new(transparent.outputs[0], mixshader.inputs[2])
    
    links.new(emission.outputs[0], mixshader.inputs[1]) 
    links.new(colorramp0.outputs[0], emission.inputs[0])
    links.new(fresnel.outputs[0], colorramp0.inputs[0])
    

    links.new(colorramp1.outputs[0], mixshader.inputs[0])
    links.new(voronoi.outputs[0], colorramp1.inputs[0])
    links.new(fresnel.outputs[0], voronoi.inputs[1])

    bpy.context.object.data.materials.append(explosionmat)


class OBJECT_OT_generateExplosion(bpy.types.Operator):
    """Create a stylized explosion"""
    bl_idname = "mesh.generate_explosion"
    bl_label = "Add Stylized Explosion"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateExplosion()
        #assignDrivers()

        return {'FINISHED'}
