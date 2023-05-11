#!/bin/env python
#coding=utf-8

import os
import openai
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completions(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
            )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            )
    time.sleep(20)
    return response.choices[0].message["content"]
