from django.shortcuts import render
from happytransformer import HappyTextToText
from happytransformer import TTSettings


def home_fun(request):
    result = ""
    user_input_text = ""
    if request.method == 'POST':
        user_input_text = str(request.POST.get('text', ''))
        if user_input_text:  # Check if input text exists
            happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
            top_k_sampling_settings = TTSettings(do_sample=True, top_k=50, temperature=0.7, min_length=1, max_length=1000)
            results = happy_tt.generate_text(user_input_text, args=top_k_sampling_settings)
            result=results.text
    
    return render(request, 'home.html', {'result': result,'user_input_text':user_input_text})