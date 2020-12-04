with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def year_validator(lower_year, upper_year):
    def _validator(value):
        integer_value = int(value)
        return lower_year <= integer_value and integer_value <= upper_year
    return _validator

def dimension_validator(value):
    if value.endswith('cm'):
        integer_value = int(value[0:-2])
        return 150 <= integer_value and integer_value <= 193
    if value.endswith('in'):
        integer_value = int(value[0:-2])
        return 59 <= integer_value and integer_value <= 76
    return False

import re
def regex_validator(regex_pattern):
    compiled_matcher = re.compile(regex_pattern)
    def _validator(value):
        return True if compiled_matcher.match(value) else False
    return _validator

def fixed_value_validator(fixed_values):
    def _validator(value):
        return value in fixed_values
    return _validator

def return_true(value):
    return True

validator_map = {
    'byr': year_validator(1920, 2002),
    'iyr': year_validator(2010, 2020),
    'eyr': year_validator(2020, 2030),
    'hgt': dimension_validator,
    'hcl': regex_validator(r'^#[0-9a-f]{6}$'),
    'ecl': fixed_value_validator(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': regex_validator(r'^[0-9]{9}$'),
    'cid': return_true,
}

def get_field_map():
    return {
        'byr': False,
        'iyr': False,
        'eyr': False,
        'hgt': False,
        'hcl': False,
        'ecl': False,
        'pid': False,
        'cid': False,
    }

def tokenize(lines):
    tokens = []
    for line in lines:
        tokens.extend(line.split())
    return tokens

def parse_tokens(tokens):
    field_map = get_field_map()
    for token in tokens:
        field, value = token.split(':')
        field_map[field] = True
    return field_map

def parse_tokens_with_validation(tokens):
    field_map = get_field_map()
    for token in tokens:
        field, value = token.split(':')
        validator = validator_map[field]
        field_map[field] = validator(value)
    return field_map

def is_valid_passport(field_map):
    for field, available in field_map.items():
        if field != 'cid' and not available:
            return False
    return True

def check_valid_passport(lines):
    tokens = tokenize(lines)
    field_map = parse_tokens_with_validation(tokens)
    print(tokens)
    print(field_map)
    print(is_valid_passport(field_map))
    print(' ')
    return is_valid_passport(field_map)

valid_passport_count = 0
selected_lines = []
lines.append('')
for line in lines:
    if len(line) > 0:
        selected_lines.append(line)
    else:
        if check_valid_passport(selected_lines):
            valid_passport_count += 1
        selected_lines = []
print(valid_passport_count)