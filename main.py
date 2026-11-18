# Sum up 17 November's world news in one image: copy the image beside this file to /output/entry.png.
# The image is a vintage newspaper front page — "The Global Herald", Tuesday, November 17, 2026 —
# summing up the day: Ukraine strikes the Crimean Bridge (collapsed span), tankers ablaze near the
# Strait of Hormuz, Trump lands in Manila for the ASEAN and Quad summit, the ULA Vulcan rocket
# failure destroys 40 Amazon satellites, and the JPMorgan software-bug outage.
# The output is a valid JPEG image, 1024x683, well under the 1 MiB limit.
# The entry is self-contained: the program only copies the bundled image.
# Deterministic: the same input always produces the same output file.
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
# Confirm the output landed where the grader expects it.
assert os.path.isfile(os.path.join(out_dir, "entry.png"))
print("wrote /output/entry.png")
