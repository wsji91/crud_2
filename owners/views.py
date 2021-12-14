import json

from django.http     import JsonResponse
from django.views    import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            # data 는 딕셔너리 형태로 저장 
            Owner.objects.create(name=data['name'],
                             email=data['email'],
                             age=data['age'])
        
            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)


    def get(self, request):
        # 다 불러서 변수에 할당??????? xxxx.all() 이거????????
        # 빈 리스트 할당하고 시작
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list = []
            
            for dog in dogs:
                dogs = owner.dog_set.all()
                dog_info = (
                    {
                        'name': dog.name,
                        'age': dog.age
                    }
                )
                dog_list.append(dog_info)
            results.append(
                {
                    'name': owner.name,
                    'age': owner.age,
                    'email': owner.email,
                    'my_dog': dog_list
                }
            )
        return JsonResponse({'result': results}, status=200)



class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Dog.objects.create(name=data['name'],
                           age=data['age'],
                           owner=Owner.objects.get(name=data['owner']))
        
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)
    
    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        
        for dog in dogs:
            results.append(
                {
                    'owner': dog.owner.name,
                    'name': dog.name,
                    'age': dog.age
                }
            )
        return JsonResponse({'MESSAGE': results}, status=200)