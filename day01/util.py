import openpyxl
import yaml

class GetYaml:
    def get(self,yaml_path):
        '''
        读取Yaml格式文件，返回一个字典类型的数据
        yaml_path:yaml文件的路径
        '''
        with open(yaml_path,'r',encoding='utf-8') as file:
            return yaml.load(file.read(),Loader=yaml.FullLoader)

class GetExcel:
    def get(self,excel_path,sheet_name):
        '''
        读取Excel格式文件，返回一个列表类型的数据
        excel_path:excel文件的路径
        sheet_name:工作表名
        '''
        # 打开工作簿
        workbook = openpyxl.load_workbook(excel_path)

        # 打开指定的工作表
        login_success = workbook[sheet_name]
        r = []
        for row in login_success:
            e = []
            for cell in row:
                e.append(cell.value)
            r.append(tuple(e))
        return r[1:]

class GetCsv:

    def get(self,csv_path):
        '''
        读取csv格式文件，返回一个列表类型的数据
        csv_path:csv文件的路径
        '''
        with open(csv_path,'r',encoding='utf-8') as file:
            lines = file.readlines()

            return [tuple(l.strip() for l in line.split(',')) for line in lines][1:]