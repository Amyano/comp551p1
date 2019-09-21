import pypandoc
from glob import glob

def generate():
    pypandoc.convert_file(
        " ".join(glob("./src/docs/*.md")),
        "pdf",
        outputfile="doc.pdf"
    )