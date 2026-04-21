import pandas as pd

# Load your data into a dataFrame
df = pd.read_csv("clothing_data.csv")
# print(df)

print("Yzybot: Hello there, I am your yeezy clothing assistance bot. Ask me about any yeezy clothes shopping advice")


while True:
    #1.  Get the user input and store the same into a variable
    user_text = input("\n You: ").lower()

    # 2.Check if the users want to exit
    if user_text == "quit":
        print("Yzybot: Goodbye!  Nice to have been of service to you.")
        break

    # Create a variable that will store the details structured in the csv file
    found_answer = False

    # come up with a loop that loops through the entire data frame created before.
    for index, row in df.iterrows():
        # clean up the keywords from the CSV row
        keywords_list = str(row["Keyword"]).split(',')

        # Below we check every keyword in that given row (Keywords)

        for word in keywords_list:
            clean_word = word.strip().lower()

            # if the keyword is inside of the user's sentence
            if clean_word in user_text:
                print("Yzybot:", row["Response"])
                found_answer = True
                break

            if found_answer:
                break # Stop looking at other answers since we already found a match

            # 4.If we went through the entire/whole CSV file and never found any match of the keywords,
            # we need to display a message to the user

            if not found_answer:
                print("Yzybot: Sorry, i don't know that one, Try asking for something else.")


