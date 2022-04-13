bl_info = {
    "name": "Ghibli Generator",
    "author": "Spectral Vectors",
    "version": (0, 3),
    "blender": (2, 80, 0),
    "location": "View 3D > Properties Panel",
    "description": "Procedural Anime Assets",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy
from .Backgrounds import *
from .Objects.ActionPlanes import *
from .Objects.GrassPlane import *
from .Objects.RainPlane import *
from .Objects.Rock import *
from .Objects.WaterPlanes import *

class GhibliGeneratorPanel(bpy.types.Panel):
    bl_label = "Ghibli Generator"
    bl_category = "Ghibli Generator"
    bl_idname = "VIEW3D_PT_GhibliGeneratorPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):

        layout = self.layout
        column = layout.column()
        column.label(text="Procedural Anime Assets")
        box = layout.box()
        box.label(text="Objects:")
        box.operator(OBJECT_OT_generateGrassPlane.bl_idname, text='Grass Plane', icon='HAIR')
        box.operator(OBJECT_OT_generateRock.bl_idname, text='Rock', icon='MESH_CAPSULE')
        box.operator(OBJECT_OT_generateWaterPlanes.bl_idname, text='Water Planes', icon='MOD_OCEAN')
        box.operator(OBJECT_OT_generateRainPlane.bl_idname, text='Rain Plane', icon='MOD_FLUIDSIM')
        box = layout.box()
        box.label(text="Effects:")
        box.operator(OBJECT_OT_generateActionPlanes.bl_idname, text='Action Planes', icon='ALIGN_FLUSH')
        box = layout.box()
        box.label(text="Backgrounds:")
        box.operator(OBJECT_OT_generateBlueSkyBG.bl_idname, text='Blue Sky', icon='LIGHT_SUN')
        box.operator(OBJECT_OT_generateSunsetBG.bl_idname, text='Sunset', icon='ANCHOR_BOTTOM')
        box.operator(OBJECT_OT_generateTwilightBG.bl_idname, text='Twilight', icon='MOD_TIME')
        box.operator(OBJECT_OT_generateStarryNightBG.bl_idname, text='Starry Night', icon='SOLO_OFF')
        
classes = (
            OBJECT_OT_generateGrassPlane,
            OBJECT_OT_generateRock,
            OBJECT_OT_generateRainPlane,
            OBJECT_OT_generateActionPlanes,
            OBJECT_OT_generateWaterPlanes,
            OBJECT_OT_generateBlueSkyBG,
            OBJECT_OT_generateSunsetBG,
            OBJECT_OT_generateTwilightBG,
            OBJECT_OT_generateStarryNightBG,
            GhibliGeneratorPanel,
            )

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__package__":
    register()