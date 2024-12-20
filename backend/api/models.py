# from django.db import models






# class BilanBiologique(models.Model):
#     id = models.AutoField(primary_key=True)
#     description = models.CharField(max_length=255, null=True, blank=True)
#     consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
#     laborantient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='biological_tests')
#     satisfait = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Bilan Biologique {self.id} - {'Satisfied' if self.satisfait else 'Unsatisfied'}"


# class ParamValeur(models.Model):
#     id = models.AutoField(primary_key=True)
#     valeur = models.FloatField()
#     unite = models.CharField(max_length=255)
#     parametre = models.CharField(max_length=255)
#     bilan = models.ForeignKey(BilanBiologique, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Param {self.parametre} - {self.valeur} {self.unite}"


# class BilanRadiologique(models.Model):
#     id = models.AutoField(primary_key=True)
#     compte_rendu = models.CharField(max_length=255, null=True, blank=True)
#     type = models.CharField(max_length=255)
#     consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
#     radiologe = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='radiological_tests')

#     def __str__(self):
#         return f"Bilan Radiologique {self.id} - Type: {self.type}"


# class ExamenImagerieMedicale(models.Model):
#     id = models.AutoField(primary_key=True)
#     examen_image_path = models.CharField(max_length=255)
#     bilan = models.ForeignKey(BilanRadiologique, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Imagerie {self.id} - {self.examen_image_path}"


# class Soins(models.Model):
#     id = models.AutoField(primary_key=True)
#     description = models.CharField(max_length=255)
#     dpi = models.ForeignKey(Dpi, on_delete=models.CASCADE)
#     infirmier = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='soins')
#     la_date = models.DateField()

#     def __str__(self):
#         return f"Soins {self.id} - {self.description}"


# class Notification(models.Model):
#     id = models.AutoField(primary_key=True)
#     type = models.CharField(max_length=255)
#     descirption = models.CharField(max_length=255)
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Notification {self.id} - Type: {self.type}"
