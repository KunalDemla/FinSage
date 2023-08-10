from django import forms


class ExclusiveForm(forms.Form):
    gender = forms.ChoiceField(
        label='Gender',
        choices=(
            ('male', "Male"),
            ('female', "Female"),
            ('others', "Others"),
        )
    )
    area = forms.ChoiceField(
        label='Region',
        choices=(
            ('urban', "Urban"),
            ('rural', "Rural"),
        )
    )
    category = forms.ChoiceField(
        label='Category',
        choices=(
            ('Gen', "Gen"),
            ('ST', "ST"),
            ('PWD', "PWD"),
            ('SC', "SC"),
        )
    )