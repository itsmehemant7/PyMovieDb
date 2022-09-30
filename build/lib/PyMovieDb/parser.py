# for manipulate incoming data/json from IMDB (for invalid json string)
class ImdbParser:
    """
      - A class to manipulate incoming json string data of a movie/TV from IMDB.
      - Changes are required as sometimes the json contains invalid chars in description/reviewBody/trailer schema
    """
    def __init__(self, json_string):
        self.json_string = json_string

    @property
    def remove_trailer(self):
        """
         @description:- Helps to remove 'trailer' schema from IMDB data json string.
         @returns:- New updated JSON string.
        """
        try:
            self.json_string = ''.join(self.json_string.splitlines())
            trailer_i = self.json_string.index('"trailer"')
            actor_i = self.json_string.index('"actor"')
            to_remove = self.json_string[trailer_i:actor_i:1]
            self.json_string = self.json_string.replace(to_remove, "")
        except ValueError:
            self.json_string = self.json_string
        return self.json_string

    @property
    def remove_description(self):
        """
         @description:- Helps to remove 'description' schema from IMDB file json string.
         @returns:- New updated JSON string.
        """
        try:
            review_i = self.json_string.index('"review"')
            des_i = self.json_string.index('"description"', 0, review_i)
            to_remove = self.json_string[des_i:review_i:1]
            self.json_string = self.json_string.replace(to_remove, "")
        except ValueError:
            self.json_string = self.json_string
        return self.json_string

    @property
    def remove_review_body(self):
        """
         @description:- Helps to remove 'reviewBody' schema from IMDB file json string.
         @returns:- New updated JSON string.
        """
        try:
            reviewrating_i = self.json_string.index('"reviewRating"')
            reviewbody_i = self.json_string.index('"reviewBody"', 0, reviewrating_i)
            to_remove = self.json_string[reviewbody_i:reviewrating_i:1]
            self.json_string = self.json_string.replace(to_remove, "")
        except ValueError:
            self.json_string = self.json_string
        return self.json_string

