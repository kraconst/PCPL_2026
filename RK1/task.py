from operator import itemgetter

class Piece:
    def __init__(self, id, title, composer, duration, orch_id):
        self.id = id
        self.title = title
        self.composer = composer
        self.duration = duration
        self.orch_id = orch_id

    def __repr__(self):
        return '{} by {}, duration: {}'.format(
            self.title,
            self.composer,
            self.duration
        )

class Orchestra:
    def __init__(self, id, conductor, name):
        self.id = id
        self.conductor = conductor
        self.name = name

    def __repr__(self):
        return 'The {} orchestra performs under the direction of conductor {}'.format(
            self.name,
            self.conductor
        )

class Repertoire:
    def __init__(self, orch_id, piece_id):
        self.orch_id = orch_id
        self.piece_id = piece_id


orchestras = [
    Orchestra(1, 'Sokolov', 'Academic Symphony'),
    Orchestra(2, 'Morozov', 'Grand Symphony'),
    Orchestra(3, 'Lebedev', 'Astrakhan Philharmonic'),
    Orchestra(4, 'Volkov', 'Chamber Virtuosi'),
]

pieces = [
    Piece(1, 'Scheherazade', 'Rimsky-Korsakov', 42, 1),
    Piece(2, 'The Nutcracker', 'Tchaikovsky', 90, 2),
    Piece(3, 'Piano Concerto No. 2', 'Rachmaninov', 34, 2),
    Piece(4, 'The Snowstorm', 'Sviridov', 30, 3),
    Piece(5, 'Ruslan and Lyudmila Overture', 'Glinka', 5, 3),
    Piece(6, 'Symphony No. 5', 'Tchaikovsky', 45, 1),
]

repertoires = [
    Repertoire(1, 1),
    Repertoire(1, 6),
    Repertoire(1, 3),
    Repertoire(2, 2),
    Repertoire(2, 3),
    Repertoire(2, 1),
    Repertoire(3, 4),
    Repertoire(3, 5),
    Repertoire(4, 2),
    Repertoire(4, 5),
]

def main():
    one_to_many = [(piece.title, piece.composer, orch.name)
                   for orch in orchestras
                   for piece in pieces
                   if piece.orch_id == orch.id]

    many_to_many_temp = [(orch.name, rep.orch_id, rep.piece_id)
                    for orch in orchestras
                    for rep in repertoires
                    if orch.id == rep.orch_id]

    many_to_many = [(piece.title, piece.composer, orch_name)
                    for orch_name, orch_id, piece_id in many_to_many_temp
                    for piece in pieces
                    if piece.id == piece_id]

    print("task 1")
    res1 = [(title, orch_name)
            for title, composer, orch_name in one_to_many
            if composer[-2:] == 'ov']
    print(res1)

    print("task 2")
    res2_unsorted = []
    for orch in orchestras:
        durations = [piece.duration for piece in pieces if piece.orch_id == orch.id]
        if len(durations) > 0:
            res2_unsorted.append((orch.name, sum(durations) / len(durations)))

    res2 = sorted(res2_unsorted, key=itemgetter(1))
    print(res2)

    print("task 3")
    res3 = {}
    for orch in orchestras:
        if orch.name[0] == 'A':
            orch_pieces = list(filter(lambda i: i[2] == orch.name, many_to_many))
            orch_pieces_titles = [title for title, _, _ in orch_pieces]
            res3[orch.name] = orch_pieces_titles

    print(res3)

if __name__ == '__main__':
    main()
