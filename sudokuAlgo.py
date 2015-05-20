def cross(row, col):
	return [r+c for r in row for c in col]


def parse_grid(grid):
	# converts a grid into a dictionary of possible values, {square:digits}
	# It returns false if a contradiction is detected
	values = dict((s, digits) for s in squares)
	for s,d in grid_values(grid).items():
		if d in digits and not assign(values, s, d):
			return False # we cant assign d to square s
	return values

def grid_values(grid):
	# converting the given grid into a dictionary of {square:digits} with '0' or '.'
	# for empty values, depending on how it is represented in the grid itself

	dict_values = [ch for ch in grid if ch in digits or ch in '0.']
	assert len(dict_values) == 81 # raises an error if total is not equal to 81
	return dict(zip(squares, dict_values))

def assign(values, s, d):
	# eliminate all values except d from values[s] and propagate. Return the values
	# return false if a contradiction is detected
	other_values = values[s].replace(d, '')
	if all(eliminate(values, s, d2) for d2 in other_values):
		return values
	else:
		return False

def eliminate(values, s, d):
	# eliminate d from values[s]. Propagate when values or places <=2.
	# return values. Return false if a contradiciton is detected
	if d not in values[s]:
		return values # already eliminated
	values[s] = values[s].replace(d, '')
	# if a square s is reduced to one values, then eliminate that from its peers
	if len(values[s])==0:
		return False # contradiciton. removed last values
	elif len(values[s])==1:
		d2 = values[s]
		if not all(eliminate(values, s2, d2) for s2 in peers[s]):
			return False
	# if a unit is reduced to only one place for d, then place it there
	for u in units[s]:
		dplaces = [s for s in u if d in values[s]]
		if len(dplaces)==0:
			return False # contradiction
		elif len(dplaces)==1:
			# d can only be in one place
			if not assign(values, dplaces[0], d):
				return False
	return values

def display(values):
	# display as a 2d grid
	width = 1+max(len(values[s]) for s in squares)
	line = '+'.join(['-'*(width*3)]*3)
	for r in rows:
		print ''.join(values[r+c].center(width)+ ('|' if c in '36' else '') for c in cols)
		if r in 'CF':
			print line

def solve(grid):
	 return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
		for d in values[s])

def some(seq):
    # return some element of seq that is true
    for e in seq:
        if e: return e
    return False




cols = '123456789'
rows = 'ABCDEFGHI'
digits = cols

squares = cross(rows, cols)

unit_list = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

units = dict((s, [u for u in unit_list if s in u]) for s in squares)
	
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)

solved_grid = solve('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
# display(solved_grid)


