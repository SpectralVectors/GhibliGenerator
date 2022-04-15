# Creating Action Cylinder

import bpy

bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

for i in bpy.context.object.data.polygons:
   i.select = False
for i in bpy.context.object.data.edges:
   i.select = False
for i in bpy.context.object.data.vertices:
   i.select = False
   
bpy.context.object.data.polygons[30].select=True
bpy.context.object.data.polygons[33].select=True

bpy.ops.object.editmode_toggle()

bpy.ops.mesh.delete(type='FACE')

bpy.ops.object.editmode_toggle()
bpy.context.object.data.edges[0].select=True

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.loop_multi_select(ring=False)
bpy.ops.transform.resize(value=(0.01,0.01,0.01))
