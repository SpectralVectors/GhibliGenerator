# GhibliGenerator
![GhibliGenerator](/screenshots/GhibliGenerator.PNG)

Procedural Anime Assets for Blender

## What It Is

Using only Blender's internal procedural textures this addon gives you infinitely customizable anime-style assets based on common stylized workflows.

I have tried to synthesize and simplify different approaches to stylized assets that give quick, easy but versatile results. All of the objects can receive colored light from standard scene lights and cast dynamic shadows. This allows you to quickly tint or shade your entire stylized scene with global lights, but comes with a couple of catches (see: Limitations)

In addition to that, each asset comes with a customized driver control panel to give you access to all the most common settings (colors, opacity, texture scale etc) without leaving the 3D Viewport.

The assets are divided into categories for easier navigation:

## Ground Planes

### Grass
![GrassPlane](/screenshots/GrassPlane.png)

### Water
![WaterPlanes](/screenshots/WaterPlanes.png)

### Sand
![SandPlane](/screenshots/SandPlane.png)

### Ice
![IcePlane](/screenshots/IcePlane.png)

### Stone Path
![StonePath](/screenshots/StonePath.png)

### Rock Wall
![RockWallPlane](/screenshots/RockWallPlane.png)

## Objects

### Rock
![Rock](/screenshots/Rock.png)

### Rain Plane
![RainPlane](/screenshots/RainPlane.png)

### Smoke Cloud
![SmokeCloud](/screenshots/SmokeCloud.png)

### Explosion
![Explosion](/screenshots/Explosion.png)


## Effects

### Action Planes
![ActionPlanes](/screenshots/ActionPlanes.png)

### Color Flash
![ColorFlash](/screenshots/ColorFlash.png)

### Gradient Flash
![GradientFlash](/screenshots/GradientFlash.png)

### Circular Flash
![CircularFlash](/screenshots/CircularFlash.png)

## Backgrounds

### Blue Sky
![BlueSky](/screenshots/BlueSky.png)

### Sunset
![Sunset](/screenshots/Sunset.png)

### Overcast
![Overcast](/screenshots/Overcast.png)

### Twilight
![Twilight](/screenshots/Twilight.png)

### Starry Night
![StarryNight](/screenshots/StarryNight.png)


## Limitations
The shader trick I have used to receive scene lights on "emissive" materials comes with a couple of catches, but first, what is the trick?

Instead of using a color ramp or Emission shader we use a Translucent shader with a Normal node that has the Z-axis inverted.

This gives us global lighting now affecting what otherwise appears to be an emissive material, HOWEVER:

1 - It does not give banded light (like cel-shading), but traditional gradient light falloff, I think this looks good on the background objects in a scene, and can help set it apart from a character that has full cel shading for their lighting, but, in order to get banded light you must add a colorramp after the Translucent node, which negates all the light color in your scene.

2 - The other catch is, I believe, related to getting our color information from a Normal node: Certain colors of light are more powerful than others, Green is the strongest, followed by Red, then Blue. This can be compensated for in your scene by turning up the intensity on lights that appear too dim manually, but I have not found a way to fix it in the nodes, my attempts seem to just shift the coordinates of the light, rather than the color.

## Acknowledgements and Thanks
This addon would not have been possible without the techniques, hard work and generosity of many Blender users, including:

- [Kristof Dedene](https://www.youtube.com/channel/UCAcXkKCYidxGU-VIA5z-ZzQ)
- [Lightning Boy Studio](https://www.youtube.com/c/LightningBoyStudio)
- [Marius Oberholster](https://www.youtube.com/c/MariusOberholster)
- [Pierrick Picault](https://www.youtube.com/c/PierrickPicaut_P2DESIGN)
- [lateasusual](https://twitter.com/lateasusual_)
- [POLYCOSM](https://www.youtube.com/c/POLYCOSM)
- [LanceBeryl.Dev](https://www.youtube.com/c/LanceBerylDev)
- [Loop](https://www.youtube.com/channel/UChS_1gry7bQeIbdHVSRqMAw)

And thanks, of course, to all the inspired, dedicated and hard working artists and animators from Toei to Ghibli and all across the anime industry!
