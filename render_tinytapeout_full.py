import mitsuba as mi
import argparse

RENDER_WIDTH = 1920
RENDER_HEIGHT = 1080
# Samples per pixel:
RENDER_SPP = 256

argparser = argparse.ArgumentParser(description='Render scene_tinytapeout.xml')
argparser.add_argument('-width', "--output_width", required=False, type=int, help="Output resolution width")
argparser.add_argument('-height', "--output_height", required=False, type=int, help="Output resolution height")
argparser.add_argument('-spp', "--samples_per_pixel", required=False, type=int, help="Render samples per pixel")
args = vars(argparser.parse_args())

if args["output_width"] is not None:
    RENDER_WIDTH = args["output_width"]
if args["output_height"] is not None:
    RENDER_HEIGHT = args["output_height"]
if args["samples_per_pixel"] is not None:
    RENDER_SPP = args["samples_per_pixel"]

mi.set_variant("scalar_rgb")

scene = mi.load_file("scene_tinytapeout.xml")

def update_film_size(sensor, width, height):
    # Traverse the sensor properties
    params = mi.traverse(sensor)
    # Update the film size
    params['film.size'] = mi.Vector2u(width, height)
    # Apply the changes
    params.update()

def set_top_orthographic_view(scene, width, height):
    sensor = scene.sensors()[1]  # Assuming the second sensor is the top orthographic view
    bbox = scene.bbox()

    # Calculate the center of the bounding box
    center = bbox.center()

    # Calculate the scale based on the bounding box dimensions
    scale = max(bbox.extents().x, bbox.extents().y) / 2

    # Update the camera transformation to fit the entire scene in view
    to_world = mi.ScalarTransform4f.scale(scale) @ mi.ScalarTransform4f.translate([center.x, center.y, bbox.max.z])
    
    params = mi.traverse(sensor)
    params['to_world'] = to_world
    params.update()

# Print the bounding box of the scene
bounding_box = scene.bbox()
print(f"Bounding box of the scene: min={bounding_box.min}, max={bounding_box.max}")

print("Rendering TOP LEFT Orthographic view")
update_film_size(scene.sensors()[0], RENDER_WIDTH, RENDER_HEIGHT)
img = mi.render(scene, spp=RENDER_SPP, sensor=0)
mi.util.write_bitmap("scene_tinytapeout_TOPLEFT.png", img, False)

print("Rendering TOP Orthographic view")
update_film_size(scene.sensors()[1], RENDER_WIDTH, RENDER_HEIGHT)
set_top_orthographic_view(scene, RENDER_WIDTH, RENDER_HEIGHT)
img = mi.render(scene, spp=RENDER_SPP, sensor=1)
mi.util.write_bitmap("scene_tinytapeout_TOP.png", img, False)

print("Rendering Perspective view")
update_film_size(scene.sensors()[2], RENDER_WIDTH, RENDER_HEIGHT)
img = mi.render(scene, spp=RENDER_SPP, sensor=2)
mi.util.write_bitmap("scene_tinytapeout_PERSP.png", img, False)

# mi.Bitmap(img).write('scene_tinytapeout.exr')
