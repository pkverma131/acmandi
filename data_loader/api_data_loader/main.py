from split_ac_data_loader import get_split_ac_links
from constants import API_BASE_URL, SPLIT_AC_API_URL
from utils import generate_filename, write_josn_to_file

if __name__=='__main__':
    product_list = get_split_ac_links(API_BASE_URL+SPLIT_AC_API_URL)
    filename = generate_filename('split_ac')
    write_josn_to_file(product_list,filename)
    #TODO: Manually get all category listing page API url
    #TODO: Scrap product details of each product
    #TODO: Dynamically get URLS of all the product categories