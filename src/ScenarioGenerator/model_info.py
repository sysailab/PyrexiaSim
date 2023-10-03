
class ModelInfo:
	def __init__(self, model_type, in_ports, out_ports):
		self.model_type = model_type
		self.in_ports = in_ports
		self.out_ports = out_ports

	def get_model_type(self):
		return self.model_type

	def get_in_ports(self):
		return self.in_ports

	def get_out_ports(self):
		return self.out_ports

class InstanceInfo:
	def __init__(self, model_type, model_uri, imported_uri):
		self.model_type = model_type
		self.model_uri = model_uri
		self.imported_uri = imported_uri
		pass

	def get_model_uri(self):
		return self.model_uri

	def get_imported_uri(self):
		return self.imported_uri