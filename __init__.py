bl_info = {
    "name": "Ghibli Generator",
    "author": "Spectral Vectors",
    "version": (0, 7, 5),
    "blender": (2, 80, 0),
    "location": "View 3D > Properties Panel",
    "description": "Procedural Anime Assets",
    "warning": "",
    "doc_url": "https://github.com/SpectralVectors/GhibliGenerator",
    "category": "Object",
}

import bpy

from .Backgrounds import *

from .Effects.ActionPlanes import *
from .Effects.ColorFlashPlane import *
from .Effects.GradientFlashPlane import *
from .Effects.CircularFlashPlane import *

from .GroundPlanes.GrassPlane import *
from .GroundPlanes.WaterPlanes import *
from .GroundPlanes.SandPlane import *
from .GroundPlanes.IcePlane import *
from .GroundPlanes.StonePathPlane import *
from .GroundPlanes.RockWallPlane import *

from .Objects.RainPlane import *
from .Objects.Rock import *
from .Objects.SmokeCloud import *
from .Objects.Explosion import *


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
        
        row = box.row()
        icon = 'TRIA_DOWN' if context.scene.groundplanes_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'groundplanes_panel_open', icon=icon, icon_only=True)
        row.label(text="Ground Planes")        
        
        if context.scene.groundplanes_panel_open:
            column = box.column()
            column.operator(OBJECT_OT_generateGrassPlane.bl_idname, text='Grass', icon='HAIR')
            column.operator(OBJECT_OT_generateWaterPlanes.bl_idname, text='Water', icon='MOD_OCEAN')
            column.operator(OBJECT_OT_generateSandPlane.bl_idname, text='Sand', icon='RNDCURVE')
            column.operator(OBJECT_OT_generateIcePlane.bl_idname, text='Ice', icon='FREEZE')
            column.operator(OBJECT_OT_generateStonePathPlane.bl_idname, text='Stone Path', icon='POINTCLOUD_DATA')
            column.operator(OBJECT_OT_generateRockWallPlane.bl_idname, text='Rock Wall', icon='LINCURVE')
        
        box = layout.box()
        row = box.row()
        icon = 'TRIA_DOWN' if context.scene.objects_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'objects_panel_open', icon=icon, icon_only=True)        
        row.label(text="Objects")
        if context.scene.objects_panel_open:
            column = box.column()
            column.operator(OBJECT_OT_generateRock.bl_idname, text='Rock', icon='MESH_CAPSULE')
            column.operator(OBJECT_OT_generateRainPlane.bl_idname, text='Rain Plane', icon='MOD_FLUIDSIM')
            column.operator(OBJECT_OT_generateSmokeCloud.bl_idname, text='Smoke Cloud', icon='MOD_FLUID')
            column.operator(OBJECT_OT_generateExplosion.bl_idname, text='Explosion', icon='SORTBYEXT')
        
        box = layout.box()
        row = box.row()
        icon = 'TRIA_DOWN' if context.scene.effects_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'effects_panel_open', icon=icon, icon_only=True) 
        row.label(text="Effects")
        if context.scene.effects_panel_open:
            column = box.column()
            column.operator(OBJECT_OT_generateActionPlanes.bl_idname, text='Action Planes', icon='MOD_OPACITY')
            column.operator(OBJECT_OT_generateColorFlashPlane.bl_idname, text='Color Flash', icon='MATPLANE')
            column.operator(OBJECT_OT_generateGradientFlashPlane.bl_idname, text='Gradient Flash', icon='NODE_TEXTURE')
            column.operator(OBJECT_OT_generateCircularFlashPlane.bl_idname, text='Circular Flash', icon='CLIPUV_DEHLT')
        
        box = layout.box()
        row = box.row()
        icon = 'TRIA_DOWN' if context.scene.backgrounds_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'backgrounds_panel_open', icon=icon, icon_only=True) 
        row.label(text="Backgrounds")
        if context.scene.backgrounds_panel_open:
            column = box.column()
            column.operator(OBJECT_OT_generateBlueSkyBG.bl_idname, text='Blue Sky', icon='LIGHT_SUN')
            column.operator(OBJECT_OT_generateSunsetBG.bl_idname, text='Sunset', icon='ANCHOR_BOTTOM')
            column.operator(OBJECT_OT_generateOvercastBG.bl_idname, text='Overcast', icon='VOLUME_DATA')
            column.operator(OBJECT_OT_generateTwilightBG.bl_idname, text='Twilight', icon='MOD_TIME')
            column.operator(OBJECT_OT_generateStarryNightBG.bl_idname, text='Starry Night', icon='SOLO_OFF')
            column.operator(OBJECT_OT_generateDefaultBG.bl_idname, text='Default', icon='BLENDER')
        
classes = (
            # Ground Planes
            OBJECT_OT_generateGrassPlane,
            OBJECT_OT_generateWaterPlanes,
            OBJECT_OT_generateSandPlane,
            OBJECT_OT_generateIcePlane,
            OBJECT_OT_generateStonePathPlane,
            OBJECT_OT_generateRockWallPlane,

            # Objects
            OBJECT_OT_generateRock,
            OBJECT_OT_generateSmokeCloud,
            OBJECT_OT_generateExplosion,
            OBJECT_OT_generateRainPlane,

            # Effects
            OBJECT_OT_generateActionPlanes,
            OBJECT_OT_generateColorFlashPlane,
            OBJECT_OT_generateGradientFlashPlane,
            OBJECT_OT_generateCircularFlashPlane,            

            # Backgrounds            
            OBJECT_OT_generateBlueSkyBG,
            OBJECT_OT_generateSunsetBG,
            OBJECT_OT_generateTwilightBG,
            OBJECT_OT_generateOvercastBG,
            OBJECT_OT_generateStarryNightBG,
            OBJECT_OT_generateDefaultBG,

            # UI
            GhibliGeneratorPanel,
            )

# Register an app handler to enable this addon to clean up node trees
# bpy.ops.preferences.addon_enable(module="node_arrange")

def register():
    
    bpy.types.Scene.groundplanes_panel_open = bpy.props.BoolProperty(
        default=False
    )

    bpy.types.Scene.objects_panel_open = bpy.props.BoolProperty(
        default=False
    )

    bpy.types.Scene.effects_panel_open = bpy.props.BoolProperty(
        default=False
    )

    bpy.types.Scene.backgrounds_panel_open = bpy.props.BoolProperty(
        default=False
    )
    
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__package__":
    register()