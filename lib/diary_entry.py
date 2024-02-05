class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.contents_origin = contents
        

    def format(self):
        return f'{self.title}: {self.contents}'

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes
        chunk = ' '.join(self.contents.split()[:words_to_read])
        self.contents = ' '.join(self.contents.split()[words_to_read:])
        if self.contents == '':
            self.contents = self.contents_origin
        return chunk