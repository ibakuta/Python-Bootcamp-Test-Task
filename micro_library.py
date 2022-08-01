class MicroLibrary:
    def __init__(self, film_name, note, rating):
        self.film_name = film_name
        self.note = note
        self.rating = rating
	
    def read_notes(self, file):
        f = open(file, 'r')
        text = f.readlines()
        f.close()
        for i in text:
            print(i)

    def add_note(self, file):
        f = open(file, 'w')
        for i in self.text:
            f.write(f'{i.film_name}, {i.note}, {i.rating}')
        f.close()

    def remove_note(self, file):
        f = open(file, 'w')
        for i in text:
            f.pop(f'{self.film_name}, {i.note}, {i.rating}')
        f.close()

    def highest_rating (self):
        return max(self.note)

    def lowest_rating(self):
        return min(self.note)





    

