from django.db import models
from datetime import date
from datetime import datetime

class Invoice(models.Model):
    # Informations générales
    num_facture = models.CharField(max_length=50, default='inv-xxx')
    grossiste = models.BooleanField(default=False)
    paiement_comptant = models.BooleanField(default=False)
    vente_emportee = models.BooleanField(default=False)

    # Détails de la facture
    marchandise_ht = models.DecimalField(max_digits=10, decimal_places=2)
    remise_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remise_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sous_total_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sous_total_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    escompte = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_ht = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_ttc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    frais_de_port = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_a_payer = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculer_facture(self):

        current_date = date.today()
        current_time = datetime.now()

        self.num_facture = f"INV-{current_date.year}{current_date.month}{current_date.day}{current_time.hour}{current_time.minute}{current_time.second}"
        
        if self.grossiste:
            self.remise_1 = float(self.marchandise_ht) * 0.02
        else:
            self.remise_1 = 0

        self.sous_total_1 = float(self.marchandise_ht) - self.remise_1
        
        if self.grossiste and self.sous_total_1 > 10000:
            self.remise_2 = self.sous_total_1 * 0.05
        else:
            self.remise_2 = 0

        self.sous_total_2 = self.sous_total_1 - self.remise_2
        
        if self.paiement_comptant:
            if self.grossiste:
                self.escompte = self.sous_total_2 * 0.03
            else:
                self.escompte = self.sous_total_2 * 0.02
        else:
            self.escompte = 0

        self.total_ht = self.sous_total_2 - self.escompte
        
        self.tva = self.total_ht * 0.196 
        self.total_ttc = self.total_ht + self.tva

        if self.vente_emportee or self.total_ttc > 15000:
            self.frais_de_port = 0
        else:
            self.frais_de_port = 50

        self.total_a_payer = self.total_ttc + self.frais_de_port

        self.save()
