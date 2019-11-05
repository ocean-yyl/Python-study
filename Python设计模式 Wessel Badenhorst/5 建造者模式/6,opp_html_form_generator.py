# encoding=utf-8

class HtmlField(object):
	def __init__(self, **kwargs):
		self.html = ""

		if kwargs["type"] == "text":
			self.html = self.construct_text_field(kwargs["label"],
												  kwargs["name"])
		elif kwargs["type"] == "checkbox":
			self.html = self.construct_checkbox(kwargs["id"],
												kwargs["value"],kwargs["label"])

	def construct_text_field(self, label, field_name):
		return '{0}:<br><input type="text" name="{1}"><br>'.format(
			label,
			field_name
		)

	def construct_checkbox(self, field_id, value, label):
		return '<lable><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
			field_id, value, label
		)

	def __str__(self):
		return self.html


def generate_webform(field_dict_list):
	generated_field_list = []
	for field in field_dict_list:
		try:
			generated_field_list.append(str(HtmlField(**field)))
		except Exception as e:
			print("erro->",e)
	generate_fields = "\n".join(generated_field_list)
	return "<form>{fields}</form>".format(fields=generate_fields)

def build_html_form(field_list):
	with open("form_file.html", "w") as f:
		f.write(
			"<html><body>{}</body></html>".format(
				generate_webform(
					field_list
				))
		)


if __name__ == '__main__':
	field_dict_list = [
		{
			"type": "text",
			"label": "Best text you hace written",
			"name": "best_text",
		},
		{
			"type": "checkbox",
			"id": "check_it",
			"value": "1",
			"label": "check for one",
		},
		{
			"type": "text",
			"label": "2 text you hace written",
			"name": "2_text",
		},
	]
	build_html_form(field_dict_list)

