
def read_seat(seat):
    x1, x2, mid_x = 0, 127, 0
    y1, y2, mid_y = 0, 7, 0

    for letter in seat:
        if letter == "F":
            mid_x = (x1 + x2) // 2
            x2 = mid_x
        elif letter == "B":
            mid_x = (x1 + x2) // 2 + 1
            x1 = mid_x
        elif letter == "L":
            mid_y = (y1 + y2) // 2
            y2 = mid_y
        elif letter == "R":
            mid_y = (y1 + y2) // 2 + 1
            y1 = mid_y

    return mid_x, mid_y, mid_x * 8 + mid_y
    

def five_a():
    with open("input_5.txt", "r") as f:
        line = f.readline()
        max_seat_id = 0
        while line:
            row, col, seat_id = read_seat(line)
            if seat_id > max_seat_id:
                max_seat_id = seat_id
            line = f.readline()
        return max_seat_id

def five_b():
    all_the_seats = {}
    for i in range(128):
        for j in range(8):
            all_the_seats[(i, j)] = True
    with open("input_5.txt", "r") as f:
        line = f.readline()
        while line:
            row, col, seat_id = read_seat(line)
            del all_the_seats[(row, col)]
            line = f.readline()
    # remove the fictious seats in the front and back
    cnt_front = 0
    cnt_back = 127
    while True:
        found = False
        found_back = False
        if (cnt_front, 0) in all_the_seats:
            for i in range(8):
                if (cnt_front, i) in all_the_seats:
                    del all_the_seats[(cnt_front, i)]
            cnt_front += 1
            found = True
        for i in range(8):
            if (cnt_back, i) in all_the_seats:
                del all_the_seats[(cnt_back, i)]
                found_back = True
        if found_back:
            cnt_back -= 1
        
        if not found and not found_back:
            break
    
    seat_id = 0
    for k in all_the_seats.keys():
        seat_id = k[0] * 8 + k[1]
    return seat_id

print(five_b())