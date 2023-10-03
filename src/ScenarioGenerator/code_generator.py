'''
Code Generator for Scenario Generator
'''

from pathlib import Path
import pprint
class CodeGenerator:
	def __init__(self, sce_obj, model_types, instances, code_tmt):
		pprint.pprint(sce_obj)
		#self.scenario_sim_config = sce_obj['SimConfig']
		self.scenario_variation = sce_obj['Variations']
		self.participate_models = model_types
		self.model_instances = instances
		self.code_template = code_tmt
	
	def write_line(self, f, content=""):
		f.write(content)
		f.write("\n")

	def generate(self, _path):
		dir = Path(_path)
		for var in self.scenario_variation:
			for rseed in range(var['rand_seed'][0], var['rand_seed'][1]):
				file_name = f"{dir/var['name']}_{rseed}.py"
				with open(file_name, 'w') as f:
					self.generate_prefix(f, var['ex_mode'], var['time_res'])
					for model in var['models']:
						self.generate_model(f, model)
					
					for relation in var['couplings']:
						self.generate_coupling(f, relation)
					self.generate_postfix(f)
	
	def generate_prefix(self, f, mode, t_res):
		self.write_line(f, self.code_template.env_setup)
		sim_init = self.code_template.simulator_initalize.format(
			sim_name=self.code_template.simulator_name,
			eng_name=self.code_template.engine_name,
			mode=mode,
			t_res=t_res)
		self.write_line(f, sim_init)
		self.write_line(f)

	def generate_postfix(self, f):
		self.write_line(f, f"{self.code_template.simulator_name}.get_engine('{self.code_template.engine_name}').simulate()")
		self.write_line(f)

	def generate_model(self, f, model):
		content = self.code_template.model_restore.format(
			model_uri=self.model_instances[model['name']].get_model_uri(),
			depend_uri=self.model_instances[model['name']].get_imported_uri(),
			model_name=model['name'],
			sim_name=self.code_template.simulator_name,
			eng_name=self.code_template.engine_name,
			init_time=model['init_time'],
			dest_time=model['destroy_time']
			)
		self.write_line(f, content)
		self.write_line(f)

	def generate_coupling(self, f, relation):
		content = self.code_template.coupling_relation.format(
			sim_name=self.code_template.simulator_name,
			eng_name=self.code_template.engine_name, 
			src_name=relation['src_name'],
			src_port=relation['src_port'],
			dst_name=relation['dst_name'],
			dst_port=relation['dst_port'],
			)
		self.write_line(f, content)
		self.write_line(f)
