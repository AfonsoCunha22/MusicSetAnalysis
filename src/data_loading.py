import os
import shutil
import kagglehub

# Processed data
def download_data():
    try:
        # Download latest version
        path = kagglehub.dataset_download("imsparsh/musicnet-dataset")
        print("Path to dataset files:", path)
        return path
    except Exception as e:
        print(f"Error downloading or loading data: {e}")
        return None


def move_data(source_directory, target_directory):
    try:
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        for file in os.listdir(source_directory):
            source_file = os.path.join(source_directory, file)
            target_file = os.path.join(target_directory, file)
            if os.path.isfile(source_file):
                shutil.move(source_file, target_file)
            else:
                shutil.move(source_file, target_directory)
            
        print("Data moved successfully")

    except Exception as e:
        print(f"Error moving data: {e}")

def main():
    dataset_path = download_data()
    if dataset_path:
        target_directory = "data/raw"
        move_data(dataset_path, target_directory)


if __name__ == "__main__":
    main()
