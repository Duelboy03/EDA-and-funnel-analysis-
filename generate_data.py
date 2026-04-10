#importing all the python modules and faker for creating a fake dataset
import pandas as pd
import random 
from faker import Faker
from datetime import datetime,timedelta

fake = Faker()
data = []

#Defining the business universe(Parameters of my fake company for visualization)
stages =['Browse','Add to Cart','Checkout','Purchase']
devices = ['Desktop','Mobile','Laptop']
regions = ['North','South','East','West']
channels = ['Organic','Google Ads','Social Media','Email']
categories = ['Electronics','Fashion','Home','Beauty','Sports']



#Creating the users(This is the main loop that generates user attributes)
for i in range(1,10001):
    user_id = f"USR{i:05d}"
    session_id = f"SESS{fake.uuid4()[:8]}"
    start_time = fake.date_time_between(start_date="-30d", end_date="now")

    device = random.choice(devices)
    region = random.choice(regions)
    channel = random.choice(channels)
    category = random.choice(categories)

#randomly simulating customer behaviour 
    rand_val = random.random()
    if rand_val < 0.30:
        final_stage_idx = 3 
    elif rand_val < 0.50:
        final_stage_idx = 2
    elif rand_val < 0.70:
        final_stage_idx =1 
    else:
        final_stage_idx = 0

#EVent simulation for funnel analysis
    current_time = start_time
#move through stages
    for stage_idx in range(final_stage_idx + 1):
        stage= stages[stage_idx]
        revenue = round(random.uniform(200,2000), 2) if stage == 'Purchase' else 0.0
#store each step 
        data.append({
            'User_ID': user_id,
            'Session_ID': session_id,
            'Timestamp':current_time.strftime("%Y-%m-%d %H:%M:%S"),
            'Event': stage,
            'Device': device,
            'Region': region,
            'Channel': channel,
            'Product_category': category,
            'Revenue': revenue
        })
#increment between actions
        current_time += timedelta(minutes=random.randint(2,5))

df = pd.DataFrame(data)
df.to_csv('funnel_analysis_data.csv', index = False)
print(f"Success! Generated {len(df)} rows of event data and saved to 'funnel_analysis_data.csv'")