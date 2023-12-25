from datetime import datetime, timedelta
import os
import sys
import glob
import pprint

def delta_date(days_for_purging):
    """
    Calculate the date for purging based on the given number of days.

    Args:
    - days_for_purging: Number of days for purging.

    Returns:
    - Date for purging as a datetime object.
    """
    today = datetime.today()
    date_for_purging_from = today - timedelta(days=days_for_purging)
    return date_for_purging_from

def building_dictionary(files_list):
    """
    Build a list of dictionaries containing file information.

    Args:
    - files_list: List of file paths.

    Returns:
    - List of dictionaries containing file and creation date information.
    """
    files_dictionary_array = []
    for each_item in files_list:
        full_path = os.path.join(user_input_path, each_item)
        creation_date = os.path.getmtime(full_path)
        files_dictionary = {"file": each_item, "date": datetime.fromtimestamp(creation_date)}
        files_dictionary_array.append(files_dictionary)
    return files_dictionary_array

def deletion_dictionary_function(files_dictionary_array):
    """
    Create a list of files for deletion based on the purging date.

    Args:
    - files_dictionary_array: List of dictionaries containing file information.

    Returns:
    - List of dictionaries containing file and creation date for deletion.
    """
    files_for_deletion_dictionary_array = []
    for each_item in files_dictionary_array:
        if delta_date(days_for_purging) >= each_item["date"]:
            files_for_deletion_dictionary = {"file": each_item["file"], "date": each_item["date"]}
            files_for_deletion_dictionary_array.append(files_for_deletion_dictionary)
    return files_for_deletion_dictionary_array

def delete_all_function(deletion_dictionary_array):
    """
    Delete all files in the provided list and exit the program.

    Args:
    - deletion_dictionary_array: List of dictionaries containing file and creation date for deletion.
    """
    pprint.pprint(deletion_dictionary_array)
    for each_item in deletion_dictionary_array:
        try:
            os.remove(each_item["file"])
        except Exception as e:
            print(f"Error deleting file {each_item['file']}: {e}")

    sys.exit("All the files have been deleted")

# Get user input
user_input_path = input("Type your path:\n")
days_for_purging = int(input("Type days for purging:\n"))
files_list = glob.glob(user_input_path + '/**/*', recursive=True)
files_dictionary_array = building_dictionary(files_list)

# Check if there are files to delete
deletion_dictionary_array = deletion_dictionary_function(files_dictionary_array)
if not deletion_dictionary_array:
    sys.exit("No files to delete. Exiting from Purger program")
else:
    for each_item in deletion_dictionary_array:
        # Confirm deletion with the user
        are_you_sure_input = input(f"Are you sure you want to delete {each_item['file']} ? (y/n/a)\n")
        while are_you_sure_input not in ['y', 'n', 'a']:
            print("Unsupported value, please try again")
            are_you_sure_input = input(f"Are you sure you want to delete {each_item['file']} ? (y/n/a)\n")

        if are_you_sure_input == 'y':
            try:
                os.remove(each_item["file"])
            except Exception as e:
                print(f"Error deleting file {each_item['file']}: {e}")
        elif are_you_sure_input == 'a':
            delete_all_function(deletion_dictionary_array)
        else:
            sys.exit("You have exited from Purger program")
