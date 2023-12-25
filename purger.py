from datetime import date, datetime
import os, sys, glob, pprint

def delta_date (days_for_purging):
    from datetime import datetime, timedelta
    today = datetime.today()
    date_for_purging_from = today - timedelta(days=days_for_purging)
    return (date_for_purging_from)

def building_dictionary (files_list):
    files_dictionary_arry = []
    for each_item in files_list:
        full_path = os.path.join(userinput_path, each_item)
        creation_date = os.path.getmtime(full_path)
        files_dictionary = {"file":each_item,"date":datetime.fromtimestamp(creation_date)}
        files_dictionary_arry.append(files_dictionary)
    return (files_dictionary_arry)

def deletion_dictionary_function (files_dictionary_arry):
    files_for_deletion_dictionary_array =[]
    for eachitem in files_dictionary_arry:
        if delta_date (days_for_purging) >= eachitem["date"]:
            files_for_deletion_dictionary = {"file":eachitem["file"],"date":eachitem["date"]}
            files_for_deletion_dictionary_array.append(files_for_deletion_dictionary)
    return (files_for_deletion_dictionary_array)

def delete_all_function(deletion_dictionary_array):
    pprint.pprint (deletion_dictionary_array)
    for eachitem in deletion_dictionary_array:
        try:
            os.remove(eachitem["file"])
        except:
            pass
    sys.exit ("All the files have been deleted")


userinput_path = input ("type your path\n")
days_for_purging = int (input("Type days for purging\n"))    
files_list = glob.glob(userinput_path + '/**/*', recursive=True)
files_dictionary_arry = building_dictionary (files_list)


if not deletion_dictionary_function (files_dictionary_arry):
        sys.exit("No files to delete. Exiting from Purger program")
else:
    for eachitem in deletion_dictionary_function (files_dictionary_arry):
        areyousure_input = input("Are you sure you want to delete " + str(eachitem["file"]) + " ?\n")
        while ((areyousure_input != 'a') and (areyousure_input != 'n') and (areyousure_input !='y')):
            print ("Unsupported value, please try again")
            areyousure_input = input("Are you sure you want to delete " + str(eachitem["file"]) + " ?\n")
        if areyousure_input == 'y':
            try:
                os.remove(eachitem["file"])
            except:
                pass
                os.rmdir(eachitem["file"])
        elif areyousure_input == 'a':
            deletion_dictionary_array = deletion_dictionary_function (files_dictionary_arry)
            delete_all_function (deletion_dictionary_array)
        else :
            sys.exit("You have exited from Purger program")

