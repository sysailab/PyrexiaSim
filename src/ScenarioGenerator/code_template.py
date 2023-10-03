'''
Code Template for Scenario Generator
'''


class CodeTemplate:
	def __init__(self):
		self.env_setup = "import dill\nfrom pyevsim import SystemSimulator\nfrom pyevsim.definition import Infinite"
		self.stochastic_setup = "import random\nrandom.seed({seed})"
		self.simulator_name = "ss"
		self.engine_name = "sim"
		self.simulator_initalize = "{sim_name} = SystemSimulator()" +\
								   "\n{sim_name}.register_engine('{eng_name}', '{mode}', {t_res})"
		self.model_instantiate = "from {class_file} import {class_name}\n{mod_name} = {class_name}({itime}, {dtime},'{mod_name}','{eng_name}')" +\
							  "'{sim_name}'.get_engine('{eng_name}').register_entity({mod_name})"
		self.model_restore = "with open('{depend_uri}', 'rb') as f:\n    dill.load_module(f)\n"\
							 + "with open('{model_uri}', 'rb') as f:\n    {model_name} = dill.load(f)\n"\
							 + "{model_name}._instance_t = {init_time}\n"\
							 + "{model_name}._destruct_t = {dest_time}\n"\
							 + "{sim_name}.get_engine('{eng_name}').register_entity({model_name})\n"

		self.coupling_relation = "{sim_name}.get_engine('{eng_name}').coupling_relation({src_name},'{src_port}',{dst_name},'{dst_port}')"
		self.external_input_port = "{sim_name}.get_engine('{eng_name}').insert_input_port('{port_name}')"
		self.external_intput_event = "{sim_name}.get_engine('{eng_name}').insert_external_event('{port_name}', {content})')"