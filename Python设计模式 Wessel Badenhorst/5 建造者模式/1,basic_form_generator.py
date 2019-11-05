def generate_webform(field_list):
	"""
	map(func, *iterables) --> return iterables
	map 接受一个iterables 经过函数处理,并返回一个迭代器iter
	"""

	generate_fields = "\n".join(
		map(
			lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x),
			field_list
		)
	)

	return "<form>{fields}</form>".format(fields=generate_fields)


if __name__ == '__main__':
	fields = ['name', 'age', 'email', 'telephone']

	print(generate_webform(fields))
