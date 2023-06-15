class DictAverage:
    def __init__(self, new_dict):
        self.new_dict = [index for index in new_dict if isinstance(index, int)]

    def average_dict(self):
        return sum(self.new_dict) / len(self.new_dict)


def main():
    dict_1 = [1, 3, 5, "slow", 2, "what", 123, 90, (), "wddd"]
    dict_2 = DictAverage(dict_1)
    print(dict_2.new_dict, dict_2.average_dict())

if __name__ == "__main__":
    main()
