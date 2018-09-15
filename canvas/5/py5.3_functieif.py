def lang_genoeg(lengte):
    if lengte >= 120:
        result = 'Je bent lang genoeg voor de attractie!'
    else:
        result = 'Sorry, je bent te klein!'
    return result

print(lang_genoeg(120))