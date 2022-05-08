bl_info = {
    "name": "Ghibli Generator",
    "author": "Spectral Vectors",
    "version": (0, 8, 3),
    "blender": (2, 80, 0),
    "location": "View 3D > Properties Panel",
    "description": "Procedural Anime Assets",
    "warning": "",
    "doc_url": "https://github.com/SpectralVectors/GhibliGenerator",
    "category": "Object",
}

import bpy

from bpy.app.handlers import persistent

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
from .GroundPlanes.RoadPlane import *

from .Objects.RainPlane import *
from .Objects.FirePlane import *
from .Objects.Rock import *
from .Objects.SmokeCloud import *
from .Objects.SmokeRing import *
from .Objects.SmokeTrail import *
from .Objects.Explosion import *
from .Objects.EnergyRing import *
from .Objects.EnergySphere import *
from .Objects.ElectricArcSphere import *
from .Objects.HeatRipplePlane import *

@persistent
def addon_enabler(dummy):   
    bpy.ops.preferences.addon_enable(module="add_curve_sapling")
    bpy.ops.preferences.addon_enable(module="node_arrange")    

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
            column.operator(OBJECT_OT_generateRoadRlane.bl_idname, text='Road', icon='COLLAPSEMENU')
        
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
            column.operator(OBJECT_OT_generateSmokeRing.bl_idname, text='Smoke Ring', icon='RADIOBUT_OFF')
            column.operator(OBJECT_OT_generateSmokeTrail.bl_idname, text='Smoke Trail', icon='FORCE_FLUIDFLOW')
            column.operator(OBJECT_OT_generateExplosion.bl_idname, text='Explosion', icon='SORTBYEXT')
            column.operator(OBJECT_OT_generateEnergyRing.bl_idname, text='Energy Ring', icon='TRIA_DOWN_BAR')
            column.operator(OBJECT_OT_generateEnergySphere.bl_idname, text='Energy Sphere', icon='SHADING_RENDERED')
            column.operator(OBJECT_OT_generateElectricArcSphere.bl_idname, text='Electric Arc Sphere', icon='MOD_SMOOTH')
            column.operator(OBJECT_OT_generateFirePlane.bl_idname, text='Fire Plane', icon='SEQ_HISTOGRAM')
            column.operator(OBJECT_OT_generateHeatRipplePlane.bl_idname, text='Heat Ripple', icon='FORCE_TURBULENCE')
        
        box = layout.box()
        row = box.row()
        icon = 'TRIA_DOWN' if context.scene.effects_panel_open else 'TRIA_RIGHT'
        row.prop(context.scene, 'effects_panel_open', icon=icon, icon_only=True) 
        row.label(text="BG Effects")
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
        row.label(text="World Backgrounds")
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
            OBJECT_OT_generateRoadRlane,

            # Objects
            OBJECT_OT_generateRock,
            OBJECT_OT_generateSmokeCloud,
            OBJECT_OT_generateSmokeRing,
            OBJECT_OT_generateSmokeTrail,
            OBJECT_OT_generateExplosion,
            OBJECT_OT_generateRainPlane,
            OBJECT_OT_generateEnergyRing,
            OBJECT_OT_generateEnergySphere,
            OBJECT_OT_generateElectricArcSphere,
            OBJECT_OT_generateFirePlane,
            OBJECT_OT_generateHeatRipplePlane,

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

    bpy.app.handlers.load_post.append(addon_enabler)
    
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    bpy.app.handlers.load_post.remove(addon_enabler)


if __name__ == "__package__":
    register()