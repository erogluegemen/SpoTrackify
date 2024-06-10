# SpoTrackify

## Overview
SpoTrackify is a simple tool designed to monitor your Spotify follower count. With SpoTrackify, you can easily track changes in your follower numbers and receive notifications to stay informed about your audience growth on Spotify.

## Features
- Track your Spotify follower count.
- Receive notifications about changes in your follower numbers.
- Stay informed about your audience growth effortlessly.

## Getting Started
To use SpoTrackify, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies.
3. Configure your Spotify API credentials.
4. Run the Trackify application.
5. Sit back and let Trackify monitor your Spotify follower count!

## Dependencies
Trackify relies on the following dependencies:
- [Python](https://www.python.org/) (version 3.0 or higher)
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) (for interacting with the Spotify API)
- [Requests](https://docs.python-requests.org/en/latest/) (for sending HTTP requests)
- [Python-dotenv](https://pypi.org/project/python-dotenv/) (for managing environment variables)

## Configuration
Before running Trackify, make sure to configure your Spotify API credentials. You can do this by creating a `.env` file in the root directory of the project and adding your credentials as follows:

```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
```

## Usage
To start using Trackify, simply run the `spotrackify.py` script:

```
python spotrackify.py
```

## Contributing
Contributions to Trackify are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.
