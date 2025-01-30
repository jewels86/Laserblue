import axinite as ax
from axinite import axtools

args = axtools.read("semi-accurate-solar-system.tmpl.ax")
axtools.load(args, "semi-accurate-solar-system.ax", verbose=True)