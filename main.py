import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Bulbasaur",
            "Charmander",
            "Squirtle"
        ],
        "Type":[
            "Grass",
            "Fire",
            "Water"
        ],
        "Gender":[
            "Female",
            "Male",
            "Male"
        ],
        "Level":[
            50,
            45,
            89
        ]
    }
)
#print(df)
types = pd.Series(["Grass", "Fire", "Water"], name="Type")
#print(types)
maximus_level = df["Level"].max()
#print(f"the maximus level is: {maximus_level}")
#print(df.count())
different_from_50 = df.loc[df["Level"]!= 50] 
#print(different_from_50)
total_level_sum = df["Level"].sum()
print(f"The total sim off all levels is: {total_level_sum}")


