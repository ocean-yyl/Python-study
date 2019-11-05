#encoding=utf-8
def generate_webform(text_field_list=[],checkbox_field_list=[]):
	"""
	map(func, *iterables) --> return iterables
	map 接受一个iterables 经过函数处理,并返回一个迭代器iter
	"""

	generate_fields = "\n".join(
		map(
			lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x),
			text_field_list
		)
	)

	generate_fields += "\n".join(
		map(
			lambda x: '<lable><input type="checkbox" id="{0}" value="{0}">{0}<br>'.format(x),
			checkbox_field_list
		)
	)

	return "<form>{fields}</form>".format(fields=generate_fields)


def build_html_form(text_field_list=[],checkbox_field_list=[]):
	with open("form_file.html","w") as f:
		f.write(
			"<html><body>{}</body></html>".format(
				generate_webform(
					text_field_list,
					checkbox_field_list
				))
		)

if __name__ == '__main__':
	text_field_list = ['name', 'age', 'email', 'telephone']
	checkbox_field_list = ["check1","check2","check3"]
	build_html_form(text_field_list,checkbox_field_list)
