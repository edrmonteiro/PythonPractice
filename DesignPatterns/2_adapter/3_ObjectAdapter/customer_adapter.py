from abstract_adapter import AbstractAdapter

class CustomerAdapter(AbsAdapter):
    def name(self):
        return self._adapt.name

    def address(self):
        return self._adapt.address
        