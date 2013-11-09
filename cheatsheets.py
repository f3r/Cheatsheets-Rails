import sublime_plugin, os
  
class CheatSheetRailsCommand(sublime_plugin.WindowCommand):  
    def run(self, filename):  
        self.window.open_file(os.path.join(os.path.dirname(__file__), "cheatsheets/"+filename))
