from tiktok_analysis.data_processing import DataProcessor
from tiktok_analysis.campaign import Campaign

def main():
    csv_path = 'data/tiktok_creators.csv'
    df = DataProcessor.load_data(csv_path)

    campaign = Campaign(
        target_audience="Gen Z content creator, aged 16 to 35, with content primarily in English",
        briefing="Knowledge of gaming, especially RPGs or simulation games",
        guideline="Infuse videos with humor, creativity, and artistic elements. Skilled in storytelling.",
        min_followers=500000,
        max_followers=1300000,
        required_hashtags=['#gaming', '#RPG', '#simulation'],
        location="USA"
    )

    eligible_creators = campaign.find_eligible_creators(df)
    print("Eligible Creators:\n", eligible_creators)

if __name__ == '__main__':
    main()
