from DrissionPage import Chromium, ChromiumOptions
from module.ExcelProcessing import write_to_excel

chromium_option = ChromiumOptions ( )
chromium_option.mute ( True )
browser = Chromium ( )
tab = browser.latest_tab


def data_crawling ( file_path, urls: list [ str ] ):
	total = len ( urls )
	for idx, url in enumerate ( urls, start = 1 ):
		tab.get ( url )
		data = {
			'release_time': tab.ele ( 'xpath://*[@id="viewbox_report"]/div[2]/div/div[3]/div' ).text,
			'video_title': tab.ele ( 'xpath://*[@id="viewbox_report"]/div[1]/div/h1' ).text,
			'video_playback': tab.ele ( 'xpath://*[@id="viewbox_report"]/div[2]/div/div[1]/div' ).text,
			'video_barrage': tab.ele ( 'xpath://*[@id="viewbox_report"]/div[2]/div/div[2]/div' ).text,
			'video_likes': tab.ele ( 'xpath://*[@id="arc_toolbar_report"]/div[1]/div/div[1]/div/span' ).text,
			'video_coin_drop': tab.ele ( 'xpath://*[@id="arc_toolbar_report"]/div[1]/div/div[2]/div/span' ).text,
			'video_collection': tab.ele ( 'xpath://*[@id="arc_toolbar_report"]/div[1]/div/div[3]/div/span' ).text,
			'video_sharing': tab.ele ( 'xpath://*[@id="share-btn-outer"]/div/span' ).text
		}
		print ( f"共 {total} 条数据，正在爬取第 {idx} 条数据，视频链接：{urls [ idx - 1 ]}。" )
		write_to_excel ( file_path, idx, data )
