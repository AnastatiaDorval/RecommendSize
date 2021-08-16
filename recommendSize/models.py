from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import URLField

class Measurement(models.Model):
    name = models.CharField(max_length=100)
    cloth = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __init__(self, measName, typeCloth):
        self.name = measName
        self.cloth = typeCloth
        self.save()

    def __str__(self):
        return self.name

    def addSize(self, size, val):
        self.size = size
        self.value = val
        self.save()

class SizeGuide(models.Model):
#attributes
    measurements = models.ManyToManyField(Measurement)
    url = models.URLField
#methods
  #add sizes
    def __init__(self, url):
        self.url = url
        self.save()

    def __str__(self):
        return self.url

    def addMeasurement(self, measName, measVal, sizeName, cloth):
        meas = Measurement(measName, cloth)
        meas.addSize(sizeName, measVal)
        if meas not in self.measurements.all():
            self.measurements.add(meas)
            self.save()
        else:
            meas.delete()

    def getMeasurement(self, sizeName):
        #returns object Measurement meaning size name, measval, etc.
        return self.measurements.get(size=sizeName)

class ClothingItem(models.Model):
#attributes
    name = models.CharField(max_length=100)
    typeCloth = models.CharField(max_length=20)
    sizeguide = models.ForeignKey(SizeGuide, on_delete=CASCADE)

#methods
  #initilize clothing item with type, self, and name
    def __init__(self, name, typeCloth):
        self.name = name
        self.typeCloth = typeCloth
        self.save()

    def __str__(self):
        return self.name

    def addSizeGuide(self, url):
        self.sizeguide = SizeGuide(url)
        self.save()

class Store(models.Model):
    sizeguide = models.ForeignKey(SizeGuide, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    inventory = models.ManyToManyField(ClothingItem)
#methods
  #initilze clothing store, with self and name
    def __init__(self, name):
        self.name = name
        self.save()

    def __str__(self):
        return self.name
  #add size guide
    def addSizeGuide(self, url):
        self.sizeguide = SizeGuide(url)
        self.save()

    def addClothing(self, nameOfCloth, typeCloth):
        clothItem = ClothingItem(nameOfCloth, typeCloth)
        if clothItem not in self.inventory.all():
            self.inventory.add(ClothingItem(nameOfCloth, typeCloth))
            self.save()
        else:
            clothItem.delete()
