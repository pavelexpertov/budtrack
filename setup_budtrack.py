'''Purpose of the script is to set up what's necessary to run the
program.
Keep in mind that you will have to install module dependencies (via
requirements.txt) separately.
Furthermore, you need to run the script as a user
'''

import os
import shutil, errno

def check_and_create_folder(given_directory_path):
    '''Check if a given directory path doesn't exist and create it.'''
    directory_path = os.path.expanduser(given_directory_path)
    directory_exists = os.path.exists(directory_path)
    if not directory_exists:
        os.mkdir(directory_path)


def create_hidden_budtrack_folder():
    '''Create '~/.budtrack' folder if it doesn't exist.'''
    check_and_create_folder("~/.budtrack")


def create_bin_folder():
    '''Create '~/bin' folder if it doesn't exist.'''
    check_and_create_folder("~/bin")


def copy_folder_to_destination(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise


def copy_budtrack_folder_to_usr_bin():
    '''Copy contents of 'budtrack' source folder to '/usr/bin'.'''
    budtrack_directory_path = os.path.join(os.getcwd(), "budtrack")
    installation_path = os.path.join("/usr/bin", "budtrack")
    budtrack_exists_in_usr_bin = os.path.exists(installation_path)
    if budtrack_exists_in_usr_bin:
        shutil.rmtree(installation_path)
    copy_folder_to_destination(budtrack_directory_path,
                               installation_path)


def create_sym_link_to_the_file():
    '''Create a symbolic link to the program.'''
    main_file_path = os.path.join("/usr/bin", "budtrack/budtrack.py")
    symlink_main_file_path = os.path.expanduser("~/bin/budtrack")
    os.symlink(main_file_path, symlink_main_file_path)


if __name__ == "__main__":
    create_hidden_budtrack_folder()
    create_bin_folder()
    copy_budtrack_folder_to_usr_bin()
    create_sym_link_to_the_file()
