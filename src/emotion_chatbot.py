import pandas as pd
import random
import streamlit as st

# This is to suppress the warning messages (if any) generated in our code
import warnings
warnings.filterwarnings('ignore')

# Read the data
df_lyrics = pd.read_csv("lyric_emotion.csv")
df_song = pd.read_csv("song_emotion.csv")

def find_quotes(df_lyrics, df_song, emotions, num_quotes=10):
    matching_quotes = []
    playlist = []

    # Retrieve the Song Name that matches the emotions
    for index, row in df_song.iterrows():
        if row['Emotion'] in emotions:
            playlist.append(row['Song Name'])

    # Iterate over each song in the playlist
    for song in playlist:
        # Filter DataFrame to get rows for the current song and matching emotion
        song_lyrics = df_lyrics[(df_lyrics['Song Name'] == song) & df_lyrics['Emotion'].isin(emotions)]

        # Iterate over the lyrics for the current song
        for index, row in song_lyrics.iterrows():
            matching_quotes.append((row['Lyric Line'], row['Song Name'], row['Emotion']))

    # Randomly select num_quotes number of quotes if more are found
    random.shuffle(matching_quotes)
    return matching_quotes[:num_quotes], playlist

def main():
    st.title("Playlist Recommendation based on Emotions")
    user_input_emotions = st.text_input("Enter emotions separated by commas (e.g., happy, sad):")

    if st.button("Generate Playlist"):
        emotions = [emotion.strip() for emotion in user_input_emotions.split(',')]
        st.write(f"Emotions you feel: {emotions}")

        quotes, playlist = find_quotes(df_lyrics, df_song, emotions)

        # Display the list of songs
        st.write("Your playlist based on these emotions will have the following songs:")
        st.write("Playlist:", playlist)

        # Display the results
        st.write("\nLyrics from songs matching your feelings:\n")
        for lyric, song, emotion in quotes:
            st.write(f"Lyric: {lyric} \nFrom the song: {song}, matching the emotion ({emotion.strip()})\n\n")

if __name__ == "__main__":
    main()
