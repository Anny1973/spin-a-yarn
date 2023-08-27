def mad_libs():
  """Creates a mad lib story."""

  adjective = input("Enter an adjective: ")
  preposition = input("Enter a preposition: ")
  noun = input("Enter a noun: ")
  verb = input("Enter a verb: ")
  adverb = input("Enter an adverb: ")
  noun2 = input("Enter a noun: ")

  story = "The quick {} {} {} {} {} the {}.".format(adjective, noun, preposition, verb, adverb, noun2)
  print(story)

if __name__ == "__main__":
  mad_libs()
