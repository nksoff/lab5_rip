posts = [
    {
        'id': i,
        'title': 'Title {}'.format(i),
        'description': 'Short description for {}. Description seems to be very long.'.format(i),
        'text': 'Full text for {}'.format(i)
    } for i in range(1, 20)
    ]

posts_dict = {val.get('id'): val for val in posts}