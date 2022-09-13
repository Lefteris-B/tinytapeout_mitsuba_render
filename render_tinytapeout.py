import mitsuba as mi

RENDER_WIDTH = 1920*2
RENDER_HEIGHT = 1080*2
# Samples per pixel:
RENDER_SPP = 8

mi.set_variant("scalar_rgb")

scene = mi.load_file("scene_tinytapeout.xml")

print("Rendering TOP LEFT Orthographic view")
scene.sensors()[0].film().set_size([RENDER_WIDTH, RENDER_HEIGHT])
scene.sensors()[0].parameters_changed()
img = mi.render(scene, spp=RENDER_SPP, sensor=0)
mi.util.write_bitmap("scene_tinytapeout_TOPLEFT.png", img, False)

print("Rendering TOP Orthographic view")
scene.sensors()[1].film().set_size([RENDER_WIDTH, RENDER_HEIGHT])
scene.sensors()[1].parameters_changed()
img = mi.render(scene, spp=RENDER_SPP, sensor=1)
mi.util.write_bitmap("scene_tinytapeout_TOP.png", img, False)

print("Rendering Perspective view")
scene.sensors()[2].film().set_size([RENDER_WIDTH, RENDER_HEIGHT])
scene.sensors()[2].parameters_changed()
img = mi.render(scene, spp=RENDER_SPP, sensor=2)
mi.util.write_bitmap("scene_tinytapeout_PERSP.png", img, False)

# mi.Bitmap(img).write('scene_tinytapeout.exr')
  