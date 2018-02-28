class UnpickleModelException(Exception):
    def __init__(self, model_id, host, error_text):
        self.text = "Error loading model %s host %s" % (model_id, host)
        self.error_text = error_text

    def __str__(self):
        return self.text
