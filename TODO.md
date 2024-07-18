README
users -> User Model(with role) + Role Model + Factory Model + UserFactory Model
invoices -> Model(status, total price, date of order, date of ...(eachProcess)), new orders and previous orders can be filtered by status
blocks -> price for showing in invoice + status (available, sold(ordered, applied))
mines
factories
app name > module > method or var or ... > more depth ... : description
blocks > pop_pics_ids ViewSet method
blocks > add_vids_ids ViewSet method
blocks > pop_vids_ids ViewSet method
Pic > signals > post delete: pop_pics_ids 
Vid > signals > post delete: pop_vids_ids
blocks > pic_reorder ViewSet method: takes 2 args: pic_id (not index of it in pics list), idx to insert
blocks > vid-reorder ViewSet method: takes 2 args: pic_id (not index of it in pics list), idx to insert

captcha:
```
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json

class AjaxExampleForm(CreateView):
    template_name = ''
    form_class = AjaxForm

    def form_invalid(self, form):
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['status'] = 0
            to_json_response['form_errors'] = form.errors

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['status'] = 1

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')
```