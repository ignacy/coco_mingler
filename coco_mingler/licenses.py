class Licenses:
    def __init__(self, data):
        self.licenses_dict = {}
        for license in data:
            self.licenses_dict[license["id"]] = license

    def get(self, license_id):
        if license_id not in self.licenses_dict:
            return None
        else:
            return self.licenses_dict[license_id]
