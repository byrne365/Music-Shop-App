from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import MusicShop, Base, StockItem, User

engine = create_engine('sqlite:///musicshop.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Brandon Byrne", email="byrnevideo@gmail.com",
           picture='/static/img3.jpg')
session.add(User1)
session.commit()

# stock for CoastalMusic
music_shop1 = MusicShop(user_id=1, name="Coastal Music")

session.add(music_shop1)
session.commit()

stockItem1 = StockItem(user_id=1, name="Gibson Les Paul Classic", description="A Maple and Mahogany body with a warm tone produced from the '57 Classic Zebra Coil pickups",
                     price="$2069.00", instrument="Electric Guitar", music_shop=music_shop1)

session.add(stockItem1)
session.commit()


stockItem2 = StockItem(user_id=1, name="Ibanez Left Handed Electric Cherry Burst", description="A traditionally styled guitar with 3 single coil pickups. The contoured body has a maple neck, rosewood or maple fingerboard.",
                     price="$130.99", instrument="Electric Guitar", music_shop=music_shop1)

session.add(stockItem2)
session.commit()

stockItem3 = StockItem(user_id=1, name="ESP E-II STREAM SEE THRU BLACK", description="White ash body with a flamed maple topand a rosewood fingerboard and 3 single coil pickups",
                     price="$599.50", instrument="Bass Guitar", music_shop=music_shop1)

session.add(stockItem3)
session.commit()

stockItem4 = StockItem(user_id=1, name="Takamine G-series GC18CE-NS", description="A 3/4 size guitar with a full size voice a solid spruce top in a scaled down version of the famous Takamine NEX body style,  Mahogany back and sides, rosewood fingerboard and TP4T preamp",
                     price="$245.99", instrument="Acoustic Guitars", music_shop=music_shop1)

session.add(stockItem4)
session.commit()

stockItem5 = StockItem(user_id=1, name="Chord Mini D tambourine", description="Mini tambourine, dark blue",
                     price="$4.99", instrument="Percussion", music_shop=music_shop1)

session.add(stockItem5)
session.commit()

stockItem6 = StockItem(user_id=1, name="Chord Jingle Stick", description="6 pairs of steel tambourine jingles on a moulded plastic shacker stick. The handle has a foam grip for comfort and control.",
                     price="$10.99", instrument="Percussion", music_shop=music_shop1)

session.add(stockItem6)
session.commit()

stockItem7 = StockItem(user_id=1, name="Takamine TB 10", description="This fretless instrument produces a tone heavy and fundamental with the rich harmonics you would expect from an upright bass.",
                     price="$689.99", instrument="Acoustic Bass", music_shop=music_shop1)

session.add(stockItem7)
session.commit()

stockItem8 = StockItem(user_id=1, name="Medeli GRAND1000-GB Grand Piano", description="Grand1000 brings the most stunning realistic Piano sounds. It features the world acclaimed Fatar keybed to provide the real touch of a piano",
                     price="$4079.95", instrument="Electric Piano", music_shop=music_shop1)

session.add(stockItem8)
session.commit()

stockItem9 = StockItem(user_id=1, name="Alesis Crimson Mesh Kit", description="A five-piece electronic drum kit featuring exclusive Alesis mesh drum heads (Patent Pending) that delivers the perfect feel and expression",
                     price="$1191.99", instrument="Electric Drum Kits", music_shop=music_shop1)

session.add(stockItem9)
session.commit()


# stock for Toms Drum Music Shop
music_shop2 = MusicShop(user_id=1, name="Toms Drum Music Shop")

session.add(music_shop2)
session.commit()

stockItem11 = StockItem(user_id=1, name="MEINL Aluminum Darbukas", description="The hand engraved shell will get all the attention thanks to its look and sound",
                     price="$79.99", instrument="Drum", music_shop=music_shop2)

session.add(stockItem11)
session.commit()

stockItem12 = StockItem(user_id=1, name="Pearl Primero Fiber Conga Set",
                     description=" Available in your choice of Hand-selected Thai oak or Hand-layered fiberglass. Only the finest materials are used to create Primero congas", price="$433.15", instrument="Drum", music_shop=music_shop2)

session.add(stockItem12)
session.commit()

stockItem13 = StockItem(user_id=1, name="DB Percussion DCBS1018 Cymbal Boom Stand", description="Double braced cymbal boom stand.",
                     price="$37.55", instrument="Drum Hardware", music_shop=music_shop2)

session.add(stockItem13)
session.commit()

stockItem14 = StockItem(user_id=1, name="DB Percussion DHS616 Hi-Hat Stand", description="Double braced hi-hat stand",
                     price="$53.20", instrument="Drum Hardware", music_shop=music_shop2)

session.add(stockItem14)
session.commit()

stockItem15 = StockItem(user_id=1, name="DB Percussion DBU-01 Drum Brushes", description="DBU-01 Jazz Drum Brushes - black",
                     price="$12.10", instrument="Drum Sticks", music_shop=music_shop2)

session.add(stockItem15)
session.commit()

stockItem16 = StockItem(user_id=1, name="Zildjian SDSP216 STICKS AND PRACTICE PAD PACK", description="This pack is ideal for the beginner,intermediate, professional drummer. consists of 2 x pairs 5ANN sticks and a Zildjian practice pad.",
                     price="$27.30", instrument="Drum Sticks", music_shop=music_shop2)

session.add(stockItem16)
session.commit()


# stock for Kleens Piano Music Shop
music_shop3 = MusicShop(user_id=1, name="Kleens Piano Music Shop")

session.add(music_shop3)
session.commit()


stockItem17 = StockItem(user_id=1, name="Casio CTK-1200/1250 61 Keyboard", description="61 piano-style keys that are virtually the same size of acoustic piano keys, 100 quality tones, 100 versatile rhythms with auto-accompaniment and 100 Song Bank tunes",
                     price="$808.99", instrument="Digital Piano", music_shop=music_shop3)

session.add(stockItem17)
session.commit()

stockItem18 = StockItem(user_id=1, name="Korg Krome 61", description="Offering full-length, unlooped samples of every key for a spectacular piano sound, this new keyboard redefines your expectations for an instrument in this class.",
                     price="$1987.99", instrument="Digital Piano", music_shop=music_shop3)

session.add(stockItem18)
session.commit()

stockItem19 = StockItem(user_id=1, name="Korg Krome 73", description="Offering full length, unlooped samples of every key for a spectacular piano sound, this new keyboard redefines your expectations for an instrument in this class. Taking its name from the Greek word meaning color KROME is the new standard for sonic excellence in a gigging musicians keyboard",
                     price="$2237.95", instrument="Digital Piano", music_shop=music_shop3)

session.add(stockItem19)
session.commit()

stockItem20 = StockItem(user_id=1, name="Alesis CODA Pro 88 Key Digital Piano", description="The Alesis Coda and Coda Pro are full-featured 88-key digital pianos that have the versatility and rich sound youre looking for.",
                     price="$1056.99", instrument="Digital Piano", music_shop=music_shop3)

session.add(stockItem20)
session.commit()


# stock for Pavillion Music Shop
music_shop4 = MusicShop(user_id=1, name="Pavillion Music Shop")

session.add(music_shop4)
session.commit()


stockItem21 = StockItem(user_id=1, name="Sandner 4/4 Cello", description="Handmade cello,selected at least 3 years dry spruce top,maple back and side with clear flame,hand made workmanship and varnish,ebony fittings, BAUSCH bridge.Outfit: (with Bow B-27, Case SA-560).",
                     price="$1112.99", instrument="Strings", music_shop=music_shop4)

session.add(stockItem21)
session.commit()

stockItem22 = StockItem(user_id=1, name="Sandner SC-2 Cello", description="Crafted cello with solid spruce top, maple back and side, Hand purfling, ebony fittings metal tail-piece. BAUSCH bridge.",
                     price="$1250.50", instrument="Strings", music_shop=music_shop4)

session.add(stockItem22)
session.commit()

stockItem23 = StockItem(user_id=1, name="Sandner RCA4 15.5 Viola",
                     description="Well flamed hard maple back, ribs and neck, solid spruce top, hand crafted of exquisite European naturally aged tone wood.", price="$609.50", instrument="Strings", music_shop=music_shop4)

session.add(stockItem23)
session.commit()

stockItem24 = StockItem(user_id=1, name="Sandner 1/2 Violin", description="An ideal starter violin or viola outfit with effortless playability and pleasant tone. Constructed of properly dried spruce and maple, and ebony fingerboard and pegs. Outfit includes a durable dart shaped case and half-mounted Brazilwood bow.",
                     price="$226.95", instrument="Strings", music_shop=music_shop4)

session.add(stockItem24)
session.commit()

stockItem25 = StockItem(user_id=1, name="Sandner 3/4 Violin", description="Size: 3/4 with a Matt varnish / Polished varnish, Ebony pegs, Carbon tailpiece, Chinrest & Endpin are jujube in black Outfit with bow and case. A basic model with good quality for student",
                     price="$229.95", instrument="Strings", music_shop=music_shop4)

session.add(stockItem25)
session.commit()

print "added item to Stock!"