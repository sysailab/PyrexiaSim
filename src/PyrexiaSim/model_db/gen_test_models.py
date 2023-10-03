from pyevsim import BehaviorModelExecutor, SysMessage
from pyevsim.definition import Infinite
import datetime

class BaseModel(BehaviorModelExecutor):
	def __init__(self, instance_time, destruct_time, name, engine_name):
		BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
		self.init_state("Generate")
		self.insert_state("Generate", 1)

		self.insert_output_port("out")

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

class PathModel(BehaviorModelExecutor):
	def __init__(self, instance_time, destruct_time, name, engine_name):
		BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

		self.init_state("Wait")
		self.insert_state("Wait", Infinite)
		self.insert_input_port("in")

	def ext_trans(self,port, msg):
		if port == "in":
			print(f"[{self.get_name()}][IN]: {datetime.datetime.now()}")
			data = msg.retrieve()
			print(data[0])
			self._cur_state = "Wait"

	def output(self):
		return None
		
	def int_trans(self):
		if self._cur_state == "Wait":
			self._cur_state = "Wait"

import dill

if __name__ == "__main__":
	#with open('./base_model.imported', "wb") as fm:
	#	dill.dump_module(fm, refimported=True)

	p = BaseModel(0, Infinite, "BaseModel", "")
	with open("./base_model.simx", "wb") as f:		
		dill.dump(p, f)
	with open("./base_model.imported", "wb") as f:		
		dill.dump_module(f, refimported=True)

	for idx in range(1, 5):
		p = PathModel(0, Infinite, f"path_{idx}", "")
		with open(f"./path_model0{idx}.simx", "wb") as f:       
			dill.dump(p, f)
		with open(f"./path_model0{idx}.imported", "wb") as f:		
			dill.dump_module(f, refimported=True)
