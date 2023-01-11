import shutil as sh
import os
import filecmp
import logging
import time



#Create and configure logger 
logging.basicConfig(filename="Logfile.log", 
					format='%(asctime)s %(message)s', 
					filemode='w') 


logger=logging.getLogger() 

# Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 




def are_dir_trees_equal(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal. Copy into replica / Delete from Replica

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
   """

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0:
        print('<<<---Copying the following files/folders into Replica--->>>' )
        logger.info("<<<---Copying the following files/folders into Replica--->>>")
        for str1 in dirs_cmp.left_only:
            path1 = os.path.join(dir1,str1)
            if os.path.isdir(path1):
                print("<<<---Copied Folder from Source into Replica--->>>")
                logger.info("<<<---Copied Folder from Source into Replica--->>>")
                print(path1)
                logger.info(path1)    
            if os.path.isfile(path1):
                print("<<<<<---------Copied file from Source into Replica--->>>")
                logger.info("<<<---Copied file from Source into Replica--->>>")
                print(path1)
                logger.info(path1)
           
    if len(dirs_cmp.right_only)>0:
        for str2 in dirs_cmp.right_only:
            path = os.path.join(dir2,str2)
            if os.path.isfile(path):
                os.remove(path)
                print("<<<---Removed file at--->>>")
                logger.info(" <<<---Removed file at--->>> ")
                print(path)
                logger.info(path)
            if os.path.isdir(path):
                sh.rmtree(path)
                print("<<<---Removed entire directory tree at--->>>")
                logger.info("<<<---Removed entire directory tree at--->>>")
                print(path)
                logger.info(path)  
        return True           
    if len(dirs_cmp.funny_files)>0:
        print('Some files could not be compared!!!!!!')      
        logger.warning("Some files could not be compared!!!")  
        return False
    
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not are_dir_trees_equal(new_dir1, new_dir2):
            return False
    return True



src_path = 'Source'
rep_path = 'Replica'
check = True
synchronisation_interval_in_sec = 30 
while(check):
    print('<<<--- The Synchronisation interval is '+ str(synchronisation_interval_in_sec) + 'sec')  
    if are_dir_trees_equal(src_path,rep_path) == True:
        sh.copytree(src_path, rep_path, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
        print('<<<---The folders are now synchronised!!--->>>')
        logger.info("<<<---The folders are now synchronised!!--->>>")
        
        print('Press Ctrl+C to exit the program')
        
    else:
        print('!!!!!!!!!!!!ERROR!!!!!!!!!!!!')
        logger.error("!!!!!!!!!ERROR!!!!!!!!!!!!")
        
    time.sleep(synchronisation_interval_in_sec)    
    


    
   
                    
                
        
            
        
      
                                   
    
        

        
   
 

  

