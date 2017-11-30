class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        li = []
        for x in self.pattern:
            if x == '.':
                li.append('dot')
            elif x == '_':
                li.append('dash')
        return ('-'.join(li))


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)
#
#
class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        return self*self