{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "61051960-2dbe-4e05-b32c-b12c25baa1e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data processing complete. Output saved to formatted_output.csv.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# Define the full path to the data folder\n",
    "data_folder = r\"C:\\Users\\91966\\OneDrive\\Desktop\\data\"\n",
    "\n",
    "# Initialize an empty DataFrame to store the combined results\n",
    "all_data = pd.DataFrame(columns=[\"sales\", \"date\", \"region\"])\n",
    "\n",
    "# Process each CSV file in the data folder\n",
    "for file_name in os.listdir(data_folder):  # Correct usage\n",
    "    if file_name.endswith(\".csv\"):\n",
    "        file_path = os.path.join(data_folder, file_name)\n",
    "        \n",
    "        # Load the CSV file\n",
    "        df = pd.read_csv(file_path)\n",
    "        \n",
    "        # Filter for \"Pink Morsels\" only\n",
    "        df = df[df[\"product\"] == \"Pink Morsels\"]\n",
    "        \n",
    "        # Add a \"sales\" column\n",
    "        df[\"sales\"] = df[\"quantity\"] * df[\"price\"]\n",
    "        \n",
    "        # Keep only the required columns\n",
    "        df = df[[\"sales\", \"date\", \"region\"]]\n",
    "        \n",
    "        # Append to the combined DataFrame\n",
    "        all_data = pd.concat([all_data, df], ignore_index=True)\n",
    "\n",
    "# Save the combined and processed data to a new CSV file\n",
    "output_file = \"formatted_output.csv\"\n",
    "all_data.to_csv(output_file, index=False)\n",
    "\n",
    "print(f\"Data processing complete. Output saved to {output_file}.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0c0869f-a30d-4ee2-876f-6f5578d32631",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
