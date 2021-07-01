import pandas as pd

main_data = pd.read_csv("input_third_slot_data.csv")
print("155 Brands in total:==")
print("------------------------")
print(main_data)

third_lot = pd.read_csv("metaData_pages_third_slot.csv", names=['pages', 'url'])
print("---------------------------")
print("---------------------------")
print("Third Lot - Data")
print("---------------------------")
scrapped = third_lot.url.unique()
tbl = pd.DataFrame(scrapped, columns = ['url'])
print(tbl)

print("---------------------------")
print("---------------------------")
print("New Input Data - Fourth Lot")
new_data = main_data[~main_data['url'].isin(tbl['url'])]
print(new_data)
new_data.to_csv("input_fourth_slot_data.csv", index=False)
