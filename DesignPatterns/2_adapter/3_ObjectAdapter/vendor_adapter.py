from abstract_adapter import AbstractAdapter

class VendorAdapter(AbstractAdapter):
    @property
    def name(self):
        return self.adapt.name

    @property
    def address(self):
        return '{} {}'.format(
            self.adapt.number,
            self.adapt.street
        )
