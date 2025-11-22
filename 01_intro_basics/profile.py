def print_profile(name,age,profession,skills):
  print("*********** prrsonal profile card ***********")
  print(f"name: {name}")
  print(f"age : {age}")
  print(f"profession: {profession}")
  print(f"skills: ")
  for skill in skills:
    print(f"- {skill}")
  print("*******************************************")

# Define your personal information
name = "saeid ptzl"
age = 28
profession = "Software Developr"
skills = ["Python", "JavaScript", "Machine Learning", "css and html"]

# Call the function to display the profile
print_profile(name, age, profession, skills)
