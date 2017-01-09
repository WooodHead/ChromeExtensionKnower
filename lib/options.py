import click
from config import conf
from core.chromeStoreSpider import chromeStoreSpider
from core.googleExtDownloader import web_list_exec


def tmp_dir_check():
    if not os.path.exists(conf['tmp_path']):
        exit('[!] tmp path :{} not exist'.format(conf['tmp_path']))


@click.group()
@click.pass_context
def option_init(ctx):
    pass


@option_init.command('etxInfo', help='Crawl and update Chrome Etx infomation')
@click.pass_obj
@click.option('-O', '--outfile', default='', type=str,
        help='Output result a json file, default use config.py:conf["data_file"]')
@click.option('-u', '--users', default=0, type=int,
        help='Only get the users great than the number, default 0 get all')
def etxinfo(ctx, outfile, users):
    conf['data_file'] = outfile if outfile else conf['data_file']
    conf['more_then_user_num'] = users if users else conf['more_then_user_num']
    csspider = chromeStoreSpider()
    csspider.run()


@option_init.command('etxDownload',
        help='This commond will Download Chrome Etx .crx file')
@click.pass_context
@click.option('-O', '--outfile', type=str,
        help='Output result a json file, default use config.py:conf["etx_info_weblist_file"]')
@click.option('-f', '--jsonfile', type=str,
        help='Input the jsonfile as baseinfo, default use config.py:conf["data_file"]')
@click.option('-p', '--tmppath', type=str,
        help='The program will download etx file to tmppath, default use config.py:conf["tmp_path"]')
@click.option('-t', '--thread', type=int,
        help='Thread number, default use config.py:conf["threadnum"]')
@click.option('-d', '--deltmp', is_flag=True, 
        help='del the dowload config.py:conf["del_tmp"]')
def weblist(ctx, outfile, jsonfile, tmppath, thread, deltmp):
    conf['del_tmp'] = deltmp if deltmp else conf['del_tmp']
    conf['etx_info_weblist_file'] = outfile if outfile else conf['etx_info_weblist_file']
    conf['data_file'] = jsonfile if jsonfile else conf['data_file']
    conf['tmp_path'] = tmppath if tmppath else conf['tmp_path']
    conf['threadnum'] = thread if thread else conf['threadnum']
    web_list_exec()


@option_init.command('spec-fileCheck',
        help='Check filename in web_accessible_resources is exists or not')
@click.pass_context
def weblist_file_check():
    pass

@option_init.command('spec-weblistAgain',
        help='Re get weblist')
@click.pass_context
def weblist_again():
    d_weblist_1000p_1st = './data/etx_weblist_info_1000p.json'
    d_1000p_1st = './data/data2_1000.json'
    d_all = './data/etx_info_all_2.json'
