import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def add_site(name):
    new_site = copy.deepcopy(site)
    new_site['html']['head']['title'] = 'Куплю/продам {} недорого'.format(name)
    new_site['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(name)
    return new_site


sites_count = int(input('Сколько сайтов: '))
sites = dict()
for _ in range(sites_count):
    site_name = input('Введите название продукта для нового сайта:')
    added_site = add_site(site_name)
    sites[site_name] = added_site
    for key, value in sites.items():
        print('Сайт для {}'.format(key))
        print('{}\n'.format(value))
