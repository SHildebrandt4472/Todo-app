#
# HTML Helper functions
#

from flask import url_for , request
from markupsafe import Markup
import datetime
#from app.utils.misc import tz_offset, utc_to_aiclocal, utc_to_user_local, get_localtime, get_user_timezone

display_timezones = False  # should be user pref

#
# General Text Formatting
#

def display_if(cond,t,f=''):
  if cond:
    return t
  return f

def fmt_val(val, dp):
  return f"{val:.{dp}f}"

def pluralise(word, cnt, suffix="s"):
  n = int(cnt)
  if n == 1 or n == -1:
    return(word)
  else:
    return(word+suffix)

#
# UTC Date Time Routines
#
def fmt_date(dt):
  if not isinstance(dt, datetime.datetime):
    return ''
  return dt.strftime("%d %b %y")

def fmt_datetime(dt, include_tz=False):
  if not isinstance(dt, datetime.datetime):
    return ''

  if include_tz:
    return dt.strftime("%d %b %Y, %H:%M:%S (%Z)")
  else:
    return dt.strftime("%d %b %Y, %H:%M:%S")

#
# HTML Generators
#

def link_to_url(link_text, url, attr={}):
  html_attr = ''
  for key, value in attr.items():
    html_attr += f'{key}="{value}" '
  return Markup(f'<a href="{url}" {html_attr}>{link_text}</a>')

def button_to_url(button_text, url, attr={}):
  if 'class' in attr:
    attr['class'] += ' button'
  else:
    attr['class'] = 'button'
  return link_to_url(button_text, url, attr)

def link_to(link_text, endpoint, **endpoint_opts):
  url = url_for(endpoint, **endpoint_opts)
  return Markup(f'<a href="{url}" class="link">{link_text}</a>')

def button_to(button_text, endpoint, selected=False, **endpoint_opts):
  url = url_for(endpoint, **endpoint_opts)
  cls = "button"
  if selected:
    cls += " selected"
  return Markup(f'<a href="{url}" class="{cls}">{button_text}</a>')

def post_to(link_text, endpoint, confirm_mesg="", **endpoint_opts):
  url = url_for(endpoint, **endpoint_opts)
  onclick=""  
  if confirm_mesg:
    onclick = f'onclick="return confirm(\'{confirm_mesg}\')"'
  html = (f'<form class="postlink" action="{url}" method="post">'
          f'  <input type="submit" class="link" value="{link_text}" {onclick}>'
          f'</form>')
  return Markup(html)

def nav_link(link_text, endpoint, **endpoint_opts):
  url = url_for(endpoint, **endpoint_opts)
  class_str = "current-page" if request.endpoint == endpoint else ""
  return Markup(f'<a href="{url}" class="{class_str}">{link_text}</a>')


