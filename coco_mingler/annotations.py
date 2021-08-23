class Annotations:
    def __init__(self, data):
        self.annotations_dict = {}
        for annotation in data:
            self.annotations_dict[annotation['image_id']] = annotation

    def get(self, image_id):
        return self.annotations_dict[image_id]

