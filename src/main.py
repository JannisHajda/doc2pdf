from subprocess import Popen, PIPE
import glob

files = []
types = ["doc", "docx", "pptx", "ppt"]

for type in types:
    files.extend(glob.glob("/input/*." + type))

for file in files:
    p = Popen(
        ["soffice", "--headless", "--convert-to", "pdf", file, "--outdir", "/output"],
        stdout=PIPE,
        stderr=PIPE,
    )
    output, error = p.communicate()
    if p.returncode != 0:
        print(
            f"Couldn't convert the following file: {file}\nOutput: {output}\nError: {error}"
        )
    else:
        print(f"Successfully converted: {file}")

print("Finished converting! Exiting process.")
