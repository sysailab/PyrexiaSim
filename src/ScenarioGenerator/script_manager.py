'''
Script Manager for Scenario Generator
'''

import yaml


class ScriptManager:
    def __init__(self):
        self.script_path = ""
        self.scenario_obj = {}

    def load_script(self, _path):
        self.file_path = _path
        with open(self.file_path) as f:
            objs = yaml.load_all(f, Loader=yaml.FullLoader)

            for obj in objs:
                self.scenario_obj.update(obj)

    def get_script_object(self):
        return self.scenario_obj


if __name__ == "__main__":
    script_manager = ScriptManager()
    script_manager.load_script("temp_sce_ex.yaml")
    print(script_manager.get_script_object())
