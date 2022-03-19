from django.db import models

# Create your models here.
class Temperatures(models.Model):
    date = models.DateField("Date Created", auto_now_add=True)
    time = models.TimeField("Time Created", auto_now_add=True)
    burnerz_2 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_2A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_3 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_3A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_4 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_4A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_5 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_5A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_6 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_6A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_7 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_7A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_8 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_8A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_9 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_9A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_10 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_10A = models.IntegerField("Actual",null=True,blank=True)
    burnerz_11 = models.IntegerField("Setpoint",null=True,blank=True)
    burnerz_11A = models.IntegerField("Actual",null=True,blank=True)
    pushrate = models.FloatField("Push Rate",null=True,blank=True)
    firingcurve = models.IntegerField("Firing Curve #",null=True,blank=True)
    flashtubes = models.IntegerField("How many flash tubes?",null=True,blank=True)
    product = models.TextField("What is the product?")
    dryerexhaust = models.IntegerField("Setpoint",null=True,blank=True)
    dryerexhaustA = models.IntegerField("Actual",null=True,blank=True)
    rec_2 = models.IntegerField("Temperature",null=True,blank=True)
    rec_3 = models.IntegerField("Temperature",null=True,blank=True)
    rec_5 = models.IntegerField("Temperature",null=True,blank=True)
    rec_7 = models.IntegerField("Temperature",null=True,blank=True)
    rec_9 = models.IntegerField("Temperature",null=True,blank=True)
    rec_11 = models.IntegerField("Temperature",null=True,blank=True)
    rec_13 = models.IntegerField("Temperature",null=True,blank=True)
    rec_15 = models.IntegerField("Temperature",null=True,blank=True)
    rec_17 = models.IntegerField("Temperature",null=True,blank=True)
    rec_19 = models.IntegerField("Temperature",null=True,blank=True)
    rec_20 = models.IntegerField("Temperature",null=True,blank=True)
    rec_22 = models.IntegerField("Temperature",null=True,blank=True)
    drexh = models.IntegerField("Temperature",null=True,blank=True)
    rpdcl1 = models.IntegerField("Setpoint",null=True,blank=True)
    rpdcl2 = models.IntegerField("Setpoint",null=True,blank=True)
    rpdcl1A = models.IntegerField("Actual",null=True,blank=True)
    rpdcl2A = models.IntegerField("Actual",null=True,blank=True)
    undercarsuc = models.IntegerField("SetPoint",null=True,blank=True) 
    dampcombair = models.IntegerField("SetPoint",null=True,blank=True) 
    freshairuds = models.IntegerField("SetPoint",null=True,blank=True) 
    uds1 = models.IntegerField("SetPoint",null=True,blank=True) 
    uds2 = models.IntegerField("SetPoint",null=True,blank=True) 
    lds = models.IntegerField("SetPoint",null=True,blank=True) 
    undercarcool = models.IntegerField("SetPoint",null=True,blank=True) 
    freshairdryer = models.IntegerField("SetPoint",null=True,blank=True) 
    hotairds = models.IntegerField("SetPoint",null=True,blank=True) 
    hotairde = models.IntegerField("SetPoint",null=True,blank=True) 
    hotairdamp = models.IntegerField("SetPoint",null=True,blank=True) 
    freshairdrypress = models.IntegerField("SetPoint",null=True,blank=True) 
    uds1red = models.IntegerField("SetPoint",null=True,blank=True) 
    uds2red = models.IntegerField("SetPoint",null=True,blank=True) 
    ldsred = models.IntegerField("SetPoint",null=True,blank=True)
    undercarsucA = models.IntegerField("SetPoint",null=True,blank=True) 
    dampcombairA = models.IntegerField("SetPoint",null=True,blank=True) 
    freshairudsA = models.IntegerField("SetPoint",null=True,blank=True) 
    uds1A = models.IntegerField("Actual",null=True,blank=True) 
    uds2A = models.IntegerField("Actual",null=True,blank=True) 
    ldsA = models.IntegerField("Actual",null=True,blank=True) 
    undercarcoolA = models.IntegerField("Actual",null=True,blank=True) 
    freshairdryerA = models.IntegerField("Actual",null=True,blank=True) 
    hotairdsA = models.IntegerField("Actual",null=True,blank=True) 
    hotairdeA = models.IntegerField("Actual",null=True,blank=True) 
    hotairdampA = models.IntegerField("Actual",null=True,blank=True) 
    freshairdrypressA = models.IntegerField("Actual",null=True,blank=True) 
    uds1redA = models.IntegerField("Actual",null=True,blank=True) 
    uds2redA = models.IntegerField("Actual",null=True,blank=True) 
    ldsredA = models.IntegerField("Actual",null=True,blank=True) 
    eg1 = models.IntegerField("Setpoint",null=True,blank=True)
    eg2 = models.IntegerField("Setpoint",null=True,blank=True)
    eg3 = models.IntegerField("Setpoint",null=True,blank=True)
    egoxid = models.IntegerField("Setpoint",null=True,blank=True)
    egred = models.IntegerField("Setpoint",null=True,blank=True)
    egfan = models.IntegerField("Setpoint",null=True,blank=True)
    addairox = models.IntegerField("Setpoint",null=True,blank=True)
    addairred = models.IntegerField("Setpoint",null=True,blank=True)
    redbz11 = models.IntegerField("Setpoint",null=True,blank=True)
    eg1A = models.IntegerField("Actual",null=True,blank=True)
    eg2A = models.IntegerField("Actual",null=True,blank=True)
    eg3A = models.IntegerField("Actual",null=True,blank=True)
    egoxidA = models.IntegerField("Actual",null=True,blank=True)
    egredA = models.IntegerField("Actual",null=True,blank=True)
    egfanA = models.IntegerField("Actual",null=True,blank=True)
    addairoxA = models.IntegerField("Actual",null=True,blank=True)
    addairredA = models.IntegerField("Actual",null=True,blank=True)
    redbz11A = models.IntegerField("Actual",null=True,blank=True)
    egtemp = models.IntegerField("Temperature",null=True,blank=True)
    prefire = models.IntegerField("Temperature",null=True,blank=True)
    egprefire = models.IntegerField("Setpoint",null=True,blank=True)    
    postfire1 = models.IntegerField("Setpoint",null=True,blank=True)      
    postfire2 = models.IntegerField("Temperature",null=True,blank=True)
    postfire3 = models.IntegerField("Temperature",null=True,blank=True)
    postfire4 = models.IntegerField("Temperature",null=True,blank=True)
    undercartemp1 = models.IntegerField("Temperatures",null=True,blank=True)
    undercartemp2 = models.IntegerField("Temperatures",null=True,blank=True)
    undercartemp3 = models.IntegerField("Temperatures",null=True,blank=True)
    undercartemp4 = models.IntegerField("Temperatures",null=True,blank=True)
    hotairfromuds = models.IntegerField("Temperatures",null=True,blank=True)
    hotairfromlds = models.IntegerField("Temperatures",null=True,blank=True)
    tempcoolrec = models.IntegerField("Temperatures",null=True,blank=True)   
    user = models.CharField("User", max_length=30,null=True,blank=True)

    def __str__(self):
        return str(self.date)
        return str(self.product)