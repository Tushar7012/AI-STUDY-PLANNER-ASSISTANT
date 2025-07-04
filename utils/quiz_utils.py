import random
from flashcards_core import Deck, FlashCard

def create_flashcards(topic: str, items: dict[str, str]) -> Deck:
    deck = Deck(name=f"{topic} Deck")
    for question, answer in items.items():
        deck.add_card(FlashCard(prompt=question, answer=answer))
    return deck

def pick_random_questions(deck: Deck, n: int) -> list[FlashCard]:
    cards = deck.cards.copy()
    random.shuffle(cards)
    return cards[:n]
