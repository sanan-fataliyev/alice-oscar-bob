from messaging.network import PublicNetwork, Person

alice = Person(name='Alice')
bob = Person(name='Bob')
oscar = Person(name='Oscar', is_bad_man=True)

# insecure network
internet = PublicNetwork(name="Internet")
internet.join(alice)
internet.join(oscar)  # man in the middle
internet.join(bob)


alice.send_message(bob,
                   'Hi Bob, I want to tell you our meeting place and time',
                   internet)

# now, Alice decided to use "victory" key for their next messages
alice.exchange_key_with(bob, 'victory', internet)

alice.send_message(bob,
                   'I will meet you at the central square at 3PM.',
                   internet)

bob.send_message(alice,
                 "Okay Alice, I got you. I cant wait to see you again!",
                 internet)
