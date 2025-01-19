class method_oloading:
    def __init__(self, gene, race):
        self.gene = gene
        self.race = race

    def info(self):
        print(
            f"I used as an example for method overolaoding and my race is {self.race}"
        )

    def info(self, test):
        self.test = test
        print(
            f"I used as an example for method overolaoding and my race is  {self.race} and my gene belongs to {self.gene}"
        )


look1 = method_oloading("Y", "asian")
try:
    look1.info()
except TypeError as e:
    print(
        "\n We may define many methods of the same name and different arguments, but we can only use the latest defined method. Calling the other method will produce an error."
    )
