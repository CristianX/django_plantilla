from django import forms
from django.core import validators


class FormArticle(forms.Form):
    title = forms.CharField(
        label="Título",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Escribe el título", "class": "titulo_form_article"}
        ),
        validators=[
            validators.MinLengthValidator(4, "El título es demasiado corto"),
            validators.RegexValidator(
                "^[A-Za-z0-9 ñ]*$", "El título está mal formado", "invalid_title"
            ),
        ],
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Ingrese el contendio",
                "class": "contenido_form_article",
                "id": "contendio_form",
            }
        ),
        validators= [
            validators.MaxLengthValidator(20, 'Te haz pasado, solo 20 carácteres')
        ]
    )
    # content.widget.attrs.update(
    #     {
    #         "placeholder": "Ingrese el contendio",
    #         "class": "contenido_form_article",
    #         "id": "contendio_form",
    #     }
    # )

    public_options = [(1, "Si"), (2, "No")]
    public = forms.TypedChoiceField(label="¿Publicado?", choices=public_options)
