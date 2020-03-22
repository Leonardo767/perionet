class Patient:
    def __init__(self, name=None):
        self.measurements = [['0 0 0', '1 2 2']]*32
        self.missing = {3: True, 4: True, 28: True, 10: True}


def update_patient(patient_instance):
    return patient_instance
