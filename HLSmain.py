import uuid

# Generate a UUID using the uuid4() function
generated_uuid = uuid.uuid4()
uuid_string = str(generated_uuid) + "\""
header_preface = "#EXT-X-DEFINE:NAME=\"WMUUID\",VALUE=\""
header = header_preface + uuid_string  # Custom header
print("UUID Generated...\n")

insertion = "./"  # Formats m3u8 so it points to each of the 3 streams from the manifest
outputMarker = "./output_"

# Read from the "master.m3u8" file and write to the "output.m3u8" file
with open("master.m3u8", "r") as input_file, open("output.m3u8", "w") as output_file:
    for line in input_file:
        line = line.strip()
        if line.startswith("#EXT-X-VERSION"):
            line = f"{header}\n{line}"  # Add the custom header before the specific header tag
        if line.endswith(".m3u8"):
            line = f"{outputMarker}{line}"  # Add the custom header before the specific header tag
        if line.startswith("stream_0"):
            line = f"{insertion}{line}"  # Adds a ./ before the stream_0 reference, so from the manifest the stream will play
        if line.startswith("stream_1"):
            line = f"{insertion}{line}"  # Adds a ./ before the stream_1 reference, so from the manifest the stream will play
        if line.startswith("stream_2"):
            line = f"{insertion}{line}"  # Adds a ./ before the stream_2 reference, so from the manifest the stream will play
        output_file.write(line + "\n")

print("UUID inserted into output playlist.\n")
print("Output playlist paths to output stream playlists set.\n")

# The following three sections format the stream playlists, updating the references to video segments.
# The updated playlists are written to separate output files.

# Formats the stream 0 playlist so that the path points to each of the data segments for playing
insertion0 = "./stream_0/"
with open("stream_0.m3u8", "r") as input_file, open("output_stream_0.m3u8", "w") as output_file:
    for line in input_file:
        line = line.strip()
        if line.startswith("data"):
            line = f"{insertion0}{line}"  # Add the custom header before the specific header tag
        output_file.write(line + "\n")

# Formats the stream 1 playlist so that the path points to each of the data segments for playing
insertion1 = "./stream_1/"
with open("stream_1.m3u8", "r") as input_file, open("output_stream_1.m3u8", "w") as output_file:
    for line in input_file:
        line = line.strip()
        if line.startswith("data"):
            line = f"{insertion1}{line}"  # Add the custom header before the specific header tag
        output_file.write(line + "\n")

# Formats the stream 2 playlist so that the path points to each of the data segments for playing
insertion2 = "./stream_2/"
with open("stream_2.m3u8", "r") as input_file, open("output_stream_2.m3u8", "w") as output_file:
    for line in input_file:
        line = line.strip()
        if line.startswith("data"):
            line = f"{insertion2}{line}"  # Add the custom header before the specific header tag
        output_file.write(line + "\n")

print("Stream Playlists paths to video segments set.\n")

# Validate the presence of the UUID in the specified file
print("Enter filename for validation: ")
filename = str(input())
filename = filename + ".m3u8"
with open(filename, "r") as input_file:
    for line in input_file:
        line = line.strip()
        if line.startswith("#EXT-X-DEFINE"):
            print(line)
