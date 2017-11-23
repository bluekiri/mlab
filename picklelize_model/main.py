# coding: utf-8
import dill as pkl


class DummyModel:
    def __init__(self, random_seed):
        self.random_seed = random_seed

    def run_model(self, model_request):
        # Read model_request and do something...
        import random
        random.seed = self.random_seed
        return random.randint(1, 100)


if __name__ == "__main__":
    model = DummyModel(3)
    pkl.dump(model, open("./mlmodel.p", "wb"), protocol=3)
    print("Model exported")
