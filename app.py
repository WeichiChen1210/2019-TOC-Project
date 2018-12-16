# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bottle import route, run, request, abort, static_file

from fsm import TocMachine

VERIFY_TOKEN = "876546587565122"

machine = TocMachine(
    states=[
        'usr',
        'menu',
        'signup_info',
        'introduction',
        'download',
        'traffic'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'usr',
            'dest': 'menu',
            'conditions': 'is_going_to_menu'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'signup_info',
            'conditions': 'is_going_to_signup_info'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'introduction',
            'conditions': 'is_going_to_introduction'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'download',
            'conditions': 'is_going_to_download'
        },
        {
            'trigger': 'advance',
            'source': [
                'signup_info',
                'introduction',
                'download',
            ],
            'dest': 'menu',
            'conditions': 'back_to_menu'
        },
        # {
        #     'trigger': 'advance',
        #     'source': 'menu',
        #     'dest': 'traffic',
        #     'conditions': 'is_going_to_traffic'
        # },
        {
            'trigger': 'go_back',
            'source': [
                'signup_info',
                'introduction',
                'download',
                'traffic'
            ],
            'dest': 'menu'
        }
    ],
    initial='usr',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)

# for receiving message
@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        #print("here")
        event = body['entry'][0]['messaging'][0]
        #   print(event)
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
