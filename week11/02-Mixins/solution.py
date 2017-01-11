import json
import xml.etree.ElementTree as ET


class XmlableMixin:
    types = {
        t.__name__: t
        for t in (str, int)
    }

    @classmethod
    def from_xml(cls, xmlstring):
        root = ET.fromstring(xmlstring)

        if root.tag != cls.__name__:
            raise ValueError

        data = {}

        for child in root:
            type_name = child.get('type', 'str')
            type = cls.types.get(type_name, str)

            data[child.tag] = type(child.text)

        return cls(**data)

    def to_xml(self):
        classname = self.__class__.__name__
        root = ET.Element(classname)

        for k, v in self.__dict__.items():
            kelement = ET.SubElement(root, k, {'type': type(v).__name__})
            kelement.text = str(v)

        return ET.tostring(root).decode('utf8')


class JsonableMixin:
    serializable_types = (dict,
                          list,
                          tuple,
                          str,
                          int,
                          float,
                          bool,
                          None)

    def to_before_json(self):
        data = {
            'dict': {},
            'classname': self.__class__.__name__
        }

        for k, v in self.__dict__.items():
            if type(v) in self.serializable_types:
                data['dict'][k] = v

            if isinstance(v, JsonableMixin):
                data['dict'][k] = v.to_before_json()

        return data

    def to_json(self):
        return json.dumps(self.to_before_json(), indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        classname = data.get('classname', None)

        if cls.__name__ != classname:
            raise ValueError('{} != {}'.format(cls.__name__,
                                               classname))

        return cls(**data['dict'])


class Panda(JsonableMixin, XmlableMixin):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


p = Panda(name='Ivo', age=23)
xmlstring = p.to_xml()
print(xmlstring)

p1 = Panda.from_xml(xmlstring)
print(p1.name, type(p1.age))
