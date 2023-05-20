class TableModel:

    # name string
    # fields map[name]type
    def __init__(self, name, fields: {}, fields_condition: {}, pk: str):
        self.name = name
        self.fields = fields  # field_name -> type
        self.fields_condition = fields_condition  # field_name -> not null / AUTOINCREMENT etc.
        self.pk = pk

    def get_name(self):
        return self.name

    def get_fields(self):
        return self.fields

    def get_pk(self):
        return self.pk
