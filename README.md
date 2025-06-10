# Nama: Farhan Riyandi

## Task 1: Project Initialization
1. Create a new directory on your computer named customer-churn-analysis.
   ![image](https://github.com/user-attachments/assets/9059b148-7f19-4367-9414-7ec23a24e02a)

2. Navigate into this new directory.
   ![image](https://github.com/user-attachments/assets/24a99f71-927e-4859-8d9c-f858a38c1c19)

3. Initialize a new public Git repository.
   ![image](https://github.com/user-attachments/assets/df13eba0-a056-4d63-90c8-0f396f6f2f54)

## Task 2: Initial Commit
1. Create a Python file named analysis.py.
   ![image](https://github.com/user-attachments/assets/7088b8bd-40ca-46a6-b789-6b8450fd5ca8)

2. Inside analysis.py, add the following code:
   ```
   import pandas as pd
   def load_data(file_path):
      """Loads data from a CSV file."""
      return pd.read_csv(file_path)
   print("Data loading function created.")
   ```
   ![image](https://github.com/user-attachments/assets/03ff4d1d-3ce1-4e47-9c9a-38d1cb3b38e6)
   ![image](https://github.com/user-attachments/assets/77e059ba-7be5-4239-b538-2a5e1b8f8d1f)

3. Create a .gitignore file.
   ![image](https://github.com/user-attachments/assets/42fdfd55-190f-4091-b350-d8a609a10610)

4. Inside .gitignore, add the following lines to prevent data files and environment folders from being tracked:
   ```
   *.csv
   data/
   .ipynb_checkpoints/
   __pycache__/
   venv/
   ```
   ![image](https://github.com/user-attachments/assets/fdee9792-dab5-45b9-85df-1f5f6242c0e6)
   ![image](https://github.com/user-attachments/assets/42d69593-b4bb-4080-ad34-763930d70fb3)

5. Stage both analysis.py and .gitignore.
   ![image](https://github.com/user-attachments/assets/2ec21612-a9e1-496f-bce4-17209ee595d1)

6. Commit the staged files with the message: feat: Initial commit with data loading script
   ![image](https://github.com/user-attachments/assets/b4404c16-d3a4-438c-87c4-9859e53210c8)
   ![image](https://github.com/user-attachments/assets/af2655ed-1a5d-4b88-ab44-72a5e857da2d)

## Task 3: Feature Development with Branching
1. Create a new branch called feature/data-visualization.
   ![image](https://github.com/user-attachments/assets/ab95313a-f1b0-4bef-9d5d-8576260e5255)

2. Switch to the new branch.
   ![image](https://github.com/user-attachments/assets/63108541-5aa7-469f-b84e-f4d9bce242d1)

3. Modify analysis.py by adding a new function to generate a summary plot:
   Python
   ```
   import pandas as pd
   import matplotlib.pyplot as plt
   
   def load_data(file_path):
       """Loads data from a CSV file."""
       return pd.read_csv(file_path)

   def plot_churn_distribution(df):
       """Plots the distribution of the churn column."""
       df['churn'].value_counts().plot(kind='bar')
       plt.title('Customer Churn Distribution')
       plt.xlabel('Churn')
       plt.ylabel('Count')
       plt.show()

   print("Added data visualization function.")
   ```
   ![image](https://github.com/user-attachments/assets/dc8feaa6-4e3a-438f-bf65-f6f5966032c8)
   ![image](https://github.com/user-attachments/assets/f225891b-29da-4bb8-a2aa-57bf2ffd76ef)

4. Stage the changes in analysis.py.
   ![image](https://github.com/user-attachments/assets/c4e488ff-c716-43ea-966a-b9343b8b1802)

5. Commit the changes with the message: feat: Add function to plot churn distribution
   ![image](https://github.com/user-attachments/assets/0bb86073-21f5-42b1-ae3d-61d2f3e262e5)
   ![image](https://github.com/user-attachments/assets/14106f02-62d6-429e-adab-6195eed1d2f1)

## Task 4: Merging the Feature
1. Switch back to the main branch.
   ![image](https://github.com/user-attachments/assets/6b6941b8-90e0-4b58-b77e-3ad4c1acf419)

2. Merge the feature/data-visualization branch into main.
   ![image](https://github.com/user-attachments/assets/cf1a3b0c-2387-4a38-a3d4-b8a73e6c7a96)
   ![image](https://github.com/user-attachments/assets/0d8577b8-4e8e-4854-9ff3-87939d83f894)

3. (Optional Cleanup) Delete the feature/data-visualization branch.
   * Delete local branch
     ![image](https://github.com/user-attachments/assets/60e1e75d-787d-4dfc-988d-e48417bf94a6)

   * Delete branch in Github
     ![image](https://github.com/user-attachments/assets/f041cac1-f3ce-4e3c-b83d-fa2a26255478)

