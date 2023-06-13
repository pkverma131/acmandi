from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import json
from pathlib import Path

PROJECT_BASE_LOCATION = str(settings.BASE_DIR.parent.absolute())


def get_brands(file_path, file_names:str)->list:
    brands = []
    for file_name in file_names:
                file_obj = open(f"{file_path}/{file_name}")
                product_data = json.load(file_obj)
                # print(product_data)
                brand_name = product_data['specifications'][6]['specification_value']
                brands.append(brand_name) if brand_name not in brands else brands
                file_obj.close()
    return brands


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("product_file_paths", nargs="+", type=str)

    def handle(self, *args, **options):
        for product_file_path in options["product_file_paths"]:
            file_path = os.path.join(PROJECT_BASE_LOCATION, product_file_path)
            print(file_path)
            file_names = os.listdir(file_path)
            print(file_names)
            brands = get_brands(file_path, file_names)
            print(brands)
