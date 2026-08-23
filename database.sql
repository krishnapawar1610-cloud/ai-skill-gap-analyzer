-- Core SQL Database Table Setup for AI Skill Gap Analyzer
CREATE TABLE jobs_repository (
    id INT PRIMARY KEY,
    job_role VARCHAR(100),
    required_skills TEXT
);

-- Insert Structural Baseline Corporate Skill Data Metrics
INSERT INTO jobs_repository (id, job_role, required_skills) VALUES
(1, 'Python Developer', 'python, django, flask, sql, git, docker, rest api'),
(2, 'Data Analyst', 'sql, excel, python, pandas, tableau, power bi, statistics'),
(3, 'Web Developer', 'html, css, javascript, react, node.js, git, mongodb');
