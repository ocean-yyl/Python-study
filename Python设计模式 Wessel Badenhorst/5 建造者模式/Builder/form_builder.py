# encoding=utf-8
from abc import ABCMeta, abstractmethod


class Director(object, metaclass=ABCMeta):
	def __init__(self):
		self._builder = None

	def set_builder(self, builder):
		self._builder = builder

	@abstractmethod
	def construct(self, field_list):
		pass

	def get_constructed_object(self):
		return self._builder.constracted_object


class AbstractFormBuilder(object, metaclass=ABCMeta):
	def __init__(self):
		self.constracted_object = None

	@abstractmethod
	def add_textfield(self, textfield_dict):
		pass

	@abstractmethod
	def add_checkbox(self, checkbox_dict):
		pass

	@abstractmethod
	def add_button(self, button_dict):
		pass


class HtmlForm(object):
	def __init__(self):
		self.field_list = []

	def __repr__(self):
		return "<form>{}</form>".format("".join(self.field_list))


class HtmlFormBuilder(AbstractFormBuilder):
	def __init__(self):
		super().__init__()
		self.constracted_object = HtmlForm()

	def add_textfield(self, textfield_dict):
		self.constracted_object.field_list.append(
			'{0}:<br><input type="text" name="{1}"><br>'.format(
				textfield_dict["label"],
				textfield_dict["name"]
			)
		)

	def add_checkbox(self, checkbox_dict):
		self.constracted_object.field_list.append(
			'<input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
				checkbox_dict["id"],
				checkbox_dict["value"],
				checkbox_dict["label"]
			)
		)

	def add_button(self, button_dict):
		self.constracted_object.field_list.append(
			'<button type="button">{}</button>'.format(
				button_dict["text"]
			)
		)


class FormDirector(Director):
	def __init__(self):
		Director.__init__(self)

	def construct(self, field_list):
		for field in field_list:
			if field["type"] == "text":
				self._builder.add_textfield(field)
			elif field["type"] == "checkbox":
				self._builder.add_checkbox(field)
			elif field["type"] == "button":
				self._builder.add_button(field)


if __name__ == '__main__':
	director = FormDirector()
	html_form_builder = HtmlFormBuilder()
	director.set_builder(html_form_builder)

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
		{
			"type": "button",
			"text": "确定",
		},
	]

	director.construct(field_dict_list)
	print(director.get_constructed_object())
	with open("form_file.html", "w") as f:
		f.write(
			"<html><body>{0!r}</body></html>".format(
				director.get_constructed_object()
			)
		)
