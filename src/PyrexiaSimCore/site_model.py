from pyevsim import BehaviorModelExecutor, SysMessage
from pyevsim.definition import Infinite
import datetime

import random
'''
site_info = {
	"site_id":"vision1",
	"work_intensity": 2,
	"temperature":29.9,
	"noise":1,
	"specifics":{
		"space": "open",
		"type": "independent"
	}
}

site_sim_info = {
	"temp_model_type": 0,
	"temp_model_seed": 0,
	"noise_model_type": 0,
	"noise_model_seed": 0
}
'''

class SiteModel(BehaviorModelExecutor):
	'''
	Model that Simulates Site's Status
	'''
	def __init__(self, inst_time, dest_time, model_name, engine_name, site_info, site_sim_info):
		BehaviorModelExecutor.__init__(self, inst_time, dest_time, model_name, engine_name)
		self.init_state("Update")
		self.insert_state("Update", 1) # Update Frequency

		self.insert_output_port("out") # Broadcast event to connected agents

		self.site_info = site_info
		self.temp_model = self.get_temp_model(site_sim_info["temp_model_type"], site_sim_info["temp_model_seed"])
		self.noise_model = self.get_noise_model(site_sim_info["noise_model_type"], site_sim_info["noise_model_seed"])

	def ext_trans(self,port, msg):
		return

	def output(self):
		# Usage 
		# self.temp_model.get_value(10)
		# self.noise_model.get_value(10)
		
		return None
		
	def int_trans(self):
		if self._cur_state == "Update":
			self._cur_state = "Update"

	def get_temp_model(self, _type, _seed):
		if _type == 0:
			class gen:
				def __init__(self):
					self.rand = random.Random(_seed)

				def get_value(self, current_temp):
					return current_temp + self.rand.randint(-3, 3)
			return gen()

	def get_noise_model(self, type, seed):
		if type == 0:
			class gen:
				def __init__(self):
					self.rand = random.Random(seed)

				def get_value(self, current_temp):
					return current_temp + self.rand.randint(-1, 1)
			return gen()

if __name__ == "__main__":
	from pyevsim import SystemSimulator

	ss = SystemSimulator()
	ss.register_engine("first", "REAL_TIME", 1)

	gen = SiteModel(0, Infinite, "Gen", "first", {}, {
		"temp_model_type": 0,
		"temp_model_seed": 0,
		"noise_model_type": 0,
		"noise_model_seed": 0
	})
	ss.get_engine("first").register_entity(gen)
	ss.get_engine("first").simulate()