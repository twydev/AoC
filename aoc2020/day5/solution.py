with open('input.txt', 'r') as f:
    boarding_passes = f.read().splitlines()

def extract_tokens(boarding_pass):
    return boarding_pass[0:7], boarding_pass[7:]

def binary_index_finder(lowerbound_partition, lowerbound, upperbound_partition, upperbound):
    def _finder(token):
        _lowerbound, _upperbound = lowerbound, upperbound
        for partition in token:
            if partition == lowerbound_partition:
                _upperbound = (_upperbound+_lowerbound)/2
            else:
                _lowerbound = (_upperbound+_lowerbound)/2
        return _lowerbound
    return _finder

def row_finder(row_token):
    finder = binary_index_finder('F', 0, 'B', 128)
    return finder(row_token)

def column_finder(column_token):
    finder = binary_index_finder('L', 0, 'R', 8)
    return finder(column_token)

def compute_seat_id(boarding_pass):
    row_token, column_token = extract_tokens(boarding_pass)
    return int(row_finder(row_token) * 8 + column_finder(column_token))

seat_ids = [compute_seat_id(boarding_pass) for boarding_pass in boarding_passes]
print('max id', max(seat_ids))

seat_ids.sort()
counter = seat_ids[0]
for seat_id in seat_ids:
    if counter == seat_id:
        counter += 1
    else:
        print('expecting seat', counter, 'but found', seat_id)
        break
