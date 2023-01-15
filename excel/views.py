from django.shortcuts import render
from django.http import HttpResponse
from excel.models import Exceldata
import numpy as np    
from django.db import transaction
#@transaction.commit_manually
import json
import datetime


#listing view of excel elements
def index(request):
    all_data = Exceldata.objects.all()
    datas = { 
          'list_datas' :  all_data,
        }
    return render(request,'index.html',datas)

#show excel
def show_excel(request):
    all_fields  =  [field.name for field in Exceldata._meta.get_fields() if field.name not in ('updated_at', 'created_at')]
    data_obj    = Exceldata.objects.all().values_list(*all_fields)
    row_data    = np.array(list(data_obj)).tolist() #spreadsheet row datas
    #row_data.append(['', '', '', '', '', '', '', ''])
    ss_data = { 
          'columns' : all_fields,
          'rows'    : row_data
        }
    return render(request,'excel.html',ss_data)

#save excel data
def save_excel(request):
    jsonData = request.POST['data']
    changedRowIds = request.POST['changedRowIds']
    json_object   = json.loads(jsonData)

    for item in json_object:
        try:
            data_id = str(item[0])
            if data_id==0 or data_id=='' or data_id=='None': #insert new item
                Exceldata.objects.create(
                    color   = check_empty(item[1]),
                    group   = check_empty(item[2]),
                    size    = check_empty(item[3],'int'),
                    article = check_empty(item[4]),
                    pairs   = check_empty(item[5],'int'),
                    rate    = check_empty(item[6],'int'),
                    amount  = check_empty(item[7],'int'),
                    created_at = datetime.date.today()
                )
            elif data_id in changedRowIds: #update existing item
                ExcelTb         = Exceldata.objects.get(data_id=data_id)
                ExcelTb.color   = check_empty(item[1]),
                ExcelTb.group   = check_empty(item[2]),
                ExcelTb.size    = check_empty(item[3],'int'),
                ExcelTb.article = check_empty(item[4]),
                ExcelTb.pairs   = check_empty(item[5],'int'),
                ExcelTb.rate    = check_empty(item[6],'int'),
                ExcelTb.amount  = check_empty(item[7],'int'),
                ExcelTb.save()
            message = 'success'
        except Exception as e:
            message = 'failed'
            raise e
    return HttpResponse(message)

def check_empty(param,isInt=None):
    newParam = param if param!='' and param!=None else None
    newParam2 = int(newParam) if isInt!=None and newParam!=None else newParam
    return newParam2