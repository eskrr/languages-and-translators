class symbol:
    def __init__(self, variable_id, variable_type, variable_address, function_index):
        self.id = variable_id
        self.type = variable_type
        self.value = variable_address
        self.index = function_index