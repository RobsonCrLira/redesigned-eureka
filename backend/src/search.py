import requests
from bs4 import BeautifulSoup
from flask_restful import Resource
from util import Util


class Search(Resource):
    def findProduct(url):

        req = requests.get(url)
        content = req.content
        products = []
        if req.status_code == 200:
            soup = BeautifulSoup(content, 'html.parser')
            for post in soup.findAll('article', attrs={'class': "stack-system ps-stack"}):
                id = Util.findHTML('div', 'ps-oc', post)
                name = Util.findHTML('h3', 'ps-title', post)
                originalPrice = Util.findValores(
                    'div', 'ps-orig ps-simplified', post)
                newPrice = Util.findValores(
                    'div', 'ps-dell-price ps-simplified', post)
                desconto = Util.findValores('div', 'ps-sav', post)
                frete = Util.findHTML('span', 'smart-popover-btn', post)
                processor = Util.findHTML(
                    'div', 'short-specs ps-dds-font-icon dds_processor', post)
                video = Util.findHTML(
                    'div', 'short-specs ps-dds-font-icon dds_disc-system', post)
                discSystem = Util.findHTML(
                    'div', 'short-specs ps-dds-font-icon dds_video-card', post)
                memory = Util.findHTML(
                    'div', 'short-specs ps-dds-font-icon dds_memory', post)
                hardDrive = Util.findHTML(
                    'div', 'short-specs ps-dds-font-icon dds_hard-drive', post)
                display = Util.findHTML(
                    'div', 'ps-dds-font-icon featured-spec dds_display device-laptop', post)
                peso = Util.findHTML(
                    'div', 'ps-dds-font-icon featured-spec dds_weight dimensions-weight', post)

                products.append({
                    'id:': id,
                    'name:': name,
                    'originalPrice:': originalPrice,
                    'newPrice:': newPrice,
                    'desconto:': desconto,
                    'frete': frete,
                    'processor:': processor,
                    'discSystem:': discSystem,
                    'video:': video,
                    'memory:': memory,
                    'hardDrive:': hardDrive,
                    'display:': display,
                    'peso:': peso
                })
        else:
            print(f'Problemas de conexao {req.status_code} - {req.text}')

        return products
