class Generator:
    @staticmethod
    def gen(numbers):
        numbers= numbers.split(",")
        mynumbers = tuple(numbers)

        return f"{numbers} {mynumbers}"

