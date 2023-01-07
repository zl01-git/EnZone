import folium
from dataclasses import dataclass




@dataclass
class MarkerCoordinates:
    name: str
    descriptions: str
    lat: float  # latitude
    long: float  # longitude


markers = [
    dinamo := MarkerCoordinates("dinamo","dinamo", 54.988144, 73.360309),
    sobor := MarkerCoordinates("sobor","sobor", 54.990163, 73.366649),
    school_66 := MarkerCoordinates("school_66","school_66", 54.998086, 73.358870),
    omgau := MarkerCoordinates("omgau","omgau", 54.998086, 73.358870),
    metalist := MarkerCoordinates("metalist","metalist", 55.005108, 73.360576),
    liza_park := MarkerCoordinates("liza_park", "liza_park", 54.972215, 73.419350),
    pobedy_park := MarkerCoordinates("pobedy_park", "pobedy_park", 54.961690, 73.359938),
    mega := MarkerCoordinates("mega", "mega", 54.971659, 73.285662),
    autovokzal := MarkerCoordinates("autovokzal","autovokzal", 54.998618, 73.281255),
    telecentr := MarkerCoordinates("telecentr", "telecentr", 55.022123, 73.307333),
    crystal := MarkerCoordinates("crystal","crystal", 55.028522, 73.284507),
    school_61 := MarkerCoordinates("school_61","school_61", 55.037582, 73.294586),
    himik := MarkerCoordinates("himik","himik", 55.042303, 73.295035),
    vesna := MarkerCoordinates("vesna","vesna", 55.029315, 73.249763),
    lenta_amur := MarkerCoordinates("lenta_amur","lenta_amur", 55.035971, 73.416491),
    dk_kolos := MarkerCoordinates("dk_kolos","dk_kolos", 55.065669, 73.417727),
    poselok_omskiy := MarkerCoordinates("poselok_omskiy","poselok_omskiy", 55.101813, 73.349626),
    poselok_podgorodka := MarkerCoordinates("poselok_podgorodka","poselok_podgorodka", 55.143093, 73.548335),
    poselok_hvoiny := MarkerCoordinates("poselok_hvoiny","poselok_hvoiny", 55.110584, 73.580322),
    poselok_rostovka := MarkerCoordinates("poselok_rostovka","poselok_rostovka", 55.020270, 73.575121),
    jd_vokzal := MarkerCoordinates("jd_vokzal", "jd_vokzal", 54.939560, 73.385721),
    school_20 := MarkerCoordinates("school_20", "school_20", 54.907496, 73.357351),
    agroprom := MarkerCoordinates("agroprom", "agroprom", 54.911893, 73.301592),
    poselok_morozovka := MarkerCoordinates("poselok_morozovka", "poselok_morozovka", 54.924548, 73.549382),
    poselok_rakitinka := MarkerCoordinates("poselok_rakitinka", "poselok_rakitinka", 54.898357, 73.520180),
    putevaya := MarkerCoordinates("putevaya", "putevaya", 54.917225, 73.435557),
    ledoviy_dvorec := MarkerCoordinates("ledoviy_dvorec", "ledoviy_dvorec", 54.921137, 73.457235),
    gasheka := MarkerCoordinates("gasheka", "gasheka", 54.908537, 73.444933),
    metro := MarkerCoordinates("metro", "metro", 54.896516, 73.429477)
]


if __name__ == "__main__":
    for __marker in markers:
        print(__marker.name, __marker.lat, __marker.long)