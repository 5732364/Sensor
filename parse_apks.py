import os
import subprocess

def parse_apks_in_current_dir():

    for file in os.listdir():
        if file.endswith(".apk") or file.endswith(".xapk"):
            apk_path = os.path.abspath(file)
            output_dir = os.path.join(os.getcwd(), file.replace(".apk", "").replace(".xapk", ""))

            #command = f"d:\\tools\\apktool\\apktool d -f \"{apk_path}\" -o {output_dir}"
            #command = f"d:\\tools\\apktool\\apktool d -f \"{apk_path}\" "
            command = f"d:\\tools\\jadx\\bin\\jadx -d \"{output_dir}\" \"{apk_path}\" "
            try:
                subprocess.check_call(command, shell=True)
                print(f"Successful {apk_path} to {output_dir}")
            except subprocess.CalledProcessError as e:
                print(f"decompile {apk_path} failed: {e}")

if __name__ == "__main__":
    parse_apks_in_current_dir()