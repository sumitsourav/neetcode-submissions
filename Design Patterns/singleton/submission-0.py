class Singleton:
    _unique_instance = None
    _data = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._unique_instance is None:
            cls._unique_instance = super().__new__(cls)
            cls._unique_instance.value = None
        return cls._unique_instance
    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
