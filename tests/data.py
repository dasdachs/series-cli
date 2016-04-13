"""Fixed and parsed data for testing"""


SERIES = {
    "_links": { "nextepisode": { "href": "http://api.tvmaze.com/episodes/664353"},
                "previousepisode": { "href": "http://api.tvmaze.com/episodes/631872"},
                "self": { "href": "http://api.tvmaze.com/shows/60"}
    },
    "externals": { "imdb": "tt0364845", "thetvdb": 72108, "tvrage": 4628},
    "genres": ["Drama", "Action", "Crime"],
    "id": 60, "image": { "medium": "http://tvmazecdn.com/uploads/images/medium_portrait/34/85849.jpg", "original": "http://tvmazecdn.com/uploads/images/original_untouched/34/85849.jpg" }, "language": "English", "name": "NCIS",
    "network": { "country": { "code": "US", "name": "United States",
                               "timezone": "America/New_York"},
                  "id": 2,
                  "name": "CBS"
    },
    "premiered": "2003-09-23",
    "rating": { "average": 8.8},
    "runtime": 60,
    "schedule": { "days": ["Tuesday"], "time": "20:00"},
    "status": "Running",
    "summary": """
         <p>NCIS (Naval Criminal Investigative Service) is more than
         just an action drama. With liberal doses of humor, it\"s a show that focuses
         on the sometimes complex and always amusing dynamics of a team forced to work
         together in high-stress situations. Leroy Jethro Gibbs, a former Marine
         gunnery sergeant, whose skills as an investigator are unmatched, leads this
         troupe of colorful personalities. Rounding out the team are Anthony DiNozzo,
         an ex-homicide detective whose instincts in the field are unparalleled and
         whose quick wit and humorous take on life make him a team favorite; the
         youthful and energetic forensic specialist Abby Sciuto, a talented scientist
         whose sharp mind matches her Goth style and eclectic tastes; Caitlin Todd, an
         ex-Secret Service Agent; and Timothy McGee, an MIT graduate whose brilliance
         with computers far overshadows his insecurities in the field; Assisting the
         team is medical examiner Dr. Donald "Ducky" Mallard, who knows it all because
         he\"s seen it all, and he\"s not afrad to let you know. From murder and
         espionage to terrorism and stolen submarines, these special agents travel the
         globe to investigate all crimes with Navy or Marine Corps ties.</p>
    """,
    "type": "Scripted",
    "updated": 1460310820,
    "url": "http://www.tvmaze.com/shows/60/ncis",
    "webChannel": None,
    "weight": 11
}

PREV = {
    '_links': {'self': {'href': 'http://api.tvmaze.com/episodes/2284'}},
    'airdate': '2003-09-23',
    'airstamp': '2003-09-23T20:00:00-04:00',
    'airtime': '20:00',
    'id': 2284,
    'image': None,
    'name': 'Yankee White',
    'number': 1,
    'runtime': 60,
    'season': 1,
    'summary': """
       <p>A Marine mysteriously drops dead aboard Air Force
       One and jurisdiction problems force Gibbs to share the
       investigation with a Secret Service agent.</p>
    """  ,
    'url': 'http://www.tvmaze.com/episodes/2284/ncis-1x01-yankee-white'
}

NEXT = {
    '_links': {'self': {'href': 'http://api.tvmaze.com/episodes/2285'}},
    'airdate': '2003-09-30',
    'airstamp': '2003-09-30T20:00:00-04:00',
    'airtime': '20:00',
    'id': 2285,
    'image': None,
    'name': 'Hung Out to Dry',
    'number': 2,
    'runtime': 60,
    'season': 1,
    'summary': """
         <p>A Marine dies when his parachute fails and he crashes
         through a car during a training exercise, and Gibbs
         suspects he was murdered.</p>
    """,
    'url': 'http://www.tvmaze.com/episodes/2285/ncis-1x02-hung-out-to-dry'
}


mock_data = {"series": SERIES, "previousepisode": PREV, "nextepisode": NEXT}

def mock_get_data(data_name, **kwargs):
    """
    Mocks the response JSON from TVMaze.

    :param data_name: a string, either series, prev or next
    :kwargs: a dictionary that change the mock data dict
    :return: a dict, representing the mocked data
    """
    data = mock_data[data_name]
    if kwargs:
        for key in kwargs.keys():
            if data.get(key):
                data[key] = kwargs[key]
    return data
