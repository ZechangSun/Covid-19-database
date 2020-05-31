/* 
This part supports for basic query operations
*/
/*
Basic_query
1、查询所有研究机构在北京的研究人员的姓名（包括first_name和last_name）
*/
Select researcher.first_name, researcher.last_name
From researcher, institution
Where researcher.institution_id = institution.institution_id and institution.location = "beijing"
                         /*
2、查询使用药物名为Redsivir进行的研究的编号、阶段和状态（trial_id,trial_stage,trial_status）
                         */
Select trial_id,trial_stage,trial_status
From trial_drug natural join clinical_trial as drugntrial
Where drug_id in(select drug_id
From drug
Where drug_name='Redsivir')
                         /*
3、查询不同性别病例的平均年龄
                         */
Select gender,avg(age)
From cases
Group by gender
                         /*
4、列出表中记录的所有城市名称和每个城市的疑似、确诊和死亡病例数
                         */
with site_suspected(site_id,suspected_case)
as (select site_id,count(case_id)
From cases
where situation='suspected'
Group by site_id),
site_confirmed(site_id,confirmed_case)
As (select site_id,count(case_id)
From cases
	where situation='confirmed'
Group by site_id),
site_dead(site_id,dead_case)
As (select site_id,count(case_id)
From cases
	where situation='dead'
Group by site_id)
Select site_id,suspected_case,confirmed_case,dead_case
From site_suspected natural join site_confirmed natural join site_dead
                         /*
5、查询第一批次的实验编号、药物名称及参与志愿者总数
                         */
With trial(trial_id)
As(select trial_id
From experiment
Where experiment.batch_id=1),
trialndrug(trial_id,drug_name)
As(select trial_id,drug_name
From trial_drug natural join drug
Where trial_id in 
  (select * from trial)
  ),
trialnvolunteer(trial_id,volunteer_num)
As(select trial_id,count(volunteer_id)
From volunteer_experiment
Group by trial_id
Having trial_id in 
  (select * from trial)
  )
Select *
From trialndrug natural join trialnvolunteer
                         /*
6、列出武汉所有确诊医生的病例编号和确诊日期
                         */
Select case_id,confirmed_date
From cases
Where job='doctor' and situation='confirmed'
And site_id in (select site_id
From SITE
Where city='wuhan')
                         /*
7、构建触发机制：每新增死亡病例，确诊病例减一
                         */
CREATE OR REPLACE FUNCTION caseupdate() RETURNS TRIGGER AS $$
begin
if(OLD.situation='confirmed' and NEW.situation='dead') THEN
update cases
set live='NOT';
set left_time=now;
end if;
return NEW;
end;
$$
language plpgsql;
create trigger caseupdate after update on cases
for each row
execute procedure caseupdate();
/*
8、创建视图，显示呼吸科医生的编号和姓名
                         */
Create view pneumology_doctor(pneum_doc_id,pneum_doc_fname,pneum_doc_lname) as
Select doctor_id,first_name,last_name
From doctor
Where department='pneumology'
select*
from pneumology_doctor
			 
/*得到某个国家各个省市病例人数
#sql语句部分定义函数date_num*/
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

/*得到某个类型药物的研发情况
sql语句定义函数drug_num*/
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

/* 					     
