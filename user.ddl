CREATE TABLE user (
    user_id integer primary key autoincrement not null
    , account_id varchar(50) not null
    , emp_no varchar(50) not null
    , email varchar(255) not null
    , password varchar(255) not null
    , user_nm varchar(100) not null
    , user_nm_kn varchar(100) not null
    , user_nm_en varchar(100) not null
    , join_dt varchar(8) not null
    , quit_dt varchar(8) null
    , version_no integer not null
    , created_at timestamp not null
    , created_by varchar(50) not null
    , updated_at timestamp not null
    , updated_by varchar(50) not null
    , is_actived varchar(1) not null
);
