marks = {
    "Hamid": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Hamid"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Hamid": 99, "Renuka": 100})
# print(marks)

print(marks.get("Hamid2")) # Prints None
print(marks["Hamid2"]) # Returns an error