#得到某个国家各个省市病例人数
#sql语句部分定义函数date_num
CREATE OR REPLACE FUNCTION date_num(DATE_ date)
  RETURNS table(case_num bigint,
			   city_name VARCHAR(20)) AS $$
begin
return QUERY SELECT count(case_id) as case_num,city
From cases,SITE
Where cases.site_id=SITE.site_id
and situation='confirmed' and confirmed_date<DATE_ and country='china'
Group by city;
end;$$
LANGUAGE 'plpgsql';
#python批量生成sql语句
import pandas as pd
def get_date_list(begin_date,end_date):
    date_list = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start=begin_date, end=end_date))]
return date_list
sql_file=open(r'C:\Users\26089\Desktop\update_file.txt','w',encoding='utf-8')#路径根据文件位置确定
def wsql(begin_date,end_date):
for i in get_date_list(begin_date,end_date):
print(i)
str_i=str(i)
line="select * from date_num('%s');"%i
    sql_file.write(line+'\n')
wsql('DATE1','DATE2')
sql_file.close()

#得到某个类型药物的研发情况
#sql语句定义函数drug_num
CREATE OR REPLACE FUNCTION drug_num(DATE_ date)
  RETURNS table(insti_location VARCHAR(20),
			   drug_count bigint) AS $$
begin
return QUERY With researcher_institution(researcher_id,trial_id,institution_id,institution_location)
As (select researcher_id,trial_id,institution_id,institution_location
From researcher_experiment natural join institution natural join institution_researcher natural join experiment
Where start_date<=DATE_ and end_date>=DATE_),
Drug_trial(trial_id,drug_id,drug_type)
As (select trial_id,drug_id,drug_type
From trial_drug natural join drug)
Select institution_location,count(drug_id) as drug_count
From researcher_institution natural join drug_trial
Where drug_type='TYPE'
group by institution_location;
end;$$
LANGUAGE 'plpgsql';
#python批量生成sql语句
import pandas as pd
def get_date_list(begin_date,end_date):
    date_list = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start=begin_date, end=end_date))]
return date_list
sql_file=open(r'C:\Users\26089\Desktop\update_file.txt','w',encoding='utf-8')#路径根据文件位置确定
def wsql(begin_date,end_date):
for i in get_date_list(begin_date,end_date):
print(i)
str_i=str(i)
line="select * from drug_num('%s');"%i
    sql_file.write(line+'\n')
wsql('DATE1','DATE2')
sql_file.close()
