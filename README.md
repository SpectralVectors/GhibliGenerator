# GhibliGenerator
![GhibliGenerator](/screenshots/GhibliGenerator.PNG)

## Table of Contents
- [What It Is](#what-it-is)

- [Ground Planes](#ground-planes)
  - [Grass](#grass)
  - [Water](#water)
  - [Sand](#sand)
  - [Ice](#ice)
  - [Stone Path](#stone-path)
  - [Rock Wall](#rock-wall)

- [Objects](#objects)
  - [Rock](#rock)
  - [Rain Plane](#rain-plane)
  - [Smoke Cloud](#smoke-cloud)
  - [Explosion](#explosion)

- [Effects](#effects)
  - [Action Planes](#action-planes)
  - [Color Flash](#color-flash)
  - [Gradient Flash](#gradient-flash)
  - [Circular Flash](#circular-flash)

- [Backgrounds](#backgrounds)
  - [Blue Sky](#blue-sky)
  - [Sunset](#sunset)
  - [Overcast](#overcast)
  - [Twilight](#twilight)
  - [Starry Night](#starry-night)

- [Limitations](#limitations)
- [Acknowledgments & Thanks](#acknowledgements-and-thanks)

## What It Is

Using only Blender's internal procedural textures this addon gives you infinitely customizable anime-style assets based on common stylized workflows.

I have tried to synthesize and simplify different approaches to stylized assets that give quick, easy but versatile results. All of the objects can receive colored light from standard scene lights and cast dynamic shadows. This allows you to quickly tint or shade your entire stylized scene with global lights, but comes with a couple of catches (see: Limitations)

In addition to that, each asset comes with a customized driver control panel to give you access to all the most common settings (colors, opacity, texture scale etc) without leaving the 3D Viewport.

The assets are divided into categories for easier navigation:

## Ground Planes

### Grass
![GrassPlane](/screenshots/GrassPlane.png)
### Grass Properties
**Color1** - The first color in the color ramp

**Color1Position** - Default 0, A value between 0-1, the closer to the center, the more intense the color will be.

**Color2** - The second color in the color ramp

**Color2Position** - Default 1, A value between 0-1, the closer to the center, the more intense the color will be.

**DisplaceScale** - The scale of the displacement texture, how _wide_ do you want the hills

**DisplaceStrength** - The intensity of the displacement, how _tall_ do you want the hills

**ExtendX/Y** - Extends the object procedurally to avoid tiling or repetition

**GrassLength** - How long is the grass

**RenderMultiplier** - This number will be applied to the total number of grass particles during rendering, set to 1 if you want your grass to appear exactly as it does in the viewport, set up to 1000 to compensate for sparse coverage, or to give a painterly look

---

### Water
![WaterPlanes](/screenshots/WaterPlanes.png)
### Water Properties
**BigRippleScale** - The size of the large distortions

**BigRippleSpeed** - The speed of the large distortions - **Driver Value**

**BottomColor1** - The first color of the bottom layer

**BottomColor2** - The second color of the bottom layer, can act like a shadow for the top ripples

**ExtendX/Y** - Extends the object procedurally to avoid tiling or repetition

**MotionX/Y** - Moves the wave texture, all motion and speed controls affect both water planes in sync - **Driver Value**

**SmallRippleScale** - The size of the small distortions

**SmallRippleSpeed** - The speed of the small distortions - **Driver Value**

**SurfaceColor1** - The first color of the surface layer, less visible when transparency is used

**SurfaceColor2** - The second color of the surface layer, less visible when transparency is used

**SurfaceColor3** - The third color of the surface layer, the ripple highlight color, always visible

**SurfaceTransparentColor** - The color of the water, itself

---

### Sand
![SandPlane](/screenshots/SandPlane.png)

---

### Ice
![IcePlane](/screenshots/IcePlane.png)

---

### Stone Path
![StonePath](/screenshots/StonePath.png)

---

### Rock Wall
![RockWallPlane](/screenshots/RockWallPlane.png)

---

## Objects

### Rock
![Rock](/screenshots/Rock.png)
### Rock Properties
**Brightness** - Brightness of the rock texture

**Contrast** - Contrast of the rock texture

**DisplaceScale** - The scale of the displacement texture, how _wide_ are the deformations

**DisplaceStrength** - The intensity of the displacement, how _deep_ are the deformations

**PatternMix** - Blend between texture distortion patterns

**RockColor** - Color tint for the rock

---

### Rain Plane
![RainPlane](/screenshots/RainPlane.png)

---

### Smoke Cloud
![SmokeCloud](/screenshots/SmokeCloud.png)

---

### Explosion
![Explosion](/screenshots/Explosion.png)


---

## Effects

### Action Planes
![ActionPlanes](/screenshots/ActionPlanes.png)
### Action Planes Properties

**BG_Color1** - The outermost color of the gradient plane

**BG_Color2** - The middle color of the gradient plane

**BG_Color3** - The innermost color of the gradient plane

**BG_EmitStrength** - The light intensity of the gradient plane, use with Bloom

**BG_NoiseLength** - The vertical length of the background noise, can affect the impression of speed

**BG_NoiseWidth** - Not to be confused with background width, this controls the width of the noise texture

**BG_Opacity** - Use to fade the gradient plane in/out - **Keyframe Value**

**BG_Speed** - How fast the noise texture moves - **Driver Value**

**BG_Width** - How wide is the central background color

**LineColor** - The color of the lines

**LineEmitStrength** - The light intensity of the lines, use with Bloom

**LineLength** - How long are the lines, from dots to lines

**LineOpacity** - Use to fade the lines in/out - **Keyframe Value**

**LineSpeed** - How fast the lines move - **Driver Value**

**LineThickness** - How thick are the lines, from thin sticks to thick brush-like strokes

---

### Color Flash
![ColorFlash](/screenshots/ColorFlash.png)

---

### Gradient Flash
![GradientFlash](/screenshots/GradientFlash.png)

---

### Circular Flash
![CircularFlash](/screenshots/CircularFlash.png)

## Backgrounds

### Blue Sky
![BlueSky](/screenshots/BlueSky.png)

---

### Sunset
![Sunset](/screenshots/Sunset.png)

---

### Overcast
![Overcast](/screenshots/Overcast.png)

---

### Twilight
![Twilight](/screenshots/Twilight.png)

---

### Starry Night
![StarryNight](/screenshots/StarryNight.png)


---

## Limitations
The shader trick I have used to receive scene lights on "emissive" materials comes with a couple of catches, but first, what is the trick?

Instead of using a color ramp or Emission shader before the Material Output we use a Translucent shader with a Normal node that has the Z-axis inverted.

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

[Back to the Top](#ghibligenerator)

