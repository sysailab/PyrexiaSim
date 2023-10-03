from code_template import CodeTemplate
from code_generator import CodeGenerator
from model_manager import ModelManager
from script_manager import ScriptManager


script_manager = ScriptManager()
script_manager.load_script('temp_sce_ex.yaml')
sce_obj = script_manager.get_script_object()

model_manager = ModelManager(sce_obj)
model_map = model_manager.get_model_types()
instance_map = model_manager.get_model_instances()

code_tmt = CodeTemplate()
code_gen = CodeGenerator(sce_obj, model_map, instance_map, code_tmt)
code_gen.generate('../PyrexiaSim/scenarios/')