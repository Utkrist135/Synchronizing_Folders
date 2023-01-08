import shutil as sh
import os
import filecmp

def are_dir_trees_equal(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
   """

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or \
        len(dirs_cmp.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not are_dir_trees_equal(new_dir1, new_dir2):
            return False
    return True


src_path = "Source"
rep_path = "Replica"

sh.copytree(src_path, rep_path, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
print ('Copied')


if(are_dir_trees_equal(src_path, rep_path) == False):
    src_files = []
    src_dirs = []
    rep_files = []
    rep_dirs = []
    for (src_path, directory, files) in os.walk(src_path):
        src_files.extend(files)
        src_dirs.extend(directory)
    for (rep_path, directory, files) in os.walk(rep_path):
        rep_files.extend(files)
        rep_dirs.extend(directory)
print(src_dirs)
print(src_files)   

print(rep_dirs)
print(rep_files)   

print(are_dir_trees_equal(src_path, rep_path))  

