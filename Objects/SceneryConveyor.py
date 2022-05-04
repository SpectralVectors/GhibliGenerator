# Scenery Conveyor

import bpy

# Creating the Curve

bpy.ops.curve.primitive_bezier_curve_add(radius=1)

converyorcurve = bpy.context.object
converyorcurve.name = 'ConveyorCurve'

bpy.ops.transform.rotate(value=1.5708)

bpy.ops.object.editmode_toggle()

bpy.ops.curve.select_all(action='DESELECT')

bpy.ops.curve.de_select_first()

bpy.ops.transform.rotate(value=0.785398, orient_axis='Z')

bpy.ops.curve.select_all(action='SELECT')

bpy.ops.curve.duplicate_move(CURVE_OT_duplicate={}, TRANSFORM_OT_translate={"value":(0, 0, 1)})

bpy.ops.curve.select_all(action='DESELECT')

bpy.ops.curve.de_select_first()

bpy.ops.curve.make_segment()

bpy.ops.curve.select_all(action='DESELECT')

bpy.ops.curve.de_select_first()

bpy.ops.curve.de_select_last()

bpy.ops.curve.make_segment()

bpy.ops.object.editmode_toggle()

bpy.ops.transform.resize(value=(-10, -100, -10))

bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

# Creating the Plane
bpy.ops.mesh.primitive_plane_add()

conveyorplane = bpy.context.object
conveyorplane.name = 'ConveyorPlane'

bpy.ops.transform.resize(value=(1, 0.5, 1))

bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'
bpy.context.object.modifiers["Array"].curve = bpy.data.objects["ConveyorCurve"]

bpy.ops.object.modifier_add(type='CURVE')
bpy.context.object.modifiers["Curve"].object = bpy.data.objects["ConveyorCurve"]

bpy.ops.object.particle_system_add()
bpy.context.object.particle_systems[0].name = 'SceneryParticles'
particle = bpy.context.object.particle_systems[0].settings
particle.name = 'SceneryParticleSettings'
particle.type = 'HAIR'
particle.count = 100
#particle.hair_length = 2
particle.hair_step = 2
particle.render_step = 2
particle.distribution = 'RAND'
particle.use_modifier_stack = True

# Creating the Transparent Material
conveyormat = bpy.data.materials.new(name='ConveyorMaterial')
conveyormat.use_nodes = True
conveyormat.blend_method = 'BLEND'
conveyormat.shadow_method = 'NONE'
conveyormat.node_tree.nodes.clear()

nodes = conveyormat.node_tree.nodes

output = nodes.new(type='ShaderNodeOutputMaterial')

transparent = nodes.new(type='ShaderNodeBsdfTransparent')

links = conveyormat.node_tree.links

links.new(transparent.outputs[0], output.inputs[0])

bpy.context.object.data.materials.append(conveyormat)

