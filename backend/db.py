from mongoengine import connect, Document, StringField, IntField, FloatField, ListField, DateTimeField

class BarHopMeta(Document):
    hopId = StringField()
    hopName = StringField()
    sll = StringField()
    ell = StringField()
    stime = DateTimeField()
    barCount = IntField()
    duration = IntField()

class HopMember(Document):
    memberId = IntField()
    memberName = StringField()
    drunkLevel = IntField()
    maxCost = IntField()
    crowdSize = IntField()
    curentHop = StringField()

class DrinkData(Document):
    drinkName = StringField()
    drinkCost = FloatField()
    alcoholVol = IntField()
    val ingredients = ListField(StringField())   

class BarData(Document):
    barId = StringField()
    barName = StringField()
    barAddress = StringField()
    barRating = StringField()
    barCost = IntField()

