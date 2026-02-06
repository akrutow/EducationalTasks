class DevelopmentTeam:
    junior = []
    senior = []

    def add_junior(self, *args):
        for i in args:
            self.junior.append((i, 'junior'))

    def add_senior(self, *args):
        for i in args:
            self.senior.append((i, 'senior'))

    def __iter__(self):
        yield from self.junior
        yield from self.senior
