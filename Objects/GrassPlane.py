# Grass Generator
import bpy

from .Drivers.GrassPlaneDrivers import *

def generateGrassPlane():

    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    grassplane = bpy.context.object
    grassplane.name = 'Grass'
    bpy.ops.object.shade_smooth()

    bpy.ops.object.modifier_add(type='ARRAY')
    array_x = grassplane.modifiers['Array']
    array_x.count = 1

    bpy.ops.object.modifier_add(type='ARRAY')
    array_y = grassplane.modifiers['Array.001']
    array_y.count = 1
    array_y.relative_offset_displace[0] = 0
    array_y.relative_offset_displace[1] = 1

    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = grassplane.modifiers["Subdivision"]
    subsurf.levels = 3
    subsurf.render_levels = 3
    subsurf.subdivision_type = 'SIMPLE'

    grasstex = bpy.data.textures.new(name='GrassTexture', type = 'CLOUDS')
    grasstex.noise_scale = 1

    bpy.ops.object.modifier_add(type='DISPLACE')
    displace = grassplane.modifiers["Displace"]
    displace.texture_coords = 'GLOBAL'
    displace.strength = 0.5
    displace.texture = grasstex

    bpy.ops.object.particle_system_add()
    bpy.context.object.particle_systems[0].name = 'GrassParticles'
    particle = bpy.context.object.particle_systems[0].settings
    particle.name = 'GrassParticleSettings'
    particle.type = 'HAIR'
    particle.count = 5000
    particle.hair_length = 0.2
    particle.hair_step = 2
    particle.render_step = 2
    particle.child_type = 'SIMPLE'
    particle.clump_factor = -1
    particle.use_modifier_stack = True
    bpy.context.scene.render.hair_type = 'STRIP'

    grassmat = bpy.data.materials.new(name='GrassMaterial')
    grassmat.use_nodes = True
    grassmat.shadow_method = 'NONE'
    grassmat.node_tree.nodes.clear()

    nodes = grassmat.node_tree.nodes

    output = nodes.new(type='ShaderNodeOutputMaterial')

    # Translucent & Normal Node
    translucent = nodes.new(type='ShaderNodeBsdfTranslucent')
    normal = nodes.new(type='ShaderNodeNormal')
    normal.outputs[0].default_value = (0, 0, -1)
    # Ends

    colorramp = nodes.new(type='ShaderNodeValToRGB')
    colorramp.color_ramp.elements[0].color = (0, 0.1, 0.04, 1)
    colorramp.color_ramp.elements[1].color = (0, 0.5, 0.15, 1)
    noise = nodes.new(type='ShaderNodeTexNoise')

    links = grassmat.node_tree.links

    links.new(translucent.outputs[0], output.inputs[0])
    links.new(colorramp.outputs[0], translucent.inputs[0])
    links.new(normal.outputs[0], translucent.inputs[1])
    links.new(noise.outputs[0], colorramp.inputs[0])
    
    bpy.context.object.data.materials.append(grassmat)

# Add a third color to the Grass ColorRamp

class OBJECT_OT_generateGrassPlane(bpy.types.Operator):
    """Create a stylized grass plane"""
    bl_idname = "mesh.generate_grass_plane"
    bl_label = "Add Stylized Grass"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        generateGrassPlane()
        assignDrivers()

        return {'FINISHED'}
