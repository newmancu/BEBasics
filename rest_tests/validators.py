from django.core import validators
from django.utils.regex_helper import _lazy_re_compile
from django.utils.translation import gettext as _

list_validator = validators.RegexValidator(
  _lazy_re_compile(r"^\[\d+(, ?\d+)*\]\Z"),
  message=_("Enter Not empty List[int]"),
  code="invalid"
) 

def validate_list(value):
  return list_validator(value)