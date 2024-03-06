import instaloader

def download_instagram_posts(account_name):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Load the profile of the account
        profile = instaloader.Profile.from_username(loader.context, account_name)
        
        # Iterate over each post and download it
        for post in profile.get_posts():
            loader.download_post(post, target=account_name)

        print("Download completed successfully!")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Error: Account not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
download_instagram_posts("example_account")
