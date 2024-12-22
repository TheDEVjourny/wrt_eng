import google.generativeai as genai
import textwrap
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, ' ', predicate=lambda _: True))

# do prompt
def do_gmni_processing(prompt,API_KEY ):
    API_KEY = API_KEY.replace("#",'').replace("%",'').replace("!",'')
    genai.configure(api_key=API_KEY)
    
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         print(m.name)

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    message = to_markdown(response.text).data
    return message

def get_gpt_response(req_data,GEMINI_API_KEY):
    print(req_data)
    answer = 'no response from AI'
    
    try:
        prompt = f"enhance the mentioned paragraph '{req_data['title']}' like a professionals, where the consept is {req_data['context']} "
        answer = do_gmni_processing(prompt,GEMINI_API_KEY)
        prompt = f"please give sugessions only for improvements in my writing skill"
        sugession = do_gmni_processing(prompt,GEMINI_API_KEY)
        sugession = sugession.replace('**',':\n').replace('*',"")
        print(sugession)
    except:
        print('issue in gpt')
        
    ans_dict ={
        'text': answer,
        'sugession': sugession
    }

    return ans_dict

