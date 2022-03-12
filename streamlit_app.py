from __future__ import unicode_literals
from yt_dlp import YoutubeDL
import streamlit as st
import pyshorteners as sh

st.title("YT Video Link Generator")

yt_link = st.text_input("Enter Youtube video URL")

ydl_opts = {}
links_dict = {}
if yt_link != '':
	with YoutubeDL(ydl_opts) as ydl:
		test = ydl.extract_info(str(yt_link), download = False)

	fmts =  test.get("formats", None)
	for each in fmts:
		if each.get('ext',None) == 'mp4' and each.get('protocol',None) == 'https' \
		and each.get('vcodec',None).startswith('avc'):
			if each.get('acodec') != 'none':
				links_dict[each.get('format_note') + ' (with audio)'] = each.get('url')
			else:
				links_dict[each.get('format_note')] = each.get('url')

	
	# st.write('\n HTTP link is \n', yt_url)		
	physical_form = st.selectbox("Select format", options=links_dict.keys())
                        
submit = st.button("Submit")

if submit:
    st.write("Video link is: \n\n\n ", links_dict[physical_form])

    shortener = sh.Shortener()
    try:
    	short_url = shortener.tinyurl.short(links_dict[physical_form])
    	st.write("\n\nShortened link: \n", short_url)
    except:
    	st.write('\n\nCannot connect to TinyURL server to create a short link.')

    # st.write(shortener.tinyurl.expand(short_url))


