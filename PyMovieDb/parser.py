import html
# for manipulate incoming data/json from IMDB (for invalid json string)
class ImdbParser:
    """
      - A class to manipulate incoming json object data of a movie/TV from IMDB.
      - Changes are required as sometimes the json contains escaped quotes that should be unescaped
    """
    def __init__(self, json_obj):
        self.json_obj = json_obj
        self.visited = set()
        
    @property
    def unescape_json_values(self):
        """
        Unescape all json values in a json object
        """
        if id(self.json_obj) in self.visited:
            return self.json_obj

        self.visited.add(id(self.json_obj))

        if isinstance(self.json_obj, dict):
            for key, value in self.json_obj.items():
                if isinstance(value, str):
                    self.json_obj[key] = html.unescape(value).replace("\n", " ").replace("  ", " ")
                elif isinstance(value, (dict, list)):
                    self.json_obj[key] = ImdbParser(value).unescape_json_values

        elif isinstance(self.json_obj, list):
            for i, value in enumerate(self.json_obj):
                if isinstance(value, str):
                    self.json_obj[i] = html.unescape(value).replace("\n", " ").replace("  ", " ")
                elif isinstance(value, (dict, list)):
                    self.json_obj[i] = ImdbParser(value).unescape_json_values

        return self.json_obj
