from openai import OpenAI
import os
import streamlit as st

client = OpenAI(api_key=os.environ['openai_ai_key'])

def story_gen(prompt):
  system_prompt = '''you are a world renowned 50 years experience storyteller. you will be given a concept to generate a story suitable for ages 5-7 years old''' 


  response = client.chat.completions.create( 
    model="gpt-4o-mini", 
    messages=[ 
      {"role": "system", "content": system_prompt}, 
      {"role": "user", "content": prompt} 
    ] ,
    temperature=1.3,
    max_tokens= 200
  )
  return response.choices[0].message.content

def cover_gen(prompt):
  system_prompt = '''you will be given a storybook. generate a prompt for a cover art that is suitable for the storybook. the prompt will be sent to dall-e-2.''' 


  response = client.chat.completions.create( 
    model="gpt-3.5-turbo", 
    messages=[ 
      {"role": "system", "content": system_prompt}, 
      {"role": "user", "content": prompt} 
    ] ,
    temperature=1.3,
    max_tokens= 100
  )
  return response.choices[0].message.content

def image_gen(prompt):
  response = client.images.generate(
    model = 'dall-e-2',
    prompt=prompt,
    n=1,
    size="1024x1024"
  )
  return response.data[0].url

st.title("Storybook Generator for Kids for fun")
st.divider()

prompt=st.text_area("Enter your story concept:")

if st.button("generate storybook"):
  story=story_gen(prompt)
  cover=cover_gen(story)
  image=image_gen(cover)

  st.image(image)
  st.write(story)