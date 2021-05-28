from django.db import models

# Create your models here.


PROPERTY_TYPE = (
    ('PJ','Project'),
    ('BF','Builder Floor'),
)

BEDROOMS = (
    ('2','2 BHK'),
    ('3','3 BHK'),
)

PROJECT_STATUS = (
    ('R','Ready To Move'),
    ('U', 'Under Construction'),
)

AVAILIBLE = (
    ('N','New'),
    ('R','Resale'),
)

DEVELOPER = (
    ('D1','DLF'),
    ('D2','Godrej'),
    ('D3','Emaar'),
    ('D4','Shobha'),
    ('D5','Shapoorji Pallonji'),
)

SECTOR = (
    ('1','Sector-1'),('2','Sector-2'),('3','Sector-3'),('4','Sector-4'),('5','Sector-5'),('6','Sector-6'),('7','Sector-7'),
    ('8','Sector-8'),('9','Sector-9'),('10','Sector-10'),('11','Sector-11'),('12','Sector-12'),('13','Sector-13'),('14','Sector-14'),
    ('15','Sector-15'),('16','Sector-16'),('17','Sector-17'),('18','Sector-18'),('19','Sector-19'),('20','Sector-20'),('21','Sector-21'),
    ('22','Sector-22'),('23','Sector-23'),('24','Sector-24'),('25','Sector-25'),('26','Sector-26'),('27','Sector-27'),('28','Sector-28'),
    ('29','Sector-29'),('30','Sector-30'),('31','Sector-31'),('32','Sector-32'),('33','Sector-33'),('34','Sector-34'),('35','Sector-35'),
    ('36','Sector-36'),('37','Sector-37'),('38','Sector-38'),('39','Sector-39'),('40','Sector-40'),('41','Sector-41'),('42','Sector-42'),
    ('43','Sector-43'),('44','Sector-44'),('45','Sector-45'),('46','Sector-46'),('47','Sector-47'),('48','Sector-48'),('49','Sector-49'),
    ('50','Sector-50'),('51','Sector-51'),('52','Sector-52'),('53','Sector-53'),('54','Sector-54'),('55','Sector-55'),('56','Sector-56'),
    ('57','Sector-57'),('58','Sector-58'),('59','Sector-59'),('60','Sector-60'),('61','Sector-61'),('62','Sector-62'),('63','Sector-63'),
    ('64','Sector-64'),('65','Sector-65'),('66','Sector-66'),('67','Sector-67'),('68','Sector-68'),('69','Sector-69'),('70','Sector-70'),
    ('71','Sector-71'),('72','Sector-72'),('73','Sector-73'),('74','Sector-74'),('75','Sector-75'),('76','Sector-76'),('77','Sector-77'),
    ('78','Sector-78'),('79','Sector-79'),('80','Sector-80'),('81','Sector-81'),('82','Sector-82'),('83','Sector-83'),('84','Sector-84'),
    ('85','Sector-85'),('86','Sector-86'),('87','Sector-87'),('88','Sector-88'),('89','Sector-89'),('90','Sector-90'),('91','Sector-91'),
    ('92','Sector-92'),('93','Sector-93'),('94','Sector-94'),('95','Sector-95'),('96','Sector-96'),('97','Sector-97'),('98','Sector-98'),
    ('99','Sector-99'),('100','Sector-100'),('101','Sector-101'),('102','Sector-102'),('103','Sector-103'),('104','Sector-104'),
    ('105','Sector-105'),('106','Sector-106'),('107','Sector-107'),('108','Sector-108'),('109','Sector-109'),('110','Sector-110'),
    ('111','Sector-111'),('112','Sector-112'),('113','Sector-113'),('114','Sector-114'),('115','Sector-115'),
    )

#class Property(models.Model):
#    type = models.CharField(choices=PROPERTY_TYPE, max_length=2)

class Project(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    developer = models.CharField(choices=DEVELOPER , max_length=50) # Auto Choice
    sector = models.CharField(choices=SECTOR, max_length=3) # Auto Choic
    bedrooms = models.CharField(choices=BEDROOMS, max_length=1)
    status = models.CharField(choices=PROJECT_STATUS , max_length=1)
    availible = models.CharField(choices=AVAILIBLE , max_length=1,default="")
    #size  =
    #location =
    #microMarket =
    #catergory =
    #P_DATE = models.DateField()
    #gated =
    #parking =
    #power backup =
    # Extra Project Fields
    #area =
    #towers =
    #floors =
    #units =

    def __str__(self):
        return self.title

class Builder_Floor(models.Model):
    #id =
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sector = models.CharField(choices=SECTOR, max_length=3) # Auto Choice
    bedrooms = models.CharField(choices=BEDROOMS, max_length=1)
    status = models.CharField(choices=PROJECT_STATUS , max_length=1)
    availible = models.BooleanField(default=True)
    #location =
    #microMarket =
    #size  =
    #gated =
    #parking =
    #power backup =

    def __str__(self):
        return self.title
