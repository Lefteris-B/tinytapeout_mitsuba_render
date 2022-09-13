import mitsuba as mi
import argparse


RENDER_WIDTH = 1920
RENDER_HEIGHT = 1080
# Samples per pixel:
RENDER_SPP = 256

argparser = argparse.ArgumentParser(description='Render scene_tinetapeout.xml')
argparser.add_argument('-width', "--output_width", required=False, type=int, help="Output resolution width")
argparser.add_argument('-height', "--output_height", required=False, type=int, help="Output resolution height")
argparser.add_argument('-spp', "--samples_per_pixel", required=False, type=int, help="Render samples per pixel")
args = vars(argparser.parse_args())

if(args["output_width"]!=None):
    RENDER_WIDTH = args["output_width"]
if(args["output_height"]!=None):
    RENDER_HEIGHT = args["output_height"]
if(args["spp"]!=None):
    RENDER_SPP = args["spp"]


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
  