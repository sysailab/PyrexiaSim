'''
Model Manager for Scenario Generator
'''

from model_info import InstanceInfo, ModelInfo

class ModelManager:
	def __init__(self, sce_obj):
		self.scenario_models = sce_obj['Models']
		self.instance_map = {}
		self.model_type_map = {}
		self.init_models()

	def init_models(self):
		for model in self.scenario_models:			
			self.model_type_map[model['model_type']] = ModelInfo(model['model_type'],\
													   model['in_ports'],\
													   model['out_ports'])
			for instance in model['instances']:
				self.instance_map[instance['name']] = InstanceInfo(self.model_type_map[model['model_type']],
													   instance['model_uri'],
													   instance['imported_uri'])
	
	def check_model_db(self, model):
		pass

	def get_model_types(self):
		return self.model_type_map

	def get_model_instances(self):
		return self.instance_map