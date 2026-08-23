# Core Backend Processing Algorithm for AI Job Skill Gap Analyzer

def analyze_skill_gap(target_role, user_skills_list):
    # Simulated SQL Database Matrix Fetch
    database_records = {
        'Python Developer': ['python', 'django', 'flask', 'sql', 'git', 'docker', 'rest api'],
        'Data Analyst': ['sql', 'excel', 'python', 'pandas', 'tableau', 'power bi', 'statistics'],
        'Web Developer': ['html', 'css', 'javascript', 'react', 'node.js', 'git', 'mongodb']
    }
    
    # Validation Safety Check: Ensure the requested job title exists inside the matrix
    if target_role not in database_records:
        return "Error: Selected job role could not be located in our system."
        
    # Convert text strings into formal Python Data Sets for logical computation
    required_set = set(database_records[target_role])
    user_set = set([skill.strip().lower() for skill in user_skills_list])
    
    # Execute relational set subtraction to isolate missing core items
    missing_skills = required_set - user_set
    
    # Calculate an exact technical overlap ratio percentage metrics
    total_count = len(required_set)
    matched_count = len(required_set & user_set)
    match_percentage = round((matched_count / total_count) * 100)
    
    return {
        "job_title": target_role,
        "current_match_score": f"{match_percentage}%",
        "skills_to_learn": list(missing_skills) if missing_skills else ["None! Profiles match 100%"]
    }

# --- SYSTEM SANDBOX TEST EXECUTION ---
# Simulating a student checking a 'Data Analyst' role with custom profile metrics
my_skills = ['Excel', 'SQL', 'Tableau']
evaluation_output = analyze_skill_gap('Data Analyst', my_skills)

print("--- AI EVALUATION MATRIX ENGINE RUNNING ---")
print(f"Target Career: {evaluation_output['job_title']}")
print(f"Calculated Score: {evaluation_output['current_match_score']}")
print(f"Missing Core Competencies: {evaluation_output['skills_to_learn']}")
