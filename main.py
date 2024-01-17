import os
from pydub import AudioSegment

def merge_audio(folder_path, output_folder):
    try:
        audio_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith((".wav", ".mp3"))]
    except FileNotFoundError:
        print(f"Error: The specified folder '{folder_path}' does not exist.")

    if not audio_files:
        print("No audio files found in the specified folder.")
        return

    output_file_name = input("Enter the name of the merged file (without extension): ")

    audio_segments = []
    for file in audio_files:
        try:
            audio_segments.append(AudioSegment.from_file(file))
        except Exception as e:
            print(f"Error reading file '{file}': {e}")

    combined = sum(audio_segments)

    output_folder_path = os.path.join(folder_path, "finished")
    os.makedirs(output_folder_path, exist_ok=True)

    output_file_path = os.path.join(output_folder_path, f"{output_file_name}.wav")
    try:
        combined.export(output_file_path, format="wav")
        print(f"Audio files merged successfully. Merged file saved at: {output_file_path}")
    except Exception as e:
        print(f"Error exporting merged file: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder containing audio files: ")

    merge_audio(folder_path, "finished")
