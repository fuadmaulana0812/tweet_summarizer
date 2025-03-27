import pandas as pd

async def read_user():
    df = pd.read_excel('Twitter Accounts_DeSci AI Agent_210325.xlsx', skiprows=2)

    # Filter rows where "Twitter Account" starts with "https"
    df_filtered = df[df["Twitter Account"].astype(str).str.startswith("https")].copy()

    # Extract username from the "Twitter Account" URL
    df_filtered.loc[:, "Username"] = df_filtered["Twitter Account"].str.extract(r"https://x\.com/([^/]+)")

    # Convert the usernames to a list
    user_list = df_filtered["Username"].tolist()

    return user_list

async def export_txt(formatted_tweets):
    with open("output_tweets.txt", "a", encoding="utf-8") as f:
        f.write("\n\n\n")
        f.write(formatted_tweets)
    print("✅ Tweets exported to output_tweets.txt")