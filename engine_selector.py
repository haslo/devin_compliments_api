from itertools import cycle
from engines.simple_compliment_engine import SimpleComplimentEngine
from engines.feature_compliment_engine import FeatureComplimentEngine
from engines.creative_compliment_engine import CreativeComplimentEngine
from engines.imaginative_compliment_engine import ImaginativeComplimentEngine
from engines.inspirational_compliment_engine import InspirationalComplimentEngine
from engines.whimsical_compliment_engine import WhimsicalComplimentEngine
from engines.admiration_compliment_engine import AdmirationComplimentEngine
from engines.elegant_compliment_engine import ElegantComplimentEngine
from engines.short_compliment_engine import ShortComplimentEngine
from engines.personal_quality_compliment_engine import PersonalQualityComplimentEngine
from engines.metaphor_compliment_engine import MetaphorComplimentEngine
from engines.action_based_compliment_engine import ActionBasedComplimentEngine
from engines.direct_praise_compliment_engine import DirectPraiseComplimentEngine
from engines.superlative_compliment_engine import SuperlativeComplimentEngine

class EngineSelector:
    def __init__(self):
        self.engine_classes = [
            SimpleComplimentEngine,
            FeatureComplimentEngine,
            CreativeComplimentEngine,
            ImaginativeComplimentEngine,
            InspirationalComplimentEngine,
            WhimsicalComplimentEngine,
            AdmirationComplimentEngine,
            ElegantComplimentEngine,
            ShortComplimentEngine,
            PersonalQualityComplimentEngine,
            MetaphorComplimentEngine,
            ActionBasedComplimentEngine,
            DirectPraiseComplimentEngine,
            SuperlativeComplimentEngine
        ]
        self.engine_cycle = cycle(self.engine_classes)
        self.engine_selection_tracker = {engine_class.__name__: 0 for engine_class in self.engine_classes}

    def get_next_engine(self):
        engine_class = next(self.engine_cycle)
        self.engine_selection_tracker[engine_class.__name__] += 1
        return engine_class

    def get_engine_usage_stats(self):
        return self.engine_selection_tracker
