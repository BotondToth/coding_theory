from string import ascii_lowercase
from steckerbrett import Steckerbrett

DEFAULT_STECKERBRETT = Steckerbrett


class Enigma:
    def __init__(self, steckerbrett_data=DEFAULT_STECKERBRETT.data, alpha=0, beta=0, gamma=0):
        self.alphabet = list(ascii_lowercase)
        self.steckerbrett = steckerbrett_data

        if alpha is not None and beta is not None and gamma is not None:
            self.alpha = alpha
            self.beta = beta
            self.gamma = gamma

        # Parok letrehozasa a kapcsolotablaban
        for letter in list(self.steckerbrett.keys()):
            if letter in self.alphabet:
                self.alphabet.remove(letter)
                self.alphabet.remove(self.steckerbrett[letter])
                self.steckerbrett.update({self.steckerbrett[letter]: letter})

        # forditott abc
        self.reflector = [let for let in reversed(self.alphabet)]

    """ Fordit a rotorokon a szabaly szerint:
        1. Alfa rotort tekerjuk
        2. Ha alfa korbeert, beta rotort tekerjuk, alfat alaphelyzetbe allitjuk
        3. Ha beta korbeert, gammat tekerjuk (ilyenkor betat is kell!)
    """
    def rotate(self):
        self.alpha += 1
        if self.alpha % len(self.alphabet) == 0:
            self.beta += 1
            self.alpha = 0
        if self.beta % len(self.alphabet) == 0:
            # and self.alpha % len(self.alphabet) != 0 and self.beta >= len(self.alphabet) - 1
            self.gamma += 1
            self.beta = 1

    """ Parameterben kapott rotor abc-t permutalja """
    def permutate_rotor(self, rotor):
        altered_alphabet = list(''.join(self.alphabet))
        for i in range(rotor):
            altered_alphabet.insert(0, altered_alphabet[len(altered_alphabet) - 1])
            altered_alphabet.pop()
        return altered_alphabet

    """ Parameterben kapott rotor abc-t hatrafele permutalja """
    def inverse_permutate_rotor(self, rotor):
        altered_alphabet = list(''.join(self.alphabet))
        for i in range(rotor):
            altered_alphabet.append(altered_alphabet[0])
            altered_alphabet.pop(0)
        return altered_alphabet

    """ Parameterben kapott betut viszi keresztul a kapott rotoron"""
    def encrypt_letter(self, rotor, letter):
        return self.permutate_rotor(rotor)[self.alphabet.index(letter)]

    """ Parameterben kapott betut viszi keresztul a kapott rotoron (hatrafele fordit)"""
    def inverse_encrypt_letter(self, rotor, letter):
        return self.inverse_permutate_rotor(rotor)[self.alphabet.index(letter)]

    """ A kodolasi folyamatot vegzo fuggveny, kimenete a kodolt/dekodolt szoveg """
    def encrypt_text(self, text):
        encrypted_text = []
        text = text.lower()
        text.split()
        # Betunkent titkositjuk a szoveget
        for letter in text:
            if letter in self.steckerbrett:
                encrypted_text.append(self.steckerbrett[letter])
                self.rotate()
            else:
                """ --------- elso titkositas  ---------- """

                letter_on_alpha = self.encrypt_letter(self.alpha, letter)
                # print(letter, ' parja alfa rotoron: ', letter_on_alpha)
                letter_on_beta = self.encrypt_letter(self.beta, letter_on_alpha)
                # print(letter_on_alpha, ' parja beta rotoron: ', letter_on_beta)
                letter_on_gamma = self.encrypt_letter(self.gamma, letter_on_beta)
                # print(letter_on_beta, ' parja gamma rotoron: ', letter_on_gamma)
                letter_reflection = self.reflector[self.alphabet.index(letter_on_gamma)]
                # print(letter_on_gamma, ' parja: ', letter_reflection)

                """ --------- visszafele titkositas ---------- """

                letter_on_gamma_r = self.inverse_encrypt_letter(self.gamma, letter_reflection)
                # print(letter_reflection, ' parja gamma rotoron: ', letter_on_gamma_r)
                letter_on_beta_r = self.inverse_encrypt_letter(self.beta, letter_on_gamma_r)
                # print(letter_on_gamma_r, ' parja beta rotoron: ', letter_on_beta_r)
                letter_on_alpha_r = self.inverse_encrypt_letter(self.alpha, letter_on_beta_r)
                # print(letter_on_beta_r, ' parja alfa rotoron: ', letter_on_alpha_r)

                encrypted_text.append(letter_on_alpha_r)
                self.rotate()

        return ''.join(encrypted_text)


steckerbrett = Steckerbrett({'b': 'a', ' ': ' ', 'e': 'z'})
enigmaToEncrypt = Enigma(steckerbrett.data, alpha=5, beta=17, gamma=24)
enigmaToDecrypt = Enigma(steckerbrett.data, alpha=5, beta=17, gamma=24)
text_to_encrypt = raw_input('Titkositando szoveg: ')
encrypted = enigmaToEncrypt.encrypt_text(text_to_encrypt)

print(encrypted)

decrypted = enigmaToDecrypt.encrypt_text(encrypted)

print(decrypted)