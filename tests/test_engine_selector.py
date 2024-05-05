from engine_selector import EngineSelector

class TestEngineSelector(EngineSelector):
    def __init__(self, engine_classes):
        super().__init__(engine_classes)
        self.engine_usage_count = {}

    def get_next_engine(self):
        engine_class = super().get_next_engine()
        engine_name = engine_class.__name__
        if engine_name not in self.engine_usage_count:
            self.engine_usage_count[engine_name] = 0
        self.engine_usage_count[engine_name] += 1
        return engine_class

    def get_engine_usage_stats(self):
        return self.engine_usage_count
