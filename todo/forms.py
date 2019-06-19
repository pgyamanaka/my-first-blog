from django import forms 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control', 'placeholder' : 'Adicione metas aqui, exemplo beber 2 litros de água', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
