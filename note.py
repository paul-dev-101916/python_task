class NoteType:
    note_id = None
    note_type =  None
    note_text = None

    def set_note_id(self, id):
        self.note_id = id

    def get_note_id(self):
        return self.note_id

    def set_note_type(self, type):
        self.note_type = type

    def get_note_type(self):
        return self.note_type

    def set_note_text(self, text):
        self.note_text = text

    def get_note_text(self):
        return self.note_text
