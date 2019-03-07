
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
class OrderField(models.PositiveIntegerField): #③
#自定义的字段属性在本质上就是一个类，定义了类的名称，并且继承自models.PositiveIntegerField
#-->>这里所定义的OrderField是要得到对象排序的序号，其值为整数，所以继承models.PositiveIntegerField
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)
#在django的字段属性中，都继承了Field类，pre_save()就是Field类中的一个方法
#pre_save()方法的作用就是在保存之前对数字进行预处理，在具体的某个字段中，因为特殊需要，常常将Field类中的这个方法重写。例如，DateTimeField,created = models.DateTimeField(auto_now_add=True)
#-->>在DateTimeField中就重写了pre_save()方法，对时间进行了预处理，使得我们不需要单独显示地把保存的当前时间写出来，而是在调用实例的save()方法之后，字段完成时间的写入保存
#重写pre_save()方法，最终将实例的序号记录下来从前面的Filed.pre_save()方法可以得知，参数model_instance和add是与祖先类保持一致的，这样的写法友好性更强。model_instance引用的是实例，add为该实例是否第一次被保存
    def pre_save(self, model_instance, add): #④
        if getattr(model_instance, self.attname) is None: #⑤
#getattr(),它能返回一个对象属性的值，self.attname也是在Fields类里面规定的一个参数
#判断当前对象(实例)中是否有某个属性(字段)，如果有，就执行else分支，调用父类的pre_save()方法，但不会在数据库中增加记录；否则就执行try..except语句，在try中主要计算新增一条数据后的序号
            try:
                qs = self.model.objects.all() #⑥#得到当前实例的所有记录
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields} #⑦
#
                    qs = qs.filter(**query) #⑧
                last_item = qs.latest(self.attname) #⑨
                value = last_item.order + 1 #⑩
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value) #⑪
            return value
        else:
            return super(OrderField, self).pre_save(model_instance, add)