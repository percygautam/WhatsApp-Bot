# Import required packages
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.listview import ListItemButton
# import all the attributes from logic.py file
from logic import *

class GroupListButton(ListItemButton):
    pass
 
class GroupDB(BoxLayout):
 
    # Connects the value in the TextInput widget to these fields

    first_name_text_input = ObjectProperty()
    group_name_text_input=ObjectProperty()
    group_list = ObjectProperty()
    def submit_member(self):
 
        # Get the student name from the TextInputs
        group_mem_name = self.first_name_text_input.text 
        
        if(self.first_name_text_input.text!=""):

            # Add the student to the ListView
            self.group_list.adapter.data.extend([group_mem_name])
            # Reset the ListView
            self.group_list._trigger_reset_populate()
            # add the item in the list
            gpmembers.append(group_mem_name)
        self.first_name_text_input.text=""

           
    def delete_member(self, *args):
 
        # If a list item is selected
        if self.group_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.group_list.adapter.selection[0].text
 
            # Remove the matching item
            self.group_list.adapter.data.remove(selection)
            # Remove the matching item from list 
            gpmembers.remove(selection)
            # Reset the ListView
            self.group_list._trigger_reset_populate()

    def Exit_app(self):
        group_name = self.group_name_text_input.text 
        # Add the name to group name list
        gpname.append(group_name)
        # Exits the GUI after successful completion of data acquiring
        App.get_running_app().stop()
        Window.close()      # Closes the window


 
class GroupDBApp(App):
    def build(self):
        return GroupDB()

# Create the instance of the class GroupDBApp
dbApp = GroupDBApp()
dbApp.run()     # Running the app


# Print the group members inputted by GUI
print("Names of the paerticipants : ", gpmembers)
# Print the group name inputted by GUI
print("Group name: " ,gpname[0])        #if supplied with various group names first one is selected by default
# Calls the function mainfun() from logic.py
mainfun()
exit()      # Exits the process