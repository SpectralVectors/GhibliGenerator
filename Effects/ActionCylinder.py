# Creating Action Cylinder

import bpy

bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, end_fill_type='NOTHING')
bpy.ops.object.shade_smooth()

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='DESELECT')

bpy.ops.object.editmode_toggle()
bpy.context.object.data.edges[0].select = True

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.loop_multi_select(ring=False)
bpy.ops.transform.resize(value=(0, 0, 0))