

class PasswordParser:
	min: int
	max: int
	letter: str
	password: str

	def __init__(self, line: str):
		cols = line.split(" ")
		range = cols[0].split("-")
		self.min = int(range[0])
		self.max = int(range[1])
		self.letter = cols[1][0]
		self.password = cols[2]


with open("input.txt", "r") as file:
	lines = file.read().splitlines()
	valid_a = [
		pp.password
		for pp
		in [PasswordParser(line) for line in lines]
		if pp.min <= pp.password.count(pp.letter) <= pp.max
	]

	valid_b = [
		pp.password
		for pp
		in [PasswordParser(line) for line in lines]
		if (pp.password[pp.min-1] == pp.letter) != (pp.password[pp.max-1] == pp.letter)
	]

print("A: " + str(len(valid_a)))
print("B: " + str(len(valid_b)))
