CREATE TABLE IF NOT EXISTS Student (
  id INTEGER UNIQUE NOT NULL,
  password TEXT NOT NULL,
  user_type CHAR NOT NULL, 
  username TEXT NOT NULL,
  user_dept TEXT NOT NULL, 
  user_yr INTEGER NOT NULL,
  phone_no INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Teacher (
  id INTEGER UNIQUE NOT NULL,
  password TEXT NOT NULL,
  user_type CHAR NOT NULL, 
  username TEXT NOT NULL,
  user_dept TEXT NOT NULL, 
  phone_no INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Courses (
  teacher_id INTEGER NOT NULL,
  student_id INTEGER NOT NULL,
  course_id INTEGER UNIQUE NOT NULL,
  course_name TEXT NOT NULL
);