import os

game_dir = r"C:\Users\508un\Documents\Programming Projects\grand-theft-git\x64\dlcpacks"
modkit_list = []

for folder_name, subfolders, files in os.walk(game_dir):
    for file in files:
        if file.endswith(".modkitid"):
            folder_name_only = os.path.basename(folder_name) 
            modkit_id = file.replace(".modkitid", "")
            modkit_list.append((folder_name_only, modkit_id))

output_file = r"C:\Users\508un\Documents\Programming Projects\grand-theft-git\Modkit Tracker\modkit_list.txt"

with open(output_file, "w") as f:
    if modkit_list:
        modkit_list.sort(key=lambda x: x[0])
        f.write("Modkit ID List:\n")
        for folder, modkit_id in modkit_list:
            f.write(f"{folder}: {modkit_id}\n")
    else:
        f.write("No modkitid files found.\n")

print(f"Modkit ID list has been saved to {output_file}")
