# Smoke Cloud Generator
import bpy

#from .Drivers.smokeDrivers import *

def generateSmokeCloud():

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    smoke = bpy.context.object
    smoke.name = 'Smoke'
    bpy.ops.object.shade_smooth()

    smoketex = bpy.data.textures.new(name='Clouds', type = 'CLOUDS')
    smoketex.noise_scale = 1.0

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = smoke.modifiers["Subdivision"]
    subsurf.levels = 2
    subsurf.render_levels = 2

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = smoke.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.texture = smoketex

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf1 = smoke.modifiers["Subdivision.001"]
    subsurf1.levels = 2
    subsurf1.render_levels = 2

    smokemat = bpy.data.materials.new(name='smokeMaterial')
    smokemat.use_nodes = True
    smokemat.node_tree.nodes.clear()

    nodes = smokemat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    mixshader = nodes.new(type='ShaderNodeMixShader')
    
    transparent = nodes.new(type='ShaderNodeBsdfTransparent')

    colorramp0 = nodes.new(type='ShaderNodeValToRGB')
    colorramp0.color_ramp.interpolation = 'CONSTANT'
    colorramp0.color_ramp.elements[0].color = [0.104094, 0.104094, 0.104094, 1.000000]
    colorramp0.color_ramp.elements[1].color = [0.369217, 0.369217, 0.369217, 1.000000]
    colorramp0.color_ramp.elements[1].position = 0.164

    shadertorgb = nodes.new(type='ShaderNodeShaderToRGB')
    
    diffuse = nodes.new(type='ShaderNodeBsdfDiffuse')

    colorramp1 = nodes.new(type='ShaderNodeValToRGB')
    colorramp1.color_ramp.interpolation = 'CONSTANT'
    colorramp1.color_ramp.elements[0].color = [0.0, 0.0, 0.0, 1.0]
    colorramp1.color_ramp.elements[1].color = [1.0, 1.0, 1.0, 1.0]
    colorramp1.color_ramp.elements[1].position = 1.0

    voronoi = nodes.new(type='ShaderNodeTexVoronoi')
    voronoi.voronoi_dimensions = '2D'

    fresnel = nodes.new(type='ShaderNodeFresnel')

    links = smokemat.node_tree.links

    links.new(mixshader.outputs[0], output.inputs[0])
    
    links.new(transparent.outputs[0], mixshader.inputs[2])
    
    links.new(colorramp0.outputs[0], mixshader.inputs[1])    
    links.new(shadertorgb.outputs[0], colorramp0.inputs[0])
    links.new(diffuse.outputs[0], shadertorgb.inputs[0])

    links.new(colorramp1.outputs[0], mixshader.inputs[0])
    links.new(voronoi.outputs[0], colorramp1.inputs[0])
    links.new(fresnel.outputs[0], voronoi.inputs[1])

    bpy.context.object.data.materials.append(smokemat)


class OBJECT_OT_generateSmokeCloud(bpy.types.Operator):
    """Create a stylized smoke cloud"""
    bl_idname = "mesh.generate_smoke_cloud"
    bl_label = "Add Stylized Smoke Cloud"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateSmokeCloud()
        #assignDrivers()

        return {'FINISHED'}
