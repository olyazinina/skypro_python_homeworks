from user import User
from card import Card

Kelly = User("Kelly")

Kelly.sayName()
Kelly.setAge(33)
Kelly.sayAge()

card = Card("1234 9876 4567 8475", "11/25", "Kelly M")
card.pay(1000)