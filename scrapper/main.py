from comparator import comparator
from getUrl import getUrl as url
from sportium.scrapSportium import scrap as scrapSportium
from juegging.scrapJuegging import scrap as scrapJuegging

comparator(scrapSportium(url('sportium')), scrapJuegging(url('juegging')))