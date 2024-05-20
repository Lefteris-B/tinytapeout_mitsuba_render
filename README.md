# tinytapeout_mitsuba_render

Original project from [mbalestrini](https://github.com/mbalestrini): 
[https://github.com/mbalestrini/tinytapeout_mitsuba_render](https://github.com/mbalestrini/tinytapeout_mitsuba_render)

Works with mitsuba 3

Installation:
1. Clone repo
```
git clone https://github.com/Lefteris-B/tinytapeout_mitsuba_render
```
2. Install requirements
```
pip install -r requirements.txt
```
Usage:

`render_tinytapeout.py [-h] [-width OUTPUT_WIDTH] [-height OUTPUT_HEIGHT] [-spp SAMPLES_PER_PIXEL]`

When no arguments are given, script assumes 1920x1080

## Input files
Expects theses files to be on the same path:

- tinytapeout.gds_licon.obj
- tinytapeout.gds_poly.obj
- tinytapeout.gds_nwell.obj
- tinytapeout.gds_diff.obj
- tinytapeout.gds_met4.obj
- tinytapeout.gds_via3.obj
- tinytapeout.gds_met3.obj
- tinytapeout.gds_via2.obj
- tinytapeout.gds_met2.obj
- tinytapeout.gds_via.obj
- tinytapeout.gds_mcon.obj
- tinytapeout.gds_substrate.obj
- tinytapeout.gds_li1.obj
- tinytapeout.gds_met1.obj



## Output files
- scene_tinytapeout_PERSP.png
- scene_tinytapeout_TOP.png
- scene_tinytapeout_TOPLEFT.png

Usage:

`render_tinytapeout_full.py 

Still in working progress.
Renders the whole gds file.