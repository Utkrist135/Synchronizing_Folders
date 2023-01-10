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
        for str in dirs_cmp.right_only:
            
            path = os.path.join(dir2,str)
            if os.path.isfile(path):
                os.remove(path)
                print("----------------Removed file at-----------")
                print(path)
            if os.path.isdir(path):
                sh.rmtree(path)
                print("---------------Removed entire directory tree at-----------")
                print(path)    
        return True
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:  
        print("mismatch or errors")          
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not are_dir_trees_equal(new_dir1, new_dir2):
            return False
    return True


src_path = 'Source'
rep_path = 'Replica'


sh.copytree(src_path, rep_path, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
print ('Copied')


src_files = set()
src_dirs = set()
rep_files = set()
rep_dirs = set()

for (dir_, _, files) in os.walk(src_path):
    for file_name in files:
        src_dirs_temp = os.path.relpath(dir_,src_path)
        src_files_temp = os.path.join(src_dirs_temp, file_name)
        src_files.add(src_files_temp)
        src_dirs.add(src_dirs_temp)

for (dir_, _, files) in os.walk(rep_path):
    for file_name in files:
        rep_dirs_temp = os.path.relpath(dir_,rep_path)
        rep_files_temp = os.path.join(rep_dirs_temp, file_name)
        rep_files.add(rep_files_temp)
        rep_dirs.add(rep_dirs_temp)        





if (are_dir_trees_equal(src_path, rep_path)):

    print ("The folders are fully synchronized")
else:
    print ("Not fully synchronised")
    
   
                    
                
        
            
        
        
    
          
                                   
    
        

        
   
 

  

