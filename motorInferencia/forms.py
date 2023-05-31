from django import forms


class FormArticle(forms.Form):
    title = forms.CharField(
        label="Título",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Escribe el título", "class": "titulo_form_article"}
        ),
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
