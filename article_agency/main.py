from crew import crew

result = crew.kickoff(inputs={"topic": "Artifical Intelligence"})

with open("output.txt", "w") as file:
    file.write(result)