"""
Fixed and parsed data for testing
"""


SERIES = { 
    u'_links': { u'nextepisode': { u'href': u'http://api.tvmaze.com/episodes/664353'},
                u'previousepisode': { u'href': u'http://api.tvmaze.com/episodes/631872'},
                u'self': { u'href': u'http://api.tvmaze.com/shows/60'}
    },
    u'externals': { u'imdb': u'tt0364845', u'thetvdb': 72108, u'tvrage': 4628},
    u'genres': [u'Drama', u'Action', u'Crime'],
    u'id': 60,
    u'image': {
        u'medium': u'http://tvmazecdn.com/uploads/images/medium_portrait/34/85849.jpg',
        u'original': u'http://tvmazecdn.com/uploads/images/original_untouched/34/85849.jpg'
    },
    u'language': u'English',
    u'name': u'NCIS',
    u'network': { u'country': { u'code': u'US', u'name': u'United States',
                               u'timezone': u'America/New_York'},
                  u'id': 2,
                  u'name': u'CBS'
    },
    u'premiered': u'2003-09-23',
    u'rating': { u'average': 8.8},
    u'runtime': 60,
    u'schedule': { u'days': [u'Tuesday'], u'time': u'20:00'},
    u'status': u'Running',
    u'summary': u'<p>NCIS (Naval Criminal Investigative Service) is more than
     just an action drama. With liberal doses of humor, it\'s a show that focuses
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
     he\'s seen it all, and he\'s not afraid to let you know. From murder and
     espionage to terrorism and stolen submarines, these special agents travel the
     globe to investigate all crimes with Navy or Marine Corps ties.</p>',
    u'type': u'Scripted',
    u'updated': 1460310820,
    u'url': u'http://www.tvmaze.com/shows/60/ncis',
    u'webChannel': None,
    u'weight': 11
}


NEXT = {"name": "next", 

