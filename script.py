#Class to model works of art
class Art:
  def __init__(self, artist, title, year, medium, owner):
    self.artist = artist
    self.title = title
    self.year = year
    self.medium = medium
    self.owner = owner
  def __repr__(self):
    return '%s. "%s". %s, %s. %s, %s.' % (self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

#Class for a marketplace to maintain the responsibility of buying, selling, listing and delisting artwork
class Marketplace:
  def __init__(self):
    self.listings = []

#Method for adding a listing
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

#Method for removing a listing
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)

#Functionality for the persual of marketplace listings
  def show_listing(self):
    for listing in self.listings:
      print(listing)

#Class for tracking clients
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = 'Private Collection'
      
#Method for selling artwork, checks if client owns the art they're trying to sell and adds the listing to the marketplace
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)

#Method for buying artwork, checkd if client does not own artwork and if listed artwork is in veneer.listings
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
#If the art is not owned but is listed, the artwork owner will change to the client doing the purchasing and the listing will be removed from the marketplace
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
                  
#Class for listing works of art
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = Client
  def __repr__(self):
    return '%s, %s' % (self.art, self.price)
