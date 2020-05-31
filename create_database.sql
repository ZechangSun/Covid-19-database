
/*
create Covid-19 database
*/
CREATE TABLE drug
(
	drug_id int,
	drug_name varchar(50),
	drug_status varchar(25),
    drug_type varchar(25),
    primary key (drug_id)
);

CREATE TABLE clinical_trial
(
	trial_id int,
    title varchar(50),
    trial_type varchar(25),
    trial_stage varchar(25),
    trial_status varchar(25),
    record_date date,
    start_date date,
    end_date date,
    bid_institution varchar(50),
    trial_institution varchar(50),
    primary key (trial_id)
);

CREATE TABLE trial_drug
(
	trial_id int,
	drug_id int,
    primary key(trial_id),
    foreign key(trial_id) references clinical_trial(trial_id),
    foreign key(drug_id) references drug(drug_id)
);

create table researcher
(
    institution_id int,
	researcher_id int,
    first_name varchar(25),
    last_name varchar(25),
    position varchar(25),
    email varchar(25),
    phonenumber varchar(25),
    department varchar(25),
    primary key (institution_id, researcher_id),
    FOREIGN KEY (institution_id) REFERENCES institution(institution_id)
);

create table institution
(
	institution_id int,
    institution_location varchar(50),
    instituiton_money int,
    institution_email varchar(25),
    institution_phone varchar(25),
    primary key (institution_id)
);


create table experiment
(
	trial_id int,
    batch_id int,
    experiment_description varchar(100),
    start_date date,
    end_date date,
    dose float,
    result varchar(20),
    adverse_reaction varchar(20),
    more_details varchar(50),
    primary key (trial_id, batch_id),
    foreign key (trial_id) references clinical_trial(trial_id)
);

create table researcher_experiment
(
	researcher_id int,
    trial_id int,
	batch_id int,
    division varchar(20),
    primary key(researcher_id),
    foreign key(researcher_id) references researcher(researcher_id),
    foreign key(trial_id,batch_id) references experiment(trial_id,batch_id)
);

CREATE TABLE volunteer
(
    volunteer_id INT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    gender VARCHAR(5),
    age INT,
    blood_type VARCHAR(5),
    country VARCHAR(10),
    PRIMARY KEY (volunteer_id)
);

CREATE TABLE volunteer_experiment
(
    volunteer_id int,
    trial_id int,
    batch_id int,
    PRIMARY KEY (volunteer_id),
    FOREIGN KEY (volunteer_id) REFERENCES volunteer(volunteer_id),
    FOREIGN KEY (trial_id, batch_id) REFERENCES experiment(trial_id, batch_id)
);

CREATE TABLE SITE
(
    site_id int,
    country VARCHAR(20),
    province VARCHAR(20),
    city VARCHAR(20),
    other_details VARCHAR(20),
    PRIMARY KEY (site_id)
);

CREATE TABLE hospital
(
    hospital_id int,
    site_id int,
    hospital_name VARCHAR(20),
    PRIMARY KEY (hospital_id,site_id),
    FOREIGN KEY (site_id) REFERENCES SITE(site_id)
);

CREATE TABLE doctor
(
    doctor_id int,
    hospital_id int,
    site_id INT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    department VARCHAR(20),
    gender VARCHAR(5),
    age INT,
    PRIMARY KEY (doctor_id,site_id ,hospital_id),
    FOREIGN KEY (hospital_id, site_id) REFERENCES hospital(hospital_id, site_id)
);

CREATE TABLE cases
(
    case_id int,
    site_id int,
    first_name varchar(20),
    last_name varchar(20),
    gender varchar(5),
    age int,
    job varchar(20),
    reason VARCHAR(20),
    situation varchar(20),
    suspected_date date,
    confirmed_date date,
    left_date date,
    PRIMARY KEY (case_id, site_id),
    FOREIGN KEY (site_id) REFERENCES SITE(site_id) 
);

CREATE TABLE close_contact
(
    site_id int,
    close_contact_id int,
    first_name varchar(20),
    last_name varchar(20),
    gender VARCHAR(5),
    age int,
    status varchar(10),
    primary key (site_id, close_contact_id),
    foreign key(site_id) references SITE(site_id)
);

CREATE Table contact
(
    case_site_id int,
    case_id int,
    close_contact_site_id int,
    close_contact_id int,
    relation VARCHAR(20),
    contact_date date,
    contact_place_id int,
    contact_form varchar(20),
    primary key (case_site_id, case_id, close_contact_site_id, close_contact_id),
    foreign key (case_site_id, case_id) references cases(site_id, case_id),
    foreign key (close_contact_site_id, close_contact_id) references close_contact(site_id, close_contact_id)
);

CREATE TABLE case_move
(
    site_id int,
    case_id int,
    start_id int,
    depart_date date,
    destination_id int,
    arrive_date date,
    vehicle varchar(50),
    PRIMARY KEY (site_id, case_id, start_id, depart_date, destination_id, arrive_date),
    FOREIGN KEY (site_id, case_id) REFERENCES cases(site_id, case_id),
    FOREIGN KEY (start_id) REFERENCES SITE(site_id),
    FOREIGN KEY (destination_id) REFERENCES SITE(site_id)
);

CREATE TABLE close_contact_move
(
    site_id int,
    close_contact_id int,
    start_id int,
    depart_date date,
    destination_id int,
    arrive_date date,
    vehicle varchar(50),
    PRIMARY KEY (site_id, close_contact_id, start_id, depart_date, destination_id, arrive_date),
    FOREIGN KEY (site_id, close_contact_id) REFERENCES close_contact(site_id, close_contact_id),
    FOREIGN KEY (start_id) REFERENCES SITE(site_id),
    FOREIGN KEY (destination_id) REFERENCES SITE(site_id)
);

CREATE TABLE treat_method
(
    treat_id int,
    doctor_id int,
    doctor_site_id int,
    doctor_hospital_id int,
    case_id int,
    case_site_id int,
    treat_method VARCHAR(20),
    start_date date,
    end_date date,
    result VARCHAR(50),
    PRIMARY KEY (treat_id),
    FOREIGN KEY (doctor_id, doctor_site_id, doctor_hospital_id) REFERENCES doctor(doctor_id, site_id, hospital_id),
    FOREIGN key (case_id, case_site_id) references cases(case_id, site_id)
);

CREATE TABLE cases_experiment
(
    case_id int,
    case_site_id int,
    trial_id int,
    batch_id int,
    PRIMARY KEY (case_id, case_site_id, trial_id, batch_id),
    FOREIGN KEY (case_id, case_site_id) REFERENCES cases (case_id, site_id),
    FOREIGN KEY (trial_id, batch_id) REFERENCES experiment(trial_id, batch_id)
);

CREATE TABLE symptom
(
    symptom_id int,
    symptom_name VARCHAR(20),
    symptom_description VARCHAR(100),
    PRIMARY KEY (symptom_id)
);

CREATE TABLE case_develop
(
    site_id int,
    case_id int,
    develop_date date,
    symptom_id int,
    PRIMARY KEY (site_id, case_id, develop_date),
    FOREIGN KEY (site_id, case_id) REFERENCES cases(site_id, case_id),
    FOREIGN KEY (symptom_id) REFERENCES symptom(symptom_id)
);

CREATE TABLE comorbidity
(
    comorbidity_id int,
    comorbidity_name VARCHAR(20),
    comorbidity_description VARCHAR(50),
    PRIMARY KEY (comorbidity_id)
);

CREATE TABLE comorbidity_case
(
    site_id int,
    case_id int,
    comorbidity_id int,
    PRIMARY KEY (site_id, case_id, comorbidity_id),
    FOREIGN KEY (site_id, case_id) REFERENCES cases(site_id, case_id),
    FOREIGN KEY (comorbidity_id) REFERENCES comorbidity(comorbidity_id)
);
