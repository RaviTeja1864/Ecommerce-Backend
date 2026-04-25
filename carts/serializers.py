from rest_framework import serializers

class AddCarItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


    def validate_product_id(self,value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Product does not exist")
        return value

        def save(self, **kwargs):
            cart_id = self.context['cart_id']
            product_id = self.validated_data['product_id']
            quantity = self.validated_data['quantity']

            try:
                cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
                cart_item.quantity += quantity
                cart_item.save()
                sef.instance = cart_item

            except CartItem.DoesNotExist:
                self.instance = CartItem.objects.create(cart_id=cart_id, product_id=product_id, quantity=quantity)
            
            return self.instance
    class Meta:
        model = CartItem
        fields = ['id' , 'product_id' , 'quantity']
    
    

        