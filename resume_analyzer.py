def read_resume(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print("❌ Resume file not found.")
        return ""


def extract_skills(text):
    if text == "":
        return []

    if "Skills:" not in text:
        print("❌ Skills section not found in resume.")
        return []

    start = text.find("Skills:")
    skills_text = text[start:]
    skills = skills_text.replace("Skills:", "").strip().splitlines()

    return skills


def clean_skills(skills):
    cleaned = []

    for skill in skills:
        skill = skill.strip()

        if skill != "":
            cleaned.append(skill)

    return cleaned


def prepare_skills(skills):
    unique_skills = set()

    for skill in skills:
        unique_skills.add(skill.lower())

    return unique_skills


def find_matched_skills(required_skills, resume_skills):
    matched = []

    for skill in required_skills:
        if skill.lower() in resume_skills:
            matched.append(skill)

    return matched


def find_missing_skills(required_skills, resume_skills):
    missing = []

    for skill in required_skills:
        if skill.lower() not in resume_skills:
            missing.append(skill)

    return missing


def calculate_percentage(total, matched):
    if total == 0:
        return 0

    percentage = (matched / total) * 100

    return round(percentage, 2)


def generate_suggestions(missing_skills):
    suggestions = []

    for skill in missing_skills:

        if skill == "SQL":
            suggestions.append(
                "Learn SQL for database querying and data analysis."
            )

        elif skill == "Data Visualization":
            suggestions.append(
                "Learn Matplotlib, Seaborn, and dashboard creation."
            )

        elif skill == "Power BI":
            suggestions.append(
                "Learn Power BI and practice creating dashboards."
            )

        elif skill == "Statistics":
            suggestions.append(
                "Strengthen statistics, probability, and hypothesis testing."
            )

        elif skill == "Machine Learning":
            suggestions.append(
                "Practice supervised and unsupervised machine learning."
            )

        elif skill == "Python":
            suggestions.append(
                "Strengthen Python programming and problem-solving."
            )

        elif skill == "Pandas":
            suggestions.append(
                "Practice Pandas for data cleaning and analysis."
            )

        elif skill == "NumPy":
            suggestions.append(
                "Practice NumPy arrays and numerical operations."
            )

        elif skill == "Git and GitHub":
            suggestions.append(
                "Learn Git commands and practice GitHub projects."
            )

    return suggestions


required_skills = [
    "Python",
    "SQL",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Data Visualization",
    "Power BI",
    "Statistics",
    "Git and GitHub"
]


resume_content = read_resume("resume.txt")


if resume_content == "":
    print("\n❌ Analysis stopped.")
    print("Please check your resume file.")

else:

    resume_skills = extract_skills(resume_content)

    if len(resume_skills) == 0:

        print("\n❌ Analysis stopped.")
        print("Please add a Skills section to your resume.")

    else:

        cleaned_skills = clean_skills(resume_skills)

        prepared_skills = prepare_skills(cleaned_skills)

        matched_skills = find_matched_skills(
            required_skills,
            prepared_skills
        )

        missing_skills = find_missing_skills(
            required_skills,
            prepared_skills
        )

        match_percentage = calculate_percentage(
            len(required_skills),
            len(matched_skills)
        )

        suggestions = generate_suggestions(missing_skills)


        print("\n==========================================")
        print("          RESUME ANALYZER")
        print("==========================================")

        print("\n📄 Resume Status: Successfully Analyzed")

        print("\n📊 Total Required Skills:", len(required_skills))

        print("✅ Matched Skills:", len(matched_skills))

        print("❌ Missing Skills:", len(missing_skills))

        print("📈 Match Percentage:", match_percentage, "%")


        print("\n------------------------------------------")
        print("           MATCHED SKILLS")
        print("------------------------------------------")

        for skill in matched_skills:
            print("✅", skill)


        print("\n------------------------------------------")
        print("           MISSING SKILLS")
        print("------------------------------------------")

        for skill in missing_skills:
            print("❌", skill)


        print("\n------------------------------------------")
        print("           SKILL SUGGESTIONS")
        print("------------------------------------------")

        for suggestion in suggestions:
            print("👉", suggestion)


        print("\n==========================================")
        print("          ANALYSIS COMPLETED")
        print("==========================================")