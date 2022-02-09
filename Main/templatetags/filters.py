from django import template

register = template.Library()


@register.filter(name='range_')
def range_(number, diff=1):
    return range(0, number, diff)


@register.filter(name='querysetToList')
def querysetToList(queryset, index):
    if not index:
        if queryset.count() > 0:
            return [element for element in queryset]
        return []
    else:
        list_ = [element for element in queryset]
        return list_[index]


@register.filter(name='quotient')
def quotient(number, divideby):
    return int(number / divideby)


@register.filter(name='remainder')
def remainder(number, divideby):
    return number % divideby


@register.filter(name='toGrid')
def toGrid(querySet, column):
    if querySet.count() > 0:
        list_ = []
        temp = []
        i = 0
        for element in querySet:
            if not i == 0 and i % column == 0:
                list_.append([temp, i])
                temp = []
            temp.append(element)
            i += 1
        if len(temp) > 0:
            list_.append([temp, i])
        return list_
    return []