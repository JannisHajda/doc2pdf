from subprocess import Popen, PIPE
import glob

files = []
types = ['doc', 'docx', 'pptx', 'ppt']

for type in types:
    files.extend(glob.glob('./input/*.' + type))

for file in files:
    p = Popen(['soffice', '--headless', '--convert-to', 'pdf', file, '--outdir', './output'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    if p.returncode != 0:
        print("Couldn't convert to following file: %d %s %s" % (file, output, error))

print("Finished converting! Exiting process.")