from rest_framework import serializers
from invoices.models import Invoice, Transcation


class TransactionSerializer(serializers.ModelSerializer):

    """
    Purpose: A serializer that deals with Details instances and
    querysets.
    """

    class Meta(object):
        model = Transcation
#         fields = ('category',)
#         read_only_fields = ('entries',)
#         exclude = ('broken_url_flag',)


class InvoiceSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(many=True,
                                    required=False, read_only=False)
#     transaction = serializers.SlugRelatedField(many=True, queryset=Transcation.objects.all(), read_only=False, slug_field='category')

    def create(self, validated_data):
        import ipdb;ipdb.set_trace()
        if validated_data.get('transaction'):
            transaction_list = validated_data.pop('transaction')
        inv_obj = Invoice.objects.create(**validated_data)
        for tarnsaction_record in transaction_list:
            inv_obj.transaction.add(*tarnsaction_record)
        return inv_obj 

    class Meta(object):
        model = Invoice
        fields = ('id','custumer', 'invoice_date', 'quantity', 'total_amount','transaction')


