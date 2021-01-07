class Steckerbrett:
    data = None

    def __init__(self, data=None):
        if data is None:
            self.data = {" ": " "}
        else:
            try:
                if type(data) is not dict:
                    raise Exception('Steckerbrett formatuma nem megfelelo!')
                else:
                    self.data = data
            except Exception as e:
                print("Hiba a steckerbrett inicializalasa soran!", e)