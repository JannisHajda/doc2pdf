from subprocess import Popen, PIPE
import os
import glob
from tqdm import tqdm

input_path = '/input'
output_path = '/output'

file_types = ['doc', 'docx', 'odt', 'pptx', 'ppt', 'odp']

if __name__ == "__main__":
    files = []
    errors_during_conversion = []

    # Collect all files of the specified types in the input folder and subfolders
    for file_type in file_types:
        files.extend(glob.glob(f"{input_path}/**/*.{file_type}", recursive=True))
    
    print(f"\n🎯 Found {len(files)} files to convert.\n")

    # Convert each file and maintain folder structure
    for file in tqdm(files, desc="Converting files"):
        filename = os.path.basename(file)
        # Get the relative path from the input folder to the file
        relative_path = os.path.dirname(file).replace(input_path, "").lstrip('/')

        # Construct the output directory based on the relative path
        output_dir = os.path.join(output_path, relative_path)
        os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

        # Launch the LibreOffice conversion
        p = Popen(
            ["soffice", "--headless", "--convert-to", "pdf", file, "--outdir", output_dir],
            stdout=PIPE,
            stderr=PIPE,
        )

        output, error = p.communicate()
        if p.returncode != 0:
            errors_during_conversion.append((file, error.decode("utf-8").strip()))

    if errors_during_conversion:
        print("\n❌ Failed to convert the following files:")
        for file, err in errors_during_conversion:
            print(f"  - {file}: {err}")
    else:
        print("\n✅ All files converted successfully!")

    print("\n🎉 Conversion process finished. Thanks for using doc2pdf!")
    print("⭐ If you found this useful, please consider giving a star to the GitHub repo.\n")
