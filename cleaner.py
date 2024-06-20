import os
import shutil

def delete_temp_files():
    temp_folder = os.environ.get('TEMP')  
    
    if temp_folder:
        print("Deleting files in the temp folder:", temp_folder)
        try:
            for filename in os.listdir(temp_folder):
                file_path = os.path.join(temp_folder, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)  
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  
                except PermissionError:
                    print(f"Permission denied: {file_path}. Skipping...")
                except FileNotFoundError:
                    print(f"File not found: {file_path}. Skipping...")
        except FileNotFoundError:
            print("Temp folder not found.")
    else:
        print("Temp folder not found in environment variables.")

if __name__ == "__main__":
    delete_temp_files()
