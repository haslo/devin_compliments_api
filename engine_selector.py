from itertools import cycle

class EngineSelector:
    def __init__(self, engine_classes):
        self.engine_classes = engine_classes
        self.engine_cycle = cycle(self.engine_classes)
        self.engine_selection_tracker = {engine_class.__name__: 0 for engine_class in self.engine_classes}

    def get_next_engine(self):
        engine_class = next(self.engine_cycle)
        # Added print statement for debugging
        print(f"Selected engine: {engine_class.__name__}")
        self.engine_selection_tracker[engine_class.__name__] += 1
        return engine_class

    def get_engine_usage_stats(self):
        return self.engine_selection_tracker
