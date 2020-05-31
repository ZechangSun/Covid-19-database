from pyecharts.charts import Map, Geo, Line, Page
from pyecharts import options as opts
import datetime
import random


def fetch_country_data(start_date='2020-1-11', end_date='2020-5-10', country='美国', demands=('', '', '', '累计治愈数', '累计确诊数')):
    data4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 12, 12, 48, 48,
             106, 108, 147, 171, 178, 178, 178, 616, 1544, 2438, 2612, 4865, 5896, 7136, 8672, 9228, 12729, 15021,
             17582, 19972, 22539, 24213, 26522, 29192, 37024, 42735, 44319, 49966, 52739, 56257, 63510, 66854, 71011,
             73533, 75682, 84050, 85922, 99120, 118162, 118869, 139419, 142238, 147473, 156089, 164015, 175382, 180152,
             188069, 201152, 213109, 217251, 223930, 238081]
    data5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 3, 5, 5, 5, 5, 6, 6, 8, 9, 11, 11, 12, 12, 12, 12, 12, 13,
             13, 14, 15, 15, 15, 15, 15, 15, 15, 15, 34, 34, 34, 53, 53, 54, 60, 62, 62, 77, 96, 122, 160, 236, 324,
             445, 572, 849, 1004, 1004, 1635, 2084, 2885, 3774, 4661, 6552, 10259, 14250, 19624, 171, 40961, 46450,
             55041, 69197, 85840, 104839, 124763, 143836, 164785, 189800, 216768, 245573, 279500, 312249, 337971,
             368533, 399979, 432554, 466396, 501701, 530203, 558526, 587752, 609696, 639733, 672246, 710272, 735366,
             760570, 788920, 826184, 849092, 886709, 906551, 960896, 990021, 1012147, 1035765, 1065739, 1099275,
             1134059, 1162383, 1191854, 1214023, 1239848, 1263705, 1293907, 1324352, 1349605]
    data = [data4, data5]
    return data


def fetch_province_data(start_date='12020-1-1', end_date='2020-5-10', province='武汉', demands=('', '', '', '累计治愈数', '累计确诊数')):
    data4 = [6, 7, 7, 7, 12, 15, 19, 24, 25, 25, 25, 28, 31, 32, 42, 44, 47, 80, 90, 116, 166, 215, 295, 396, 520, 633,
             817, 1115, 1439, 1795, 2222, 2639, 3441, 3862, 4774, 5623, 6639, 7862, 9128, 10337, 11788, 13557, 15299,
             16738, 18854, 20912, 23200, 26403, 28895, 31187, 33757, 36167, 38556, 40479, 41966, 43468, 45011, 46433,
             47585, 49056, 50298, 51553, 52943, 54278, 55094, 55987, 56883, 57678, 58381, 58942, 59432, 59879, 60323,
             60810, 61201, 61731, 62098, 62565, 62882, 63153, 63326, 63471, 63612, 63762, 63945, 64014, 64073, 64142,
             64187, 64236, 64264, 64281, 64338, 64363, 64402, 64435, 63487, 63494, 63507, 63511, 63514, 63519, 63547,
             63569, 63593, 63604, 63616, 63616, 63616, 63616, 63616, 63616, 63616, 63616, 63616, 63616, 63616, 63616,
             63616, 63616, 63616]
    data5 = [41, 41, 41, 41, 41, 45, 62, 121, 198, 270, 375, 444, 549, 729, 1052, 1423, 2714, 3554, 4586, 5806, 7153,
             9074, 11177, 13522, 16678, 19665, 22112, 24953, 27100, 29631, 31728, 33366, 48206, 51986, 54406, 56249,
             58182, 59989, 61682, 62031, 62662, 63454, 64084, 64287, 64786, 65187, 65596, 65914, 66337, 66907, 67103,
             67217, 67332, 67466, 67592, 67666, 67707, 67743, 67760, 67773, 67781, 67786, 67790, 67794, 67798, 67799,
             67800, 67800, 67800, 67800, 67800, 67800, 67801, 67801, 67801, 67801, 67801, 67801, 67801, 67801, 67802,
             67802, 67802, 67803, 67803, 67803, 67803, 67803, 67803, 67803, 67803, 67803, 67803, 67803, 67803, 67803,
             68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128,
             68128, 68128, 68128, 68128, 68128, 68128, 68128, 68128, 68129, 68134]
    data = [data4, data5]
    return data


def fetch_city_data(start_date='2020-5-31', end_date='2020-5-31', city='信阳', demands=('', '', '', '累计治愈数', '累计确诊数')):
    data4 = [272]
    data5 = [274]
    data = [data4, data5]
    return data


def fetch_drug_date(date, type='疫苗'):
    return [('中国', 5), ('美国', 18), ('英国', 8), ('德国', 4)]


def calendar(start_date='2019-1-11', end_date='2020-5-10'):
    # 有头有尾
    datestart = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    dateend = datetime.datetime.strptime(end_date, '%Y.%m.%d')
    date_list = []
    while datestart <= dateend:
        datestart += datetime.timedelta(days=1)
        date_list.append(datestart.strftime('%Y.%m.%d'))
    return date_list


def generate_line_chart(start_date='2020-1-11', end_date='2020-5-10', country1='中国', province1='武汉', country2='美国',
                        province2='全国',
                        demands=('', '', '', '累计治愈数', '累计确诊数')):
    date = calendar(start_date, end_date)
    line1 = Line()
    line1.add_xaxis(date)

    data = []
    for province in (province1, province2):
        if province == '全国':
            data += fetch_country_data(start_date, end_date, country1, demands)
        elif province:
            data += fetch_province_data(start_date, end_date, province1, demands)

    demands = [demand for demand in demands if demand] * 2
    for num, datum in enumerate(data):
        line1.add_yaxis('{}{}的{}'.format((country1, country1, country2, country2)[num],
                                         (province1, province1, province2, province2)[num], demands[num]), datum[num])
    line1.render(path='1.html')


def generate_heat_map(date, country='世界', province=''):
    # 累计病例热力图
    if country == '世界':
        countries = ['Albania', 'Algeria', 'Afghanistan', 'Argentina', 'Akrotiri and Dhekelia', 'United Arab Emirates',
                   'Aruba', 'Oman', 'Azerbaijan', 'Egypt', 'Ethiopia', 'Ireland', 'Estonia', 'Andorra', 'Angola',
                   'Anguilla', 'Antigua and Barbuda', 'Austria', 'Aland', 'Australia', 'Barbados', 'Papua New Guinea',
                   'Bahamas', 'Pakistan', 'Paraguay', 'Palestine', 'Bahrain', 'Panama', 'Brazil', 'Belarus', 'Bermuda',
                   'Bulgaria', 'Northern Mariana Islands', 'Northern Cyprus', 'Benin', 'Belgium', 'Iceland', 'Poland',
                   'Bosnia and Herzegovina', 'Bolivia', 'Belize', 'Botswana', 'Bonaire, Sint Eustatius and Saba',
                   'Bhutan', 'Burkina Faso', 'Bouvet Island', 'North Korea', 'Equatorial Guinea', 'Denmark', 'Germany',
                   'Timor-Leste', 'Togo', 'Dominica', 'Dominica', 'Russia', 'Ecuador', 'Eritrea', 'France',
                   'Faroe Islands', 'French Polynesia', 'French Guiana', 'French Southern Territories', 'Vatican City',
                   'Philippines', 'Fiji', 'Finland', 'Cape Verde', 'Falkland Islands', 'Gambia', 'Republic of Congo',
                   'Democratic Republic of the Congo', 'Colombia', 'Costa Rica', 'Guernsey', 'Grenada', 'Greenland',
                   'Georgia', 'Cuba', 'Guadeloupe', 'Guam', 'Guyana', 'Kazakhstan', 'Haiti', 'South Korea',
                   'Netherlands', 'Heard Island and McDonald Islands', 'Montenegro', 'Ruby Princess', 'Honduras',
                   'Kiribati', 'Djibouti', 'Kyrgyzstan', 'Guinea', 'Guinea-Bissau', 'Canada', 'Ghana', 'Gabon',
                   'Burundi', 'Cambodia', 'Czech Republic', 'Zimbabwe', 'Cameroon', 'Qatar', 'Cayman Islands',
                   'Cocos Islands', 'Comoros', 'Kosovo', "Côte d'Ivoire", 'Kuwait', 'Clipperton Island', 'Croatia',
                   'Kenya', 'Cook Islands', 'Curaçao', 'Latvia', 'Lesotho', 'Laos', 'Lebanon', 'Caspian Sea',
                   'Lithuania', 'Liberia', 'Libya', 'Liechtenstein', 'Reunion', 'Luxembourg', 'Rwanda', 'Romania',
                   'Madagascar', 'Isle of Man', 'Maldives', 'Malta', 'Malawi', 'Malaysia', 'Mali', 'Macedonia',
                   'Marshall Islands', 'Martinique', 'Mayotte', 'Mauritius', 'Mauritania', 'United States',
                   'Virgin Islands, U.S.', 'United States Minor Outlying Islands', 'American Samoa', 'Mongolia',
                   'Montserrat', 'Bangladesh', 'Peru', 'Micronesia', 'Myanmar', 'Moldova', 'Morocco', 'Monaco',
                   'Mozambique', 'Mexico', 'Namibia', 'South Africa', 'Antarctica',
                   'South Georgia and the South Sandwich Islands', 'Spratly Islands', 'South Sudan', 'Nauru', 'Nepal',
                   'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norway', 'Norfolk Island', 'Palestina', 'Palau',
                   'Pitcairn Islands', 'Portugal', 'Japan', 'Sweden', 'Switzerland', 'El Salvador', 'Samoa', 'Serbia',
                   'Sierra Leone', 'Senegal', 'Cyprus', 'Seychelles', 'Saudi Arabia', 'Saint-Barthélemy',
                   'Christmas Island', 'São Tomé and Príncipe', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia',
                   'Saint-Martin', 'San Marino', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines',
                   'Sri Lanka', 'Slovakia', 'Slovenia', 'Svalbard and Jan Mayen', 'Swaziland', 'Sudan', 'Suriname',
                   'Solomon Islands', 'Somalia', 'Tajikistan', 'Thailand', 'Tanzania', 'Tonga',
                   'Turks and Caicos Islands', 'Trinidad and Tobago', 'Tunisia', 'Tuvalu', 'Turkey', 'Turkmenistan',
                   'Tokelau', 'Wallis and Futuna', 'Vanuatu', 'Guatemala', 'Venezuela', 'Brunei', 'Uganda', 'Ukraine',
                   'Uruguay', 'Uzbekistan', 'Spain', 'Western Sahara', 'Paracel Islands', 'Greece', 'Sint Maarten',
                   'Singapore', 'New Caledonia', 'New Zealand', 'Hungary', 'Syria', 'Jamaica', 'Armenia', 'Yemen',
                   'Iraq', 'Iran', 'Israel', 'Italy', 'India', 'Indonesia', 'United Kingdom', 'British Virgin Islands',
                   'British Indian Ocean Territory', 'Jordan', 'Vietnam', 'Zambia', 'Jersey', 'Chad', 'Gibraltar',
                   'Chile', 'Central African Republic', 'China', 'Diamond Princess']

        # case_num = [fetch_country_data(date, date, country) for country in countries]
        case_num = [650, 2546, 558, 1728, 0, 4804, 89, 1117, 1620, 2002, 97, 17110, 750, 545, 13, 0, 19, 13991, 0, 6163,
                    57, 8, 37, 8023, 155, 263, 2065, 4501, 61685, 6406, 0, 444, 0, 0, 62, 13642, 1773, 5698, 1106, 258,
                    16, 12, 0, 5, 569, 0, 0, 13, 8415, 147171, 21, 87, 2584, 14, 34306, 3433, 37, 56148, 157, 56, 122,
                    0, 2, 1924, 14, 4000, 56, 0, 9, 33, 136, 2569, 480, 0, 13, 11, 309, 1140, 0, 0, 35, 1901, 17, 9610,
                    322, 0, 274, 0, 195, 0, 834, 675, 698, 25, 31262, 378, 110, 7, 120, 4448, 9, 1465, 2753, 0, 0, 0, 0,
                    769, 2729, 0, 1764, 239, 0, 0, 464, 0, 13, 234, 0, 828, 83, 24, 55, 0, 3550, 140, 7051, 101, 0, 29,
                    433, 14, 5025, 298, 1136, 0, 0, 0, 320, 6, 238081, 0, 0, 0, 13, 2, 2650, 20246, 0, 72, 1925, 2545,
                    82, 34, 21824, 11, 3983, 0, 0, 0, 2, 0, 31, 7, 617, 745, 0, 32, 0, 0, 0, 0, 2549, 5906, 4971, 26400,
                    293, 0, 2732, 67, 650, 401, 10, 11457, 0, 0, 4, 0, 14, 17, 0, 126, 0, 9, 321, 941, 256, 0, 14, 119,
                    9, 0, 110, 0, 2794, 183, 0, 5, 104, 660, 0, 89480, 0, 0, 0, 0, 104, 190, 134, 55, 3060, 513, 1881,
                    176439, 5, 0, 1374, 0, 2296, 17, 1371, 933, 29, 78, 1325, 1, 1702, 86143, 11384, 103031, 19358,
                    2698, 1002, 0, 0, 387, 241, 117, 0, 53, 142, 12667, 10, 79527, 645]

        world = Map()
        world.add('{}疫情地图'.format(country), [list(z) for z in zip(countries, case_num)], 'world')
        world.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        world.set_global_opts(title_opts=opts.TitleOpts(title='截至5月26日各国的累计治愈人数'),
                              visualmap_opts=opts.VisualMapOpts(max_=cal_upper_bound(max(case_num)),
                                                                is_piecewise=True,
                                                                range_color=('#ffffff', '#ff3838')
                                                                )
                              )
        world.render(path='2.html')

    elif province == '全国':
        provinces = ['新疆', '西藏', '青海', '甘肃', '四川', '云南', '宁夏', '陕西', '重庆', '贵州', '广西', '内蒙古',
                         '山西', '河南', '湖北', '湖南', '广东', '澳门', '香港', '海南', '江西', '安徽', '河北', '北京',
                         '天津', '安徽', '江苏', '浙江', '上海', '福建', '山东', '南海诸岛', '台湾', '辽宁', '吉林',
                         '黑龙江']

        case_num = [fetch_province_data(date, date, province) for province in provinces]

        world = Map()
        world.add('{}疫情地图'.format(country), [list(z) for z in zip(provinces, case_num)], country)
        world.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        world.set_global_opts(title_opts=opts.TitleOpts(title='截至5月26日各国的累计治愈人数'),
                              visualmap_opts=opts.VisualMapOpts(max_=cal_upper_bound(max(case_num)),
                                                                is_piecewise=True,
                                                                range_color=('#ffffff', '#ff3838')
                                                                )
                              )
        world.render(path='2.html')

    else:
        cities = ['北京']

        case_num = [fetch_city_data(data, data, city) for city in cities]

        world = Map()
        world.add('{}疫情地图'.format(province), [list(z) for z in zip(cities, case_num)], 'province')
        world.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        world.set_global_opts(title_opts=opts.TitleOpts(title='截至5月26日各国的累计治愈人数'),
                              visualmap_opts=opts.VisualMapOpts(max_=cal_upper_bound(max(case_num)),
                                                                is_piecewise=True,
                                                                range_color=('#ffffff', '#ff3838')
                                                                )
                              )
        world.render(path='2.html')


def generate_drug_map(date, type='疫苗'):
    data = fetch_drug_date(date, type)
    points = []
    for country, num in data:
        poins.append('1', random.sample(random_points[country], num))
    count = [1] * len(data)
    addresses = []
    json_data = {}
    for address in test_data:
        json_data[address[0]] = [address[1], address[2]]
        addresses.append(address[0])

    json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
    with open('test_data.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)

    geo = Geo()
    geo.add_schema(maptype='world')
    geo.add_coordinate_json(json_file='test_data.json')
    geo.add('研发中的{}类药物'.format(type), [list(z) for z in zip(addresses, data)], type_=ChartType.EFFECT_SCATTER, color='#1e90ff',
            symbol_size=10, symbol='diamond')
    geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False), effect_opts=opts.EffectOpts(scale=5))
    geo.set_global_opts(title_opts=opts.TitleOpts(title="Geo-EffectScatter"),
                        tooltip_opts=opts.TooltipOpts(is_show=False))
    geo.render(path='3.html')


