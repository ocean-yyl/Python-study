#encoding=utf-8
def generate_webform(field_dict_list):
	generated_field_list = []
	"""
	map(func, *iterables) --> return iterables
	map 接受一个iterables 经过函数处理,并返回一个迭代器iter
	"""
	for field_dict in field_dict_list:
		if field_dict["type"] == "text":
			# print(field_dict)
			field_html = generate_text_field(field_dict)
			generated_field_list.append(field_html)
		elif field_dict["type"] == "checkbox":
			# print(field_dict)
			field_html = generate_checkbox(field_dict)
			generated_field_list.append(field_html)
	print(generated_field_list)
	generate_fields = "\n".join(generated_field_list)
	return "<form>{fields}</form>".format(fields=generate_fields)

def generate_text_field(text_field_dict):
	return '{0}:<br><input type="text" name="{1}"><br>'.format(
			text_field_dict["label"],
			text_field_dict["name"]
		)


def generate_checkbox(checkbox_dict):
	return '<lable><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
		checkbox_dict["id"],
		checkbox_dict["value"],
		checkbox_dict["label"]
	)


def build_html_form(field_dict_list):
	with open("form_file.html","w") as f:
		f.write(
			"<html><body>{}</body></html>".format(
				generate_webform(
					field_dict_list
				))
		)

if __name__ == '__main__':
	field_dict_list=[
		{
			"type":"text",
			"label":"Best text you hace written",
			"name":"best_text",
		},
		{
			"type":"checkbox",
			"id":"check_it",
			"value":"1",
			"label":"check for one",
		},
		{
			"type": "text",
			"label": "2 text you hace written",
			"name": "2_text",
		},
	]
	build_html_form(field_dict_list)
