import pandas as pd
import pickle

filename = 'list_of_column_names.sav'
model_columns = pickle.load(open(filename, 'rb'))


def transform_categorical_feature(
    df: pd.DataFrame, column_name: str
) -> pd.DataFrame:
    """
    creates columns of binary values from categorical textual information
    """

    df1 = pd.get_dummies(df[column_name].astype(str))
    new_df = pd.concat([df, df1], axis=1)

    # we don't need transformed column anymore
    new_df = new_df.drop(columns=[column_name])
    return new_df

# df = pd.DataFrame(item, index=[0], columns=model_columns).fillna(0)
# item = {"subtype": "CASTLE"}
# df[item['subtype']] = 1

def preprocess(house_data):
    
    df = transform_categorical_feature(house_data, "subtype", "is_subtype_")
    df = transform_categorical_feature(
        df, "building_condition", "is_building_condition_"
    )
    df = transform_categorical_feature(df, "location", "zipcode_")

    # for key, value in df.items():
    #     return

    # house_data.get("")
