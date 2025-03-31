from homework_02.old_version.base import Vehicle
from homework_02.old_version.engine import Engine


class Car(Vehicle):
    engine: Engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine
