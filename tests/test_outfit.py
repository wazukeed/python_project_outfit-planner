from models.outfit import Outfit


def test_outfit():

    outfit = Outfit(
        "T-shirt",
        "Jeans",
        "Nike",
        "Casual",
        "University",
        "Sunny",
        "photo.jpg"
    )

    assert outfit.top == "T-shirt"
    assert outfit.style == "Casual"


def test_to_dict():

    outfit = Outfit(
        "Hoodie",
        "Jeans",
        "Adidas",
        "Sport",
        "Walk",
        "Cold",
        "image.jpg"
    )

    data = outfit.to_dict()

    assert data["top"] == "Hoodie"
    assert data["weather"] == "Cold"