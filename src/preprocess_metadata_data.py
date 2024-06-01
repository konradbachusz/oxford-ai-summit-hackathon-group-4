
import pandas as pd



# Read images.csv and styles.csv into pandas DataFrames
images_df = pd.read_csv("data/images.csv")

images_df[["id", "extension"]] = images_df["filename"].str.split(".", expand=True)
images_df=images_df[["id", "link","filename"]]
images_df.id=images_df.id.astype(str)

images_df.head()




styles = pd.read_csv("data/styles.csv",on_bad_lines='skip')
styles.id=styles.id.astype(str)
styles.head()


# Merge images_df and styles on the "filename" column
merged_df = pd.merge(images_df, styles, left_on="id", right_on="id", how="inner")

merged_df=merged_df[['id','link','filename','articleType']]
# Display the head of the merged DataFrame
merged_df.head()


merged_df.to_csv("data/processed_metadata.csv",index=False)




