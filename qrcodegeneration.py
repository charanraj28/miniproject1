import shutil

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import pyqrcode
class Enterdetails(Screen):
    pass

class ViewQR(Screen):
    pass
string="""<Enterdetails>:
    MDLabel:
        text: "VASAVI COLLEGE OF ENGINEERING"
        font_size: 35
        pos_hint: {"center_x": 0.5, "center_y": 0.95}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDLabel:
        text: "Enter details to get QR Code"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.89}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    MDCard:
        size_hint: 0.95, 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

    MDTextField:
        id: rno
        hint_text: "Roll number"
        size_hint_x: 0.4
        font_size: 25
        required: True
        input_type: 'number'
        pos_hint: {"center_x": 0.75, "center_y": 0.75}
        helper_text_mode: "on_error"
        helper_text: "Enter 12 digit roll number"
    MDTextField:
        id: name
        hint_text: "Name"
        size_hint_x: 0.4
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.75}

    MDTextField:
        id: fname
        hint_text: "Father Name"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.65}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"

    MDTextField:
        id: dob
        hint_text: "Date of Birth"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.65}
        required: True
        helper_text_mode: "on_error"
        helper_text: "dd/mm/yyyy"
    MDTextField:
        id: gender
        hint_text: "Gender"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.55}
        required: True
        max_text_length: 1
        helper_text_mode: "on_error"
        helper_text: "M/F"

    MDTextField:
        id: semester
        hint_text: "Semester"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.55}
        required: True
        max_text_length: 1
        helper_text_mode: "on_error"
        helper_text: "1/2/3/4"
    MDTextField:
        id: branch
        hint_text: "Branch"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.25, "center_y": 0.45}
        required: True
        max_text_length: 3
        helper_text_mode: "on_error"
        helper_text: "Enter your branch"

    MDTextField:
        id: section
        hint_text: "Section"
        size_hint_x: 0.4
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.45}
        required: True
        max_text_length: 1
        helper_text_mode: "on_error"
        helper_text: "A/B/C"

    MDTextField:
        id: phn
        hint_text: "Phone number"
        size_hint_x: 0.4
        font_size: 25
        required: True
        pos_hint: {"center_x": 0.25, "center_y": 0.35}
        helper_text_mode: "on_error"
        helper_text: "Enter 10-digit phone number"

    MDTextField:
        id: email
        hint_text: "Email"
        size_hint_x: 0.9
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"

    MDTextField:
        id: blood
        hint_text: "Blood Group"
        size_hint_x: 0.4
        width: 180
        font_size: 25
        pos_hint: {"center_x": 0.75, "center_y": 0.35}
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter text"

    MDRoundFlatButton:
        text: "Submit"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        size_hint_x: 0.7
        on_press: app.finalSubmit(name.text,rno.text,fname.text,dob.text,gender.text,semester.text,branch.text,section.text,phn.text,blood.text,email.text)

<ViewQR>:
    MDLabel:
        text: "VASAVI COLLEGE OF ENGINEERING"
        font_size: 40
        pos_hint: {"center_x": 0.5, "center_y": 0.95}
        halign: 'center'
        size_hint_y: None
        padding_y: 15

    MDLabel:
        text: "Scan this QR Code to get your details"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.88}
        halign: 'center'
        size_hint_y: None
        padding_y: 15
    Image:
        source: app.source
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_y: 0.7

    MDRoundFlatButton:
        text: "Download"
        font_size: 25
        pos_hint: {"center_x": 0.5, "center_y": 0.08}
        size_hint_x: 0.8
        on_press: app.download()"""
Builder.load_string(string)
sm = ScreenManager()
Window.size = (800, 600)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        sm.add_widget(Enterdetails(name='enterdetails'))

        sm.current = 'enterdetails'

        return sm

    def finalSubmit(self,name, rno, fname, dob, gender, semester,branch,section,phone,blood,email):
        s = f"VASAVI COLLEGE OF ENGINEERING\n====== ======= == ===========\nName\t\t:{name}\nRoll no\t\t:{rno}\nFather Name\t:{fname}\nDOB   \t\t:{dob}\nGender\t\t:{gender}\nSemester\t\t:{semester}\nBranch\t\t:{branch}\nSection\t\t:{section}\nPhone no\t\t:{phone}\nBlood Group\t:{blood}\nEmail id\t\t:{email}\n"
        print(s)
        # Generate QR code
        url = pyqrcode.create(s)
        url.png(f'{name}.png', scale=6)
        self.source=f'{name}.png'
        sm.add_widget(ViewQR(name='viewQR'))
        sm.current='viewQR'
        self.p=name

    def download(self):
        shutil.move(rf'C:\Users\Gouri Manasa\PycharmProjects\ManasaMiniProject\{self.p}.png' , r'C:\Users\Gouri Manasa\PycharmProjects\ManasaMiniProject\ALLQRS')

MainApp().run()
