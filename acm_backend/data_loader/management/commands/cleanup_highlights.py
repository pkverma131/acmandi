from django.core.management.base import BaseCommand
from catalogue.models import ProductHighlight, ProductToProductHighlight

class Command(BaseCommand):
    help = 'Cleanup duplicate ProductHighlights'

    def handle(self, *args, **options):
        product_ids = ProductToProductHighlight.objects.values_list('product_id', flat=True).distinct()

        for product_id in product_ids:
            product_highlight_ids = ProductToProductHighlight.objects.filter(product_id=product_id).values_list('highlight_id', flat=True)
            highlight_list = []
            highlights_to_delete = []

            for highlight_id in product_highlight_ids:
                highlight = ProductHighlight.objects.get(id=highlight_id).highlight
                if highlight in highlight_list:
                    highlights_to_delete.append(highlight_id)
                    print(f'highlight to be deleted: {highlight_id}')
                else:
                    highlight_list.append(highlight)
                    print(f'highlight to be kept: {highlight_id}')

            # Delete mapping from ProductToProductHighlight for this product            
            ProductToProductHighlight.objects.filter(product_id=product_id, highlight_id__in=highlights_to_delete).delete()

            # Delete duplicate ProductHighlights for this product
            ProductHighlight.objects.filter(id__in=highlights_to_delete).delete()

            self.stdout.write(self.style.SUCCESS(f'Cleanup completed for Product ID {product_id}'))
