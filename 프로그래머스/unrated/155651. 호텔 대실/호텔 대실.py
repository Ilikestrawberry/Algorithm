def solution(book_time):
    rooms = []
    book_time = sorted([[int(n[0].split(':')[0]) * 60 + int(n[0].split(':')[1]), int(n[1].split(':')[0]) * 60 + int(n[1].split(':')[1])] for n in book_time], key=lambda x: x[0])

    for b in book_time:

        if not rooms:
            rooms.append(b[1])
            continue
        for i, r in enumerate(rooms):
            if b[0] >= (r + 10):
                rooms.remove(r)
                rooms.append(b[1])
                break
            if i == len(rooms) - 1:
                rooms.append(b[1])
                break

    return len(rooms)