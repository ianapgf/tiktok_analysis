class Campaign:
    def __init__(self, target_audience, briefing, guideline, min_followers, max_followers, required_hashtags, location):
        self.target_audience = target_audience
        self.briefing = briefing
        self.guideline = guideline
        self.min_followers = min_followers
        self.max_followers = max_followers
        self.required_hashtags = required_hashtags
        self.location = location

    def is_creator_eligible(self, creator):
        try:
            if not self.min_followers <= creator['Followers'] <= self.max_followers:
                return False
            if not any(hashtag in creator['Hashtags'] for hashtag in self.required_hashtags):
                return False
            if creator['Location'] != self.location:
                return False
            return True
        except Exception as e:
            raise RuntimeError(f"Error checking creator eligibility: {e}")

    def find_eligible_creators(self, df):
        try:
            eligible_creators = df[df.apply(self.is_creator_eligible, axis=1)]
            return eligible_creators
        except Exception as e:
            raise RuntimeError(f"Error finding eligible creators: {e}")
