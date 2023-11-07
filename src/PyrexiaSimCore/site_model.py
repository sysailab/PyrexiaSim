from pyevsim import BehaviorModelExecutor, SysMessage
from pyevsim.definition import Infinite
import datetime

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
		self.insert_state("Update", 1)

		self.insert_output_port("out")

		self.site_info = site_info
		self.site_sim_info = site_sim_info

	def ext_trans(self,port, msg):
		return

	def output(self):
		msg = SysMessage(self.get_name(), "out")
		print(f"[{self.get_name()}][OUT]: {datetime.datetime.now()}")
		msg.insert(f"[{self.get_name()}][OUT]: {datetime.datetime.now()}")
		return msg
		
	def int_trans(self):
		if self._cur_state == "Generate":
			self._cur_state = "Generate"