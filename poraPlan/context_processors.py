


def my_context(request):
    context_data = dict()
    context_data['notification_count'] = "11111111111"
    print "sss"
    return {'notification_count': "888888888888888888888888888888888888"}

