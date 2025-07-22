from module.ExcelProcessing import *
from module.Spiders import *

if __name__ == '__main__':
	fileAddress = input ( "请输入文件地址：" )
	if is_excel_file ( fileAddress ):
		video_url = read_excel ( fileAddress )
		data_crawling ( fileAddress, video_url )
	else:
		print ( "文件不是有效的 Excel 文件或文件不存在，请检查文件地址。" )
		input ( "按任意键退出。" )
