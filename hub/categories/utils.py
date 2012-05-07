from django.core.urlresolvers import reverse
from django.db import models
from hub.categories.models import Category

def get_category_choices(selectable_parents = False):
  groups = []
  for cat in Category.objects.filter(parent__isnull=True):
    childs = () 
    
    # Add parent to children
    if selectable_parents == True:
      childs = childs + ((str(cat.id), str(cat.title)),)
    
    # Get the children
    for child in cat.children:
      childs = childs + ((str(child.id), str(child.title)),)
    
    # Add children to there parent
    if len(childs) != 0:
      groups.append((str(cat.title), childs))
  
  return groups