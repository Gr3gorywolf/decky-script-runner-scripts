import json
import os
import re


METADATA_FILE = "store-metadata.json"
SCRIPTS_DIR = "scripts"
suported_script_langs = [".js", ".py", ".sh", ".lua", ".pl", ".php", ".rb"]

def parse_metadata(file_path):
    """
    Parse the metadata from the top of a script file, or set default values if metadata is missing.
    """
    metadata = {}
    file_name = os.path.basename(file_path)
    file_title = os.path.splitext(file_name)[0].replace("_", " ").replace("-", " ").title()
    file_extension = os.path.splitext(file_name)[1][1:]
    validKeys = ["title", "language", "version", "author", "root", "description", "image"]

    with open(file_path, 'r') as f:
        content = f.read()
        # Find metadata section using regex
        metadata_match = re.search(r"----------metadata---------\n(.+?)\n----------metadata---------", content, re.DOTALL)
        if metadata_match:
            # Parse metadata if found
            for line in metadata_match.group(1).splitlines():
                key, value = line.split(":", 1)
                if key.strip() in validKeys:
                    if key.strip() == "root":
                        metadata[key.strip()] = value.strip().lower() == "true"
                    else:
                        metadata[key.strip()] = value.strip()

    # Set default values for missing metadata fields
    metadata.setdefault("title", file_title)  # Humanized file name
    metadata.setdefault("language", file_extension)  # File extension as language
    metadata.setdefault("version", "0.0.0")
    metadata.setdefault("author", "unknown")
    metadata.setdefault("root", False)
    metadata.setdefault("description", "")
    metadata.setdefault("image", "")
    return metadata

def compile_metadata():
    """
    Compile metadata from all script files in SCRIPTS_DIR and save to METADATA_FILE.
    Only reparse files whose last modification time has changed.
    """
    # Load existing metadata if available
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            try:
                existing_metadata = {item['name']: item for item in json.load(f)}
            except json.JSONDecodeError:
                existing_metadata = {}
    else:
        existing_metadata = {}

    metadata_list = []
    for file_name in os.listdir(SCRIPTS_DIR):
        file_path = os.path.join(SCRIPTS_DIR, file_name)
        if [file_name.endswith(ext) for ext in suported_script_langs].count(True) == 0:
            continue
        if file_name.endswith('.json') or not os.path.isfile(file_path):
            continue

        # Get the last modification time of the file
        mtime = os.path.getmtime(file_path)

        # Check if we need to reparse metadata based on mtime
        if (file_name in existing_metadata and
            existing_metadata[file_name].get("mtime") == mtime):
            # Use existing metadata entry if mtime matches
            metadata_list.append(existing_metadata[file_name])
        else:
            # Parse metadata and add mtime if the file has been modified
            metadata = parse_metadata(file_path)
            metadata["name"] = file_name
            metadata["mtime"] = mtime
            metadata_list.append(metadata)
        # Save the updated metadata list
        with open(METADATA_FILE, 'w') as f:
            json.dump(metadata_list, f, indent=4)
    return metadata_list


print("Compiling metadata...")
compile_metadata()